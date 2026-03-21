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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YWBAEKE%2F20260321%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260321T032342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQD6fOb75GQZZ4XU2pKnXBJAD%2B4T9lu%2FnlB62EQYsyvefgIgaGRtW8ySm68acSY%2FqxDfs3pKxAJ4oPMqAfR8TwIegTEq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDBBWUmdQmlKU0tVfFCrcA1gxi8yNky7qfR3nh8jtH0NBqc%2BnZRtfP0L5Dcq68mdy1pOta7RKiiuyOj9R1WdUbgcSFPKjxzvkoG2TwDfCFQ7twQUQg8Dkmg66axO6Js90EQxOTADf%2BQrH7caqxusBRmZ06kzy4PvqOkTqr6OKn2DVCMILwD%2BCWq%2BibvA3XITjonZcZklKXREH91KuKLwD0kl0fnTmczmJIKu4i5MgHTlAJtP8OsHRECYAd6kb7MuDu1fnAiBs7u0N%2BAfJrH9ArwjmH%2FRkddVNr%2FVLtvKn7p%2FifyLnp4T8qQZCvmC%2BHq9%2F7IBZ4mS62lkNZJb6Vne22eqjwB%2FElnCYs4DPm17O5%2BoFmkgJUmJaCxQ6YrR5Vi174jTVsv943W1pyEyhZ3W7KhTDR9AA%2BfLFhFm0Lo9%2FuN1GjsAIbdfrCmSxqNtlH38LfvAb5OgecUpyjmbp6Ad%2Fw5yJm0r%2F7sBFHRrGDxx1Cnv9DJn%2FQs0hvw4pjDSvEpyEAYyazOg4u8Xw6IJlJyVCrSKKIZxj4glQZPyQtaZG9LhoQEsob0qDH492UWoslCPMegrtzjUuOrWvueMkGDIuwrbLVFqE4XCaUZLDhKw%2B9boVn0KIXzXq52tZCBRei%2B6GrwAdox%2FP7%2Fix%2Bn6CMKOP%2BM0GOqUB%2FltFro2MvEiaqW8u2%2Fb9l1qCFVKF%2Fo3WI8wLcvGn19dyuK75esYRu%2Bx6WWK0LV6C3OvoyEUeGpESCUMi4B8r32Wh1H7ML3nt1u3hk3nJ9E%2FVXSJEOekwE2CFtYcua05d9bJR9Yw51WsO0RrCRsJVYIS%2BfG5zJh4AeskeVrDXJivAR3VUYy%2BqW0xReoRBUiyFkLaMyC0AYd2nYuOPEM%2Fc%2FrFi8%2F6z&X-Amz-Signature=d0e55a5068bc49acc0d82101f67f208695eb561f803ad7da64eaa0dda69510bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YWBAEKE%2F20260321%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260321T032342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQD6fOb75GQZZ4XU2pKnXBJAD%2B4T9lu%2FnlB62EQYsyvefgIgaGRtW8ySm68acSY%2FqxDfs3pKxAJ4oPMqAfR8TwIegTEq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDBBWUmdQmlKU0tVfFCrcA1gxi8yNky7qfR3nh8jtH0NBqc%2BnZRtfP0L5Dcq68mdy1pOta7RKiiuyOj9R1WdUbgcSFPKjxzvkoG2TwDfCFQ7twQUQg8Dkmg66axO6Js90EQxOTADf%2BQrH7caqxusBRmZ06kzy4PvqOkTqr6OKn2DVCMILwD%2BCWq%2BibvA3XITjonZcZklKXREH91KuKLwD0kl0fnTmczmJIKu4i5MgHTlAJtP8OsHRECYAd6kb7MuDu1fnAiBs7u0N%2BAfJrH9ArwjmH%2FRkddVNr%2FVLtvKn7p%2FifyLnp4T8qQZCvmC%2BHq9%2F7IBZ4mS62lkNZJb6Vne22eqjwB%2FElnCYs4DPm17O5%2BoFmkgJUmJaCxQ6YrR5Vi174jTVsv943W1pyEyhZ3W7KhTDR9AA%2BfLFhFm0Lo9%2FuN1GjsAIbdfrCmSxqNtlH38LfvAb5OgecUpyjmbp6Ad%2Fw5yJm0r%2F7sBFHRrGDxx1Cnv9DJn%2FQs0hvw4pjDSvEpyEAYyazOg4u8Xw6IJlJyVCrSKKIZxj4glQZPyQtaZG9LhoQEsob0qDH492UWoslCPMegrtzjUuOrWvueMkGDIuwrbLVFqE4XCaUZLDhKw%2B9boVn0KIXzXq52tZCBRei%2B6GrwAdox%2FP7%2Fix%2Bn6CMKOP%2BM0GOqUB%2FltFro2MvEiaqW8u2%2Fb9l1qCFVKF%2Fo3WI8wLcvGn19dyuK75esYRu%2Bx6WWK0LV6C3OvoyEUeGpESCUMi4B8r32Wh1H7ML3nt1u3hk3nJ9E%2FVXSJEOekwE2CFtYcua05d9bJR9Yw51WsO0RrCRsJVYIS%2BfG5zJh4AeskeVrDXJivAR3VUYy%2BqW0xReoRBUiyFkLaMyC0AYd2nYuOPEM%2Fc%2FrFi8%2F6z&X-Amz-Signature=a8101347aab6cc0517affaa88dfa952178a0468ff1473f65f4c0deab08e69add&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







