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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZSE2HOK%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCrACZFq%2F20Wahq3fhpD6m5%2BeG9%2F2ddAcEYnC2vxCfCXwIgdF5Sl4iC9vPF9qBbrxq3xZ4RR4POik%2BlVMoYJ2e%2By%2BUq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDL0LZqbb92r2%2BP%2Ba5yrcA%2Fv9FA9B8KmU4GmEuZfqMDm%2FJPi5UWednSeUxq7Fnh1uHSktKiIqASP5tvjud%2FXnpIg%2ByDOz1OBKIKcZ0a5OsnR59PU7Xo09xWLapn55afJr1%2FeJLAFVJMcPv5j2L78Y1NRLzqkcauhgwltctlTPgrizSOVm4vwUENJ3OJGwvAwPvAZYnUqVa0n5RDQEP9Nb%2FUCiMioYyf2ZbJlkGK8fXrUk3LP7f%2BpctWEf6S%2FBK51kgN4ikq7JATZAzAnGRI%2BB%2BWbJB2R%2BE5nuUXGvnCoIePQ1hoLRiDqy9eQyCQqN008TWpD4wWt%2BWjFZMqTCHJR%2BU7%2BM%2F3iGp%2BlHowOUCykF0Zlekt2QNfA2an1euYxBAeqBUcZEirCnYZQc3b3DOPm3h%2FzBDuUQiDB178xb7jv04plOxM51TiDNXRUeQuTn4bvZktCGeHBb%2BKknafL1LoRpKxys400%2FRfsBtAlluf8cXhS2Wq%2BnyF0yllTocDYfv18%2BrRtoGPti6Q5RyCWsgI%2BZ2oEztd3nYmmIoeyXCC3Ls521Y7sXi5QNvRWSA8i%2BN5UGm5R6grwu0sZSUKR%2FgW4MhEOb2ctvAXq3aq6%2F41Hmj8tS8r2FNV%2FW9ibWfSxDJBWjO%2FoYrfH8Je9MrLffMMKtvc4GOqUBG3aJ2a6cgfYUw3v11V%2FemkY4SAqXbaTmzgDRurEVB11CFT8t%2BqotFYnQL%2FZd3n147exovN4SFJ%2F4IYftu3s6bWY1CxBMQ7bOXyOq26NHfT5K%2BKiSb1NLXyjmR5ankVvmM1TZ7g76YgF4v7lnJCen2dWR%2BvD40NDQaONh5X2VKt0P4%2B4zbVpYdS9mplHY46AuW%2Bu6%2F67zBzLpJjXfDmPaqHpc9TFO&X-Amz-Signature=0fff20e067219786767ae8d4c7003b12cf6601aa273b4ab87ee570146a74d84f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZSE2HOK%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCrACZFq%2F20Wahq3fhpD6m5%2BeG9%2F2ddAcEYnC2vxCfCXwIgdF5Sl4iC9vPF9qBbrxq3xZ4RR4POik%2BlVMoYJ2e%2By%2BUq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDL0LZqbb92r2%2BP%2Ba5yrcA%2Fv9FA9B8KmU4GmEuZfqMDm%2FJPi5UWednSeUxq7Fnh1uHSktKiIqASP5tvjud%2FXnpIg%2ByDOz1OBKIKcZ0a5OsnR59PU7Xo09xWLapn55afJr1%2FeJLAFVJMcPv5j2L78Y1NRLzqkcauhgwltctlTPgrizSOVm4vwUENJ3OJGwvAwPvAZYnUqVa0n5RDQEP9Nb%2FUCiMioYyf2ZbJlkGK8fXrUk3LP7f%2BpctWEf6S%2FBK51kgN4ikq7JATZAzAnGRI%2BB%2BWbJB2R%2BE5nuUXGvnCoIePQ1hoLRiDqy9eQyCQqN008TWpD4wWt%2BWjFZMqTCHJR%2BU7%2BM%2F3iGp%2BlHowOUCykF0Zlekt2QNfA2an1euYxBAeqBUcZEirCnYZQc3b3DOPm3h%2FzBDuUQiDB178xb7jv04plOxM51TiDNXRUeQuTn4bvZktCGeHBb%2BKknafL1LoRpKxys400%2FRfsBtAlluf8cXhS2Wq%2BnyF0yllTocDYfv18%2BrRtoGPti6Q5RyCWsgI%2BZ2oEztd3nYmmIoeyXCC3Ls521Y7sXi5QNvRWSA8i%2BN5UGm5R6grwu0sZSUKR%2FgW4MhEOb2ctvAXq3aq6%2F41Hmj8tS8r2FNV%2FW9ibWfSxDJBWjO%2FoYrfH8Je9MrLffMMKtvc4GOqUBG3aJ2a6cgfYUw3v11V%2FemkY4SAqXbaTmzgDRurEVB11CFT8t%2BqotFYnQL%2FZd3n147exovN4SFJ%2F4IYftu3s6bWY1CxBMQ7bOXyOq26NHfT5K%2BKiSb1NLXyjmR5ankVvmM1TZ7g76YgF4v7lnJCen2dWR%2BvD40NDQaONh5X2VKt0P4%2B4zbVpYdS9mplHY46AuW%2Bu6%2F67zBzLpJjXfDmPaqHpc9TFO&X-Amz-Signature=bc08438b3fce85818bcac223a6712e0c35b15de1dcde0018c1c36e137047dbf3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







