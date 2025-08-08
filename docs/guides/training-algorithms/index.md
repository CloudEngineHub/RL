---
description: "Comprehensive guides for all core RL training algorithms in NeMo RL including SFT, DPO, GRPO, and evaluation"
categories: ["training-algorithms"]
tags: ["training-algorithms", "sft", "dpo", "grpo", "evaluation", "reinforcement-learning"]
personas: ["mle-focused", "researcher-focused"]
difficulty: "intermediate"
content_type: "concept"
modality: "universal"
---

# Training Algorithms

Welcome to the NeMo RL Training Algorithms guide! This section covers all the core reinforcement learning algorithms available in NeMo RL, from foundational supervised fine-tuning to advanced preference optimization techniques.

## Overview

NeMo RL provides a comprehensive suite of training algorithms designed for reinforcement learning with large language models. Each algorithm serves specific use cases and training objectives, from basic supervised learning to advanced preference-based optimization.

## Core Algorithms

::::{grid} 1 2 2 2
:gutter: 2 2 2 2

:::{grid-item-card} {octicon}`play;1.5em;sd-mr-1` Supervised Fine-Tuning (SFT)
:link: sft
:link-type: doc

The foundation of RL training - learn supervised fine-tuning for language models with human feedback data.

+++
{bdg-primary}`Beginner`
:::

:::{grid-item-card} {octicon}`heart;1.5em;sd-mr-1` Direct Preference Optimization (DPO)
:link: dpo
:link-type: doc

Direct preference optimization for aligning language models with human preferences using preference data.

+++
{bdg-info}`Intermediate`
:::

:::{grid-item-card} {octicon}`graph;1.5em;sd-mr-1` Group Relative Policy Optimization (GRPO)
:link: grpo
:link-type: doc

Advanced reinforcement learning algorithm for training language models with group-based optimization.

+++
{bdg-warning}`Advanced`
:::

:::{grid-item-card} {octicon}`graph;1.5em;sd-mr-1` Evaluation
:link: eval
:link-type: doc

Comprehensive evaluation and benchmarking strategies for RL-trained language models.

+++
{bdg-secondary}`Analysis`
:::

::::

## Algorithm Comparison

| Algorithm | Use Case | Difficulty | Data Requirements | Training Speed |
|-----------|----------|------------|-------------------|----------------|
| **SFT** | Domain adaptation, instruction following | Beginner | Supervised pairs | Fast |
| **DPO** | Preference alignment, safety | Intermediate | Preference pairs | Medium |
| **GRPO** | Advanced RL, group optimization | Advanced | Preference + groups | Slow |

## When to Use Each Algorithm

### Supervised Fine-Tuning (SFT)
**Best for:**
- Learning from high-quality demonstrations
- Domain adaptation and instruction following
- Quick prototyping and baseline establishment
- When you have supervised training data

**Key Benefits:**
- Fastest training algorithm
- Simple to implement and debug
- Works well with existing datasets
- Good starting point for RL workflows

### Direct Preference Optimization (DPO)
**Best for:**
- Aligning models with human preferences
- Safety and helpfulness optimization
- When you have preference data (A/B comparisons)
- Improving model behavior without RL complexity

**Key Benefits:**
- Direct optimization of preferences
- No need for reward model training
- Stable training process
- Good balance of simplicity and effectiveness

### Group Relative Policy Optimization (GRPO)
**Best for:**
- Advanced reinforcement learning scenarios
- Group-based optimization objectives
- Research and experimentation
- When you need fine-grained control over training

**Key Benefits:**
- Most flexible algorithm
- Supports complex reward structures
- Advanced optimization techniques
- Research-grade capabilities

## Training Workflow

### 1. Start with SFT
Begin your RL journey with supervised fine-tuning to establish a strong baseline:

```bash
# Basic SFT training
python -m nemo_rl.train --config sft_config.yaml
```

### 2. Add Preference Learning
Once you have a good SFT model, add preference optimization:

```bash
# DPO training with preference data
python -m nemo_rl.train --config dpo_config.yaml
```

### 3. Advanced Optimization
For research or complex scenarios, use GRPO:

```bash
# GRPO with custom reward functions
python -m nemo_rl.train --config grpo_config.yaml
```

### 4. Evaluate and Iterate
Continuously evaluate your models and refine your approach:

```bash
# Comprehensive evaluation
python -m nemo_rl.eval --config eval_config.yaml
```

## Data Requirements

### SFT Data
- **Format**: Input-output pairs
- **Example**: `{"input": "Translate to French", "output": "Traduire en français"}`
- **Size**: 1K-100K examples typically sufficient

### DPO Data
- **Format**: Preference pairs with chosen/rejected responses
- **Example**: `{"prompt": "Explain quantum physics", "chosen": "Good explanation", "rejected": "Poor explanation"}`
- **Size**: 1K-10K preference pairs recommended

### GRPO Data
- **Format**: Flexible, supports custom reward structures
- **Example**: Group-based preferences with additional metadata
- **Size**: Varies based on complexity

## Performance Considerations

### Training Speed
- **SFT**: Fastest (hours to days)
- **DPO**: Medium (days to weeks)
- **GRPO**: Slowest (weeks to months)

### Memory Requirements
- **SFT**: Lowest memory usage
- **DPO**: Moderate memory usage
- **GRPO**: Highest memory usage

### Scaling Considerations
- Start with smaller models for experimentation
- Use distributed training for larger models
- Monitor GPU memory usage carefully

## Best Practices

### 1. Start Simple
- Begin with SFT to establish baselines
- Use small datasets for initial experiments
- Validate your data quality before scaling

### 2. Iterate Gradually
- Move from SFT → DPO → GRPO as needed
- Evaluate at each step
- Don't skip foundational algorithms

### 3. Monitor Training
- Track loss curves and metrics
- Use validation sets for early stopping
- Monitor for training instability

### 4. Evaluate Thoroughly
- Use multiple evaluation metrics
- Test on diverse prompts
- Compare against baselines

## Common Challenges

### Training Instability
- **Solution**: Use gradient clipping and learning rate scheduling
- **Prevention**: Start with conservative hyperparameters

### Data Quality Issues
- **Solution**: Clean and validate your datasets
- **Prevention**: Establish data quality pipelines

### Memory Constraints
- **Solution**: Use gradient checkpointing and model parallelism
- **Prevention**: Start with smaller models

### Evaluation Complexity
- **Solution**: Use automated evaluation pipelines
- **Prevention**: Define clear evaluation criteria upfront

## Next Steps

- [SFT Training](sft.md) - Learn supervised fine-tuning fundamentals
- [DPO Training](dpo.md) - Master preference optimization
- [GRPO Training](grpo.md) - Explore advanced RL techniques
- [Evaluation](eval.md) - Comprehensive model evaluation
- [Model Development](../model-development/index) - Customize models for your use case
- [Performance Optimization](../training-optimization/index) - Optimize training efficiency

## Get Help

- [Troubleshooting](../troubleshooting) - Common training issues and solutions
- [API Documentation](../../../api/index) - Complete algorithm documentation
- [Configuration Reference](../../../references/configuration-reference) - Training parameters
- [Community Support](https://github.com/NVIDIA/NeMo-RL/issues) - GitHub discussions

---

::::{toctree}
:hidden:
:caption: Training Algorithms
:maxdepth: 2
sft
dpo
grpo
eval
:::::

 