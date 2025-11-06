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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4HJDJHT%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD4UbGfToEGjCzK9naHvjFsNCBiU1l%2BrZj8011TrfhdzgIgLry%2BSOx12Bp6KsoyRTH3gkujgQtEqvNdPqWJu4HsBDMqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAYwqkXlpqFRYb7wYyrcA2wBREMpl%2FsppgqR6IVDu1zPr9Bz7HxyLYWpIhCCFQsWKfPxrIEEcQCq7ij7ZHIN9rUXjQatAJvr9YnqN9l2kso0oip1QwE%2BZk9OeTf%2Fa9S974aqolm3hZO%2FYnZe6VJEnOWJigfPy94OyanE7CSQHR6N8JMIynqKR3oe1PSwLihJmD%2BHFOX7K%2B7qH6xYgXDTh00SZeNeNY4O%2FhFBr9FoUDTx6nys2CqrshecwQoKyIQ2gbN9mGSaGApxZrmAS6KtSA%2BdlFXG%2BxHWFD7h%2B1azcvH8Xcsuu9An2ADGF%2Fku75k7%2FRKpUA%2FKg8x%2FjrMpfAiNrva8iAsixtfD7kmtbYYghne25OGQzZ3lMuzbrzGy18ywpYZAn23EusTw5GQmWmUWHatX1LMwGspG68poesWVx4Bw%2BtnA5E%2FH2DHgt0Uk%2Fa5LV5kIk7IXrIrqGp6tWAESJO3VXOCb8MEmVygApxqEgEV1YUKdV9gmy886CXpvnbi9Ly7uWTxbPe%2BLGIsJCuhRameg7eG2xYgogesE0%2BRr8nlNrz8IEu57z7e8Ucb6i3%2BaP0Ycwca9q2PNngpSWmbvgZ48HnSGDj2gDGUmZErbmf2wPcLA%2Bz0AMSHSYC86wkhJxoOhdeRYGiNbZVVcMIXxr8gGOqUBHDiz88mtCRrIHARnkb3chryhdjBOV15IUBti7rSsrHVF8Sjm0lps%2BlVjLlKi6pDbe41iURuuQ1HNmg0dlYnzFmoLn3iViGjuGWTxQKM9DV5LP7RJROWfLaWZRtArD%2BNVrdGTGG7E94jPt3SsDr6NTTQPC7GLCJ0deuxzhpdCErEfWlXm%2BFmP9v3AJZg9OXmA2ftgCid6LlB5MRdRet2K9AOVcpR3&X-Amz-Signature=bf615c50c9c497b5b76eeb84246059d1ad19fd6a07c215a9872743ce0abd0721&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4HJDJHT%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD4UbGfToEGjCzK9naHvjFsNCBiU1l%2BrZj8011TrfhdzgIgLry%2BSOx12Bp6KsoyRTH3gkujgQtEqvNdPqWJu4HsBDMqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAYwqkXlpqFRYb7wYyrcA2wBREMpl%2FsppgqR6IVDu1zPr9Bz7HxyLYWpIhCCFQsWKfPxrIEEcQCq7ij7ZHIN9rUXjQatAJvr9YnqN9l2kso0oip1QwE%2BZk9OeTf%2Fa9S974aqolm3hZO%2FYnZe6VJEnOWJigfPy94OyanE7CSQHR6N8JMIynqKR3oe1PSwLihJmD%2BHFOX7K%2B7qH6xYgXDTh00SZeNeNY4O%2FhFBr9FoUDTx6nys2CqrshecwQoKyIQ2gbN9mGSaGApxZrmAS6KtSA%2BdlFXG%2BxHWFD7h%2B1azcvH8Xcsuu9An2ADGF%2Fku75k7%2FRKpUA%2FKg8x%2FjrMpfAiNrva8iAsixtfD7kmtbYYghne25OGQzZ3lMuzbrzGy18ywpYZAn23EusTw5GQmWmUWHatX1LMwGspG68poesWVx4Bw%2BtnA5E%2FH2DHgt0Uk%2Fa5LV5kIk7IXrIrqGp6tWAESJO3VXOCb8MEmVygApxqEgEV1YUKdV9gmy886CXpvnbi9Ly7uWTxbPe%2BLGIsJCuhRameg7eG2xYgogesE0%2BRr8nlNrz8IEu57z7e8Ucb6i3%2BaP0Ycwca9q2PNngpSWmbvgZ48HnSGDj2gDGUmZErbmf2wPcLA%2Bz0AMSHSYC86wkhJxoOhdeRYGiNbZVVcMIXxr8gGOqUBHDiz88mtCRrIHARnkb3chryhdjBOV15IUBti7rSsrHVF8Sjm0lps%2BlVjLlKi6pDbe41iURuuQ1HNmg0dlYnzFmoLn3iViGjuGWTxQKM9DV5LP7RJROWfLaWZRtArD%2BNVrdGTGG7E94jPt3SsDr6NTTQPC7GLCJ0deuxzhpdCErEfWlXm%2BFmP9v3AJZg9OXmA2ftgCid6LlB5MRdRet2K9AOVcpR3&X-Amz-Signature=ce0df67ac4f6195b7852d759de86461fe07d6820fb8de4236b555c14123ee0e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







