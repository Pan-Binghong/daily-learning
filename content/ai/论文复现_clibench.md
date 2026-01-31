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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7HTN57O%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFgFdQ9UAiL1TWQkKdEb1Q176cswZzFfnbN4tAkmB%2FUxAiAgTS8dSFl5XlTne6BlXv2d6HzuI1isE8VVRLCJ8J2pBCqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3Znq2imBi0Gp5TGzKtwDesbcur0H6xPH9qjdtxpw8niCJ77tn20DQIUzMnAUrVxJEkCeftX4O9GzYKkCbY3Cema5rzsfbRj5lUWFi1utcgC9T%2BWPFTn3nRrKlbwh0b898TALKl0jRT301hsA83zfRExS7OLmoj0cqKcgFeA1yWiDloDoHahyfDcWEXaTsb8McuBM%2BofS6mIVL6w05%2F1EzmP%2B408Qn4t8Dzs6ytDeVLL7oT2S3rz2sEukJXxDHszDhVjMllMuXi17ubNFqTgHy7skGoNuYdKtOoFBDblZU3aA56dbVPF%2BlbYo7EI2CjAScXT4nK%2BZbQnQ7iyIKHFeozlWpsFO%2BQ%2B1FgRudE%2B17UgInq%2F4NFDAnnMWYJ9uuvDC3ZhU27baheNDqHrQ1n8enz2Z9yoQS2nM6nPQzFLXEbmK%2BvtWREfH4tw6eOI3EaQ6sVKmcD%2BH%2FwbFhIC2108oxX0Jrh6KmrNmxCy15d2MC8tlPf8MYts1miUQRrRqiwOpUD2hVYAo7245cVn3D0mxWr07bkCBPrzLKGIdLuPxxjhA%2F9Fx70UjJhu4tmuZdkUOISW3wg6B%2Bw6yC8F%2BudHPDn4DvlDE2DUbdZg4vI2FSner%2B4lGgk7924RjT0Sr06EBnfgXCDg9Xb4JCScwk8z1ywY6pgH4JaKaTZNk9bvGIkmmTrPQvvFykJKYS3Gz7LS84xsgSTZTpQ%2FvpSIrb6U8xfSJn3vGJbKh4nrikclo1MuzO6FYgD2CmkuVMUYubrzOLti1EoQzTUH911NNaTcYrzzO9eVWamRkRcbx3rDpTRqpdTbXmtshKquTsX1DW%2BrWYkGDaJP2oZNqFc1BFDr8rI30z7WXfz22rxkKababcpQJLtVrDHVluMmW&X-Amz-Signature=8fae486317588df755a20b48d59af115e131ca420dcd440f631ae548ce51f559&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7HTN57O%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFgFdQ9UAiL1TWQkKdEb1Q176cswZzFfnbN4tAkmB%2FUxAiAgTS8dSFl5XlTne6BlXv2d6HzuI1isE8VVRLCJ8J2pBCqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3Znq2imBi0Gp5TGzKtwDesbcur0H6xPH9qjdtxpw8niCJ77tn20DQIUzMnAUrVxJEkCeftX4O9GzYKkCbY3Cema5rzsfbRj5lUWFi1utcgC9T%2BWPFTn3nRrKlbwh0b898TALKl0jRT301hsA83zfRExS7OLmoj0cqKcgFeA1yWiDloDoHahyfDcWEXaTsb8McuBM%2BofS6mIVL6w05%2F1EzmP%2B408Qn4t8Dzs6ytDeVLL7oT2S3rz2sEukJXxDHszDhVjMllMuXi17ubNFqTgHy7skGoNuYdKtOoFBDblZU3aA56dbVPF%2BlbYo7EI2CjAScXT4nK%2BZbQnQ7iyIKHFeozlWpsFO%2BQ%2B1FgRudE%2B17UgInq%2F4NFDAnnMWYJ9uuvDC3ZhU27baheNDqHrQ1n8enz2Z9yoQS2nM6nPQzFLXEbmK%2BvtWREfH4tw6eOI3EaQ6sVKmcD%2BH%2FwbFhIC2108oxX0Jrh6KmrNmxCy15d2MC8tlPf8MYts1miUQRrRqiwOpUD2hVYAo7245cVn3D0mxWr07bkCBPrzLKGIdLuPxxjhA%2F9Fx70UjJhu4tmuZdkUOISW3wg6B%2Bw6yC8F%2BudHPDn4DvlDE2DUbdZg4vI2FSner%2B4lGgk7924RjT0Sr06EBnfgXCDg9Xb4JCScwk8z1ywY6pgH4JaKaTZNk9bvGIkmmTrPQvvFykJKYS3Gz7LS84xsgSTZTpQ%2FvpSIrb6U8xfSJn3vGJbKh4nrikclo1MuzO6FYgD2CmkuVMUYubrzOLti1EoQzTUH911NNaTcYrzzO9eVWamRkRcbx3rDpTRqpdTbXmtshKquTsX1DW%2BrWYkGDaJP2oZNqFc1BFDr8rI30z7WXfz22rxkKababcpQJLtVrDHVluMmW&X-Amz-Signature=eca216aaf0a290ecbccf7603e9344f443dff966e087f974af2234d4fa1c9bc19&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







