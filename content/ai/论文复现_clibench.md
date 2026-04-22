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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UH63CQ6P%2F20260422%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260422T040932Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIHXBgH9wL0%2B2bSTqP%2BXQl9F8zCk218DVDyu886%2BiIP%2FnAiAwZX8emm0630dbxRIVIsWVaaT0B3bVj8E%2FIWyJQMHu5yr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMirpfSLN6c%2BYQXVQFKtwDhU8bnMEsBpcCVC0ZV36Q0hHQiI1jJPrTkd01os1BF6cSi%2FH3e2lpsyj5zB%2FmkToH2Thp1UuJjIReCknb9B0diK4uWRi2Me3CB5gIrW0DEyMXZCOMOIcyWZdnIZdkEe7feLiKu6L6lvMh0ZVhlK0qUap4z%2FZfdxhnqyP2LLbF2qUYsybIXYoAjWRRSIYQWbevNVo5sPiWxV%2FCtjj7srfEqNEREJpsrM4MHRggnOuE9GG%2BGMoszNZJgd8ogboW7paGD05g3yjdxayNPl6%2Bot%2BW9r%2BuuaEAL%2FUmb8d%2BVcdgtIPqgGzAlHrG%2B5DKhdxptxro6vESAPlFSBOBqykSr%2BG6SgBOwWO4ACON2ue2l9dqMVgIOnMtjvwDRKVflM3dFZg%2BTzeJp5HKjGImKEM8Jq4U0OecSexi%2Bea5AS1KGo6vvQsbuhuHuVn58SVRB%2B0dTpQfiQR4M%2FsoKku70uHaAERg8uxO7YBrOjunpVbTyhtJihhLxAKu4ZE6sV6gviOc%2BGVJOdHlmsfYjxnKl3j7CmUYm4a32DI%2FV2kdyMxWSeqwUY8n86CE2fnAqOxwYyjgzS%2FSqxyEeg6DmjSisM1DEZYf04mDmsDHHhMJ1S%2BaTDOf0pWEYZrx386A%2Foroy00wzvmgzwY6pgGXuuYG3yEGgrJtRb0gnwbDig0%2FX3XCqvvx8Nn%2FwumJL2JT6hP6uCN02%2BzTXYeHkdgH61P9KDDUiWUMr0xYXfhVwsV3SUFjo6UOxLwkJ69hGMqtNSr7SZUHIc01bIN0Vq5%2BczCfiYaZavC5hK7GDUm8sGvkSxdUEeS6bmBkYHGG4kDdFdfWB6XTuK5eJ%2FJ3YyopsaLcqZGbWJVJNJE%2B3W6KpYKbA5EO&X-Amz-Signature=1d2d20a5172b7d5c1303307be2539a47ccab793da0caceb835dcce2f7cb65c5a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UH63CQ6P%2F20260422%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260422T040932Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIHXBgH9wL0%2B2bSTqP%2BXQl9F8zCk218DVDyu886%2BiIP%2FnAiAwZX8emm0630dbxRIVIsWVaaT0B3bVj8E%2FIWyJQMHu5yr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMirpfSLN6c%2BYQXVQFKtwDhU8bnMEsBpcCVC0ZV36Q0hHQiI1jJPrTkd01os1BF6cSi%2FH3e2lpsyj5zB%2FmkToH2Thp1UuJjIReCknb9B0diK4uWRi2Me3CB5gIrW0DEyMXZCOMOIcyWZdnIZdkEe7feLiKu6L6lvMh0ZVhlK0qUap4z%2FZfdxhnqyP2LLbF2qUYsybIXYoAjWRRSIYQWbevNVo5sPiWxV%2FCtjj7srfEqNEREJpsrM4MHRggnOuE9GG%2BGMoszNZJgd8ogboW7paGD05g3yjdxayNPl6%2Bot%2BW9r%2BuuaEAL%2FUmb8d%2BVcdgtIPqgGzAlHrG%2B5DKhdxptxro6vESAPlFSBOBqykSr%2BG6SgBOwWO4ACON2ue2l9dqMVgIOnMtjvwDRKVflM3dFZg%2BTzeJp5HKjGImKEM8Jq4U0OecSexi%2Bea5AS1KGo6vvQsbuhuHuVn58SVRB%2B0dTpQfiQR4M%2FsoKku70uHaAERg8uxO7YBrOjunpVbTyhtJihhLxAKu4ZE6sV6gviOc%2BGVJOdHlmsfYjxnKl3j7CmUYm4a32DI%2FV2kdyMxWSeqwUY8n86CE2fnAqOxwYyjgzS%2FSqxyEeg6DmjSisM1DEZYf04mDmsDHHhMJ1S%2BaTDOf0pWEYZrx386A%2Foroy00wzvmgzwY6pgGXuuYG3yEGgrJtRb0gnwbDig0%2FX3XCqvvx8Nn%2FwumJL2JT6hP6uCN02%2BzTXYeHkdgH61P9KDDUiWUMr0xYXfhVwsV3SUFjo6UOxLwkJ69hGMqtNSr7SZUHIc01bIN0Vq5%2BczCfiYaZavC5hK7GDUm8sGvkSxdUEeS6bmBkYHGG4kDdFdfWB6XTuK5eJ%2FJ3YyopsaLcqZGbWJVJNJE%2B3W6KpYKbA5EO&X-Amz-Signature=cd2cae3fb6e342d9a5107fa53f9f1a557f2e1171ac7dcefb8529fcce69546e52&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







