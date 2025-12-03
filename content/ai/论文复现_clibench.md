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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647NDSHME%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T024830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJGMEQCIFgEu28MYaJjgKgISZRCxyt7qmHjHar5IzTmTsWZV0eAAiAPt3pgh%2BEGR3RTGmgmv%2FCWIMdYE92MSoOUrGhfFiO%2F0ir%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIM3pbe9D83KxWXU5zWKtwD0bOhwT17jF%2FElTHrj%2FHMTEroIZ4F4bU5oLT4e0T%2FH2Mdpbu%2BLrSyDBx1SqefUZKuWL6%2BKBzwyxbdOoSDi1xIu8L%2Fc0mFCQknOdzN5MlmCJo9fK1CtQ9RF2tVt8qYI6AWE%2BuSK%2F6UCeZVi0E231hIDVS8BomF8jnr4eHpCDsbbGAYTqwlJHacBheWCcSEonxOtJUmgY2NVhQpJ2xNo9mVsZcO%2BuTS2pVd3NX6Z1IBQwcVenXZULbpTn8lYAgUAakyRnFAK6kq%2FEu45q5Bhhc%2BhSGWxM5MIhW8mbw7uRQ7mCCdWJtXpZMh7K0s73pbJGguV51RBoVK6Y%2FHU7cyBZnmu0jbFSxEgkchxDZImUhWIv7NhxNSiwxplQTstfT5nioIuAGMbMQKEGv68fJq2t51o%2Bo4wQOnGgyElY81XH3KOlrKpKiLZvYksWC4RiEiKZJprtbkOuemL7JuAd5O6J8qvKguJEM2X7YEYbpgre5Fz%2BbK%2Fij%2B53wMB3Ae28qBpY6RtIA0e3867FoTUzAz4gvMnTVFmkqsiPrRHoSdIG1PG%2FRxUODqY8yAYBXkE%2BLSUnpY1gwYdSTaTn1t%2FM5WPIYCWOHA2aokULc9ssAQKdfUyYxyyLEk7zk5DNaatl0wo5a%2ByQY6pgHYJAwK7iHt4cLr7v%2FBrOIcq7jAaIQ9Ky8Pw%2FpTfkI3giD5tTzXJ%2BNXNLDqxbsoxzlnP2YKBN2Lx67nZkrEzs3s%2BpaLTsQFRa5vktq%2FbjJRCWeciM4wFxSowJmwdqIKJeS3SMcA44TQwcaJToNW44IvUcBzXWElutockARlEvMopzdTMuQwem5h15RSUFNeATRkfGLaQoerzOqHTZLnPBBMpCOwjQ44&X-Amz-Signature=a895bd8a6cc7870cabf2039b975fa3219fb3d40532a5eb15dbd9f0ed22cb6ec9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647NDSHME%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T024830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJGMEQCIFgEu28MYaJjgKgISZRCxyt7qmHjHar5IzTmTsWZV0eAAiAPt3pgh%2BEGR3RTGmgmv%2FCWIMdYE92MSoOUrGhfFiO%2F0ir%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIM3pbe9D83KxWXU5zWKtwD0bOhwT17jF%2FElTHrj%2FHMTEroIZ4F4bU5oLT4e0T%2FH2Mdpbu%2BLrSyDBx1SqefUZKuWL6%2BKBzwyxbdOoSDi1xIu8L%2Fc0mFCQknOdzN5MlmCJo9fK1CtQ9RF2tVt8qYI6AWE%2BuSK%2F6UCeZVi0E231hIDVS8BomF8jnr4eHpCDsbbGAYTqwlJHacBheWCcSEonxOtJUmgY2NVhQpJ2xNo9mVsZcO%2BuTS2pVd3NX6Z1IBQwcVenXZULbpTn8lYAgUAakyRnFAK6kq%2FEu45q5Bhhc%2BhSGWxM5MIhW8mbw7uRQ7mCCdWJtXpZMh7K0s73pbJGguV51RBoVK6Y%2FHU7cyBZnmu0jbFSxEgkchxDZImUhWIv7NhxNSiwxplQTstfT5nioIuAGMbMQKEGv68fJq2t51o%2Bo4wQOnGgyElY81XH3KOlrKpKiLZvYksWC4RiEiKZJprtbkOuemL7JuAd5O6J8qvKguJEM2X7YEYbpgre5Fz%2BbK%2Fij%2B53wMB3Ae28qBpY6RtIA0e3867FoTUzAz4gvMnTVFmkqsiPrRHoSdIG1PG%2FRxUODqY8yAYBXkE%2BLSUnpY1gwYdSTaTn1t%2FM5WPIYCWOHA2aokULc9ssAQKdfUyYxyyLEk7zk5DNaatl0wo5a%2ByQY6pgHYJAwK7iHt4cLr7v%2FBrOIcq7jAaIQ9Ky8Pw%2FpTfkI3giD5tTzXJ%2BNXNLDqxbsoxzlnP2YKBN2Lx67nZkrEzs3s%2BpaLTsQFRa5vktq%2FbjJRCWeciM4wFxSowJmwdqIKJeS3SMcA44TQwcaJToNW44IvUcBzXWElutockARlEvMopzdTMuQwem5h15RSUFNeATRkfGLaQoerzOqHTZLnPBBMpCOwjQ44&X-Amz-Signature=26cde3b9f5f53a96b85feb8675137afe682026143bac18097559f5791707ec41&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







