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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVQL2GT2%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCQmXdwLJnCog174gtSP2k0ix%2BCYjdqTc%2BWXbLKYKOcswIhAO3C32olLU7F%2B1JtnkfLlmEDeYKHchP8RcBdqcD9ij2XKogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz7s%2BVnoHw5lBg6CcAq3AMrs9zv6HOV0ogNHuBS9wpF2ipIACv66Atec1GAVkdQABU9CvQbZHaKh8nMoHnJ%2BekZdntZ5y6odIu4AgntptcoxkdxBNgkjrHx%2F%2B9eE6XbckcTgs9uWW7piwb%2Bem8GtCRcIdXGlLXNP9FNf6Ma67qmSTOLhwRcXcfe%2F6tCnWfObmGaWO9UBxM53qytSSvE23YEjpqHMmeG1nJnww3qukTZ6pVT2QMLc%2BppLbkYT%2BaclAe%2B5HNLKxK2laKJgAyEQQchedsjJwqGUc0vg1gF6aHf56sluZOPn2Gt6%2FzAmecef2j%2B2E2%2Fqqp%2BK5J1nLX3tHLkoyHQL0%2FwHeIuefdyyP9ARAwuzUZFJE%2FkXrcaPV7iZo2HD%2BUzhKcNi4Rjzj9Fts7aEavC6CyWq65KDqs6mA8QLjCVf89g5Dt5C1RNuTUey6s4Qqhdn%2FOm%2FadC9RnDCHpc%2FuHH5Q0daS7YDM%2BF898gn1iwaeR%2Bxj%2FKFliEqlHrBZud5iZGHq0dV1dLYpYcB0v8Bmm5SBt0dC1%2FAb0Xx1MNqcHXLe89kLpI9vnxwSWgX1fr8wjCpFvw2LhEP06gk3mLyALWMbyLianavi30tsnnvtYeLqHuO2h%2B1GEPDyYMIu0dMDhA4De4%2FQ0DGDDjvd3NBjqkAai7yQeZdtoSWFy0NoM6YUGyYxqFwYUTnfgVf%2Fezs0N7xEx8RoITUJ%2FPU90L9Djahipm0nqoO68sIQMJapBKN0cgmaOwjycYLF%2F3JcLTle09pFzsCjV4xa1DCX3Mdhut6cEBCNJz657ZqwBgXbQ71mrCSC33xDZKWkuFi94X7mP%2FZVm8b8ZKkoRY9cgNfMfDnySJAKaKHIwY%2F7PNp9z9IFiTAqdy&X-Amz-Signature=123c591fca979e0d42cb0727078a6c0504791280e24243d013cd1877c2bed6df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVQL2GT2%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCQmXdwLJnCog174gtSP2k0ix%2BCYjdqTc%2BWXbLKYKOcswIhAO3C32olLU7F%2B1JtnkfLlmEDeYKHchP8RcBdqcD9ij2XKogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz7s%2BVnoHw5lBg6CcAq3AMrs9zv6HOV0ogNHuBS9wpF2ipIACv66Atec1GAVkdQABU9CvQbZHaKh8nMoHnJ%2BekZdntZ5y6odIu4AgntptcoxkdxBNgkjrHx%2F%2B9eE6XbckcTgs9uWW7piwb%2Bem8GtCRcIdXGlLXNP9FNf6Ma67qmSTOLhwRcXcfe%2F6tCnWfObmGaWO9UBxM53qytSSvE23YEjpqHMmeG1nJnww3qukTZ6pVT2QMLc%2BppLbkYT%2BaclAe%2B5HNLKxK2laKJgAyEQQchedsjJwqGUc0vg1gF6aHf56sluZOPn2Gt6%2FzAmecef2j%2B2E2%2Fqqp%2BK5J1nLX3tHLkoyHQL0%2FwHeIuefdyyP9ARAwuzUZFJE%2FkXrcaPV7iZo2HD%2BUzhKcNi4Rjzj9Fts7aEavC6CyWq65KDqs6mA8QLjCVf89g5Dt5C1RNuTUey6s4Qqhdn%2FOm%2FadC9RnDCHpc%2FuHH5Q0daS7YDM%2BF898gn1iwaeR%2Bxj%2FKFliEqlHrBZud5iZGHq0dV1dLYpYcB0v8Bmm5SBt0dC1%2FAb0Xx1MNqcHXLe89kLpI9vnxwSWgX1fr8wjCpFvw2LhEP06gk3mLyALWMbyLianavi30tsnnvtYeLqHuO2h%2B1GEPDyYMIu0dMDhA4De4%2FQ0DGDDjvd3NBjqkAai7yQeZdtoSWFy0NoM6YUGyYxqFwYUTnfgVf%2Fezs0N7xEx8RoITUJ%2FPU90L9Djahipm0nqoO68sIQMJapBKN0cgmaOwjycYLF%2F3JcLTle09pFzsCjV4xa1DCX3Mdhut6cEBCNJz657ZqwBgXbQ71mrCSC33xDZKWkuFi94X7mP%2FZVm8b8ZKkoRY9cgNfMfDnySJAKaKHIwY%2F7PNp9z9IFiTAqdy&X-Amz-Signature=64c713dd2c55eb824b6dd6a59dcac83becc00c6112eaedc408d9993537186850&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







