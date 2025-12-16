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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VY2YGD3L%2F20251216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251216T025502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE%2FNvLMfRHWoO5FRQGcQTuuklQuA68rrjMhvSLpQv1itAiB7AOG46%2Fu2N8MX5keSynm0dXAaYcNmtKp2Efc3QPdPPCr%2FAwhcEAAaDDYzNzQyMzE4MzgwNSIMzidlHr%2BrvoRGB6cfKtwDzNr2nApe5wEvi57xnD%2BieKSizCHmxdlL%2BDMWOGzQwk6Bq8fknt0eelemkUmsb%2BgXAu9XEJj4ijk%2Bbm49TPmEc4CVeKaBbxNqdONCy1vKw384%2FmGhTXyvqx4NRpU%2BfPPSXo1otd%2FVkDRHozi0ar%2F4fCramegxKsYt5L0%2FMqUiAsywZ2DhXGNSUWwmCgUDuTnRIiXuXx15sV9EXijqw3stGZ0k3MyLrltZ38J3EcAftq7QsCLbVrmbYdOn1VzR%2B0UIt%2BwVOzZBps8cXjLFZhEuheN%2Bi1%2BiB3WBjJph5ZAoY4DtNIrmjgVn8t5ymV6ZGs64E1hCDbxMP7TAkP%2BhgvabrNaLGDmnSk%2BDVcB3J1qquM5KntzYdeqpNsUVGL%2BxrinHfOqPtTtEKEECAyn8GTzFAG1gqnpKalyZr%2FdOBN5884OnI6bDsHRNsNX3X1v3SYQEhQ6jkb%2BSyUIfdXLn7LIu9ZgPdzZl4IaNSEpjam%2Fn8W8dEBEueRISZ78aFjCyzKtpmsiOqyqrtgh3lUZsGFxbg%2B%2BZIB39zMD2r3BOl7FL9JEuDZLn7JtFtSN35BkYbZ9y3wjPqHNIggzDvxRmgUCQ5vUPpvujL8hKqEBKlFbV4deBbR5azVeByWPL6kow9o2DygY6pgH67qdcscn6urtL3s8haqtpjrnLOdpCwu%2BVndcrMPlryL0Z2y9skeQ47836sRcdRIsqab8%2BClVoPd%2BSLVgCI0HwwCmDUkZKyMaBoYdZQ9pSKkz42zS3xsGJ6mADULZ3OTcanwdRMEM29MSVyag%2FB5OYV%2FFSv1q9UlVBPul1Lv872ImBBn89dApdmvXKKIdkY8kTj2x2ihWF%2BJRWLKh%2FeevN3DrIOKyH&X-Amz-Signature=a82ad6e01ddd719330f016dcb9c32daaa9cc771283bed2031fcb7e611a6f120c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VY2YGD3L%2F20251216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251216T025502Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE%2FNvLMfRHWoO5FRQGcQTuuklQuA68rrjMhvSLpQv1itAiB7AOG46%2Fu2N8MX5keSynm0dXAaYcNmtKp2Efc3QPdPPCr%2FAwhcEAAaDDYzNzQyMzE4MzgwNSIMzidlHr%2BrvoRGB6cfKtwDzNr2nApe5wEvi57xnD%2BieKSizCHmxdlL%2BDMWOGzQwk6Bq8fknt0eelemkUmsb%2BgXAu9XEJj4ijk%2Bbm49TPmEc4CVeKaBbxNqdONCy1vKw384%2FmGhTXyvqx4NRpU%2BfPPSXo1otd%2FVkDRHozi0ar%2F4fCramegxKsYt5L0%2FMqUiAsywZ2DhXGNSUWwmCgUDuTnRIiXuXx15sV9EXijqw3stGZ0k3MyLrltZ38J3EcAftq7QsCLbVrmbYdOn1VzR%2B0UIt%2BwVOzZBps8cXjLFZhEuheN%2Bi1%2BiB3WBjJph5ZAoY4DtNIrmjgVn8t5ymV6ZGs64E1hCDbxMP7TAkP%2BhgvabrNaLGDmnSk%2BDVcB3J1qquM5KntzYdeqpNsUVGL%2BxrinHfOqPtTtEKEECAyn8GTzFAG1gqnpKalyZr%2FdOBN5884OnI6bDsHRNsNX3X1v3SYQEhQ6jkb%2BSyUIfdXLn7LIu9ZgPdzZl4IaNSEpjam%2Fn8W8dEBEueRISZ78aFjCyzKtpmsiOqyqrtgh3lUZsGFxbg%2B%2BZIB39zMD2r3BOl7FL9JEuDZLn7JtFtSN35BkYbZ9y3wjPqHNIggzDvxRmgUCQ5vUPpvujL8hKqEBKlFbV4deBbR5azVeByWPL6kow9o2DygY6pgH67qdcscn6urtL3s8haqtpjrnLOdpCwu%2BVndcrMPlryL0Z2y9skeQ47836sRcdRIsqab8%2BClVoPd%2BSLVgCI0HwwCmDUkZKyMaBoYdZQ9pSKkz42zS3xsGJ6mADULZ3OTcanwdRMEM29MSVyag%2FB5OYV%2FFSv1q9UlVBPul1Lv872ImBBn89dApdmvXKKIdkY8kTj2x2ihWF%2BJRWLKh%2FeevN3DrIOKyH&X-Amz-Signature=d6aaaee9d0e0a0d4faac2dd52f80e296f4239bed0021ba042dfcc3333682bd9f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







