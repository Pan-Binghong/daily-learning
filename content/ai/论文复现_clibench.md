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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AQHJZII%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmJOhSikp3ciMSVIb%2BhZWLDKqtG9mtXd0OUINuiA%2BA7QIgJTpW5HPPhb%2FamhdKtRQpY1mpYKfJd8qzYDkf4IHy8asqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB1%2BgzS7qAPXr8jlzSrcAwbGBCIjYTSWi%2B18lNn6uB8oIlhPdjyXV4h9lkGvpjWhIiFIJhCiwFSc%2BODmtwxfDRun%2BivK0v7Ep3RPiWwzhucaLxx%2FGoSCfHcslzgi7DMrbB5OQYL%2FBcQ%2FluwDHfetukP3uKK3WIhgvdwtXpQAGCq%2BPeOZ%2BVHrYSYgnJrMjyL2hMbYLhWZ6RdQsyYIs0UpCM8WR2HhOkHLP2Ohrwd50I73OYyiVmBWmtTFcAZF0%2Bgnjd8hqRDaSdSKtu%2FfHybt3n1TNWc1G6tBH9EbCT5W0Fry%2BSp9paL5LlgAXUQ%2F2DIm5t5mn9TJd8uu04OtVz3tU40LSi8QIAnvV5DA2nDMWzjeZZj321Xl7NgwoUvq%2BYVqvS3aFtOuY%2FC9bp5LGUVzlbm2GwrzcGWtL%2BUwmfwnprJbt%2FJcf1m2eddyttJkcSRoz1TSo5GJIlTw1EheisqzbMx41nDGe4xww8szQ7LkOTnnhdH%2BEHVcAUC4OYX6tS5h60TxxOOKOdoNEuQbajS3rRkD%2BaD28htACZcuJ2QLcfunjsffOlDlGFJ2UXDmqwX4K1fTOdS%2FG0f4aURvBnXvA2mvLF7JpnDtDOH4lPbBzby9E42SHfC76prweFToOmB1Y1gS7ODYKa1tN24PMJy1mM0GOqUBSMdl5iMDHyZWvsx%2FFyh2X56bQ5Izz%2FFO3%2FkTa0mKoNV0miWpyotCeW3N8gMtTvpBvfcUHGlz%2FDUczuofKHyUfKadZUCEhszo%2BjU5kcQClQLsbvt7hXuZrq7QTfYlXyLJjP7aTHpmt%2F%2BKcr9O8YXOp0uIJxA%2BEYuVXt7QcXSqjh%2FHXy%2BTM2YExir3108LWx6bSxde3RAzJYfX8trJoGbpvnOG2xdY&X-Amz-Signature=47a511081339cfd422a2acefd808605165bb0854c61d165c073b248c07276ddd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AQHJZII%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmJOhSikp3ciMSVIb%2BhZWLDKqtG9mtXd0OUINuiA%2BA7QIgJTpW5HPPhb%2FamhdKtRQpY1mpYKfJd8qzYDkf4IHy8asqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB1%2BgzS7qAPXr8jlzSrcAwbGBCIjYTSWi%2B18lNn6uB8oIlhPdjyXV4h9lkGvpjWhIiFIJhCiwFSc%2BODmtwxfDRun%2BivK0v7Ep3RPiWwzhucaLxx%2FGoSCfHcslzgi7DMrbB5OQYL%2FBcQ%2FluwDHfetukP3uKK3WIhgvdwtXpQAGCq%2BPeOZ%2BVHrYSYgnJrMjyL2hMbYLhWZ6RdQsyYIs0UpCM8WR2HhOkHLP2Ohrwd50I73OYyiVmBWmtTFcAZF0%2Bgnjd8hqRDaSdSKtu%2FfHybt3n1TNWc1G6tBH9EbCT5W0Fry%2BSp9paL5LlgAXUQ%2F2DIm5t5mn9TJd8uu04OtVz3tU40LSi8QIAnvV5DA2nDMWzjeZZj321Xl7NgwoUvq%2BYVqvS3aFtOuY%2FC9bp5LGUVzlbm2GwrzcGWtL%2BUwmfwnprJbt%2FJcf1m2eddyttJkcSRoz1TSo5GJIlTw1EheisqzbMx41nDGe4xww8szQ7LkOTnnhdH%2BEHVcAUC4OYX6tS5h60TxxOOKOdoNEuQbajS3rRkD%2BaD28htACZcuJ2QLcfunjsffOlDlGFJ2UXDmqwX4K1fTOdS%2FG0f4aURvBnXvA2mvLF7JpnDtDOH4lPbBzby9E42SHfC76prweFToOmB1Y1gS7ODYKa1tN24PMJy1mM0GOqUBSMdl5iMDHyZWvsx%2FFyh2X56bQ5Izz%2FFO3%2FkTa0mKoNV0miWpyotCeW3N8gMtTvpBvfcUHGlz%2FDUczuofKHyUfKadZUCEhszo%2BjU5kcQClQLsbvt7hXuZrq7QTfYlXyLJjP7aTHpmt%2F%2BKcr9O8YXOp0uIJxA%2BEYuVXt7QcXSqjh%2FHXy%2BTM2YExir3108LWx6bSxde3RAzJYfX8trJoGbpvnOG2xdY&X-Amz-Signature=21f9dc8cd667301af1e4649f1c5664f15620e5b9df240a4aa3a3a920a0dc7815&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







