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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFV2B4N2%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T040943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4Xe2dTBt2Iq96fSh7Hxk%2BuPJIhbtMgmbDBj4KIiRBHQIhAObV%2FPROXnzEREJ8rwWT7Ujjp6muMkXJypsKC%2BLaH7VMKogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzPkRo89BCFJymHEV0q3AP6rknCQPKrbUlrstkMDR%2FSbumoBXprUBDM8CMH9FoO2TB0KZWms73IGmEN9lIO3cibGzmGzG6QvG2AsqFfP3DgR2FlLdo1lz1sHhG7X7oW%2FE7p7%2FK4qjf7j%2B2zCehDZZtZkhPL%2BxxnNCf%2BRosW438hhU4I%2Fc9Y1gOul%2BPerOCi2czV5kVAGpoT29IaBf9R%2FGVyrdrU7nJpex0d56vSHpenPLKsjPWnVKOb8doQ2m5zlqn9o0lfaO1S51uaEje7gCCYGEh3kx%2BXrcsXl%2B4QGNqwJKSetssM8YbQaWsDtZY%2B%2BZ71tgm3SVnfO%2FHmi2B%2FByxLLH0Dyar3nWD6DEq%2FJ8N%2FCgnbRgNTXlQBh%2BlmgluO8DAFIY5RO1W5W%2B3AlomDiVk%2BzmhNRVm4KqhhGm%2BceInMb3tvcXNTKSVGxQ42rAzsRRuBBSa7oT%2F5ICf19FZ3mwFnGSwF10jlH5tGUZ8iKBpiXYpMD1dPy2xumjI%2FbX5kgdncXHJFQZ0Vh%2FLrpaVAnRJVcWgcEAKjNlEMLMo9IlyLJvpUJty9rGg9P1XM4KuIvSxUJa7GlOXbHsuRuYpzG5ER0aY%2FBmYcTQzJVq8KbjC53QFnF8USHR1wCoalxWmkA2006IZRthyVpsEGujCblfzOBjqkATbAEdK7FiodNgtbvkKzY%2FKqJpFw5ke%2BtpjgPKzN8oB9Vw0gKwUwL1o14VlMQTqZ%2BS72kjihlRKrCZBXlswGq3o3SZTV%2FbXAAGhrm7DhShLVd62wbOsgHZfLlvyuRD4T4HmbdPSCy5vsA4cZFHKCL4izIDWrP5pDrqcS5Ff%2FzfD9hTacH7D0uEKD04zEHYdNNOqvv4W%2BTVhObuiaE1M9eDnFqa5i&X-Amz-Signature=b2bfc2d114d94b5b7e1b8a4d5fba86050a587a2e3e1de01feef344bdb4c2f9cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFV2B4N2%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T040943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4Xe2dTBt2Iq96fSh7Hxk%2BuPJIhbtMgmbDBj4KIiRBHQIhAObV%2FPROXnzEREJ8rwWT7Ujjp6muMkXJypsKC%2BLaH7VMKogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzPkRo89BCFJymHEV0q3AP6rknCQPKrbUlrstkMDR%2FSbumoBXprUBDM8CMH9FoO2TB0KZWms73IGmEN9lIO3cibGzmGzG6QvG2AsqFfP3DgR2FlLdo1lz1sHhG7X7oW%2FE7p7%2FK4qjf7j%2B2zCehDZZtZkhPL%2BxxnNCf%2BRosW438hhU4I%2Fc9Y1gOul%2BPerOCi2czV5kVAGpoT29IaBf9R%2FGVyrdrU7nJpex0d56vSHpenPLKsjPWnVKOb8doQ2m5zlqn9o0lfaO1S51uaEje7gCCYGEh3kx%2BXrcsXl%2B4QGNqwJKSetssM8YbQaWsDtZY%2B%2BZ71tgm3SVnfO%2FHmi2B%2FByxLLH0Dyar3nWD6DEq%2FJ8N%2FCgnbRgNTXlQBh%2BlmgluO8DAFIY5RO1W5W%2B3AlomDiVk%2BzmhNRVm4KqhhGm%2BceInMb3tvcXNTKSVGxQ42rAzsRRuBBSa7oT%2F5ICf19FZ3mwFnGSwF10jlH5tGUZ8iKBpiXYpMD1dPy2xumjI%2FbX5kgdncXHJFQZ0Vh%2FLrpaVAnRJVcWgcEAKjNlEMLMo9IlyLJvpUJty9rGg9P1XM4KuIvSxUJa7GlOXbHsuRuYpzG5ER0aY%2FBmYcTQzJVq8KbjC53QFnF8USHR1wCoalxWmkA2006IZRthyVpsEGujCblfzOBjqkATbAEdK7FiodNgtbvkKzY%2FKqJpFw5ke%2BtpjgPKzN8oB9Vw0gKwUwL1o14VlMQTqZ%2BS72kjihlRKrCZBXlswGq3o3SZTV%2FbXAAGhrm7DhShLVd62wbOsgHZfLlvyuRD4T4HmbdPSCy5vsA4cZFHKCL4izIDWrP5pDrqcS5Ff%2FzfD9hTacH7D0uEKD04zEHYdNNOqvv4W%2BTVhObuiaE1M9eDnFqa5i&X-Amz-Signature=e84b2849785211fb35e97b2fc9ad3e182082635346ec2330846c46eb8f1fe608&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







