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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SODA6HGK%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T025947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJIMEYCIQDxvOCMwNKFhhhz%2FVHcwsfes0NyL9lGrHkGF88e8ZqDOQIhANDtdL2BOCQechlePVPBkLXk%2FbNw%2FZz0%2Fk7ANbp%2FYpytKv8DCD8QABoMNjM3NDIzMTgzODA1IgxZt5dFNAwcYaI4J6Mq3APbSboojyLkpGfp5%2BBGKFp00Lio25zyGi7zpPpd44qhWlrP%2BpHFjnRRl5JDxu6dkLsoxokAKxqp16OJ70R4eaGS9Yy0DZ%2BRQ6RlLK7izA7uUN7QI0O2TqbVEj2LS%2FxZr0HMVxE%2BkGoCdD0ar%2FXq16buNxbIMGsNa77A6yQEvsH8B0eU8kVq169e4Ld4yC6V9e%2FSujJQPn8tM8hsNo%2FQJLnG1BKIGDBwgj1E%2Fh7uaEMdyUntRD0VJUfApjIj57GKq2IGDM85QSGcYHwNkQ1my9PzbLHn1%2FW0vJEZf6PZY5%2BC4osf6K1StslIuPC8wSCq1J86mIChfjnfjnaKtbi3boz14bJmViK9Ke0mJE291Ovg9wBOSdi8ilOMMFzxXQ2ISrnzciq1YyHgVhnBTB9Ddj%2BLQn7E6ln1A3OZYr%2BTb9uUhVhyvyXv9BCrVTWxXwNMmGs3etJgIuu5vo2UWptMIruR8fxEtakoW7tFTmsaN%2FdyDnLoytYy%2F8bay8GW37BIk9YpkSke6vd5m6IRnhsQ1cQh0IKHhZSaYOidajgjLChVtx329nFH2AW5%2FtQRNMKVdCojPMkdb%2FYW0huraBn2auMYNVMTBWjKv%2B1wsMS7VZb5012%2FcwZFcotIYAlJSTCw2vzJBjqkAYGjmvGRiMmAPk%2FI2wK%2FZg5dIFkWMR7K1Z64kJiHcuiY0OWkOHBIi%2FRUOoOpzeNuV8mFDfpz9C2jw8Upz%2BOIMu34CczOImPaKC7Bznqx1v%2BgoLyvX8PXxem1gfZzlBWCENAlg7ErR0Qc7Ed2XgEaan1njSllnCWChhJEIk382gvvq53xozgmUognLLyJVvtHuLp7rYeA55HZGWVDfc%2BSzLdK1huN&X-Amz-Signature=50ef5def4bf91a89129a52504e7dcb126a39368c1e3f64f7f589910bc35a0d58&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SODA6HGK%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T025947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJIMEYCIQDxvOCMwNKFhhhz%2FVHcwsfes0NyL9lGrHkGF88e8ZqDOQIhANDtdL2BOCQechlePVPBkLXk%2FbNw%2FZz0%2Fk7ANbp%2FYpytKv8DCD8QABoMNjM3NDIzMTgzODA1IgxZt5dFNAwcYaI4J6Mq3APbSboojyLkpGfp5%2BBGKFp00Lio25zyGi7zpPpd44qhWlrP%2BpHFjnRRl5JDxu6dkLsoxokAKxqp16OJ70R4eaGS9Yy0DZ%2BRQ6RlLK7izA7uUN7QI0O2TqbVEj2LS%2FxZr0HMVxE%2BkGoCdD0ar%2FXq16buNxbIMGsNa77A6yQEvsH8B0eU8kVq169e4Ld4yC6V9e%2FSujJQPn8tM8hsNo%2FQJLnG1BKIGDBwgj1E%2Fh7uaEMdyUntRD0VJUfApjIj57GKq2IGDM85QSGcYHwNkQ1my9PzbLHn1%2FW0vJEZf6PZY5%2BC4osf6K1StslIuPC8wSCq1J86mIChfjnfjnaKtbi3boz14bJmViK9Ke0mJE291Ovg9wBOSdi8ilOMMFzxXQ2ISrnzciq1YyHgVhnBTB9Ddj%2BLQn7E6ln1A3OZYr%2BTb9uUhVhyvyXv9BCrVTWxXwNMmGs3etJgIuu5vo2UWptMIruR8fxEtakoW7tFTmsaN%2FdyDnLoytYy%2F8bay8GW37BIk9YpkSke6vd5m6IRnhsQ1cQh0IKHhZSaYOidajgjLChVtx329nFH2AW5%2FtQRNMKVdCojPMkdb%2FYW0huraBn2auMYNVMTBWjKv%2B1wsMS7VZb5012%2FcwZFcotIYAlJSTCw2vzJBjqkAYGjmvGRiMmAPk%2FI2wK%2FZg5dIFkWMR7K1Z64kJiHcuiY0OWkOHBIi%2FRUOoOpzeNuV8mFDfpz9C2jw8Upz%2BOIMu34CczOImPaKC7Bznqx1v%2BgoLyvX8PXxem1gfZzlBWCENAlg7ErR0Qc7Ed2XgEaan1njSllnCWChhJEIk382gvvq53xozgmUognLLyJVvtHuLp7rYeA55HZGWVDfc%2BSzLdK1huN&X-Amz-Signature=d6c5ba20ab6986dec9d052216339953f3f6c1cc5c2b46a026b382f7c21671e19&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







