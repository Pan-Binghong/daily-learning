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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVUECTRN%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCzzdLTaeG%2FKEjxGk1I1TVJRw20jPFiNgmdv54wUaEhygIhAOsgMPeP3O04u%2BTX96n6wX%2BHLb9p1RjLLCA8VqNAX7c0Kv8DCH8QABoMNjM3NDIzMTgzODA1IgwSXWN73s9MGF3lcnsq3ANMfd%2BSuUxHL0koIwY5f5TNN105gj%2BbdPSnBy%2FybfUnUxMfS6uHvZLlUKP03NQ3s1Y%2FrXBbebomQvvGwkGFbKjU8syL%2FsLYpmlJdNEgKe%2FvYM7DDqkbkJNzVO0ThzpM9PYGmqLfUJwBPtj1rAIJgEBRbgLBRphEHGlTXK46spe7KM7Tgpfoe4EVKv5w7KS0Cr1jjhdRt8gmvKDTyfJSrR2aqipXYN8nDHYAdO62syQmsDKtLdffFRxWZ%2BdF%2BQtz6sn1Tn36GpbNd3pw9xEfRUevMSw4nE83ivbn8nSbqe8y16VnTnxRUWLyEQLEtuNIrxII933tvkxRvmkZ8Z3oGKmUcbWHpzrnfzEsTp2pFr9ll%2FLJ6G8XQBQBshRvWw3WnRVvnByAlFJOFLrNqU%2B9GmUgW9qN9qQrcQZ1C5WmlXuM2zhKtLurOTx9Vs9arEQIMSTMsVU1EnZGxIOm7FhzrjiSaMtv0wGlGcm3zBi5nIMo4nSuQwi3VIjkFAReMSwxsa5l0MxiAhZ0Gw8FboyZ7z4SMqaH16Id%2BDvM5Nhmzz0N67k4NiofKi3t%2BhT8gYYlMqsbP7rNGztBAnBQ3N4rxtpZWwFPjfebhCyX%2BXhacFBPZEQPvrttok7nv%2FV0VzDbq73OBjqkAQHLYt%2FItU5pEzh5J5j3HCNXRjq5MKjgEFA7vUeVyGL8t6ugoONiNYksWroIBfJm5mqyEsvh33f59rJEk%2FQasyaq5SZll9PrEook73AJI39l%2BPOudYyh%2BAXM1PqVEtvcytNMlCwnep0GM5btbdke7QHaXvZxYpsqZVRxEFBj80WJPh%2BEbrcnVSibLFS5BFz9mFwIxqLIsrHTk3XZQBqaZd5EKtEG&X-Amz-Signature=b1c35bc65fbaa2e573d1e3143ebf95241f2c7a3caea5fcddcd9f37b34385a1a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVUECTRN%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCzzdLTaeG%2FKEjxGk1I1TVJRw20jPFiNgmdv54wUaEhygIhAOsgMPeP3O04u%2BTX96n6wX%2BHLb9p1RjLLCA8VqNAX7c0Kv8DCH8QABoMNjM3NDIzMTgzODA1IgwSXWN73s9MGF3lcnsq3ANMfd%2BSuUxHL0koIwY5f5TNN105gj%2BbdPSnBy%2FybfUnUxMfS6uHvZLlUKP03NQ3s1Y%2FrXBbebomQvvGwkGFbKjU8syL%2FsLYpmlJdNEgKe%2FvYM7DDqkbkJNzVO0ThzpM9PYGmqLfUJwBPtj1rAIJgEBRbgLBRphEHGlTXK46spe7KM7Tgpfoe4EVKv5w7KS0Cr1jjhdRt8gmvKDTyfJSrR2aqipXYN8nDHYAdO62syQmsDKtLdffFRxWZ%2BdF%2BQtz6sn1Tn36GpbNd3pw9xEfRUevMSw4nE83ivbn8nSbqe8y16VnTnxRUWLyEQLEtuNIrxII933tvkxRvmkZ8Z3oGKmUcbWHpzrnfzEsTp2pFr9ll%2FLJ6G8XQBQBshRvWw3WnRVvnByAlFJOFLrNqU%2B9GmUgW9qN9qQrcQZ1C5WmlXuM2zhKtLurOTx9Vs9arEQIMSTMsVU1EnZGxIOm7FhzrjiSaMtv0wGlGcm3zBi5nIMo4nSuQwi3VIjkFAReMSwxsa5l0MxiAhZ0Gw8FboyZ7z4SMqaH16Id%2BDvM5Nhmzz0N67k4NiofKi3t%2BhT8gYYlMqsbP7rNGztBAnBQ3N4rxtpZWwFPjfebhCyX%2BXhacFBPZEQPvrttok7nv%2FV0VzDbq73OBjqkAQHLYt%2FItU5pEzh5J5j3HCNXRjq5MKjgEFA7vUeVyGL8t6ugoONiNYksWroIBfJm5mqyEsvh33f59rJEk%2FQasyaq5SZll9PrEook73AJI39l%2BPOudYyh%2BAXM1PqVEtvcytNMlCwnep0GM5btbdke7QHaXvZxYpsqZVRxEFBj80WJPh%2BEbrcnVSibLFS5BFz9mFwIxqLIsrHTk3XZQBqaZd5EKtEG&X-Amz-Signature=b52e0f045d6d1ea6bfb4a820f93824dc2df4f100b259560e22c63ddcf334d79b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







