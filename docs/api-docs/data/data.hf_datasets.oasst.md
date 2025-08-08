# {py:mod}`data.hf_datasets.oasst`

```{py:module} data.hf_datasets.oasst
```

```{autodoc2-docstring} data.hf_datasets.oasst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`OasstDataset <data.hf_datasets.oasst.OasstDataset>`
  - ```{autodoc2-docstring} data.hf_datasets.oasst.OasstDataset
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`parse_conversations <data.hf_datasets.oasst.parse_conversations>`
  - ```{autodoc2-docstring} data.hf_datasets.oasst.parse_conversations
    :summary:
    ```
* - {py:obj}`get_data_records <data.hf_datasets.oasst.get_data_records>`
  - ```{autodoc2-docstring} data.hf_datasets.oasst.get_data_records
    :summary:
    ```
* - {py:obj}`download_and_process_oasst <data.hf_datasets.oasst.download_and_process_oasst>`
  - ```{autodoc2-docstring} data.hf_datasets.oasst.download_and_process_oasst
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`SYSTEM_PROMPT <data.hf_datasets.oasst.SYSTEM_PROMPT>`
  - ```{autodoc2-docstring} data.hf_datasets.oasst.SYSTEM_PROMPT
    :summary:
    ```
````

### API

````{py:data} SYSTEM_PROMPT
:canonical: data.hf_datasets.oasst.SYSTEM_PROMPT
:value: <Multiline-String>

```{autodoc2-docstring} data.hf_datasets.oasst.SYSTEM_PROMPT
```

````

````{py:function} parse_conversations(tree_obj, first: bool = False)
:canonical: data.hf_datasets.oasst.parse_conversations

```{autodoc2-docstring} data.hf_datasets.oasst.parse_conversations
```
````

````{py:function} get_data_records(objs)
:canonical: data.hf_datasets.oasst.get_data_records

```{autodoc2-docstring} data.hf_datasets.oasst.get_data_records
```
````

````{py:function} download_and_process_oasst(output_directory: str = '.', seed: int = 42, split_ratio: float = 0.95) -> dict[str, list]
:canonical: data.hf_datasets.oasst.download_and_process_oasst

```{autodoc2-docstring} data.hf_datasets.oasst.download_and_process_oasst
```
````

````{py:class} OasstDataset(output_dir: str = '.')
:canonical: data.hf_datasets.oasst.OasstDataset

```{autodoc2-docstring} data.hf_datasets.oasst.OasstDataset
```

```{rubric} Initialization
```

```{autodoc2-docstring} data.hf_datasets.oasst.OasstDataset.__init__
```

````
