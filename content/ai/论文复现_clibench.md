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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2DOOLGM%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIHqOpzY%2FcNKs1HrCVAicnx%2BLQuIRqbeIJ%2BRgdGM3cddjAiBp07X7r2G2gVrMXX9hYIb89MiFUs%2FwsfMc71PQ3G8iTir%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMv6CUbF%2FPfzR1aBMaKtwDTwY7E3fY1elbyLnBS7yFg54NjxBJGMLQRd5vVRtjGvBmjTDtpl0SFA6Zazy8kvKQvuycd5BgaCO0p0UJDRL%2BHEzFY3rV787reKWaUtScIChZx6ovVxmTQM2j4B9H1vqDmvGoi6VPngX1DJGF%2Frq5SpjX0KSDsvyAQWLWFcpveBdX%2Bj%2BG34yDXTJ3Sd2ki9%2B5G9IIjaSZ1JJvCAKK3zhkDmeo5zzzgRemV4Lnj%2Fqa%2BeAvADPCeIEIJ7cfpqI9t516hGMasUnJsWBI1ZKrJDLcfzYCJTBtqfYb4wLG0akMr%2Bbb1%2FVbUew1gc9Yc13rjkL1rzJA1HYw8rhYLnymavVz1aBdVUpof61kd8uTYhzbu9qFJhFql94fonqH%2BaqJ6PY6THZtp4XkaRKlfGiZlcbeK6bL7ahoV3WOtlBgQR95QKZ4BkYffG%2FqD%2BqHoD3nmlotbanGWSghr%2BgKYZ3KKoqdSI4zz47KUzZmkq43jKI4RS7Zwldt5cwfGU3DTa0akOx5Pe%2B9H6VIIfoB5vJ3CUgS1OuEl754UXxX%2FeFmm%2FEimZ8kl32xJTF0ZEx3tsXF3uahUF8tKlBxSGqYK1QmKGVzqb4tyrUm5Tb%2BoTqVPEDanms7u8JXjniUSOt1%2BhkwgZuhywY6pgEgYxjYpS0k0kYmt5oOhhwgc2aiaasETjiEmwPEM10UFwBB5U%2BrKo8zWd2Pc01ta2nvZWW1TxBLceH0%2FDcpfh6rE8JFMD6mXaSDjNYE6itPDB0jiSCr8EZSokCALBOqJAqAesWfj7ee4JCwSwbmxY7QjuFO8AUNV3Lr1SNSfyEZOqZQ215KSrDgSFoPp2X0rhFoQhCBmU31UH2SgButOS3leb8%2FavgE&X-Amz-Signature=9fcb8ae46aa512278927d5eed4682a4a3a8421c034a95932c1cc175911be760a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2DOOLGM%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIHqOpzY%2FcNKs1HrCVAicnx%2BLQuIRqbeIJ%2BRgdGM3cddjAiBp07X7r2G2gVrMXX9hYIb89MiFUs%2FwsfMc71PQ3G8iTir%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMv6CUbF%2FPfzR1aBMaKtwDTwY7E3fY1elbyLnBS7yFg54NjxBJGMLQRd5vVRtjGvBmjTDtpl0SFA6Zazy8kvKQvuycd5BgaCO0p0UJDRL%2BHEzFY3rV787reKWaUtScIChZx6ovVxmTQM2j4B9H1vqDmvGoi6VPngX1DJGF%2Frq5SpjX0KSDsvyAQWLWFcpveBdX%2Bj%2BG34yDXTJ3Sd2ki9%2B5G9IIjaSZ1JJvCAKK3zhkDmeo5zzzgRemV4Lnj%2Fqa%2BeAvADPCeIEIJ7cfpqI9t516hGMasUnJsWBI1ZKrJDLcfzYCJTBtqfYb4wLG0akMr%2Bbb1%2FVbUew1gc9Yc13rjkL1rzJA1HYw8rhYLnymavVz1aBdVUpof61kd8uTYhzbu9qFJhFql94fonqH%2BaqJ6PY6THZtp4XkaRKlfGiZlcbeK6bL7ahoV3WOtlBgQR95QKZ4BkYffG%2FqD%2BqHoD3nmlotbanGWSghr%2BgKYZ3KKoqdSI4zz47KUzZmkq43jKI4RS7Zwldt5cwfGU3DTa0akOx5Pe%2B9H6VIIfoB5vJ3CUgS1OuEl754UXxX%2FeFmm%2FEimZ8kl32xJTF0ZEx3tsXF3uahUF8tKlBxSGqYK1QmKGVzqb4tyrUm5Tb%2BoTqVPEDanms7u8JXjniUSOt1%2BhkwgZuhywY6pgEgYxjYpS0k0kYmt5oOhhwgc2aiaasETjiEmwPEM10UFwBB5U%2BrKo8zWd2Pc01ta2nvZWW1TxBLceH0%2FDcpfh6rE8JFMD6mXaSDjNYE6itPDB0jiSCr8EZSokCALBOqJAqAesWfj7ee4JCwSwbmxY7QjuFO8AUNV3Lr1SNSfyEZOqZQ215KSrDgSFoPp2X0rhFoQhCBmU31UH2SgButOS3leb8%2FavgE&X-Amz-Signature=08a1932078283ced92f3d2b8c0fba418bc55fb033dbf934c78ba96e395ac1a62&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







