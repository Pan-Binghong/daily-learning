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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGPO6WBT%2F20260103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260103T025114Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJHMEUCICYM76STgVmXDnH4DclVYy54R0j3lxZ0NSbyPNEijYS2AiEA5atLTjVcJ4GbCn3MU4Yw8B1gAyR2G6qJ9oPXVe611hEq%2FwMICxAAGgw2Mzc0MjMxODM4MDUiDAfnTK13yZBi0BFG6yrcA6cifKOrwPRQ5Y1bHQ%2FNUIl460mNSWSg8frVh%2F%2FX7xKCYyFH95Ml%2B%2Ffdl%2BwsCD7kiuThlOQ%2BYUm%2FJTY%2FRBYKOPPDAe1G9MhqkTN%2FjDxyDkeaQEtqt63iD9%2FEi%2BpZ%2Fu47XKspyzmxa%2BW2wd4xhYp4K%2FAZyFV5Li3uWe8mTZbl8vF9by8%2FEcYAwf7z%2BT9xNzA9%2FBSpBe7Pgo6%2FnYPTXUHGbbpZgRlbf3kJEEoZRkqS0ptW3gbJCYg8lRQW554viyWS8YRFIZUVZhe0NRcLRb9AqkLIDCjAuZZtHBycJkNJzgSYRUyUr1s4rvWwzGOvHfYBrRf%2BGU4wi%2B6lWJspn6PezGaes3x9qOp0oI3hn7V9eR0tThksKrHWl48aprQjH6XHgm2a%2BhKXIF4r%2FGI%2BErOxJqBLI8SF9wXXoaZ9F3147jFo%2FdVdTzpJpmV7NrP37h07WrGRwpq9e0BEnYO1oPrUwF8FOutMcY9UMAAg6Vfj1Wj%2FGd9JsTwWor4SpSLJoacOIrGQ%2BQYDvbFNhjco7OZaNdzjjgD4cPjJO1OPJLUJl2T7ovU5N9oYyuHu8%2BS1IksBIN9tallnYszpwpjD%2FW365aOWfTtIaOwInaeOYr5MFrdhPTNPuADmHdbyo51xMLTs4coGOqUBBt1oZPzoUjF2%2FMtcKW3IoKkbs4H%2BcOsxwJTV7881dCfvv4cmMkDE2WXSoGD%2Bl09b8SQM60bfLtRFQCSckK5QXhKEZOhxnkPtbt2qxBULAm2XGJ5tqGYYm2kRELU3LGM73tFDzTjbF%2FXECTaI7oLbJFKMZ3BsQDrzdHvU02T26KD%2F0WPIIith9pbjQAn8xEC5XKopDO4syPwe5e%2B5XfVI8qWiPu28&X-Amz-Signature=3562236d6825caa37de03b4445750a0cd1adece6524e4c417b6b715d052ff47c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGPO6WBT%2F20260103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260103T025114Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJHMEUCICYM76STgVmXDnH4DclVYy54R0j3lxZ0NSbyPNEijYS2AiEA5atLTjVcJ4GbCn3MU4Yw8B1gAyR2G6qJ9oPXVe611hEq%2FwMICxAAGgw2Mzc0MjMxODM4MDUiDAfnTK13yZBi0BFG6yrcA6cifKOrwPRQ5Y1bHQ%2FNUIl460mNSWSg8frVh%2F%2FX7xKCYyFH95Ml%2B%2Ffdl%2BwsCD7kiuThlOQ%2BYUm%2FJTY%2FRBYKOPPDAe1G9MhqkTN%2FjDxyDkeaQEtqt63iD9%2FEi%2BpZ%2Fu47XKspyzmxa%2BW2wd4xhYp4K%2FAZyFV5Li3uWe8mTZbl8vF9by8%2FEcYAwf7z%2BT9xNzA9%2FBSpBe7Pgo6%2FnYPTXUHGbbpZgRlbf3kJEEoZRkqS0ptW3gbJCYg8lRQW554viyWS8YRFIZUVZhe0NRcLRb9AqkLIDCjAuZZtHBycJkNJzgSYRUyUr1s4rvWwzGOvHfYBrRf%2BGU4wi%2B6lWJspn6PezGaes3x9qOp0oI3hn7V9eR0tThksKrHWl48aprQjH6XHgm2a%2BhKXIF4r%2FGI%2BErOxJqBLI8SF9wXXoaZ9F3147jFo%2FdVdTzpJpmV7NrP37h07WrGRwpq9e0BEnYO1oPrUwF8FOutMcY9UMAAg6Vfj1Wj%2FGd9JsTwWor4SpSLJoacOIrGQ%2BQYDvbFNhjco7OZaNdzjjgD4cPjJO1OPJLUJl2T7ovU5N9oYyuHu8%2BS1IksBIN9tallnYszpwpjD%2FW365aOWfTtIaOwInaeOYr5MFrdhPTNPuADmHdbyo51xMLTs4coGOqUBBt1oZPzoUjF2%2FMtcKW3IoKkbs4H%2BcOsxwJTV7881dCfvv4cmMkDE2WXSoGD%2Bl09b8SQM60bfLtRFQCSckK5QXhKEZOhxnkPtbt2qxBULAm2XGJ5tqGYYm2kRELU3LGM73tFDzTjbF%2FXECTaI7oLbJFKMZ3BsQDrzdHvU02T26KD%2F0WPIIith9pbjQAn8xEC5XKopDO4syPwe5e%2B5XfVI8qWiPu28&X-Amz-Signature=d0b329b8f040eb48faa0c7c331b8b8f531ead40d0019af93b6ca48d73d5cfebd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







