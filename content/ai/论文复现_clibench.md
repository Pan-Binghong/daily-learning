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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SNKT7PR%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPf1WXof6dV0ulu6nlHBXntxsRBwG8pyyilnLiJLPWsAIgcYuP%2FT%2FJbTaGCONBCcJrGrwIRgD%2Bdwl9FhFB4Y67KAwq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDMjfDKLwXUO6D2du1ircA5CHdgBDqGEQpEI4AVtxvXYv0FZNIfR44DJ4QNhFoyJYguqJACHB9%2BiohaV5YWBmkKXuiOSZZz%2B2YfFqKTBCQgMucVvRQm4Io%2F%2Bo%2FafxOh1Ih57%2BTZ1Tw4%2FK2w0zDjdFRUjB6DSLFlbNGbGaiJzl1qJ2z4pXFlKSKpMSJ98XigOxMRZ4WD76cZyZ975q2%2BXPL3n8DPnN6uofdJvyIx8v5fgL0ZiMIC%2FXwQw3zv0x%2FS0jkp9Ar8qVkp3C%2BIEYR3MfWfA98FrtEPl4IrhBadfEd06z4BqUkTXKaQftiZPINsZL8S1od%2BgVCaRu9R2u2hGw1w1zYwMbHKeSQiECD%2Fe8Ae8z1bIyhiUQVSjKVIQBPKKPqgIDnV9U94Qsm4byaaqqWqCN8rCmCJubOtol2GkfwrGCvWt2Hqn8PUuoEUUFGBVi2ZYMXIIINkOb%2BFbt9ogWPn%2Fv0%2F64q2oxuXeM0e3tRo8YlS2S1X69wsL9f%2BzQfmmpdc8pBT1C3G%2B3DkAszbe1yuic6lUGcrKaZtzkhrS%2FXve5PmmbL391xZ1eqXSE0S3W2VwJJVkdgBbYc5MgrQm6KL0QgsAo5iNIif%2BJrwgZrfKZzDYAJ%2FyEkt2oUjhCsMGf4RdR5GzVyMlksSsXMOWvt84GOqUBQ6ocqoQG8FZe3XHT%2FcKEPx%2FUkzhP5%2FwOI6ROZt4%2FyqI53298G9DLw8droOQEsBYohf2BGtBVMDh5MwpdZWlYofqpqN9vDXZ2RaVRMubLmKCihcnX5KZ%2BXHfNduLT%2BNYyV5ulBVLho5xoxZKmOdjsxdBb6TMrDf%2BMy7C5eLqtF9Bo44C1%2BWEZIFBp99G91KNWMYaHfuTaOj%2BbPAN8EupcygeZC43j&X-Amz-Signature=5644acd23030a7e334de1d55fcadb74793fbc769a2bb5ebe5559f404f7f61d59&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SNKT7PR%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPf1WXof6dV0ulu6nlHBXntxsRBwG8pyyilnLiJLPWsAIgcYuP%2FT%2FJbTaGCONBCcJrGrwIRgD%2Bdwl9FhFB4Y67KAwq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDMjfDKLwXUO6D2du1ircA5CHdgBDqGEQpEI4AVtxvXYv0FZNIfR44DJ4QNhFoyJYguqJACHB9%2BiohaV5YWBmkKXuiOSZZz%2B2YfFqKTBCQgMucVvRQm4Io%2F%2Bo%2FafxOh1Ih57%2BTZ1Tw4%2FK2w0zDjdFRUjB6DSLFlbNGbGaiJzl1qJ2z4pXFlKSKpMSJ98XigOxMRZ4WD76cZyZ975q2%2BXPL3n8DPnN6uofdJvyIx8v5fgL0ZiMIC%2FXwQw3zv0x%2FS0jkp9Ar8qVkp3C%2BIEYR3MfWfA98FrtEPl4IrhBadfEd06z4BqUkTXKaQftiZPINsZL8S1od%2BgVCaRu9R2u2hGw1w1zYwMbHKeSQiECD%2Fe8Ae8z1bIyhiUQVSjKVIQBPKKPqgIDnV9U94Qsm4byaaqqWqCN8rCmCJubOtol2GkfwrGCvWt2Hqn8PUuoEUUFGBVi2ZYMXIIINkOb%2BFbt9ogWPn%2Fv0%2F64q2oxuXeM0e3tRo8YlS2S1X69wsL9f%2BzQfmmpdc8pBT1C3G%2B3DkAszbe1yuic6lUGcrKaZtzkhrS%2FXve5PmmbL391xZ1eqXSE0S3W2VwJJVkdgBbYc5MgrQm6KL0QgsAo5iNIif%2BJrwgZrfKZzDYAJ%2FyEkt2oUjhCsMGf4RdR5GzVyMlksSsXMOWvt84GOqUBQ6ocqoQG8FZe3XHT%2FcKEPx%2FUkzhP5%2FwOI6ROZt4%2FyqI53298G9DLw8droOQEsBYohf2BGtBVMDh5MwpdZWlYofqpqN9vDXZ2RaVRMubLmKCihcnX5KZ%2BXHfNduLT%2BNYyV5ulBVLho5xoxZKmOdjsxdBb6TMrDf%2BMy7C5eLqtF9Bo44C1%2BWEZIFBp99G91KNWMYaHfuTaOj%2BbPAN8EupcygeZC43j&X-Amz-Signature=64e97ce67ed8a2a9d878d7d837409eae12efb56028476e86cb431ba47a0a05d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







