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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SW7ILHS2%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034654Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDMctKoQU4ksmq%2B7Qoepo3xwlFPwE5EKrlpHNHWEBk%2ByAIhAOkvDccUiNV9BhHflHpOuGFW%2Fbyq%2F6FPAcJkNTihk9kbKv8DCHwQABoMNjM3NDIzMTgzODA1IgxVBcbScbyfg2bpbfsq3AObOLcmkKkahFa01gZNij0ZL%2FDYv8%2FBbH%2B%2FwVkJ5pw23tCHMXIkCE6CW963XqEEnxuoJ96pfyCdK7R5pPnhRxAYGDe21UVCRGlBl2tsqbEQjqbPOCudYksrBQExzAvDGDplfynL7milWqOW4a%2FsAC%2BOe6M3IQN5sAfSDbLCYdTD7svpyVVgiTgGOjQxJc9MkRuPcNk7XSHaEcK%2Bbc0ie4B%2BbeSXRHSIZ4kghxBwQ%2FDQFO5X66jAMpG3Zl04btLIWqYyz0Mdr8CLr3uJvLy4WhHoXDWSqxBsdtknZ6pssRHHTgDgXT0PGl6DbDx9QygZmZdnMnXi4siiNbOhVk5nC1I%2BU8MLdomwWX%2F9HZLpNhZE70HlFyS5lsf6BlDaHmQKtkqoThUgmCryEW0zRfB5%2BWIYVnL5dVnLlFudkhbv%2BRqtfRAEyUpw24PFAdSm1Np1zXVhrkA1ZwsX%2FL3tnpveTXQdgovjedF4n5Ea0lGHFxBtpDN1qoFAxjHY%2BBdKVKH92CSJrJ%2FDgKw%2BIlJ6RYMMMG9DGjEzb3zMmAj0Glshi4UCkLhGDBpXznJ5s1iyvA%2BNI5JQXfaJ5osLDfOcjwXXUrk3Y1WqrUC%2FERsUpm4q3qPZyQ8e6%2Fqx0FOcplZjujCP5bzOBjqkAa6TxiyVMcBVlCWl4sMAlM6JSfJdP23EvFOjgwfl4hyCt%2Bql2ggYdLiHKU1ntSUsZgV8zl6%2BvYAiJG1jzQK186VP03kEpqGDmZn5GExV%2B2yRkmnXmwhqsCTLsJ7uJkVQx9A1P7K03Zr5383MwNhlvG0C0MCPq4j%2F33vYyCp42ayTynKgDiUSpJcEk3ZhhmPYo2CBuGq%2FKVkNGyCVVNy66eoy1Hs1&X-Amz-Signature=ea1704ddc5c391347a4b29b6f9ac84144ffc8c264e1a56336e60e0509d3b21f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SW7ILHS2%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034654Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDMctKoQU4ksmq%2B7Qoepo3xwlFPwE5EKrlpHNHWEBk%2ByAIhAOkvDccUiNV9BhHflHpOuGFW%2Fbyq%2F6FPAcJkNTihk9kbKv8DCHwQABoMNjM3NDIzMTgzODA1IgxVBcbScbyfg2bpbfsq3AObOLcmkKkahFa01gZNij0ZL%2FDYv8%2FBbH%2B%2FwVkJ5pw23tCHMXIkCE6CW963XqEEnxuoJ96pfyCdK7R5pPnhRxAYGDe21UVCRGlBl2tsqbEQjqbPOCudYksrBQExzAvDGDplfynL7milWqOW4a%2FsAC%2BOe6M3IQN5sAfSDbLCYdTD7svpyVVgiTgGOjQxJc9MkRuPcNk7XSHaEcK%2Bbc0ie4B%2BbeSXRHSIZ4kghxBwQ%2FDQFO5X66jAMpG3Zl04btLIWqYyz0Mdr8CLr3uJvLy4WhHoXDWSqxBsdtknZ6pssRHHTgDgXT0PGl6DbDx9QygZmZdnMnXi4siiNbOhVk5nC1I%2BU8MLdomwWX%2F9HZLpNhZE70HlFyS5lsf6BlDaHmQKtkqoThUgmCryEW0zRfB5%2BWIYVnL5dVnLlFudkhbv%2BRqtfRAEyUpw24PFAdSm1Np1zXVhrkA1ZwsX%2FL3tnpveTXQdgovjedF4n5Ea0lGHFxBtpDN1qoFAxjHY%2BBdKVKH92CSJrJ%2FDgKw%2BIlJ6RYMMMG9DGjEzb3zMmAj0Glshi4UCkLhGDBpXznJ5s1iyvA%2BNI5JQXfaJ5osLDfOcjwXXUrk3Y1WqrUC%2FERsUpm4q3qPZyQ8e6%2Fqx0FOcplZjujCP5bzOBjqkAa6TxiyVMcBVlCWl4sMAlM6JSfJdP23EvFOjgwfl4hyCt%2Bql2ggYdLiHKU1ntSUsZgV8zl6%2BvYAiJG1jzQK186VP03kEpqGDmZn5GExV%2B2yRkmnXmwhqsCTLsJ7uJkVQx9A1P7K03Zr5383MwNhlvG0C0MCPq4j%2F33vYyCp42ayTynKgDiUSpJcEk3ZhhmPYo2CBuGq%2FKVkNGyCVVNy66eoy1Hs1&X-Amz-Signature=a82198762818ea7ba767247ab7dc570ff6f2f2f349f8d63519b73254aeb7dac8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







