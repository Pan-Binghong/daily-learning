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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKI6L6OD%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC3XrYvQwtGIEoluZrEIbaWaJVY4qMjRB3Hb40EcV4ajAIgKjleOwzdL%2FcS7ENLHrwaJVgcxc3vHmYwGknm5yNZgcEqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCrBuErE5CEtBLNyiSrcAzB%2FLyQrHIbjh9UOSSB7%2Bb%2BS5oguehWynUo3wp0myCfG%2FWTElmt6Eocb%2Fatn648y3QyDfwA6QRhWJvE2WvNlGfamG7ROFCVJYdyEQpuZL0HumKgCGsE8Evsz1ar%2BYzTu%2BEoBHO8IPadzlz3gD4jvJckC4Cii%2FGQfHFfLn6aFJx%2F7l3OvcKPSeSAgPknSPQGD0ufoEHafEdeeMPm6UKCk9f%2FzoM8bZP1PRiUG%2BXKaUBO85G%2BAHuWVkeFhGvg1iCQvR%2FZ0i7KDReOHpcsAmnIwMX6bdoEAJxGSyjtL6vIuXwUQs5gDW93eGf%2FDfYN22oogL9KnzSteYGhjMPQJgApaDTXvjXT7PqYnBD2vV3OxcWwUCh2D7XWeJTR290dZ8X0GSbbAw17HNod3I5u2eW6%2FpXg00Q3zR5Rtgen36wWCnZvkyOthJIWZDiIFreRpBv2qbI%2F%2F5K1xwuvl6Hf05dZKahfNp%2F5Wj%2F1XJ%2F3dLSWBXrBm%2FLzmN1IdYHh6h3M1JjjQMS6HlZmZLSOsHwjXvYl7eqKu%2BxqNw31JpWMpqD0SBwKtG0U6Fk2wnQZv%2BG0ywb5gpBFBSZxZu8hzAymsF8%2BakeSOsXrlg8U3oVxbRTHkpNnVG2rM%2FAS0QXhzXkTrMN3kwc4GOqUBJ1hH9wabripUh7xfe576ZViaiuRPrvhVe6HAJ5%2BpzIIYoX98FUIWWS3Hie%2FglfZ949cs36Vt63Us8QZsXiRV03qGNJwL7L%2BwWShxOmDb6sqdBFACKvm%2BxFdUCKtnlP77JYNbC%2BucdtjeOkoZJ%2FfTMbJAkOCsNC2t8OdRGKeTkb%2FIvaxhKwTpQpc9%2BBsodzRlMMJ7lsEQlyZcxaiTItB7%2F6rzgEck&X-Amz-Signature=fedb9dcb0719ec1a5dea69bd0f8bc4b45b236256c7df29045b8512419d4e6e04&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKI6L6OD%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC3XrYvQwtGIEoluZrEIbaWaJVY4qMjRB3Hb40EcV4ajAIgKjleOwzdL%2FcS7ENLHrwaJVgcxc3vHmYwGknm5yNZgcEqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCrBuErE5CEtBLNyiSrcAzB%2FLyQrHIbjh9UOSSB7%2Bb%2BS5oguehWynUo3wp0myCfG%2FWTElmt6Eocb%2Fatn648y3QyDfwA6QRhWJvE2WvNlGfamG7ROFCVJYdyEQpuZL0HumKgCGsE8Evsz1ar%2BYzTu%2BEoBHO8IPadzlz3gD4jvJckC4Cii%2FGQfHFfLn6aFJx%2F7l3OvcKPSeSAgPknSPQGD0ufoEHafEdeeMPm6UKCk9f%2FzoM8bZP1PRiUG%2BXKaUBO85G%2BAHuWVkeFhGvg1iCQvR%2FZ0i7KDReOHpcsAmnIwMX6bdoEAJxGSyjtL6vIuXwUQs5gDW93eGf%2FDfYN22oogL9KnzSteYGhjMPQJgApaDTXvjXT7PqYnBD2vV3OxcWwUCh2D7XWeJTR290dZ8X0GSbbAw17HNod3I5u2eW6%2FpXg00Q3zR5Rtgen36wWCnZvkyOthJIWZDiIFreRpBv2qbI%2F%2F5K1xwuvl6Hf05dZKahfNp%2F5Wj%2F1XJ%2F3dLSWBXrBm%2FLzmN1IdYHh6h3M1JjjQMS6HlZmZLSOsHwjXvYl7eqKu%2BxqNw31JpWMpqD0SBwKtG0U6Fk2wnQZv%2BG0ywb5gpBFBSZxZu8hzAymsF8%2BakeSOsXrlg8U3oVxbRTHkpNnVG2rM%2FAS0QXhzXkTrMN3kwc4GOqUBJ1hH9wabripUh7xfe576ZViaiuRPrvhVe6HAJ5%2BpzIIYoX98FUIWWS3Hie%2FglfZ949cs36Vt63Us8QZsXiRV03qGNJwL7L%2BwWShxOmDb6sqdBFACKvm%2BxFdUCKtnlP77JYNbC%2BucdtjeOkoZJ%2FfTMbJAkOCsNC2t8OdRGKeTkb%2FIvaxhKwTpQpc9%2BBsodzRlMMJ7lsEQlyZcxaiTItB7%2F6rzgEck&X-Amz-Signature=7158b643c6adba363af46437bb527910543b02648d07e21bfba352567b2f7f3c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







