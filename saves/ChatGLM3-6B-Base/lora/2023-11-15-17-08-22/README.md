---
base_model: F:\Models\ChatGLM-3\chatglm3-6b-base
tags:
- llama-factory
- lora
- generated_from_trainer
model-index:
- name: 2023-11-15-17-08-22
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 2023-11-15-17-08-22

This model is a fine-tuned version of [F:\Models\ChatGLM-3\chatglm3-6b-base](https://huggingface.co/F:\Models\ChatGLM-3\chatglm3-6b-base) on the self_cognition dataset.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 1
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 4
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- num_epochs: 3.0

### Training results



### Framework versions

- Transformers 4.34.1
- Pytorch 2.1.0+cu121
- Datasets 2.14.6
- Tokenizers 0.14.1
