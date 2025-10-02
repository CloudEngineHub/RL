---
description: "Learn about NeMo RL's core concepts, key features, and fundamental architecture for reinforcement learning with large language models"
categories: ["concepts-architecture"]
tags: ["overview", "concepts", "architecture", "features", "reinforcement-learning", "distributed", "large-language-models"]
personas: ["mle-focused", "researcher-focused", "admin-focused"]
difficulty: "beginner"
content_type: "concept"
modality: "universal"
---

(about-overview)=
# About NeMo RL

NeMo RL is an open-source, comprehensive framework for reinforcement learning and supervised fine-tuning of large language models. Built for scalability and efficiency, NeMo RL enables researchers and practitioners to train and evaluate RL-enhanced language models at scale.

## What is NeMo RL

NeMo RL is an open-source framework that combines the power of reinforcement learning with large language models. It provides a unified platform for training and fine-tuning language models using state-of-the-art RL algorithms.

The framework is designed for distributed training across multiple GPUs and nodes, supporting both research and production training environments. NeMo RL supports multiple backends including Hugging Face Transformers and Megatron-LM, and is focused exclusively on training and evaluation—it does not include production deployment or serving infrastructure.

::::{grid} 1 1 1 2
:gutter: 2 2 2 2

:::{grid-item-card} {octicon}`rocket;1.5em;sd-mr-1` Quick Start
:link: ../get-started/quickstart
:link-type: doc

Get up and running with your first RL training job in minutes.

+++
{bdg-primary}`Beginner`
:::

:::{grid-item-card} {octicon}`gear;1.5em;sd-mr-1` Installation
:link: ../get-started/installation
:link-type: doc

Complete setup instructions for all environments and platforms.

+++
{bdg-success}`Essential`
:::

:::{grid-item-card} {octicon}`book;1.5em;sd-mr-1` Architecture Overview
:link: architecture-overview
:link-type: doc

Learn about NeMo RL's core architecture and design principles.

+++
{bdg-info}`Foundation`
:::

:::{grid-item-card} {octicon}`graph;1.5em;sd-mr-1` Key Features
:link: key-features
:link-type: doc

Explore NeMo RL's key capabilities and technical highlights.

+++
{bdg-secondary}`Overview`
:::

::::

## Target Users

- **Researchers**: Explore state-of-the-art RL algorithms (GRPO, DPO, SFT) with large language models
- **Machine Learning Engineers**: Deploy scalable RL training pipelines with distributed computing
- **DevOps Engineers**: Manage multi-node training clusters and distributed training infrastructure
- **Data Scientists**: Fine-tune language models for specific domains and applications

## Why Choose NeMo RL?

NeMo RL is purpose-built for reinforcement learning with large language models, offering:

### Scale and Performance
- **Model Support**: 0.6B to 70B+ parameter models
- **Advanced Parallelism**: FSDP2, Tensor Parallelism, Pipeline Parallelism, Context Parallelism
- **Distributed Computing**: Ray-based orchestration across multiple nodes and GPUs
- **Memory Optimization**: Gradient checkpointing, mixed precision, efficient batching

### Algorithms and Flexibility
- **State-of-the-Art Algorithms**: GRPO, DPO, SFT with optimized implementations
- **Multiple Backends**: Hugging Face Transformers, Megatron-LM, vLLM integration
- **Extensible Design**: Easy implementation of custom algorithms and environments
- **Algorithm Development**: Clean interfaces for research and experimentation

### Research and Collaboration
- **Reproducibility**: Comprehensive logging and experiment tracking
- **Standardized Workflows**: Consistent patterns for multi-institution projects
- **Built-in Evaluation**: Evaluation frameworks and standardized metrics
- **Training Focused**: Complete tooling for distributed training and evaluation

## NeMo RL and Real-World Applications

NeMo RL enables reinforcement learning with large language models across diverse domains including code generation, mathematical reasoning, human preference alignment, and multi-turn agentic behavior. Each application includes architectural patterns, implementation details, and production considerations for building robust RL systems.

For comprehensive guides with step-by-step implementation, architectural patterns, and production deployment strategies, see the detailed [Use Cases](../learning-resources/use-cases/index) documentation.

## Architecture

NeMo RL's architecture is designed for distributed reinforcement learning with modular components, Ray-based coordination, and support for multiple training backends. The framework provides advanced scalability from single-GPU setups to multi-node clusters with thousands of GPUs.

For comprehensive details on system design, components, scalability, and technical specifications, see the [Architecture Overview](architecture-overview) documentation.

## API and Development

NeMo RL provides a comprehensive Python API for implementing custom reinforcement learning algorithms, environments, and training workflows. The framework offers clean interfaces for algorithm development, environment creation, and distributed training orchestration.

For complete API documentation, code examples, and development guides, see the [API Documentation](../apidocs/index) section.

## Get Started

Ready to begin your NeMo RL journey? Start with the [Quick Start Guide](../get-started/quickstart) for your first training job, or explore the [Installation Guide](../get-started/installation) for complete setup instructions.
