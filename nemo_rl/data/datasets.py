# Copyright (c) 2025, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import logging
from dataclasses import dataclass
from typing import Any, Dict, List, Tuple, Union

import torch
from datasets import Dataset

from nemo_rl.data.interfaces import (
    DatumSpec,
    TaskDataProcessFnCallable,
    TaskDataSpec,
)
from nemo_rl.data.llm_message_utils import (
    add_loss_mask_to_message_log,
    batched_message_log_to_flat_message,
)
from nemo_rl.distributed.batched_data_dict import BatchedDataDict
from nemo_rl.utils.logger import log_json


# TODO @sahilj handle too-long prompts and masking them out throughout the whole process and renormalizing on loss
class AllTaskProcessedDataset:
    """Dataset for processing single or multi-task data with task-specific tokenization and processing.

    Args:
        dataset: Input dataset containing raw data
        tokenizer: Tokenizer for text processing
        default_task_data_spec: Default task processing specifications.
            In the case of single-task, this is the spec used for processing all entries.
            In the case of multi-task, any values not specified in the task-specific specs will be taken from the default spec.
        task_data_processors: Either a single TaskDataProcessFnCallable for single-task,
            or a dict mapping task names to (TaskDataSpec, TaskDataProcessFnCallable) for multi-task
        max_seq_length: Maximum sequence length for tokenized outputs
    """

    def __init__(
        self,
        dataset: Union[Dataset, Any],
        tokenizer,
        default_task_data_spec: TaskDataSpec,
        task_data_processors: Union[
            Dict[str, Tuple[TaskDataSpec, TaskDataProcessFnCallable]],
            TaskDataProcessFnCallable,
        ],
        max_seq_length=None,
    ):
        self.dataset = dataset
        self.tokenizer = tokenizer
        self.default_task_data_spec = default_task_data_spec
        self.task_data_processors = task_data_processors
        self.max_seq_length = max_seq_length

        if isinstance(task_data_processors, dict):
            # apply defaults to all task data specs
            for task_name, (
                task_data_spec,
                task_data_processor,
            ) in task_data_processors.items():
                task_data_spec.copy_defaults(self.default_task_data_spec)

    def __len__(self):
        return len(self.dataset)

    def encode_single(self, text: Union[str, List[str]]) -> Tuple[List[int], int]:
        """Takes either a single string or a list of strings that represent multiple turns for the same conversation.

        Returns a single (concatenated) list of tokenized ids and the length of the tokenized ids.
        """
        if isinstance(text, str):
            text_ids = self.tokenizer.text_to_ids(text)
            return text_ids, len(text_ids)
        elif isinstance(text, list):
            text_ids = [self.tokenizer.text_to_ids(t) for t in text]
            return torch.cat(text_ids), sum(len(t) for t in text_ids)
        else:
            raise ValueError(
                f"text must be a string or a list of strings, got {type(text)}"
            )

    def __getitem__(self, idx: int) -> DatumSpec:
        """Return a single prompt."""
        entry = self.dataset[idx]

        if isinstance(self.task_data_processors, dict):
            task_name = entry["task_name"]

            assert task_name in self.task_data_processors, (
                f"task processor not provided for {task_name}. Provided processors: {self.task_data_processors.keys()}"
            )
            task_data_spec, task_data_processor = self.task_data_processors[task_name]
        else:
            task_data_spec = self.default_task_data_spec
            task_data_processor = self.task_data_processors

        datum_spec = task_data_processor(
            entry, task_data_spec, self.tokenizer, self.max_seq_length, idx
        )

        logging.debug(
            "-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_"
        )
        logging.debug("AllTaskProcessedDataset, __getitem__")
        logging.debug(f"{idx=}")
        log_json("entry", entry)
        log_json("datum_spec", datum_spec)
        logging.debug(
            "-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_"
        )
        return datum_spec


def rl_collate_fn(data_batch: List[DatumSpec]) -> BatchedDataDict:
    """Collate function for RL training."""
    message_log = [datum_spec["message_log"] for datum_spec in data_batch]
    length = torch.tensor([datum_spec["length"] for datum_spec in data_batch])
    loss_multiplier = torch.tensor(
        [datum_spec["loss_multiplier"] for datum_spec in data_batch]
    )
    extra_env_info = [datum_spec["extra_env_info"] for datum_spec in data_batch]

    task_names = []
    for datum_spec in data_batch:
        task_names.append(datum_spec.get("task_name", None))

    idx = [datum_spec["idx"] for datum_spec in data_batch]
    batch_max_length = torch.ones_like(length) * length.max()

    # Extract stop_strings if present
    stop_strings = [datum.get("stop_strings", None) for datum in data_batch]

    output = BatchedDataDict(
        message_log=message_log,
        length=length,
        loss_multiplier=loss_multiplier,
        extra_env_info=extra_env_info,
        task_name=task_names,
        idx=idx,
        batch_max_length=batch_max_length,
        stop_strings=stop_strings,
    )

    logging.debug(
        "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
    )
    logging.debug("rl_collate_fn")
    log_json("data_batch", data_batch)
    log_json("output", output)
    logging.debug(
        "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
    )

    return output


@dataclass
class PackableBatchedData:
    data: BatchedDataDict
    pack_sizes: List[int]


def group_PackableBatchedData(self):
    pass


def ungroup_PackableBatchedData(self):
    pass


