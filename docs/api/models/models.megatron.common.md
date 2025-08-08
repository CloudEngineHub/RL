# {py:mod}`models.megatron.common`

```{py:module} models.megatron.common
```

```{autodoc2-docstring} models.megatron.common
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`forward_step_arbitrary_loss <models.megatron.common.forward_step_arbitrary_loss>`
  - ```{autodoc2-docstring} models.megatron.common.forward_step_arbitrary_loss
    :summary:
    ```
* - {py:obj}`broadcast_tensor <models.megatron.common.broadcast_tensor>`
  - ```{autodoc2-docstring} models.megatron.common.broadcast_tensor
    :summary:
    ```
````

### API

````{py:function} forward_step_arbitrary_loss(state: nemo.tron.state.GlobalState, global_valid_seqs: torch.Tensor, global_valid_toks: torch.Tensor, data_iterator: typing.Iterator[nemo_rl.distributed.batched_data_dict.BatchedDataDict[typing.Any]], model: megatron.core.models.gpt.GPTModel, loss_fn: nemo_rl.algorithms.loss_functions.LossFunction)
:canonical: models.megatron.common.forward_step_arbitrary_loss

```{autodoc2-docstring} models.megatron.common.forward_step_arbitrary_loss
```
````

````{py:function} broadcast_tensor(tensor: torch.Tensor | None, src_rank: int, group: torch.distributed.ProcessGroup) -> torch.Tensor
:canonical: models.megatron.common.broadcast_tensor

```{autodoc2-docstring} models.megatron.common.broadcast_tensor
```
````
