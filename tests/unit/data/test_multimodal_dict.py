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
import pytest
import torch

from nemo_rl.distributed.batched_data_dict import (
    BatchedDataDict,
    DynamicBatchingArgs,
    SequencePackingArgs,
)
from nemo_rl.data.multimodal_utils import (
    PackedGenericDataBatch,
    PackedGenericDataItem,
    PackedMultimodalDataBatch,
    PackedMultimodalDataItem,
)

def test_packed_data_basic():
    """Test basic functionality of PackedGenericDataItem and PackedGenericDataBatch."""
    # Create sample packed items
    tensor1 = torch.randn(16, 3)
    tensor2 = torch.randn(45, 3)
    
    item1 = PackedGenericDataItem(tensor1, dim_to_pack=0)
    item2 = PackedGenericDataItem(tensor2, dim_to_pack=0)
    
    # Test item functionality
    assert torch.equal(item1(), tensor1)
    assert item1.dim_to_pack == 0
    
    # Test batch creation and concatenation
    batch = PackedGenericDataBatch([item1, item2], dim_to_pack=0)
    assert len(batch) == 2
    
    # Test as_tensor
    expected_tensor = torch.cat([tensor1, tensor2], dim=0)
    assert torch.equal(batch.as_tensor(), expected_tensor)

def test_shard_by_batch_size_with_packed_data():
    """Test shard_by_batch_size with packed multimodal data."""
    # Create sample data
    text_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    image_tensors = [PackedGenericDataItem(torch.randn(3*i + 2, 3, 128, 128), dim_to_pack=0) for i in range(4)]
    
    # Create packed image data
    packed_batch = PackedGenericDataBatch(image_tensors, dim_to_pack=0)
    
    # Create BatchedDataDict
    batch = BatchedDataDict({
        "text_ids": text_tensor,
        "image_features": packed_batch,
        "labels": [1, 2, 3, 4]
    })
    
    # Test sharding
    shards = batch.shard_by_batch_size(shards=2)
    assert len(shards) == 2
    
    # Verify first shard
    assert torch.equal(shards[0]["text_ids"], torch.tensor([[1, 2, 3], [4, 5, 6]]))
    assert isinstance(shards[0]["image_features"], PackedGenericDataBatch)
    assert len(shards[0]["image_features"]) == 2
    assert shards[0]["image_features"].as_tensor().shape == (2 + 5, 3, 128, 128)
    assert shards[0]["labels"] == [1, 2]
    
    # Verify second shard
    assert torch.equal(shards[1]["text_ids"], torch.tensor([[7, 8, 9], [10, 11, 12]]))
    assert isinstance(shards[1]["image_features"], PackedGenericDataBatch)
    assert len(shards[1]["image_features"]) == 2
    assert shards[1]["image_features"].as_tensor().shape == (8 + 11, 3, 128, 128)
    assert shards[1]["labels"] == [3, 4]

def test_packed_data_batch_dim_to_pack():
    """ Test if the dim_to_pack is correctly set for a packed data batch """
    # Create sample data
    image_tensors = [PackedGenericDataItem(torch.randn(3, 128, 128), dim_to_pack=0) for i in range(2)]
    with pytest.raises(AssertionError):
        batch = PackedGenericDataBatch(image_tensors, dim_to_pack=1)

    # add another tensor with dim_to_pack = 0
    image_tensors.append(PackedGenericDataItem(torch.randn(3, 128, 128), dim_to_pack=1))
    with pytest.raises(ValueError):
        batch = PackedGenericDataBatch(image_tensors, dim_to_pack=2)
    
    # if only tensors are provided, dim_to_pack must be provided
    actual_tensors = [torch.randn(3, 128, 128) for i in range(2)]
    with pytest.raises(AssertionError):
        batch = PackedGenericDataBatch(actual_tensors)
    
    # should be able to work
    for i in image_tensors:
        i.dim_to_pack = 0
    batch = PackedGenericDataBatch(image_tensors, dim_to_pack=0)
    # this should also work
    batch2 = PackedGenericDataBatch(image_tensors)

    assert batch.dim_to_pack == batch2.dim_to_pack == 0
    assert len(batch) == 3
    assert len(batch2) == 3

def test_truncate_tensors_with_packed_data():
    """Test truncate_tensors with packed multimodal data."""
    # Create sample data
    text_tensor = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
    image_tensors = [PackedGenericDataItem(torch.randn(5, 3, 128, 4, 2, 2), dim_to_pack=1) for i in range(2)]  # also check a different dim_to_pack
    
    # Create packed image data
    packed_batch = PackedGenericDataBatch(image_tensors, dim_to_pack=1)
    
    # Create BatchedDataDict
    batch = BatchedDataDict({
        "text_ids": text_tensor,
        "image_features": packed_batch
    })
    
    # Test truncation
    batch.truncate_tensors(dim=1, truncated_len=2)
    
    # Verify text was truncated
    assert torch.equal(batch["text_ids"], torch.tensor([[1, 2], [5, 6]]))
    # Verify image features were not affected (assumed safe as per comment in truncate_tensors)
    assert isinstance(batch["image_features"], PackedGenericDataBatch)
    assert batch["image_features"].as_tensor().shape == (5, 6, 128, 4, 2, 2)

