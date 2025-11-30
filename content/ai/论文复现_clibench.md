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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAE5JYQZ%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCIQCPhkjysg3kUaHC38k8yviwuBzIPUbANTDZpTDtG3BlSwIgS5w8v5Y1XSCXkzjg0pkGgEg22GCUrQR2B1gp8NeS8uAqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJNjc0FNv4A7AEmFBCrcAxmaYnt2BFpGm9ByzncKYf6euj4YGsgNNgxbWoK%2Bnl12t4ThDDCy0E6Fpo1UyHg4QziQBZtmbKOOe14S72M%2BA6Rr60QmpgbgNvMYBgO0w2D0oB7uHkct%2BNWXlad9JILPE7ylGaJf8NlWo%2BDLtBP9ZYTYC4%2FnhqiM%2BdO6y3TeEuEgtMraunn4tuxr7t3ubEzC680jrFxRu0pGHYjONotN%2Blfnf5Wu3zfFnQOYCUAXFarRgRhdyQRARHbzF%2BL954CjANMKNf2xuRRnFaSi7u0swLpeUm45xfyVRQrTJkppqgjDfvPBG43m8HZ519xw95zr2ezOuFYRoQ9fksHKJ8Jx%2FioocjkhsT1eYv4ZU6PyWZyhfpBNitCobVNEK%2FX%2BbftG9t%2F6ejObCYxlkY3qZd8EoJipUrigGz03lYV%2BQ2YwSJn7MTWzqOLsiQ0B6XNNjOE2Q%2FkqQtD9vpyzGcR1ZnFfev5IN0q2qBV8fvdrJVbExrlEgk2eEvcCdFJDiQxAyl9stnZx08wccRWJTXgsaCg7TqmWQlsSLYrbw2bUnTQjjle7INabSyMfcqF4DJjL0ExgxY1ACYhaxvxUN0b7HAsNgDjYEoIsS0xNf6Ar%2BuxvMkOXmpJ3zT7b0GDwA9KxMJrXrckGOqUBj6r62bJZ%2BVQGQMuOT2epjvkD6fTT%2Br1VsNoH4spwqLMigDE06e81w2%2F2UUUJmtIM8e4R5zs6bREn6e7ajr1e0MRWFw%2Bdt0nrFBV%2FXgTaDZSR2SpDZ4KaqZ1FoAGtQPJkJ9NZwBNg4CTgxogC0xNbHL13GP8yOJ3CFirIL8yxZeP8wgGnpUIOkkfH59p5iNbs0hNy%2F0uP1d0eNNd18qg2VF7SYuvw&X-Amz-Signature=ed16062de33492b326e1fb4e5378c05afb0a19137fc00161c3e4b7e389901c1c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAE5JYQZ%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCIQCPhkjysg3kUaHC38k8yviwuBzIPUbANTDZpTDtG3BlSwIgS5w8v5Y1XSCXkzjg0pkGgEg22GCUrQR2B1gp8NeS8uAqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJNjc0FNv4A7AEmFBCrcAxmaYnt2BFpGm9ByzncKYf6euj4YGsgNNgxbWoK%2Bnl12t4ThDDCy0E6Fpo1UyHg4QziQBZtmbKOOe14S72M%2BA6Rr60QmpgbgNvMYBgO0w2D0oB7uHkct%2BNWXlad9JILPE7ylGaJf8NlWo%2BDLtBP9ZYTYC4%2FnhqiM%2BdO6y3TeEuEgtMraunn4tuxr7t3ubEzC680jrFxRu0pGHYjONotN%2Blfnf5Wu3zfFnQOYCUAXFarRgRhdyQRARHbzF%2BL954CjANMKNf2xuRRnFaSi7u0swLpeUm45xfyVRQrTJkppqgjDfvPBG43m8HZ519xw95zr2ezOuFYRoQ9fksHKJ8Jx%2FioocjkhsT1eYv4ZU6PyWZyhfpBNitCobVNEK%2FX%2BbftG9t%2F6ejObCYxlkY3qZd8EoJipUrigGz03lYV%2BQ2YwSJn7MTWzqOLsiQ0B6XNNjOE2Q%2FkqQtD9vpyzGcR1ZnFfev5IN0q2qBV8fvdrJVbExrlEgk2eEvcCdFJDiQxAyl9stnZx08wccRWJTXgsaCg7TqmWQlsSLYrbw2bUnTQjjle7INabSyMfcqF4DJjL0ExgxY1ACYhaxvxUN0b7HAsNgDjYEoIsS0xNf6Ar%2BuxvMkOXmpJ3zT7b0GDwA9KxMJrXrckGOqUBj6r62bJZ%2BVQGQMuOT2epjvkD6fTT%2Br1VsNoH4spwqLMigDE06e81w2%2F2UUUJmtIM8e4R5zs6bREn6e7ajr1e0MRWFw%2Bdt0nrFBV%2FXgTaDZSR2SpDZ4KaqZ1FoAGtQPJkJ9NZwBNg4CTgxogC0xNbHL13GP8yOJ3CFirIL8yxZeP8wgGnpUIOkkfH59p5iNbs0hNy%2F0uP1d0eNNd18qg2VF7SYuvw&X-Amz-Signature=832f6e488aff3d784d63a9080802e99d96dd8ac4d040ba46442807880b8ee04f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







