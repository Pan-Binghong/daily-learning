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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7OYM4NC%2F20260307%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260307T031910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQDUeDsJtcLMFt7HgXZSIVP%2BS%2F0nAnOBK60OxrU0VTae8QIgcPNXvZZwIglafwLOV9NvsdI%2Fvk3Pu1PwgPuyuYrt%2F6EqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFX%2F6by%2F2Fo%2BIMLP%2BSrcAxurBYXQNxiDFKufT15kcN2R8qJuJCJEaz1P14klz1xrpa7piCOGCSty1QHTReUUZeDeZMKwsUh25Fqvh87kjI9tQRTlujJ9DESK8tmFzlluAfAIQmWvNX7NrTVnXQuS2jwoXhZy%2FndVFr0dU5SquZeVTW60oNhoPfrhjV%2F471ugeXgF1BB53qW1OCSTcYB%2BvV19eodcOMyHZhUoHy5gAI8IcWupIKMAP%2BDoydG5nZRnv9SOi5DAZjY76ValudVobgjQeVG7W4h4hqyChxbNB0vmGZf7f6m0nWsBeKLvehybD27uiWYVxKjZ%2B5foXeBs9zCokOM3f%2Biju0syjEmIbKZLsePdRSVNJYXR1fnnlkmjAIwleF7uH8hU0EfsMXq6WQti%2BjvPETi41cp1S9060Sp7AYdl%2F0KkD7HpcOgNudCHNb3sMk70xd2Z6Scq%2Fde8f4gll646qdnmWSS6wnDCJ%2B3FZLMfmLiP3NnIP7y6XSn1nkf%2BiZW6xJOw8sys0NzCxn4uINeCga4oNNS1zWWDF%2FX29YWJPZagVlvFkwm5t%2BdbxvF0l4IS%2FmAMwQALnXiw65jQMBkoI8UGx9g4T6OOibc%2F%2FjZP3%2BcnL6jvTTsPGMysYE7y%2Bx9LHbInIo5nMJ6Urs0GOqUB3KmwBUOee3AbU7cS78Y1QKua%2FFhKaEjv5D1aKpo0flJ7fVJ7rdU1P011LSM1AptGW2S%2FXQATzjvtd2%2B2X2WeYOFXnsUQrZjmS3WAUET5dQ29Xpgl7%2FLUp9VZSe5wjoKQccoHrRXKQEpRkndBj6ECviJKI2ttvuVtSxkXHQEJQ9aR%2FQTxaLLrfEgNwvx7bFJAxaFHwAViYlCiNecvl8%2Bvn6vteXed&X-Amz-Signature=c8b6f4741c3b57f9582a9eab18b21a82968da7c141579f2051efc338b517349c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7OYM4NC%2F20260307%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260307T031910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQDUeDsJtcLMFt7HgXZSIVP%2BS%2F0nAnOBK60OxrU0VTae8QIgcPNXvZZwIglafwLOV9NvsdI%2Fvk3Pu1PwgPuyuYrt%2F6EqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFX%2F6by%2F2Fo%2BIMLP%2BSrcAxurBYXQNxiDFKufT15kcN2R8qJuJCJEaz1P14klz1xrpa7piCOGCSty1QHTReUUZeDeZMKwsUh25Fqvh87kjI9tQRTlujJ9DESK8tmFzlluAfAIQmWvNX7NrTVnXQuS2jwoXhZy%2FndVFr0dU5SquZeVTW60oNhoPfrhjV%2F471ugeXgF1BB53qW1OCSTcYB%2BvV19eodcOMyHZhUoHy5gAI8IcWupIKMAP%2BDoydG5nZRnv9SOi5DAZjY76ValudVobgjQeVG7W4h4hqyChxbNB0vmGZf7f6m0nWsBeKLvehybD27uiWYVxKjZ%2B5foXeBs9zCokOM3f%2Biju0syjEmIbKZLsePdRSVNJYXR1fnnlkmjAIwleF7uH8hU0EfsMXq6WQti%2BjvPETi41cp1S9060Sp7AYdl%2F0KkD7HpcOgNudCHNb3sMk70xd2Z6Scq%2Fde8f4gll646qdnmWSS6wnDCJ%2B3FZLMfmLiP3NnIP7y6XSn1nkf%2BiZW6xJOw8sys0NzCxn4uINeCga4oNNS1zWWDF%2FX29YWJPZagVlvFkwm5t%2BdbxvF0l4IS%2FmAMwQALnXiw65jQMBkoI8UGx9g4T6OOibc%2F%2FjZP3%2BcnL6jvTTsPGMysYE7y%2Bx9LHbInIo5nMJ6Urs0GOqUB3KmwBUOee3AbU7cS78Y1QKua%2FFhKaEjv5D1aKpo0flJ7fVJ7rdU1P011LSM1AptGW2S%2FXQATzjvtd2%2B2X2WeYOFXnsUQrZjmS3WAUET5dQ29Xpgl7%2FLUp9VZSe5wjoKQccoHrRXKQEpRkndBj6ECviJKI2ttvuVtSxkXHQEJQ9aR%2FQTxaLLrfEgNwvx7bFJAxaFHwAViYlCiNecvl8%2Bvn6vteXed&X-Amz-Signature=161b78100c3341c48601893a9ea2458fc707bdb9b5d86e48a2bd67b9044dc8ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







