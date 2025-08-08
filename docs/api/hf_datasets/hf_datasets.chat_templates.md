# {py:mod}`hf_datasets.chat_templates`

```{py:module} hf_datasets.chat_templates
```

```{autodoc2-docstring} hf_datasets.chat_templates
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`COMMON_CHAT_TEMPLATES <hf_datasets.chat_templates.COMMON_CHAT_TEMPLATES>`
  - ```{autodoc2-docstring} hf_datasets.chat_templates.COMMON_CHAT_TEMPLATES
    :summary:
    ```
````

### API

`````{py:class} COMMON_CHAT_TEMPLATES
:canonical: hf_datasets.chat_templates.COMMON_CHAT_TEMPLATES

```{autodoc2-docstring} hf_datasets.chat_templates.COMMON_CHAT_TEMPLATES
```

````{py:attribute} simple_role_header
:canonical: hf_datasets.chat_templates.COMMON_CHAT_TEMPLATES.simple_role_header
:value: <Multiline-String>

```{autodoc2-docstring} hf_datasets.chat_templates.COMMON_CHAT_TEMPLATES.simple_role_header
```

````

````{py:attribute} passthrough_prompt_response
:canonical: hf_datasets.chat_templates.COMMON_CHAT_TEMPLATES.passthrough_prompt_response
:value: >
   "{% for message in messages %}{{ message['content'] }}{% endfor %}"

```{autodoc2-docstring} hf_datasets.chat_templates.COMMON_CHAT_TEMPLATES.passthrough_prompt_response
```

````

`````
