---
description: "Data handling, processing, and persistence mechanisms in NeMo RL."
tags: ["data", "management", "processing", "formats"]
categories: ["data-management"]
---

# Data Management

This section covers data handling, processing, and persistence mechanisms in NeMo RL. Learn how the framework manages different data formats, implements efficient padding strategies, and maintains model state.

## What You'll Find Here

- **Chat Datasets**: Explore the design of chat dataset processing and conversation handling
- **Padding**: Learn about padding strategies and their impact on training efficiency

## Data Management

::::{grid} 1 1 1 2
:gutter: 2 2 2 2

:::{grid-item-card} {octicon}`database;1.5em;sd-mr-1` Chat Datasets
:link: chat-datasets
:link-type: doc

Explore the design of chat dataset processing and conversation handling.

+++
{bdg-info}`Data`
:::

:::{grid-item-card} {octicon}`gear;1.5em;sd-mr-1` Padding
:link: padding
:link-type: doc

Learn about padding strategies and their impact on training efficiency.

+++
{bdg-secondary}`Optimization`
:::



::::

---

::::{toctree}
:hidden:
:caption: Data Management
:maxdepth: 2
chat-datasets
padding
checkpointing
:::: 

 