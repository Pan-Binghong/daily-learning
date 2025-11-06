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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFOZFJPX%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC76SiaYjdOXaIAdZwyFMgJ8uHGGabOdDulfCgt%2BjH5qgIgPE69brJGuvFlcBpf%2FDndt6IoE9YDJ37N8wNIvIzxQzEqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCM8HUoA6nlQ1UgNICrcAwvvAhTqdwy31ajALqmx7lSQo48hFklrhxXvQV2SzNPYS4QTYNo%2BrPdPAYYWhucRxMgGyX4O9K%2F6nLZ1Um4r94DsbrLDg8VjbcZmzugRUidfrLTyE9eo3YbwbksOvVK2G1CnwpSI6pG520GhGfGG43LvpfbikwcXTT7p8dJ3yx1gmPHmmf7C7IxuKwK2YGg%2BbQlGs%2Bt6kTkfJ1CU586a%2BSm0cGoNOg0%2BpgxI0Eamq6h66bmqiOhkSk2Q4a%2Bq0JU%2FlnTn6lV8yeIjaoN%2FJ159umdZtTwZOXJpx%2BDxQgBP4603XvYX91%2B%2F5XJBzuNJHB%2Fe853x%2FaJLmsHKQYUsc3fhGFgjAWkWUCJI3P8FH0r1hwsRH3QP6nHOaDShk3OHjQp%2BUKLcW0R0B4HTX1NkAnvXTxrKJLqpkl7Go1N3NDs9ajkPMbCNOXTw7QkVWNXU6jK58rF5ACMUSTCjgxuDufNFecvLZFmfyq7Ph282g%2F6PDAwFiUI6umj88NNE68WdObKbBHUpyBROHBaba2FN2%2F4y5twgcDFR%2FqY8%2FK5S%2Ftet6IQsDCdf7fCIrCeTJKmTk10I4WjLi58YE4mFENstgyXciutJjq1MY98ZVVWmCAdiViHUfJTXGgEidLp5LZcxMPDxr8gGOqUBuiY3B3XE5VYoRJ6hOp91Ry%2FEAt2kAuEnqcOCh9bmIbjCxQGH6%2F1xO4GFw%2FtvnEHwi%2Bz0uIrxLDqjILQk8r0L6NFkmp48hQ8vxatrqe1Vi5U9JyT5xjccHyztQnozObqS%2FwEtahyde9bsKvEVuQqb5DRm7qpfyhEckfWcen2X%2FG008xJebVa98jsqOoCbJlnX0L4PHDkLG6SVgNx2mh40A8120Szr&X-Amz-Signature=fcd2469608f9110fdd6484243900e50f0c4b1c059a3dfd6ec74450c8ebe179f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFOZFJPX%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC76SiaYjdOXaIAdZwyFMgJ8uHGGabOdDulfCgt%2BjH5qgIgPE69brJGuvFlcBpf%2FDndt6IoE9YDJ37N8wNIvIzxQzEqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCM8HUoA6nlQ1UgNICrcAwvvAhTqdwy31ajALqmx7lSQo48hFklrhxXvQV2SzNPYS4QTYNo%2BrPdPAYYWhucRxMgGyX4O9K%2F6nLZ1Um4r94DsbrLDg8VjbcZmzugRUidfrLTyE9eo3YbwbksOvVK2G1CnwpSI6pG520GhGfGG43LvpfbikwcXTT7p8dJ3yx1gmPHmmf7C7IxuKwK2YGg%2BbQlGs%2Bt6kTkfJ1CU586a%2BSm0cGoNOg0%2BpgxI0Eamq6h66bmqiOhkSk2Q4a%2Bq0JU%2FlnTn6lV8yeIjaoN%2FJ159umdZtTwZOXJpx%2BDxQgBP4603XvYX91%2B%2F5XJBzuNJHB%2Fe853x%2FaJLmsHKQYUsc3fhGFgjAWkWUCJI3P8FH0r1hwsRH3QP6nHOaDShk3OHjQp%2BUKLcW0R0B4HTX1NkAnvXTxrKJLqpkl7Go1N3NDs9ajkPMbCNOXTw7QkVWNXU6jK58rF5ACMUSTCjgxuDufNFecvLZFmfyq7Ph282g%2F6PDAwFiUI6umj88NNE68WdObKbBHUpyBROHBaba2FN2%2F4y5twgcDFR%2FqY8%2FK5S%2Ftet6IQsDCdf7fCIrCeTJKmTk10I4WjLi58YE4mFENstgyXciutJjq1MY98ZVVWmCAdiViHUfJTXGgEidLp5LZcxMPDxr8gGOqUBuiY3B3XE5VYoRJ6hOp91Ry%2FEAt2kAuEnqcOCh9bmIbjCxQGH6%2F1xO4GFw%2FtvnEHwi%2Bz0uIrxLDqjILQk8r0L6NFkmp48hQ8vxatrqe1Vi5U9JyT5xjccHyztQnozObqS%2FwEtahyde9bsKvEVuQqb5DRm7qpfyhEckfWcen2X%2FG008xJebVa98jsqOoCbJlnX0L4PHDkLG6SVgNx2mh40A8120Szr&X-Amz-Signature=16be228a1d25c287d51b59b719df31d4e4046dbddbadad95bed0f54100f258e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







