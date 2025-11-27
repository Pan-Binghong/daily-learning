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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3FCKQBZ%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGFqn9LOY6lMMVYm2H7QtoBK%2BGDkvZmIJCxelNCUmYHhAiEA3IqgKUuuXUH3SRPigj20iLOPzUx1SdQH3wcNhdSBYRgqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAbv02Fi7lUKC0q%2F5CrcA%2BtT8WuT5AP3djRSlFbvt%2B5H9DswNNfZFTkMOAhdz1cuX9enVe2W%2FQWsuTB3cag2JsUJrKf%2BZr4kosIvfg6sSOcO2gQXzIpmWCHrhVc6reltjVmiVDV1k7dvA3jIqb1f6OtmZilj%2FElEh%2F7WB%2Bdx%2BZWVEtIMcRxGjFwY%2FrdKQ%2BRgcxU%2F5UC9Pq2EJnvcovXQqjULGL6dieNzKDBhNH19zGzFXIQqzJwAKx8AjKrPYmnAzwlgH8PPtWu0mQyKUTrg%2B6oZoboEkiddkGgpP9Al1aF2Va49E3hxoKu2a9iJrG1w7VX6Ts%2F1%2FgkRYNmBvGgPNDMa94hNuhNFS0pGy%2BjIaBVF5zifKWaQUPboCu1Rp1sgZvXwG72F5V3vIOQRFlpzNQ14Q6G9RVD3GPSvSbVGAFbBrQ8MaH1sgfExBhI9i2Uj%2FHfbHoZIc3syaWzPYwqEc5Ht%2F3GyZOXRPbCbgLHPG%2B%2Fa3vXY%2BBE%2FeBKhJiFqFGAk2cn0ov%2BBCc2%2FprN0MAu0rynACv014O9tJEEIoAg63JOWGOjcAEIhPKrbObPydMzpQloa8dzkOfTJG7xZqr728qiyTaAR5u309hCrhMUqdVzfM16g4kSREqEaYUWuWTRmpc29B22b66hOoIXHMPDOnskGOqUBwiEo6wcpAuhsJRTx242Ec6UpLQaWUkfYXYYojqx6OYf08CVjjVWTWRa4iQ6sdcLFA8n39eMied09Qb87oDXpc7mCHH8C%2BnPPmlTJ80dFUo6lFfBeFLc4ef%2BGeHDf%2FA1UcPUiyyFKy6I4XCo6ZrPnK%2B9zgvLfHxgmYt%2FOzIKCjWGmJqs4Ym%2BF9ffR0qu7Cy%2BhdayOlpl5gruxGpSq%2Bjm9KLiQu8p9&X-Amz-Signature=6be113713794438fc8e151abce6c5fd2e61ebcb225e68a6cfa6a4201a8aa2211&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3FCKQBZ%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGFqn9LOY6lMMVYm2H7QtoBK%2BGDkvZmIJCxelNCUmYHhAiEA3IqgKUuuXUH3SRPigj20iLOPzUx1SdQH3wcNhdSBYRgqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAbv02Fi7lUKC0q%2F5CrcA%2BtT8WuT5AP3djRSlFbvt%2B5H9DswNNfZFTkMOAhdz1cuX9enVe2W%2FQWsuTB3cag2JsUJrKf%2BZr4kosIvfg6sSOcO2gQXzIpmWCHrhVc6reltjVmiVDV1k7dvA3jIqb1f6OtmZilj%2FElEh%2F7WB%2Bdx%2BZWVEtIMcRxGjFwY%2FrdKQ%2BRgcxU%2F5UC9Pq2EJnvcovXQqjULGL6dieNzKDBhNH19zGzFXIQqzJwAKx8AjKrPYmnAzwlgH8PPtWu0mQyKUTrg%2B6oZoboEkiddkGgpP9Al1aF2Va49E3hxoKu2a9iJrG1w7VX6Ts%2F1%2FgkRYNmBvGgPNDMa94hNuhNFS0pGy%2BjIaBVF5zifKWaQUPboCu1Rp1sgZvXwG72F5V3vIOQRFlpzNQ14Q6G9RVD3GPSvSbVGAFbBrQ8MaH1sgfExBhI9i2Uj%2FHfbHoZIc3syaWzPYwqEc5Ht%2F3GyZOXRPbCbgLHPG%2B%2Fa3vXY%2BBE%2FeBKhJiFqFGAk2cn0ov%2BBCc2%2FprN0MAu0rynACv014O9tJEEIoAg63JOWGOjcAEIhPKrbObPydMzpQloa8dzkOfTJG7xZqr728qiyTaAR5u309hCrhMUqdVzfM16g4kSREqEaYUWuWTRmpc29B22b66hOoIXHMPDOnskGOqUBwiEo6wcpAuhsJRTx242Ec6UpLQaWUkfYXYYojqx6OYf08CVjjVWTWRa4iQ6sdcLFA8n39eMied09Qb87oDXpc7mCHH8C%2BnPPmlTJ80dFUo6lFfBeFLc4ef%2BGeHDf%2FA1UcPUiyyFKy6I4XCo6ZrPnK%2B9zgvLfHxgmYt%2FOzIKCjWGmJqs4Ym%2BF9ffR0qu7Cy%2BhdayOlpl5gruxGpSq%2Bjm9KLiQu8p9&X-Amz-Signature=fd7b2f61f748108be8d042c7f50f842e01a1259df564f8c9341404fee1656feb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







