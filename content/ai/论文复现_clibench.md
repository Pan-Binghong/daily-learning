---
title: 论文复现_CliBench
date: '2024-11-13T02:07:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
标签:
- LLMs
- Paper
categories:
- AI
---

> 💡 对大型语言模型在诊断、手术、实验室测试订单和处方等临床决策中的多方面评估。

## 文章介绍

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCNQY67Q%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDpIuvnoasSRpruMbbDfloc89817xKgJu6yP3OHXfdv%2FwIgcJtRkBHlwQs9ZPFlUvrEUJMsfEpiNJqXz76q0XrdNuUqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIztDVcOEK9SCazWmyrcA5HyKj7laBwxlXhqzVe9amTDIXhE5kl0JXYv1VoSjrfpnlXFM7zZOcEpTDh%2BgP%2FIG%2F3kckvQqUE5a7dbwrRuqIu5%2BGtliUoBlJDb6IsXUuiGervhhexZRYO8K1mfvpK6CK80RqXdAxnkMl6FZLkOL%2FuPJ2jqVs2lMCbEZ48R7lh2TBFOTT%2FQUQUCzRrQjLvw8RK2KIfrd8R5M5n%2FrKmgRIuA5NNmOFyHipIfwm7PbUdJTgqF5arYxNntn1EoN1KMY3dSXtPF0MN3OnqDBMu5cRbgLVrgquQvkqenfRjYG%2FQYt5zOU%2Fa3rw%2BMKXWvA1%2FmqQ0LwpWHt5AoMRycoMCrJ0ciSwgAT3Cr1ZI2WcKdjzBRUsY%2BOCPwwgZirdGuB0Jxp97Tld%2Fc%2Bg4%2BRX3Xqh3tsRVxLmfaw0v4%2FKcZixTF1Pj9Zoa1kAEVVF4SsLmyHd1c0x18h4ixoVx2KLYCAvXK4BaykiFnuIRcNftziXk313PHMS5pTjFNkYWe1QcnwboVGvRA%2FFmOafGM1SSI2qOjsaF6MoFiZ2vvE6TMMK8u5R1DJS5BlHvx03qTch4dM94cuK0cz54eC6JCzBR45FJzNw4hHUqKnLbWVEizkBl0pZTbs6hv5hJG1gNTImx8MMSirMgGOqUB4gpZS4aNWRdFqFV2d3Y27VH8CnVMCvKYpBeKIFljWyLUj4wpxZkQDaD%2F34K8Ymo6r6KjoJHZezQTWo3jen1NJSNT9tA%2Fty2V9yL8HMgBKJbGBgsn4c9avMTkGtqEVJwCxOU4oNmOtMQkPodmHfcSqh%2BMfRV7wGvNt4BsRVihzo8USgjIe0ayLBkGIS1kSLIk8dEeO%2B%2BGex9INQTbGtBSMNqXSp5%2B&X-Amz-Signature=6e2079430404c1614cd1fa13e8048f51bc12424681511e9c984b41ff2aaceb1c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCNQY67Q%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDpIuvnoasSRpruMbbDfloc89817xKgJu6yP3OHXfdv%2FwIgcJtRkBHlwQs9ZPFlUvrEUJMsfEpiNJqXz76q0XrdNuUqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIztDVcOEK9SCazWmyrcA5HyKj7laBwxlXhqzVe9amTDIXhE5kl0JXYv1VoSjrfpnlXFM7zZOcEpTDh%2BgP%2FIG%2F3kckvQqUE5a7dbwrRuqIu5%2BGtliUoBlJDb6IsXUuiGervhhexZRYO8K1mfvpK6CK80RqXdAxnkMl6FZLkOL%2FuPJ2jqVs2lMCbEZ48R7lh2TBFOTT%2FQUQUCzRrQjLvw8RK2KIfrd8R5M5n%2FrKmgRIuA5NNmOFyHipIfwm7PbUdJTgqF5arYxNntn1EoN1KMY3dSXtPF0MN3OnqDBMu5cRbgLVrgquQvkqenfRjYG%2FQYt5zOU%2Fa3rw%2BMKXWvA1%2FmqQ0LwpWHt5AoMRycoMCrJ0ciSwgAT3Cr1ZI2WcKdjzBRUsY%2BOCPwwgZirdGuB0Jxp97Tld%2Fc%2Bg4%2BRX3Xqh3tsRVxLmfaw0v4%2FKcZixTF1Pj9Zoa1kAEVVF4SsLmyHd1c0x18h4ixoVx2KLYCAvXK4BaykiFnuIRcNftziXk313PHMS5pTjFNkYWe1QcnwboVGvRA%2FFmOafGM1SSI2qOjsaF6MoFiZ2vvE6TMMK8u5R1DJS5BlHvx03qTch4dM94cuK0cz54eC6JCzBR45FJzNw4hHUqKnLbWVEizkBl0pZTbs6hv5hJG1gNTImx8MMSirMgGOqUB4gpZS4aNWRdFqFV2d3Y27VH8CnVMCvKYpBeKIFljWyLUj4wpxZkQDaD%2F34K8Ymo6r6KjoJHZezQTWo3jen1NJSNT9tA%2Fty2V9yL8HMgBKJbGBgsn4c9avMTkGtqEVJwCxOU4oNmOtMQkPodmHfcSqh%2BMfRV7wGvNt4BsRVihzo8USgjIe0ayLBkGIS1kSLIk8dEeO%2B%2BGex9INQTbGtBSMNqXSp5%2B&X-Amz-Signature=162475c81b3918d62ab38ed70d2b807affa01c1c65d4164a45125a2504b432e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







