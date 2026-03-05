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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQDQ3DX7%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCL6%2BsFbb%2BNT9DNm56ZUcSrPYWz0APtWSj59jOXnlDJnAIhAPJqFIe8U%2FFEyxLjFvJKISI%2BH7d%2BEtSK2Mb41Io3AOulKogECMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxBrAPh4MwlcmihVo4q3AOFwYgVUPukAUtOpDL%2F84jB6gTaOax3vbHcWUSnyD9UVdKBPKilqG3N23MBCdKCnE%2FIAskdjRVqhgmO%2BSE1pwlAsUiCnBcPeYUZSTkSL3lCjkP5EqVI%2FyBrMAQ6ehqOdEhhn84WEcRFPYpBf1qC8yXzEpEc9pHUqnRW5a7WfFyKgK%2FWl2uKxKPkchrrOt74Zfl2XQo0ewlfvvTgDjqnq7137knAAB1lM%2FfakRNeqLu0gT63ND1XEwcWVd%2B2qsGeGPpqK4YRg6HQCHV9pQmh6nCkFq2teQX2NLbOZWI9hDBt0fyHsvDGfO5LU4YWpsM6%2FWOlDURaIu%2BN%2B4iAfPLvrXzV62MOp53NZooWVAU4vTIkl7c0G5TxN%2BcvYijKwic9xX32lFMWaGS2YAG69aNCPnth6RgZml%2FmAHhkAX89tUBcGv8aFZSANr4MRL0za1HIFZa2DAIPMps%2BQBJ7cqb%2B5WnHUd52dpvufbQDOOCdXHncNJbiC1gKVLPLe0jm4QQDOi8bYYivmc%2BYAfODY9xqdocYdJc0B4dhBI5fsGV3QRrNNvqMnkB%2Fa%2FqHcHNI839rHfCL51oJe%2FkEKXS9aVbCl2Tkv6J2c%2FnQwitHByT6ESXgl0%2BpXNYHnO4%2BrW7AMjCO4KPNBjqkAeZxZCSwjhLE1zjeepMDLumASnCzzH8plYPeAWfzQVr2PSRn0Ccgx1FCJfp%2BpQYcRAmNwvfhRkyaovu9o6Jo4Uwv5e%2BEBrXQAXIEhte8k7HF6Ak2PUsD8vMA68%2FABAbir0y9ydxfEh1zfqO4Eh2ouYVWUMT4bQuT8j3BbR6UXDYiMiHOZTGBX7pyiDriqOqVGvkK4VpLRfiA3lZBx9KmcIhywTJQ&X-Amz-Signature=3b102ead4fbca25b3eb80f8b6f3ffd0ce7ee9e2a476549e73db9e0e4352e4481&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQDQ3DX7%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCL6%2BsFbb%2BNT9DNm56ZUcSrPYWz0APtWSj59jOXnlDJnAIhAPJqFIe8U%2FFEyxLjFvJKISI%2BH7d%2BEtSK2Mb41Io3AOulKogECMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxBrAPh4MwlcmihVo4q3AOFwYgVUPukAUtOpDL%2F84jB6gTaOax3vbHcWUSnyD9UVdKBPKilqG3N23MBCdKCnE%2FIAskdjRVqhgmO%2BSE1pwlAsUiCnBcPeYUZSTkSL3lCjkP5EqVI%2FyBrMAQ6ehqOdEhhn84WEcRFPYpBf1qC8yXzEpEc9pHUqnRW5a7WfFyKgK%2FWl2uKxKPkchrrOt74Zfl2XQo0ewlfvvTgDjqnq7137knAAB1lM%2FfakRNeqLu0gT63ND1XEwcWVd%2B2qsGeGPpqK4YRg6HQCHV9pQmh6nCkFq2teQX2NLbOZWI9hDBt0fyHsvDGfO5LU4YWpsM6%2FWOlDURaIu%2BN%2B4iAfPLvrXzV62MOp53NZooWVAU4vTIkl7c0G5TxN%2BcvYijKwic9xX32lFMWaGS2YAG69aNCPnth6RgZml%2FmAHhkAX89tUBcGv8aFZSANr4MRL0za1HIFZa2DAIPMps%2BQBJ7cqb%2B5WnHUd52dpvufbQDOOCdXHncNJbiC1gKVLPLe0jm4QQDOi8bYYivmc%2BYAfODY9xqdocYdJc0B4dhBI5fsGV3QRrNNvqMnkB%2Fa%2FqHcHNI839rHfCL51oJe%2FkEKXS9aVbCl2Tkv6J2c%2FnQwitHByT6ESXgl0%2BpXNYHnO4%2BrW7AMjCO4KPNBjqkAeZxZCSwjhLE1zjeepMDLumASnCzzH8plYPeAWfzQVr2PSRn0Ccgx1FCJfp%2BpQYcRAmNwvfhRkyaovu9o6Jo4Uwv5e%2BEBrXQAXIEhte8k7HF6Ak2PUsD8vMA68%2FABAbir0y9ydxfEh1zfqO4Eh2ouYVWUMT4bQuT8j3BbR6UXDYiMiHOZTGBX7pyiDriqOqVGvkK4VpLRfiA3lZBx9KmcIhywTJQ&X-Amz-Signature=55e11da2c442f23466c2b85ab40a9a5fab910b426c55a08a3f9bdafecab09f4b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







