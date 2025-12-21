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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666BE4DQGT%2F20251221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251221T025954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJGMEQCIAhev6BS1Le5KyhEodBHc7pRO2L%2FJRJwHfI0zwC%2Fy8%2BfAiAihWxsWqlHIyeWrrRtzUbdxv9KLxB1GNZxTTtxOv%2BX0SqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPZSQg8pOwn18ctXDKtwD7WyDXn0YV1zFjR9M5ltuULVEsRipd8lIJbeXn2UIsmy1%2Fb%2B2A6Z%2Fo26FhiS0rifOetl2H4UzxRnE%2BbfGtPFFm9oxvxNxoowt1W9s4aCYKvWUrMNxtJ42tP34hEOA%2Bx9sAIjfQSef3zgTM1dtJUZr%2FzqDgaPK5B5L1OnI%2B2d6j2rQfIk0ScoYaZyE3jAbIvOVLKeWPNSk1pr962WL4SgNW7EewfXABF0Nk7Lo4WdJVqEfLie2zD%2B0cz0XWA9DhDH4wASLjL4Tkki4ZT1I5Tn%2Bd85Grna98VqH0ZjTMBe6AnFjBUyOUaFFfJzB%2FCAuMDmthEqUBjv%2FIJd%2BD%2BQWb7282r9QRTcZMeLFGQZwUYNvIsfPtuYtmrvBHu8HgFtaFteoAAECvYVQ5xf26x9i5QpQIKrfYFL6GoK6wm9sThBbxcekjkzbnKzheL1izRBr6ePYC0SLcyRALuMDAlM8yX9FgjY8PAFjxB1aoZl6bpZtqcirmSZ%2FlPU%2FjxLU5maEwhh8RXXjLb7bXPeRxrAUBVDWJ75xIhmM5upgOzGwoUjpElccvR4TPISMlCLUhlFYIozV61%2B0QSARe2sswD5TExdymzns%2FUr%2FOeUILwkDUbbDCdVtLnU2JTyAPrmoYZkwkvicygY6pgELN14k%2BCu7pxR%2FztfvhjmdQWmSgFWQ0%2FJOmZfWeKERjlyTeD9iNNEwjfHXJ8hX8i8OK7NDpzAuQYnTAQl5mUo%2FXVX2XHDq%2FZJBLrYBW9XAnIzROyPuP26ZI2KfY2LCJTDb%2FvTfdASNsG65zQcj2I9s%2FxY%2Ff885eXy1%2FVpxOEr25oDVkjWcrpya4sQ%2BwXnVeDUWAAfKryOoX5nQcDLLEE7NXiAz%2Fl89&X-Amz-Signature=7c532ee46b3a2fd5d6fd80f19c2a7357fdfcd3313f09a8cdbef719a6e2035eec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666BE4DQGT%2F20251221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251221T025954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJGMEQCIAhev6BS1Le5KyhEodBHc7pRO2L%2FJRJwHfI0zwC%2Fy8%2BfAiAihWxsWqlHIyeWrrRtzUbdxv9KLxB1GNZxTTtxOv%2BX0SqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPZSQg8pOwn18ctXDKtwD7WyDXn0YV1zFjR9M5ltuULVEsRipd8lIJbeXn2UIsmy1%2Fb%2B2A6Z%2Fo26FhiS0rifOetl2H4UzxRnE%2BbfGtPFFm9oxvxNxoowt1W9s4aCYKvWUrMNxtJ42tP34hEOA%2Bx9sAIjfQSef3zgTM1dtJUZr%2FzqDgaPK5B5L1OnI%2B2d6j2rQfIk0ScoYaZyE3jAbIvOVLKeWPNSk1pr962WL4SgNW7EewfXABF0Nk7Lo4WdJVqEfLie2zD%2B0cz0XWA9DhDH4wASLjL4Tkki4ZT1I5Tn%2Bd85Grna98VqH0ZjTMBe6AnFjBUyOUaFFfJzB%2FCAuMDmthEqUBjv%2FIJd%2BD%2BQWb7282r9QRTcZMeLFGQZwUYNvIsfPtuYtmrvBHu8HgFtaFteoAAECvYVQ5xf26x9i5QpQIKrfYFL6GoK6wm9sThBbxcekjkzbnKzheL1izRBr6ePYC0SLcyRALuMDAlM8yX9FgjY8PAFjxB1aoZl6bpZtqcirmSZ%2FlPU%2FjxLU5maEwhh8RXXjLb7bXPeRxrAUBVDWJ75xIhmM5upgOzGwoUjpElccvR4TPISMlCLUhlFYIozV61%2B0QSARe2sswD5TExdymzns%2FUr%2FOeUILwkDUbbDCdVtLnU2JTyAPrmoYZkwkvicygY6pgELN14k%2BCu7pxR%2FztfvhjmdQWmSgFWQ0%2FJOmZfWeKERjlyTeD9iNNEwjfHXJ8hX8i8OK7NDpzAuQYnTAQl5mUo%2FXVX2XHDq%2FZJBLrYBW9XAnIzROyPuP26ZI2KfY2LCJTDb%2FvTfdASNsG65zQcj2I9s%2FxY%2Ff885eXy1%2FVpxOEr25oDVkjWcrpya4sQ%2BwXnVeDUWAAfKryOoX5nQcDLLEE7NXiAz%2Fl89&X-Amz-Signature=2d82a4d5da4a53383ab51df7097a6fdfef0cf35ae9242596f9d63ecacc3a93ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







