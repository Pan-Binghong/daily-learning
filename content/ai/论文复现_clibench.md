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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZSZWS7XK%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T041614Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIAYusPTN9Zss8hl9EeYl8f7OLjWnHxb4DgYJArMAE4nXAiAvgBLmXzVrNvroqnOI6gdigohqe2b7%2BKtyuZdkdSh%2B0CqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnrKK8NWcFpWMzduUKtwDR0Mr3GNfcAfasuoSz%2BiOKohZ6FMFmusjO3ONgPNRr21pr0p8iQsodIDH%2BQz3gbcq08C2bEBkbaHa%2B3iJhhpnev1oW9k1xbI4O6MxP70kpqe9XdYL8J5ax3mmHvRWm0CCewMAPSXP28qPdJPVV4DenLC%2FkLxu1%2FW0eNjjQTzbd59qThFRfI0nt4TkeDtmY%2Bg8h9CicPF4IH4ev54Fqpx5%2FJdHuAs4mDqiYsM0Gh4%2FnUWHGJA2PiDGu%2FUHUujZLDleIt%2Bp1k2U8zCnSyuzNPkk8H3wDPiJQMMCg%2FdmA%2BF2fZCwu99Qiy7QeJjhBTKYKxwS9rPkOVc2Ve0WMv%2BRE0%2Bw7Lc8XNUeYsjTsVyyg3SkC6pX11cpAVpqZFAvh5vbtjelnvIu3CbqDw%2Bd084e6W9xSiBhGoEcFkiq0nSnJuDAlTCESsS2D%2BsYdO%2F6GdiRVl0r6nXmPv2xXVEUF8o4YAm2K8ucMRZFNCptMDa0IBCG8sao22XBi7MpGTIw0yd0lX2srUlcCtRRculbVuCP8tdYK6p2HehUOAkiD6mHoDwaQjjm%2FfPvxYxI5hpnOn2fHhASYeu5mdQ8cXOO1zj3uFkmuZ9ET9fJlFqOnCmlUDKW9nGsWgBYd2JBYiL6XsIw3tyQzwY6pgGzZu%2BV%2Fr3uSRQ6xsjHP8VPBvvN85huvB0cdFZlqDbS%2BP0pjPNEVbtVmsJhjAz1p5Pt27yqTvaavjkeDnPtloU4qTXIOmwwzjtQPrtPPnk9Nxisbj3u3B9ylf9S81xBI7C7ObEtvoSL1%2FCMBTJtCSKC2JgNTeNfTUnYUNS%2Bc8rqWvamZG6R03jG3rksXJqkhvBeMhXtQaTs92OiBjsQ3dLfkbkBiuX4&X-Amz-Signature=f0f9afe956861423e2c3b1d0a36d54cc4529186f95a38a0645372405d62172e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZSZWS7XK%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T041614Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIAYusPTN9Zss8hl9EeYl8f7OLjWnHxb4DgYJArMAE4nXAiAvgBLmXzVrNvroqnOI6gdigohqe2b7%2BKtyuZdkdSh%2B0CqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnrKK8NWcFpWMzduUKtwDR0Mr3GNfcAfasuoSz%2BiOKohZ6FMFmusjO3ONgPNRr21pr0p8iQsodIDH%2BQz3gbcq08C2bEBkbaHa%2B3iJhhpnev1oW9k1xbI4O6MxP70kpqe9XdYL8J5ax3mmHvRWm0CCewMAPSXP28qPdJPVV4DenLC%2FkLxu1%2FW0eNjjQTzbd59qThFRfI0nt4TkeDtmY%2Bg8h9CicPF4IH4ev54Fqpx5%2FJdHuAs4mDqiYsM0Gh4%2FnUWHGJA2PiDGu%2FUHUujZLDleIt%2Bp1k2U8zCnSyuzNPkk8H3wDPiJQMMCg%2FdmA%2BF2fZCwu99Qiy7QeJjhBTKYKxwS9rPkOVc2Ve0WMv%2BRE0%2Bw7Lc8XNUeYsjTsVyyg3SkC6pX11cpAVpqZFAvh5vbtjelnvIu3CbqDw%2Bd084e6W9xSiBhGoEcFkiq0nSnJuDAlTCESsS2D%2BsYdO%2F6GdiRVl0r6nXmPv2xXVEUF8o4YAm2K8ucMRZFNCptMDa0IBCG8sao22XBi7MpGTIw0yd0lX2srUlcCtRRculbVuCP8tdYK6p2HehUOAkiD6mHoDwaQjjm%2FfPvxYxI5hpnOn2fHhASYeu5mdQ8cXOO1zj3uFkmuZ9ET9fJlFqOnCmlUDKW9nGsWgBYd2JBYiL6XsIw3tyQzwY6pgGzZu%2BV%2Fr3uSRQ6xsjHP8VPBvvN85huvB0cdFZlqDbS%2BP0pjPNEVbtVmsJhjAz1p5Pt27yqTvaavjkeDnPtloU4qTXIOmwwzjtQPrtPPnk9Nxisbj3u3B9ylf9S81xBI7C7ObEtvoSL1%2FCMBTJtCSKC2JgNTeNfTUnYUNS%2Bc8rqWvamZG6R03jG3rksXJqkhvBeMhXtQaTs92OiBjsQ3dLfkbkBiuX4&X-Amz-Signature=986c7662ec423a2f030b63a3417e9b05c21436aa0dd079245bd531f119a2663e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







