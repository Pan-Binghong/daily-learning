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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VE2AGGW4%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCrjfWNAwXh9cFESco532yR1YsJB4GgFx8pzTWvGuIj6QIgWXgej51k5iquPLCENyn9b%2BvgEuSJzh0NupU6vAFW224qiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOZkTmdpSHtOipTxayrcA3z%2BSXfjEDzpZdfZNBkdGd0Y9S%2FPGpMY1nyibIC%2BM4fe9IYFPDO1CZEkHEbhc8cG5ZiCR8un3Re9M99KaHe03RypO%2BINmz4wcLjEuYgBt1qgwnnUvS0AjRDZyN%2FthU7FDrJCmjc8wCXzojwBZuJLC1979fv7lqPl8jO43rWhAP8sz3RuC4UvEH%2BPv5KuvZ%2F0VDPax%2F2ID0DRVOr6NQB8DVJVrsSpCtZXE9uwQnvh4nmx60V8AidfhRRHogL%2BXD1ZVypy3hlabxX9MiAN5rfbFFS7dLr1gqKn3CQ5PWf2tBR%2FdMFr%2BzIriZ51wIW%2BpRaZ2WcSvnHFNYqFK5a%2FLWqD0L0kw5lDF8VjT%2Fkm7LDaDRerOt2ZRlNiJGqNvVdGJZ9Vf1q4YHkHQ%2BvyS24GSrsj3O%2FNB9gMuHrJNLSnwnMC%2B%2Fun%2Fq0jAvux%2BfF98iN7tmzOXsZGUCpWS3uW8Bu3fy5vsMEYLzGb4rJ0uJw%2FdzxXb4gibgziciqoIijrBcSSIxmjvAOffrxlH04Dbnemco0FgNLNSgp3KTBn9W2Otn9s0fnTLsO6UgiziBESHzETY%2B5erXpXT2u32hqlW2v6mX%2BZ%2B%2BJlv34QOG15jw4DDVYbf3NDB6c6bqOLMEM3C%2BlpMJXfzMoGOqUBiWuTXlfgchVJwi%2FpvqBBzBZepfDHszUqBzwYUa21V24kBz8gK9VKP%2FJVM1xzrl3cuTz3ok0ia231tuNdy3%2Fqa9T%2Bd9gYjgJZHsaIfXzsiZUln1DQktSQDghNFLveKoMUN0HxfaexOmkDKMI2wN5dQb2A%2BI9XfuA35QzfRoBjgeJFMoqX%2B2RYY2XAd2QH%2FrIV2xlZC5S0qOc7JsVkzL%2B%2Ba9wKIfw5&X-Amz-Signature=a7d474ccfbc29039c8a36ac5d52c0a6623fba80eeff00cf0ba10212f86314053&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VE2AGGW4%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCrjfWNAwXh9cFESco532yR1YsJB4GgFx8pzTWvGuIj6QIgWXgej51k5iquPLCENyn9b%2BvgEuSJzh0NupU6vAFW224qiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOZkTmdpSHtOipTxayrcA3z%2BSXfjEDzpZdfZNBkdGd0Y9S%2FPGpMY1nyibIC%2BM4fe9IYFPDO1CZEkHEbhc8cG5ZiCR8un3Re9M99KaHe03RypO%2BINmz4wcLjEuYgBt1qgwnnUvS0AjRDZyN%2FthU7FDrJCmjc8wCXzojwBZuJLC1979fv7lqPl8jO43rWhAP8sz3RuC4UvEH%2BPv5KuvZ%2F0VDPax%2F2ID0DRVOr6NQB8DVJVrsSpCtZXE9uwQnvh4nmx60V8AidfhRRHogL%2BXD1ZVypy3hlabxX9MiAN5rfbFFS7dLr1gqKn3CQ5PWf2tBR%2FdMFr%2BzIriZ51wIW%2BpRaZ2WcSvnHFNYqFK5a%2FLWqD0L0kw5lDF8VjT%2Fkm7LDaDRerOt2ZRlNiJGqNvVdGJZ9Vf1q4YHkHQ%2BvyS24GSrsj3O%2FNB9gMuHrJNLSnwnMC%2B%2Fun%2Fq0jAvux%2BfF98iN7tmzOXsZGUCpWS3uW8Bu3fy5vsMEYLzGb4rJ0uJw%2FdzxXb4gibgziciqoIijrBcSSIxmjvAOffrxlH04Dbnemco0FgNLNSgp3KTBn9W2Otn9s0fnTLsO6UgiziBESHzETY%2B5erXpXT2u32hqlW2v6mX%2BZ%2B%2BJlv34QOG15jw4DDVYbf3NDB6c6bqOLMEM3C%2BlpMJXfzMoGOqUBiWuTXlfgchVJwi%2FpvqBBzBZepfDHszUqBzwYUa21V24kBz8gK9VKP%2FJVM1xzrl3cuTz3ok0ia231tuNdy3%2Fqa9T%2Bd9gYjgJZHsaIfXzsiZUln1DQktSQDghNFLveKoMUN0HxfaexOmkDKMI2wN5dQb2A%2BI9XfuA35QzfRoBjgeJFMoqX%2B2RYY2XAd2QH%2FrIV2xlZC5S0qOc7JsVkzL%2B%2Ba9wKIfw5&X-Amz-Signature=442c7e90ec83fc3b22cba43c681464f62af01aa82e91ef8ac36fda1431e6b56f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







