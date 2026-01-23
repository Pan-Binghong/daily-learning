---
title: 论文复现_CliBench
date: '2024-11-13T02:07:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
tags:
- LLMs
- Paper
categories:
- AI
---

> 💡 对大型语言模型在诊断、手术、实验室测试订单和处方等临床决策中的多方面评估。

## 文章介绍

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ASANNT4%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030149Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIQDynkV3yCNDtwoa0bG0QsNGeAzKHNUXVzpld6Gxo%2B09sgIgb6ypBxqYO4HZ3m%2F%2BkvEx6gqfRDkr981FS%2FBaJWHF0TAqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCb2m0i1%2F50X9b2VkyrcAzLh0MTtfFZwTBnZxnkSlaJnG5BP6wuBCat3MYgkmJepTAIdzlhCUWavsh2IUCtJxivSFd5zI7wHzyGYUIraLrrSZ8AoZm1JD%2FZq%2B4sadSbeYcKLLDY8w7mGxChpLXj3J2VxExoAE%2F8tA7JpbBJYlIontIy8P7%2BkdkBnkCppbT7pDJH1mhqdthUy9BDjOwNLam%2BgQJTQtyKo97x12zq%2BestEX8sUyLhsyzknenFD3p%2BA%2FMK8JNLmTJWwKQPxkpTxQ5fIe%2BTVVAQR9sORePGc5patF3bhqC7%2BxxmruQP%2FC6%2FLk2c8ArGh7L7H%2BiackiT1g3nU6wD6iaDxFuTAvLtt6dIYCeMnfl3sxmsSmdDt3zasB6E1n3TxlW2YclrcpoN81LzuAgAu%2BQeXx0yWYDX2jXFCmiPc59vsARIIsh%2BVcUfFGkwo5Qxto1puOm2At5ZkyrujbvkR8zWLt3wsnnqvkeJdY9vB7WChJACg7haYFlYk9sk35rAYI67PzDmFZukTVF9XyV6WjpUzpUE2H8%2BC%2Fqcv41l9dW3aE31vnmnVRsRMV2mexzmnpwr%2BviOzOtVdicuzF3DqCQKTTNGJs9lXxDA7F9xTnfubfWxqquo2r9Hknku69hAoHjcxgMmFMPyuy8sGOqUB7nI%2B4UsEnF7oY%2BKzPO6twt%2FKCm3qO1%2FKuX%2FGpfBjVhX2C11NKwhljfx%2Bnv9Uo0nZENjo7ROhWETdGFMDSbkjXMuJs%2F9qO%2BRk2KgDFm9%2BWcoNY34OcvRE9Hxtf55d4m84pIQQTM3tJoOHXpXH%2FohhzDvc3e9u0ZWMfbWoSX8OzRAdggD3LKaE00SLR7n7%2FW%2F%2BjXSlohZBeFliU4yXHOwzt6FuTTIl&X-Amz-Signature=19165dc8d5881371b5aa6e1e2898b6dc15ba13024191459aa83e860dd68511aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ASANNT4%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030149Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIQDynkV3yCNDtwoa0bG0QsNGeAzKHNUXVzpld6Gxo%2B09sgIgb6ypBxqYO4HZ3m%2F%2BkvEx6gqfRDkr981FS%2FBaJWHF0TAqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCb2m0i1%2F50X9b2VkyrcAzLh0MTtfFZwTBnZxnkSlaJnG5BP6wuBCat3MYgkmJepTAIdzlhCUWavsh2IUCtJxivSFd5zI7wHzyGYUIraLrrSZ8AoZm1JD%2FZq%2B4sadSbeYcKLLDY8w7mGxChpLXj3J2VxExoAE%2F8tA7JpbBJYlIontIy8P7%2BkdkBnkCppbT7pDJH1mhqdthUy9BDjOwNLam%2BgQJTQtyKo97x12zq%2BestEX8sUyLhsyzknenFD3p%2BA%2FMK8JNLmTJWwKQPxkpTxQ5fIe%2BTVVAQR9sORePGc5patF3bhqC7%2BxxmruQP%2FC6%2FLk2c8ArGh7L7H%2BiackiT1g3nU6wD6iaDxFuTAvLtt6dIYCeMnfl3sxmsSmdDt3zasB6E1n3TxlW2YclrcpoN81LzuAgAu%2BQeXx0yWYDX2jXFCmiPc59vsARIIsh%2BVcUfFGkwo5Qxto1puOm2At5ZkyrujbvkR8zWLt3wsnnqvkeJdY9vB7WChJACg7haYFlYk9sk35rAYI67PzDmFZukTVF9XyV6WjpUzpUE2H8%2BC%2Fqcv41l9dW3aE31vnmnVRsRMV2mexzmnpwr%2BviOzOtVdicuzF3DqCQKTTNGJs9lXxDA7F9xTnfubfWxqquo2r9Hknku69hAoHjcxgMmFMPyuy8sGOqUB7nI%2B4UsEnF7oY%2BKzPO6twt%2FKCm3qO1%2FKuX%2FGpfBjVhX2C11NKwhljfx%2Bnv9Uo0nZENjo7ROhWETdGFMDSbkjXMuJs%2F9qO%2BRk2KgDFm9%2BWcoNY34OcvRE9Hxtf55d4m84pIQQTM3tJoOHXpXH%2FohhzDvc3e9u0ZWMfbWoSX8OzRAdggD3LKaE00SLR7n7%2FW%2F%2BjXSlohZBeFliU4yXHOwzt6FuTTIl&X-Amz-Signature=1c0158da4799eeaf2d96909bf33439e3b6b8af12f8c4642d79f7472f7f8d7831&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 复现流程

### 下载数据

- 数据申请
- 下载 NDC 代码元数据并将ndc_metadata.json放在code_sys/NDC目录下。
### 安装环境依赖

### 运行实验

- 数据处理
- 生成输出
- 计算分数


---

### References

> https://github.com/CliBench/CliBench







