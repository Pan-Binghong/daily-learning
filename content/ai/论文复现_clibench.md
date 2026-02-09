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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWNOUL7Y%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmMM6AhmTdS390AExLLPi7lCp7ErVznu2xht9maAFlBwIhAKAVFk97yIULUQfLO%2BwJO%2B%2B4KJr5OPJApEm3mu14mX5bKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igza4YSu89Jhr00%2FGQoq3APzgGv%2FxVRA2iRUdsA8fFVUODtT%2B19XXPVC9IN4vlWQbeVOKK2xSTJN%2B1CwEq2bLImrnnFtKBQuCQZdmT49mCE%2BNsufxh0n%2FqNbMRnlR0ZQuPRdX46TSTkPb6F%2FNgxfIDfCHOyIsZNOn7H%2B6R0oFT%2FmnJL%2FtJrkkaxpjsG02T2KFpemK5mhCdDYHIzVQMnp48i3VaROWvMeNsfzg9MDgJzDSgRGmGtQBMK5cfQ62R1yVpEla7FCoPU9SBSEsKzMU2OF74%2BGj6Fa70gJXyoBHJjstQLjmaH8fxJzxSxXDrkQZRHvnBCggrwD%2Fp5VoMo5DBpu5e8BKzvGr9Jd5qCz6u%2FiwEzxUAFE7Seiled91EA5oTfkN%2FtL8FfuxoKDh2x4KT4tVECt%2B43kCtwA1kwepDWVDsAZafn%2Br6yipmp8uFrZ4wWIMOOv%2FlqKU1sPCNperAH%2FEM2B6lDkHmuFRioLoFJ%2B4RP%2Fe%2BQmhyr5sVi2YAh1JkaB1tEFe585flQMPWILv5L0uKJOV%2FBAERW%2FI6LKQLm1k%2BvDDHrwouLpPGQ8%2FKZWE5I5nZQoZXdR2QL3%2BlKm9HZj2ClbwIWcWsDed87uEgeUaNxnzl5vwmGAh3dfvJ9jExhEoG3%2BHbFBK3XTRTCYmKXMBjqkAagp4MBuD%2FEs04ohrAA%2FnKoTiGNDCvSqi3S%2FYnws3E5yfgt2iS3YNlq46%2FK4GWP8vsy1200Am1TBCA1X0S0AWMWtIsYjYSbzzGMcBdGJe6k6tRjPCYoxoUbUwA6a8uIn0L6sKYEl96iM%2BFGlXd8JolPFpyATcN7dmfRAUOfZ1ZarB6b%2F%2Fh2fc373c4tcsKmFYIgwjIXu7342TM7vnMmEUFs544Jw&X-Amz-Signature=327fd7713064ff0c964d44d5e4d3769997da74bbdc7078d991c728cec891eec3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWNOUL7Y%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmMM6AhmTdS390AExLLPi7lCp7ErVznu2xht9maAFlBwIhAKAVFk97yIULUQfLO%2BwJO%2B%2B4KJr5OPJApEm3mu14mX5bKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igza4YSu89Jhr00%2FGQoq3APzgGv%2FxVRA2iRUdsA8fFVUODtT%2B19XXPVC9IN4vlWQbeVOKK2xSTJN%2B1CwEq2bLImrnnFtKBQuCQZdmT49mCE%2BNsufxh0n%2FqNbMRnlR0ZQuPRdX46TSTkPb6F%2FNgxfIDfCHOyIsZNOn7H%2B6R0oFT%2FmnJL%2FtJrkkaxpjsG02T2KFpemK5mhCdDYHIzVQMnp48i3VaROWvMeNsfzg9MDgJzDSgRGmGtQBMK5cfQ62R1yVpEla7FCoPU9SBSEsKzMU2OF74%2BGj6Fa70gJXyoBHJjstQLjmaH8fxJzxSxXDrkQZRHvnBCggrwD%2Fp5VoMo5DBpu5e8BKzvGr9Jd5qCz6u%2FiwEzxUAFE7Seiled91EA5oTfkN%2FtL8FfuxoKDh2x4KT4tVECt%2B43kCtwA1kwepDWVDsAZafn%2Br6yipmp8uFrZ4wWIMOOv%2FlqKU1sPCNperAH%2FEM2B6lDkHmuFRioLoFJ%2B4RP%2Fe%2BQmhyr5sVi2YAh1JkaB1tEFe585flQMPWILv5L0uKJOV%2FBAERW%2FI6LKQLm1k%2BvDDHrwouLpPGQ8%2FKZWE5I5nZQoZXdR2QL3%2BlKm9HZj2ClbwIWcWsDed87uEgeUaNxnzl5vwmGAh3dfvJ9jExhEoG3%2BHbFBK3XTRTCYmKXMBjqkAagp4MBuD%2FEs04ohrAA%2FnKoTiGNDCvSqi3S%2FYnws3E5yfgt2iS3YNlq46%2FK4GWP8vsy1200Am1TBCA1X0S0AWMWtIsYjYSbzzGMcBdGJe6k6tRjPCYoxoUbUwA6a8uIn0L6sKYEl96iM%2BFGlXd8JolPFpyATcN7dmfRAUOfZ1ZarB6b%2F%2Fh2fc373c4tcsKmFYIgwjIXu7342TM7vnMmEUFs544Jw&X-Amz-Signature=4d58ee9a096b802f8decca24780e167f566054daf7d78de9dfb9a1efd1844364&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







