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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666U4YTBGT%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T034951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEomQJmGtzmadZ5MQC0U1WyohUv0VTZ4m8GlpNHTWEYAAiAE0veLbF1cV9aSB1QcRQ5d3TBmZ%2FpDKHUDUapcPjPCtyqIBAjE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGQHAOh9W8NZLavYEKtwDHthH%2BaVpzUNZtKO3%2FHwNu2CUu5z0RRSFcZVDz76QDr1M7JkUuZFkXQRbP1JenwT1J4kjvDkiyTvwaBkrdwfEZmOjhdgu%2Ff0fyCGefgoFELAaLcQVjwoi8iXecq1NF6TH3gb8oHoed8SkhIETRmn%2FmseNLOZ1GxsckEBuv1gxMz87LG14Qi%2Bmsbv9vj982xEumFg2SaUevV4rIjHPAROnwoobnX0KKT90VstlY8NmVv4eKsjOqnPVi3KP4pwkNGIb5p9Ee9VW5rpv%2F7ae7hEo301Ikgi3nsALQTwXhVTwDfrYq8cV1gtAJMwi383TbKFfUcj036lXDeqQzfSHUDzStdIvweIOuQu8ZuHto2BtlHR40tmGFkrvj0mGoW%2FhcdxiRKnj2oVhf79rz%2B1G9ub1wHoGPf8GHsjBB3Nb%2BCEx7U3RAlNyFzxk%2B2mGwYP5A23cY5uxdZnJ98h3DpPzYcm%2B43sdEHt2SlatiibimbFs7jDzgz%2BXIk3p5iCOHE9Q27DixLg%2BKwTA0RU2jTKAO3BikGZT45UcZ%2BI6D7orSzAPWm4ACPy0vwm8KXUsdaKVuuCaCWIph81xIMnHUcrWQxYrRUfkQIkW7J3y9RzJk0N2sr9KJpDd3tedXgfnF78wko37ywY6pgEFgIyG1rpu4mT%2FyJ6UgoJLsSg8JxW65%2F%2B0zfKnQsPFx%2BP1aOoENneCoj5tGARvlBxa860m5aQRiAB7g8FTVDH%2BKGNlArtsU75ZIeAvcs5CK1hOhrxkBILWpF%2Fa2A%2BT1Fg810clW75ffY%2FZuI3STwp0PaNqMYZuqQtYEiemSaE2HnY%2BYV3CXLY%2BPFF1IgfoNqaazgPJ%2F%2BRWF5wcNIZKqKTQZsUDnbsw&X-Amz-Signature=ff35b14a14c2c25ef20e4a78ba03ee26b6496f902a99b430f7a1894b9b7e0f69&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666U4YTBGT%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T034951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEomQJmGtzmadZ5MQC0U1WyohUv0VTZ4m8GlpNHTWEYAAiAE0veLbF1cV9aSB1QcRQ5d3TBmZ%2FpDKHUDUapcPjPCtyqIBAjE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGQHAOh9W8NZLavYEKtwDHthH%2BaVpzUNZtKO3%2FHwNu2CUu5z0RRSFcZVDz76QDr1M7JkUuZFkXQRbP1JenwT1J4kjvDkiyTvwaBkrdwfEZmOjhdgu%2Ff0fyCGefgoFELAaLcQVjwoi8iXecq1NF6TH3gb8oHoed8SkhIETRmn%2FmseNLOZ1GxsckEBuv1gxMz87LG14Qi%2Bmsbv9vj982xEumFg2SaUevV4rIjHPAROnwoobnX0KKT90VstlY8NmVv4eKsjOqnPVi3KP4pwkNGIb5p9Ee9VW5rpv%2F7ae7hEo301Ikgi3nsALQTwXhVTwDfrYq8cV1gtAJMwi383TbKFfUcj036lXDeqQzfSHUDzStdIvweIOuQu8ZuHto2BtlHR40tmGFkrvj0mGoW%2FhcdxiRKnj2oVhf79rz%2B1G9ub1wHoGPf8GHsjBB3Nb%2BCEx7U3RAlNyFzxk%2B2mGwYP5A23cY5uxdZnJ98h3DpPzYcm%2B43sdEHt2SlatiibimbFs7jDzgz%2BXIk3p5iCOHE9Q27DixLg%2BKwTA0RU2jTKAO3BikGZT45UcZ%2BI6D7orSzAPWm4ACPy0vwm8KXUsdaKVuuCaCWIph81xIMnHUcrWQxYrRUfkQIkW7J3y9RzJk0N2sr9KJpDd3tedXgfnF78wko37ywY6pgEFgIyG1rpu4mT%2FyJ6UgoJLsSg8JxW65%2F%2B0zfKnQsPFx%2BP1aOoENneCoj5tGARvlBxa860m5aQRiAB7g8FTVDH%2BKGNlArtsU75ZIeAvcs5CK1hOhrxkBILWpF%2Fa2A%2BT1Fg810clW75ffY%2FZuI3STwp0PaNqMYZuqQtYEiemSaE2HnY%2BYV3CXLY%2BPFF1IgfoNqaazgPJ%2F%2BRWF5wcNIZKqKTQZsUDnbsw&X-Amz-Signature=01941dc136ee4f0ecfe382af711d7c310232e515f5f8892e231edc3b84731311&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