def packed_rl_collate_fn(groups: List[List[DatumSpec]]) -> PackableBatchedData:
    """Collate function for packed RL training.

    This function handles packed data batches from PackedDataset.
    It reuses the logic from rl_collate_fn but adapts it for packed data.
    """
    # Create a list of flattened samples to pass to rl_collate_fn
    flattened_dataums: List[DatumSpec] = []

    for group in groups:
        # Create a single "unpacked" sample that represents the packed group
        group_message_log = []
        for sample in group:
            group_message_log.extend(sample["message_log"])

        # Use minimum loss multiplier from all samples
        min_loss_multiplier = min(sample["loss_multiplier"] for sample in group)

        # Create a DatumSpec from this group
        group_datum: DatumSpec = {
            "message_log": group_message_log,
            "length": sum([sample["length"] for sample in group]),
            "loss_multiplier": min_loss_multiplier,
            "extra_env_info": group[0]["extra_env_info"],
            "task_name": group[0].get("task_name", None),
            "idx": group[0]["idx"],
            "stop_strings": group[0].get("stop_strings", None),
            "__extra__": [sample.get("__extra__", None) for sample in group],
        }

        flattened_dataums.append(group_datum)

    # Use the existing rl_collate_fn to process the unpacked samples
    output: PackableBatchedData = PackableBatchedData(
        data=rl_collate_fn(flattened_dataums),
        pack_sizes=[len(group) for group in groups],
    )

    logging.debug(
        "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
    )
    logging.debug("packed_rl_collate_fn")
    log_json("data_batch", groups)
    log_json("output", output)
    logging.debug(
        "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
    )

    return output


def eval_collate_fn(data_batch: List[DatumSpec]) -> BatchedDataDict:
    """Collate function for evaluation.

    Takes a list of data samples and combines them into a single batched dictionary
    for model evaluation.

    Args:
        data_batch: List of data samples with message_log, extra_env_info, and idx fields.

    Returns:
        BatchedDataDict with message_log, extra_env_info, and idx fields.

    Examples:
    ```{doctest}
    >>> import torch
    >>> from nemo_rl.data.datasets import eval_collate_fn
    >>> from nemo_rl.data.interfaces import DatumSpec
    >>> data_batch = [
    ...     DatumSpec(
    ...         message_log=[{"role": "user", "content": "Hello", "token_ids": torch.tensor([1, 2, 3])}],
    ...         extra_env_info={'ground_truth': '1'},
    ...         idx=0,
    ...     ),
    ...     DatumSpec(
    ...         message_log=[{"role": "assistant", "content": "Hi there", "token_ids": torch.tensor([4, 5, 6, 7])}],
    ...         extra_env_info={'ground_truth': '2'},
    ...         idx=1,
    ...     ),
    ... ]
    >>> output = eval_collate_fn(data_batch)
    >>> output['message_log'][0]
    [{'role': 'user', 'content': 'Hello', 'token_ids': tensor([1, 2, 3])}]
    >>> output['message_log'][1]
    [{'role': 'assistant', 'content': 'Hi there', 'token_ids': tensor([4, 5, 6, 7])}]
    >>> output['extra_env_info']
    [{'ground_truth': '1'}, {'ground_truth': '2'}]
    >>> output['idx']
    [0, 1]
    """
    message_log = [datum_spec["message_log"] for datum_spec in data_batch]
    extra_env_info = [datum_spec["extra_env_info"] for datum_spec in data_batch]
    idx = [datum_spec["idx"] for datum_spec in data_batch]

    output = BatchedDataDict(
        message_log=message_log,
        extra_env_info=extra_env_info,
        idx=idx,
    )
    return output


def dpo_collate_fn(
    data_batch: List[DatumSpec], tokenizer, make_sequence_length_divisible_by: int
) -> BatchedDataDict:
    """Collate function for DPO training.

    This function separates the chosen and rejected responses to create
    two examples per prompt. The chosen and rejected examples are interleaved
    along the batch dimension, resulting in a batch size of 2 * len(data_batch).
    """
    message_log = []
    length = []
    loss_multiplier = []
    idx = []
    task_names = []
    for datum_spec in data_batch:
        ## interleave chosen and rejected examples
        message_log.append(datum_spec["message_log_chosen"])
        message_log.append(datum_spec["message_log_rejected"])
        length.append(datum_spec["length_chosen"])
        length.append(datum_spec["length_rejected"])
        loss_multiplier.extend([datum_spec["loss_multiplier"]] * 2)
        idx.extend([datum_spec["idx"]] * 2)
        task_names.extend([datum_spec.get("task_name", None)] * 2)
    length = torch.tensor(length)
    loss_multiplier = torch.tensor(loss_multiplier)

    batch_max_length = torch.ones_like(length) * length.max()

    batch = BatchedDataDict(
        message_log=message_log,
        length=length,
        loss_multiplier=loss_multiplier,
        task_name=task_names,
        idx=idx,
        batch_max_length=batch_max_length,
    )

    ## add loss mask based on role to every message
    add_loss_mask_to_message_log(
        batch["message_log"],
        only_unmask_final=True,
    )

    cat_and_padded, input_lengths = batched_message_log_to_flat_message(
        batch["message_log"],
        pad_value_dict={"token_ids": tokenizer.pad_token_id},
        make_sequence_length_divisible_by=make_sequence_length_divisible_by,
    )

    train_data: BatchedDataDict = BatchedDataDict(
        {
            "input_ids": cat_and_padded["token_ids"],
            "input_lengths": input_lengths,
            "token_mask": cat_and_padded["token_loss_mask"],
            "sample_mask": loss_multiplier,
        }
    )

    return train_data
