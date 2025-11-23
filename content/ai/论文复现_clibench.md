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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCLIVSKU%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T025823Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJHMEUCIBnkSaGhekfpg37EEscn1BE11Tv4zSZACSXxyT9ukxq6AiEAwZlXdsCu1f5LQnbhBksWh8xDHX0Qq62aD5%2FA71Punssq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDHOb0XsparseeQTzfCrcA9ajpQ%2BbvIiaqZU%2B6FrVdMSTVsXO62zA1agCF6RB1ARgAEFtaQ4H81zmH0OvOrfWOQ%2BeIVK0880EMta5kmf3oZGBlgAhNj1HnDixNaHalX5yHHo686eTBoImbUvJRzGz8uIyUtI6dSphz7isSS3SWjwPChB%2F7VlrNAkmtx6m3azdrRf2Aso3cdbJfa2rFsfKKizcUsVjB%2Fyt31h76AnbwoLYoWy2LkuziIkLtgtrxgC%2B1nJJqv1umSttwU6azba%2FgsTpMr4AEGHVmI57kxOPYZEoZcWWxc4M93L%2Bzb0sE%2BU3wW4OULu0chvH4YqDrysr1k8l2T69UjsOc0aK0q5NklwIF5ZifYp69Gps5XvdXqrRqb%2FmX8baTPxzQ3ln5UwU71CTaBiT3bHVtgj3uhD5fUiBY18Vy9cO8d5nBpIcPbuGbUpJH2nqiw4DbKSBcSuPArx%2BRryTAYmWkMjxfAPG28dwEyv5f1G%2BrSVBCQ9VMfhTMUOUmak5FX1VUeBh6q9tH1DFTq9WpWUKOg%2FSn0lLn%2F%2FnHN1RyQKvAEJSTCyMXk0%2Bu2xdJij66A5aGbJkOClpLi2LMy9DSlHdREn0tQ8A1eB0fuTHahU1z2z7Q0Yl9TBBM%2FwsXmxuPrWEQswYML6wickGOqUBUihjktyP%2FYJ0Uq0tO77%2BSjaRlayAabYzzLnDKR%2BFhPvxSLxjH6x%2BRNJdMbW%2FhstDtt5VJu7oNYglOS2k%2Fvq06xALJOiVQEoHRKZR%2Fx%2B%2BLpkbGCMimaf150T4xyM6cWOUq1RppEMnNTtWrZbznyZZSHzCEKgVh8UHj63BAhR67%2Fvpi%2BamGXCtsY%2F%2Bn0RZcSUF%2Bser5RFfzP8XoJjLoNojrfkJfXEd&X-Amz-Signature=61508fb8d2ac1c86571c45e3925f191ea4bdb00e835bdfda8f550d7df032526b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCLIVSKU%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T025823Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJHMEUCIBnkSaGhekfpg37EEscn1BE11Tv4zSZACSXxyT9ukxq6AiEAwZlXdsCu1f5LQnbhBksWh8xDHX0Qq62aD5%2FA71Punssq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDHOb0XsparseeQTzfCrcA9ajpQ%2BbvIiaqZU%2B6FrVdMSTVsXO62zA1agCF6RB1ARgAEFtaQ4H81zmH0OvOrfWOQ%2BeIVK0880EMta5kmf3oZGBlgAhNj1HnDixNaHalX5yHHo686eTBoImbUvJRzGz8uIyUtI6dSphz7isSS3SWjwPChB%2F7VlrNAkmtx6m3azdrRf2Aso3cdbJfa2rFsfKKizcUsVjB%2Fyt31h76AnbwoLYoWy2LkuziIkLtgtrxgC%2B1nJJqv1umSttwU6azba%2FgsTpMr4AEGHVmI57kxOPYZEoZcWWxc4M93L%2Bzb0sE%2BU3wW4OULu0chvH4YqDrysr1k8l2T69UjsOc0aK0q5NklwIF5ZifYp69Gps5XvdXqrRqb%2FmX8baTPxzQ3ln5UwU71CTaBiT3bHVtgj3uhD5fUiBY18Vy9cO8d5nBpIcPbuGbUpJH2nqiw4DbKSBcSuPArx%2BRryTAYmWkMjxfAPG28dwEyv5f1G%2BrSVBCQ9VMfhTMUOUmak5FX1VUeBh6q9tH1DFTq9WpWUKOg%2FSn0lLn%2F%2FnHN1RyQKvAEJSTCyMXk0%2Bu2xdJij66A5aGbJkOClpLi2LMy9DSlHdREn0tQ8A1eB0fuTHahU1z2z7Q0Yl9TBBM%2FwsXmxuPrWEQswYML6wickGOqUBUihjktyP%2FYJ0Uq0tO77%2BSjaRlayAabYzzLnDKR%2BFhPvxSLxjH6x%2BRNJdMbW%2FhstDtt5VJu7oNYglOS2k%2Fvq06xALJOiVQEoHRKZR%2Fx%2B%2BLpkbGCMimaf150T4xyM6cWOUq1RppEMnNTtWrZbznyZZSHzCEKgVh8UHj63BAhR67%2Fvpi%2BamGXCtsY%2F%2Bn0RZcSUF%2Bser5RFfzP8XoJjLoNojrfkJfXEd&X-Amz-Signature=4ac41684c55bec3dd84087b102d645cd0bd0b6c25daf9b2af416183b8f9d5a90&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