def test_sequence_packing_with_packed_data():
    """Test sequence packing with packed multimodal data."""
    # Create sample data
    text_tensor = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    image_tensors = [PackedGenericDataItem(torch.randn(2**i, 1176), dim_to_pack=0) for i in range(4)]
    
    # Create packed image data
    packed_batch = PackedGenericDataBatch(image_tensors, dim_to_pack=0)
    
    # Create BatchedDataDict
    batch = BatchedDataDict({
        "text_ids": text_tensor,
        "image_features": packed_batch,
        "sequence_lengths": torch.tensor([2, 3, 2, 4])
    })
    
    sequence_packing_args = SequencePackingArgs(
        max_tokens_per_microbatch=6,
        input_key="text_ids",
        input_lengths_key="sequence_lengths",
        algorithm="modified_first_fit_decreasing",
        sequence_length_pad_multiple=1,
    )
    
    # Test sequence packing
    sharded_batches, sorted_indices = batch.shard_by_batch_size(
        shards=2, sequence_packing_args=sequence_packing_args
    )
    
    # Verify basic structure
    assert len(sharded_batches) == 2
    assert len(sorted_indices) == 4

    print("sequence packing sorted indices", sorted_indices)
    
    # Verify each shard has the necessary attributes
    for shard in sharded_batches:
        assert hasattr(shard, "micro_batch_indices")
        assert hasattr(shard, "micro_batch_lengths")
        assert isinstance(shard["image_features"], PackedGenericDataBatch)


def test_dynamic_batching_with_packed_data():
    """Test dynamic batching with packed multimodal data."""
    # Create sample data
    text_tensor = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    image_tensors = [PackedGenericDataItem(torch.randn(2**i, 1176), dim_to_pack=0) for i in range(4)]
    
    # Create packed image data
    packed_batch = PackedGenericDataBatch(image_tensors, dim_to_pack=0)
    
    # Create BatchedDataDict
    batch = BatchedDataDict({
        "text_ids": text_tensor,
        "image_features": packed_batch,
        "sequence_lengths": torch.tensor([2, 3, 2, 4])
    })
    
    dynamic_batching_args: DynamicBatchingArgs = {
        "input_key": "text_ids",
        "input_lengths_key": "sequence_lengths",
        "sequence_length_round": 2,
        "max_tokens_per_microbatch": 6,
    }
    
    # Test dynamic batching
    sharded_batches, sorted_indices = batch.shard_by_batch_size(
        shards=2, dynamic_batching_args=dynamic_batching_args
    )

    print("dynamic batching sorted indices", sorted_indices)
    
    # Verify basic structure
    assert len(sharded_batches) == 2
    assert len(sorted_indices) == 4
    
    # Verify each shard has the necessary attributes
    for shard in sharded_batches:
        assert hasattr(shard, "micro_batch_indices")
        assert hasattr(shard, "micro_batch_lengths")
        assert isinstance(shard["image_features"], PackedGenericDataBatch)


def test_multimodal_specific_functionality():
    """Test functionality specific to multimodal data handling. (length, device movement, as_tensor)"""
    # Create sample data
    text_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
    image_tensor = torch.tensor([[[1.0, 2.0]], [[3.0, 4.0]]])
    
    # Test PackedMultimodalDataItem
    mm_item = PackedMultimodalDataItem(image_tensor, dim_to_pack=0)
    assert isinstance(mm_item, PackedGenericDataItem)
    assert torch.equal(mm_item(), image_tensor)
    
    # Test PackedMultimodalDataBatch
    mm_batch = PackedMultimodalDataBatch([mm_item], dim_to_pack=0)
    assert isinstance(mm_batch, PackedGenericDataBatch)
    assert len(mm_batch) == 1
    
    # Test device movement
    if torch.cuda.is_available():
        mm_batch = mm_batch.to("cuda")
        assert mm_batch.tensors[0].device.type == "cuda"
    
    # images differ along a different dimension
    image_tensors = [PackedGenericDataItem(torch.randn(3, 128, 128 + i), dim_to_pack=0) for i in range(2)]
    mm_batch = PackedMultimodalDataBatch(image_tensors, dim_to_pack=0)
    with pytest.raises(RuntimeError):
        batch_tensor = mm_batch.as_tensor()
    
    with pytest.raises(RuntimeError):
        repacked_item = mm_batch.as_packed_data_item()

    # check for packed item
    image_tensors = [PackedGenericDataItem(torch.randn(3 + 10**i, 128, 128), dim_to_pack=0) for i in range(2)]
    mm_batch = PackedMultimodalDataBatch(image_tensors, dim_to_pack=0)
    mm_tensor = mm_batch.as_packed_data_item()
    

def test_get_multimodal_dict():
    """Test the get_multimodal_dict functionality."""
    # Create sample data
    text_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
    image_tensor = torch.tensor([[[1.0, 2.0]], [[3.0, 4.0]]])
    token_type_ids = torch.tensor([[1, 1, 1], [1, 1, 1]])
    
    # Create packed image data
    packed_image = PackedMultimodalDataItem(image_tensor, dim_to_pack=0)
    packed_batch = PackedMultimodalDataBatch([packed_image], dim_to_pack=0)
    
    # Create BatchedDataDict
    batch = BatchedDataDict({
        "text_ids": text_tensor,
        "image_features": packed_batch,
        "token_type_ids": token_type_ids  # Special key that should be included
    })
    
    # Test getting multimodal dict as tensors
    mm_dict = batch.get_multimodal_dict(as_tensors=True)
    assert "image_features" in mm_dict
    assert "token_type_ids" in mm_dict
    assert torch.is_tensor(mm_dict["image_features"])
    assert torch.is_tensor(mm_dict["token_type_ids"])
    assert "text_ids" not in mm_dict  # Regular tensors should not be included
    
    # Test getting multimodal dict as packed items
    mm_dict = batch.get_multimodal_dict(as_tensors=False)
    assert "image_features" in mm_dict
    assert "token_type_ids" in mm_dict
    assert isinstance(mm_dict["image_features"], PackedGenericDataBatch)
    assert torch.is_tensor(mm_dict["token_type_ids"])