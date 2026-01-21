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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662A53LXIV%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030130Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDSjE2M0Zov6s%2BFBGJd%2Br41BMNBGSoU%2BD11zES59%2BCtkAIge%2FoYQtJSinzMfcn1RM7NfN%2F%2BQVQaWUg2DlxPrcQEc2wqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFrpovZsjIUFJoYvGSrcA6UESv%2FrAyxh7d5IeFMwhji8BhVtysjEe0YgfQt%2BG6XmgO%2BGzw1E4VDkJ0GBehJahhY9UuwY8eGHMA6tAbkmT8vcsEmw4CMX3lSYVG7jcH0%2F68akk5%2BwT%2Foxx6ogMh6mdwFxBV5Z9CvuBJkHj8eVaEDdwTb3epWWH%2ByO9FsA%2B%2Bb%2B%2B0g8YT6Tt55ybCDaexoQBy8N%2FJzq98K91uh1jGASHjtdZ0qgkZFmt8tgUerNMQFDHJ6DXLpxMAFlzgHxejljptt6y5wUOIzsupKLTWG69jz0EEfuqZbX5gCEA0s4DhTYaalw1BbUJAChQ7Afsn58M2cO4AWUvSbImjBTH7noo1%2F1JH0HvhqA%2FlViAdfC3JpRidW7CUhoqYCQU4E6tZncjhBoiiKTYzb5zr0Zl%2B7M3nVJUiKn2knqiWUoOB1yZwv5vfTmjYOqFswkXPHxYCoWK6UtYLgGEbIJJ9MzZRhfDCtMkKUW4sDhNutoiRnMBE3Z1aOg7Pdd%2FUepBg8SM49meFN50N%2B7sDi%2Firm36N7Bn0dcPMgSEf1RxXst3EbsgRANreqL50qFFVoqptSupnv%2BWlBHN5LZd3wmMEC4%2BAKYYbHvfo8ylbTMR5z5%2ByLIuk2bMFhsya5Zg6bkeNMDMJPZwMsGOqUBADxH8QYs4YtMEAQz6YXo1wmv0rBuPQNR2DgLfjHQ5Aze%2FN5IstXBPjzx3auuFH%2FIyOJmLc%2FKE2jPr%2BWaJencN8z5I9jRmVhvgfCzQn9kijqXsRNUVerje5M4hw6wySfsvh41eTm0DVW%2BL%2BXMpBnaBeGSmd4itRKKaD%2Fj7ZMK%2F6Cge8q5PezfkDRh2UE54uciYZpJ5iStWcBKS8wbnaxasVszQIm6&X-Amz-Signature=0d679908ed7b61d21bf70fb402dc470d4a64cddab1dda3bb7d0a28c96fa3671f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662A53LXIV%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030130Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDSjE2M0Zov6s%2BFBGJd%2Br41BMNBGSoU%2BD11zES59%2BCtkAIge%2FoYQtJSinzMfcn1RM7NfN%2F%2BQVQaWUg2DlxPrcQEc2wqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFrpovZsjIUFJoYvGSrcA6UESv%2FrAyxh7d5IeFMwhji8BhVtysjEe0YgfQt%2BG6XmgO%2BGzw1E4VDkJ0GBehJahhY9UuwY8eGHMA6tAbkmT8vcsEmw4CMX3lSYVG7jcH0%2F68akk5%2BwT%2Foxx6ogMh6mdwFxBV5Z9CvuBJkHj8eVaEDdwTb3epWWH%2ByO9FsA%2B%2Bb%2B%2B0g8YT6Tt55ybCDaexoQBy8N%2FJzq98K91uh1jGASHjtdZ0qgkZFmt8tgUerNMQFDHJ6DXLpxMAFlzgHxejljptt6y5wUOIzsupKLTWG69jz0EEfuqZbX5gCEA0s4DhTYaalw1BbUJAChQ7Afsn58M2cO4AWUvSbImjBTH7noo1%2F1JH0HvhqA%2FlViAdfC3JpRidW7CUhoqYCQU4E6tZncjhBoiiKTYzb5zr0Zl%2B7M3nVJUiKn2knqiWUoOB1yZwv5vfTmjYOqFswkXPHxYCoWK6UtYLgGEbIJJ9MzZRhfDCtMkKUW4sDhNutoiRnMBE3Z1aOg7Pdd%2FUepBg8SM49meFN50N%2B7sDi%2Firm36N7Bn0dcPMgSEf1RxXst3EbsgRANreqL50qFFVoqptSupnv%2BWlBHN5LZd3wmMEC4%2BAKYYbHvfo8ylbTMR5z5%2ByLIuk2bMFhsya5Zg6bkeNMDMJPZwMsGOqUBADxH8QYs4YtMEAQz6YXo1wmv0rBuPQNR2DgLfjHQ5Aze%2FN5IstXBPjzx3auuFH%2FIyOJmLc%2FKE2jPr%2BWaJencN8z5I9jRmVhvgfCzQn9kijqXsRNUVerje5M4hw6wySfsvh41eTm0DVW%2BL%2BXMpBnaBeGSmd4itRKKaD%2Fj7ZMK%2F6Cge8q5PezfkDRh2UE54uciYZpJ5iStWcBKS8wbnaxasVszQIm6&X-Amz-Signature=66448f853b627a809b6f7d0bb38d4dfe4ffa73f70b79c38d4b42d4fac37016a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







