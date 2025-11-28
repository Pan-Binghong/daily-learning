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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MYUG4DH%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024254Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHd%2B%2B8Ge7pZkKwBO7gEI%2BQvxLdkxW1O%2BOdwdsOsxNG%2B8AiEAi7%2FEmRd0W5caAkGwjnK%2BvPrlF3BiwdWDiP4Pb%2FRGX3oqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEoDxprlkg4mvYjJVCrcA9Pidt0rnsqz693QasUS5W3VbLAony8wOLYikguqhsmUMTIv6QII%2Fa2my01pNk9J6oAem7CYMz0bLbkzUPW%2Bs5ZF70psou%2FgPlC1v1AJ4eipo08PBKcpTuD3mljyhYebcTEOJ8CreBtgszu%2BYe1blhxN67uay%2FqJ7fqlj%2FlmB7QchxvgRDaM2%2BvR0IDYnQkvwv4VAyHTVMPL1hH3WDh8BdZxacvXQvWhG5l22y0ZTTuqtDvziV6b2WVqPanbRzuAe40n9jc4e%2Bw5sa4WriTOCnL1m1qYyEPn7zGZrNusXc%2BaJIC7Kk6SUIFX6DWXn%2FtrZ%2Buto2DzNEGGlZgWx7HQtPodFB%2Bz8vZWiaNRVr0uWNjfYE792ESIs%2BOWl3SWskUl0lblcieWNzauv6NmUigAZqcUCRiyQf7BoSa2POs71sI7TiwIueHyUB4DTdyC41J5NBOvWn5gxl1fe57BAGn1Gdd%2Ba9VcEVwAWHwtyqt5JBBCaqjlzIAT69jG9BjJIzzg0bYOrkWoKaniK3U%2F%2FPhotLLdQbR2%2Fy4z6dIUigUYIhafUsE0A%2BT8iJIMVTeWzia1PmeCj2r67OtxUQFfNlhICOBEbfLr0HILSoedEoxIWy%2BpaG49dkX4OhMA3ReoMNf1o8kGOqUBPcrtuD4TL5vP34is2yqqv%2FGHYC8yV9eyq9kq7cNnt6xXCw%2FMLvdDb%2B7k2zRIyfeX4mpUeyUtRuXYY%2ByTwPAOLq2VBB9ootrwHOfZDGcwieni9eJF3tIh8sEi9nYe8N8%2FaX%2FgyeQ5%2FqYDUkB4W00tzZN9m5%2FWsJIFEHuh0hqrqxnJo%2FgBKn6vS1XLfjGZW7BuIQY8P28cjyGbkiI9XBooJf8CmID3&X-Amz-Signature=83b62c67a34abdf6e76cd14bab240dc873af525bcf968d47d39ab9b3e5441c69&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MYUG4DH%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024254Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHd%2B%2B8Ge7pZkKwBO7gEI%2BQvxLdkxW1O%2BOdwdsOsxNG%2B8AiEAi7%2FEmRd0W5caAkGwjnK%2BvPrlF3BiwdWDiP4Pb%2FRGX3oqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEoDxprlkg4mvYjJVCrcA9Pidt0rnsqz693QasUS5W3VbLAony8wOLYikguqhsmUMTIv6QII%2Fa2my01pNk9J6oAem7CYMz0bLbkzUPW%2Bs5ZF70psou%2FgPlC1v1AJ4eipo08PBKcpTuD3mljyhYebcTEOJ8CreBtgszu%2BYe1blhxN67uay%2FqJ7fqlj%2FlmB7QchxvgRDaM2%2BvR0IDYnQkvwv4VAyHTVMPL1hH3WDh8BdZxacvXQvWhG5l22y0ZTTuqtDvziV6b2WVqPanbRzuAe40n9jc4e%2Bw5sa4WriTOCnL1m1qYyEPn7zGZrNusXc%2BaJIC7Kk6SUIFX6DWXn%2FtrZ%2Buto2DzNEGGlZgWx7HQtPodFB%2Bz8vZWiaNRVr0uWNjfYE792ESIs%2BOWl3SWskUl0lblcieWNzauv6NmUigAZqcUCRiyQf7BoSa2POs71sI7TiwIueHyUB4DTdyC41J5NBOvWn5gxl1fe57BAGn1Gdd%2Ba9VcEVwAWHwtyqt5JBBCaqjlzIAT69jG9BjJIzzg0bYOrkWoKaniK3U%2F%2FPhotLLdQbR2%2Fy4z6dIUigUYIhafUsE0A%2BT8iJIMVTeWzia1PmeCj2r67OtxUQFfNlhICOBEbfLr0HILSoedEoxIWy%2BpaG49dkX4OhMA3ReoMNf1o8kGOqUBPcrtuD4TL5vP34is2yqqv%2FGHYC8yV9eyq9kq7cNnt6xXCw%2FMLvdDb%2B7k2zRIyfeX4mpUeyUtRuXYY%2ByTwPAOLq2VBB9ootrwHOfZDGcwieni9eJF3tIh8sEi9nYe8N8%2FaX%2FgyeQ5%2FqYDUkB4W00tzZN9m5%2FWsJIFEHuh0hqrqxnJo%2FgBKn6vS1XLfjGZW7BuIQY8P28cjyGbkiI9XBooJf8CmID3&X-Amz-Signature=4e8d2e25f3e4ed43cddb5f7da70926f7307be9ffb85c6cfbba6ebf4c60514d3b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







