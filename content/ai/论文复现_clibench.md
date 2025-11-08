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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2NQPGEV%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIDc4PWVapLDSSO85UFlm0jZpEVfa3Xj%2Fcdayo5RAkJEDAiAQm%2BrpcYoSXEC0qrTVmoJUoYIFu3L66rx16wX7T0lcBSqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMs29gL2XphbvXrUCGKtwDWhlOAmzBqLLkRC50lZ98NjZY8n2OV00c7fN5%2BNQhd7%2FvxK7fBQ%2F%2B558CSp%2FzVcfu2qz6I5Ju9JsoZqSuhwrsYhW2RuH0nDvVb2wF8vDIgXCDKHPo0beOG8tYYx06W1Ru%2Fizyf0l0TUZeqCbC%2BKQS2fa%2FeyePp%2FH4DcRf9LZTSj%2BnzoWahqPMRFzSxCoVXZwOsDhFW7UWbqiYMvgnTPr5sQS85Mkh0BCj%2FOUXY7r9MIbWiBwKia4gqe6s1QW060eOIQHVypb8KKEpxOQfYzcI0lg2UWep5H%2FN5nueVrvIy91%2BCikAwbjjwCrLlfbo%2FhcF5N3gEFAzsiuz9uPzpidnx41GS1ords2ZRHPMe9IDVpXbaSG%2BQpBwmnnRD6nRzLdxrG6e4XSA6C%2BbeBJBeWYtW9IgfXvcDH847wFWSaetjtLODCqmkQEWkqw9M742WTSQkUbzy4IksqX2OWp94KVh66RQkuelb2SWonRjudbbzeUWfGDahNfTQtQ%2FyRiKkHD5FwDmmJHDUAI3fPrGFZ7rPfCitFKcSodpF77PgABy21xY7RdfGXimaatCRzPFKsqeBlL8%2Fl0H7OYKbrUOuyAqxYacqf2KeSaPX9R675U772ZNDfFe%2BYNJLq5EHukwndC6yAY6pgGMy2gXbwbHYft4Pv3%2FSphpPNFPkDZ5ZmtPjxQenMvj9lEqUSg82Kcw24vT2aswLs13x3Bu4xEbK5cqmMaAFJiw4gK6EUFO6m9M%2Fr7%2F0hKvf1uWmb1bXgPoOIJBIiSr6hPVGUCGOPIai2gPLdVsG7IbsJeRlkHzjUBxqXVYEOVt4G90QEOe4uj0SF6RwX6eIN1Al0BjminfnN6DXo4FCBV0RJYUzJOz&X-Amz-Signature=bff6f7dd1fd0433431d9484d73861b5c85a150158cf961747299fddb3e7eae24&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2NQPGEV%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIDc4PWVapLDSSO85UFlm0jZpEVfa3Xj%2Fcdayo5RAkJEDAiAQm%2BrpcYoSXEC0qrTVmoJUoYIFu3L66rx16wX7T0lcBSqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMs29gL2XphbvXrUCGKtwDWhlOAmzBqLLkRC50lZ98NjZY8n2OV00c7fN5%2BNQhd7%2FvxK7fBQ%2F%2B558CSp%2FzVcfu2qz6I5Ju9JsoZqSuhwrsYhW2RuH0nDvVb2wF8vDIgXCDKHPo0beOG8tYYx06W1Ru%2Fizyf0l0TUZeqCbC%2BKQS2fa%2FeyePp%2FH4DcRf9LZTSj%2BnzoWahqPMRFzSxCoVXZwOsDhFW7UWbqiYMvgnTPr5sQS85Mkh0BCj%2FOUXY7r9MIbWiBwKia4gqe6s1QW060eOIQHVypb8KKEpxOQfYzcI0lg2UWep5H%2FN5nueVrvIy91%2BCikAwbjjwCrLlfbo%2FhcF5N3gEFAzsiuz9uPzpidnx41GS1ords2ZRHPMe9IDVpXbaSG%2BQpBwmnnRD6nRzLdxrG6e4XSA6C%2BbeBJBeWYtW9IgfXvcDH847wFWSaetjtLODCqmkQEWkqw9M742WTSQkUbzy4IksqX2OWp94KVh66RQkuelb2SWonRjudbbzeUWfGDahNfTQtQ%2FyRiKkHD5FwDmmJHDUAI3fPrGFZ7rPfCitFKcSodpF77PgABy21xY7RdfGXimaatCRzPFKsqeBlL8%2Fl0H7OYKbrUOuyAqxYacqf2KeSaPX9R675U772ZNDfFe%2BYNJLq5EHukwndC6yAY6pgGMy2gXbwbHYft4Pv3%2FSphpPNFPkDZ5ZmtPjxQenMvj9lEqUSg82Kcw24vT2aswLs13x3Bu4xEbK5cqmMaAFJiw4gK6EUFO6m9M%2Fr7%2F0hKvf1uWmb1bXgPoOIJBIiSr6hPVGUCGOPIai2gPLdVsG7IbsJeRlkHzjUBxqXVYEOVt4G90QEOe4uj0SF6RwX6eIN1Al0BjminfnN6DXo4FCBV0RJYUzJOz&X-Amz-Signature=c555c6eab7923ec5d850fa6fd3370c246cf8dc293962bd96b6393007cc02561a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







