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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W3YYAFQF%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T025808Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJIMEYCIQCDqivKg3R%2BQfaMCZgCQX9sj2VkyVLLqBt9Pm0KTR%2B4iAIhAJnM6HU4ibTKTss6iabIBXBBxcp9OYE%2B843NaOYQWgSHKogECPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxwvxEGPi28C2vBuw0q3APzEC79NhQ2qgEElU%2F4fM%2B8WoYJ8duDURKwQar2aEXTWwkFv1PTg2TG2tLwC91xaMzfG9cs5lymW8ILsbIA4rsO8gDfq76bLLHrcExrCzs7NtpmqzGM73VrxhCqWcFQathuzbnA3qDvrFX94BIcdLYMvT2UpWho4Hjraq1KW%2Fi%2FKXQAEL6etabVxweBwKyYzrIbX7bpcfY1U%2FMOSyOe4YxkuLG4GosdkuiMq%2FQlBWmjwkzD0q4QXWrvMw0UQNev0YwqhRfuuHKneXCEMI9SnrQqbo2C%2FYW8cgz1ctljh%2BCIA6JIU9H0es3Kedp5UeOfvRChr8AKkHMrFotKH9CJm6HoHrPd2ma7wXDvpGF%2B2lvUvBN5iSmVYPoucFdQXwV6myKz%2Bq1ZY4c0qTbKT0WHgjPIKBALM9cf7spRf7cdItaJmRHL0mtSkq7uV4PCs5yK8QKI3ArkRDT9NZUors6CfzxDqbYCbzlDmcjtLpQnm2kPqVUTD4XCwdBrh8TEXWyG3W3T14s6h9EkfvFnKTVqp%2BFyOHRon4%2Fo6oxNTqFtwhu31KTmT85SAH%2FN%2BwX4gGAMleRkUgkaemDBTaZ4L6BuC4PlTYXhzVrE2eQkXemnMAmmy0Q3wR29GEsYX%2F6%2FdjDH5ZbLBjqkAavfvEX8nVkEjHfFxIE5E4ZtwJBeYrPfrgVw1FLIXfzCLGTAkGtFYEtmzpH3K7NgTfD4y86X1aBVXnDkPDRSAIWAVb2gjJnmvj6LdlAZ%2BHIByi63M2OypwxpT6p%2BQ2Ab9arbFUW1h5IYTZgeTWkktH%2BhhSvJe4FA05QOwKIGbETiH9Ok66axGbKmYPOU02or7lo2ZXmxd1XJH9qD5ieMAf4WitJG&X-Amz-Signature=b62b4429db7c1ddb9c2f0fe6fc7a4a8c87931a0716174b00d3d7bb76eae52bb5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W3YYAFQF%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T025808Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJIMEYCIQCDqivKg3R%2BQfaMCZgCQX9sj2VkyVLLqBt9Pm0KTR%2B4iAIhAJnM6HU4ibTKTss6iabIBXBBxcp9OYE%2B843NaOYQWgSHKogECPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxwvxEGPi28C2vBuw0q3APzEC79NhQ2qgEElU%2F4fM%2B8WoYJ8duDURKwQar2aEXTWwkFv1PTg2TG2tLwC91xaMzfG9cs5lymW8ILsbIA4rsO8gDfq76bLLHrcExrCzs7NtpmqzGM73VrxhCqWcFQathuzbnA3qDvrFX94BIcdLYMvT2UpWho4Hjraq1KW%2Fi%2FKXQAEL6etabVxweBwKyYzrIbX7bpcfY1U%2FMOSyOe4YxkuLG4GosdkuiMq%2FQlBWmjwkzD0q4QXWrvMw0UQNev0YwqhRfuuHKneXCEMI9SnrQqbo2C%2FYW8cgz1ctljh%2BCIA6JIU9H0es3Kedp5UeOfvRChr8AKkHMrFotKH9CJm6HoHrPd2ma7wXDvpGF%2B2lvUvBN5iSmVYPoucFdQXwV6myKz%2Bq1ZY4c0qTbKT0WHgjPIKBALM9cf7spRf7cdItaJmRHL0mtSkq7uV4PCs5yK8QKI3ArkRDT9NZUors6CfzxDqbYCbzlDmcjtLpQnm2kPqVUTD4XCwdBrh8TEXWyG3W3T14s6h9EkfvFnKTVqp%2BFyOHRon4%2Fo6oxNTqFtwhu31KTmT85SAH%2FN%2BwX4gGAMleRkUgkaemDBTaZ4L6BuC4PlTYXhzVrE2eQkXemnMAmmy0Q3wR29GEsYX%2F6%2FdjDH5ZbLBjqkAavfvEX8nVkEjHfFxIE5E4ZtwJBeYrPfrgVw1FLIXfzCLGTAkGtFYEtmzpH3K7NgTfD4y86X1aBVXnDkPDRSAIWAVb2gjJnmvj6LdlAZ%2BHIByi63M2OypwxpT6p%2BQ2Ab9arbFUW1h5IYTZgeTWkktH%2BhhSvJe4FA05QOwKIGbETiH9Ok66axGbKmYPOU02or7lo2ZXmxd1XJH9qD5ieMAf4WitJG&X-Amz-Signature=6e0cb4643827bf5036a9d420c3f4702d5ea3edace0acd003b550c76b53c078cd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







