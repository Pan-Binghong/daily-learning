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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673AQ6DIX%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T031242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJGMEQCIH3BYz8Z%2BUxaXWwDU8PEQRyhbDvLTIesuB%2BCYufToh2KAiAWuh46Y8vW11m7y7oqA2DJB8hz7tKGAuyNATEpljKVQCr%2FAwgcEAAaDDYzNzQyMzE4MzgwNSIMLde6ByY4BErqxmOtKtwDRi7HTmvTBsRyPMhS6htC7yTq0VYhRXWbkzUxUonCp88ySgDfy7vEFfmduoLEqxMMcGA3xYbzRXBDYMLN76CpVrO%2FYxKw80LzzMca4DwJg6oaDFhbgPlj6WGJUPUHu%2BT5GCIdJhSwoU%2F3TlIBuOIf5b0tWucr1uZWpi4rgSP1XBzEVlBxdNMxEelJfR%2Fc9LmnRpnXoGyuek3EIQat59VEiRfbL8sjog4CQ7C%2B9IGDrE%2FZR3L0qBfe0U4IlIz%2FCPe6vBHNtiQFYYLq5uU%2FJsUcMkJ0iR8d425gSgt2rHJrVdkPOj9XOTpLsalWB5cZdbBiPTdKqeGXz4bok%2BTrJdUM0MpLRux4k4jr78CuDnoPxas%2BhrNPX49BXJruuhHvlQV%2FCZhKLAxv2pSF8TOYowChPBDF%2BxTy%2FIjIuX8qk1EtfUCTa0Jo6DnIu0GuZ%2BFYm7ifdGl0VGlys%2BluOeaklqwbeU2OfrsaPoBXnvtQ5l7HkkS5GTl3TLYzyRWH2GgY8a%2FX36zBkalmF4Y4KeVgxpsPK0tRlxryvZ8hdxwF%2F%2BO47lD8otM3adVKm2ZoVQ%2Fu5FsCrvIqIxdn0WgK7hsBgNdJ4dQQ07FNotWQzwOiil8MEXovHYinPwhaDbpuYdAwj4XWywY6pgGbCXZpr5bkanG4uF9P1%2BL%2BFQWSF3iJ1nwSpNJ5%2B8SuXXzexwx0M3crWGELIyi7O%2FUXTA9HBSaP4F%2B5OBXgxpew0R6l0ShDB6pKhKv33RjVCGgabGWXilRrJmPb0FmGNrspo1EK5UOyMSx5W1Au9ndl%2FC8x2r2sQcZqWw0rET6jii2H961FMWuI0XchmooTXi2N%2BOQ1mDvOI1PNmkUImpXEpKFY08m5&X-Amz-Signature=784335b981f5928972a0d9ac898c7874523a939e1bb4065f63124c42085c43cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673AQ6DIX%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T031242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJGMEQCIH3BYz8Z%2BUxaXWwDU8PEQRyhbDvLTIesuB%2BCYufToh2KAiAWuh46Y8vW11m7y7oqA2DJB8hz7tKGAuyNATEpljKVQCr%2FAwgcEAAaDDYzNzQyMzE4MzgwNSIMLde6ByY4BErqxmOtKtwDRi7HTmvTBsRyPMhS6htC7yTq0VYhRXWbkzUxUonCp88ySgDfy7vEFfmduoLEqxMMcGA3xYbzRXBDYMLN76CpVrO%2FYxKw80LzzMca4DwJg6oaDFhbgPlj6WGJUPUHu%2BT5GCIdJhSwoU%2F3TlIBuOIf5b0tWucr1uZWpi4rgSP1XBzEVlBxdNMxEelJfR%2Fc9LmnRpnXoGyuek3EIQat59VEiRfbL8sjog4CQ7C%2B9IGDrE%2FZR3L0qBfe0U4IlIz%2FCPe6vBHNtiQFYYLq5uU%2FJsUcMkJ0iR8d425gSgt2rHJrVdkPOj9XOTpLsalWB5cZdbBiPTdKqeGXz4bok%2BTrJdUM0MpLRux4k4jr78CuDnoPxas%2BhrNPX49BXJruuhHvlQV%2FCZhKLAxv2pSF8TOYowChPBDF%2BxTy%2FIjIuX8qk1EtfUCTa0Jo6DnIu0GuZ%2BFYm7ifdGl0VGlys%2BluOeaklqwbeU2OfrsaPoBXnvtQ5l7HkkS5GTl3TLYzyRWH2GgY8a%2FX36zBkalmF4Y4KeVgxpsPK0tRlxryvZ8hdxwF%2F%2BO47lD8otM3adVKm2ZoVQ%2Fu5FsCrvIqIxdn0WgK7hsBgNdJ4dQQ07FNotWQzwOiil8MEXovHYinPwhaDbpuYdAwj4XWywY6pgGbCXZpr5bkanG4uF9P1%2BL%2BFQWSF3iJ1nwSpNJ5%2B8SuXXzexwx0M3crWGELIyi7O%2FUXTA9HBSaP4F%2B5OBXgxpew0R6l0ShDB6pKhKv33RjVCGgabGWXilRrJmPb0FmGNrspo1EK5UOyMSx5W1Au9ndl%2FC8x2r2sQcZqWw0rET6jii2H961FMWuI0XchmooTXi2N%2BOQ1mDvOI1PNmkUImpXEpKFY08m5&X-Amz-Signature=cabb120bdfb2fa9489ae31daed127dd8221e6287db5425f5c714c10fcafab4e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







