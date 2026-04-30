<<<<<<< HEAD
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png)

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







=======
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UIMIE5C%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIAMoMHKb2X2RUaaFSkIEOtBHmh0NWGy2asUtf%2Foim7cFAiEAk1JOfw0V0S7yzeUSGe%2F3ZvbV8%2BstKABCe%2FPRO9g8SJ4q%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDMzOCNCR5IFZfRnBxSrcAyEc%2FHRP2D%2FcdlE6inB7auybV9hPir47weQyWCSRw3uZ7JimfCK2GkqE44KGKE1rDkAQ0MdrgUPFkcMRoYlE6o%2F1Q%2B7cpqs9el4OrjW8mWFUNpMhBviJwXpcgNxoMgyAAEVQBvxWh0%2BL8Dc%2BZJ%2F8ci8hmhEaZ4McPOKqcOevd4cGBUhPacxyRKjEwS1fbMkMOzLhu%2BuJ2WXajILoQSNu6gp9UKVl3YSBDNv7bFc8IOnQRQkz5lb8eBtW08lmANf7wABQH14hJTFlfUCZoEYOQyB%2Fg5KRgxshxbs4Wx29vfjTTJ%2FQQIUFdg0pR%2Bch8nBIRVbdj6p60r0DoW%2BU4iCV6LkkhFxzRc61dTvA3pg1B%2FG3txJuAQZ%2BB0Afu2RrAnMTWeshb08qe%2FqdsM89hSGf4vlvkuHEEEZXhS2o9zrG8p3RrQvC0enJeR1oBv6QsU1MZ1Oh7Ktb8YDfkSs0FeSo%2Ff7Ne%2Bphpu6R64poLfWHhY0nuzBEIHHVJUacsuE5t7cWEBldAc5LyAqLLOOh6TCB5hDN860Bbsppeo%2F4I0Ej1RmDI6vhT1YcEFOHAVpOc22DOEjtMgA3Edmv8AfzQixn%2FdAD0%2Bq2z1RY%2FQXrdf6mrRd%2FaMHuCJosHvNqxAUqMLyczM8GOqUBHOtn7psJLWFqbEEfi3HuwSrZBJxELm7BuselIjSuL%2BCdNUmB5MetDTuBedPXoYbHVaOwZyrlLdGeRAKt95p1P8VdAlND1cMAyol7FWlTvj9ojPXvrff4fHji3yf2cApvpYEnFafr05aukz%2F8ppC5zdhGc6bjQSxFiH4dGqzpnCyhbmvAOgvHZdWA0vabVSF1mcPfSiRaZLnjon%2Bd6ZjRBE74X1Pf&X-Amz-Signature=adc4ca57b6cffd9649805393b9d7055019bedcdaf78363a5c4bd69d2853b10b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UIMIE5C%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIAMoMHKb2X2RUaaFSkIEOtBHmh0NWGy2asUtf%2Foim7cFAiEAk1JOfw0V0S7yzeUSGe%2F3ZvbV8%2BstKABCe%2FPRO9g8SJ4q%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDMzOCNCR5IFZfRnBxSrcAyEc%2FHRP2D%2FcdlE6inB7auybV9hPir47weQyWCSRw3uZ7JimfCK2GkqE44KGKE1rDkAQ0MdrgUPFkcMRoYlE6o%2F1Q%2B7cpqs9el4OrjW8mWFUNpMhBviJwXpcgNxoMgyAAEVQBvxWh0%2BL8Dc%2BZJ%2F8ci8hmhEaZ4McPOKqcOevd4cGBUhPacxyRKjEwS1fbMkMOzLhu%2BuJ2WXajILoQSNu6gp9UKVl3YSBDNv7bFc8IOnQRQkz5lb8eBtW08lmANf7wABQH14hJTFlfUCZoEYOQyB%2Fg5KRgxshxbs4Wx29vfjTTJ%2FQQIUFdg0pR%2Bch8nBIRVbdj6p60r0DoW%2BU4iCV6LkkhFxzRc61dTvA3pg1B%2FG3txJuAQZ%2BB0Afu2RrAnMTWeshb08qe%2FqdsM89hSGf4vlvkuHEEEZXhS2o9zrG8p3RrQvC0enJeR1oBv6QsU1MZ1Oh7Ktb8YDfkSs0FeSo%2Ff7Ne%2Bphpu6R64poLfWHhY0nuzBEIHHVJUacsuE5t7cWEBldAc5LyAqLLOOh6TCB5hDN860Bbsppeo%2F4I0Ej1RmDI6vhT1YcEFOHAVpOc22DOEjtMgA3Edmv8AfzQixn%2FdAD0%2Bq2z1RY%2FQXrdf6mrRd%2FaMHuCJosHvNqxAUqMLyczM8GOqUBHOtn7psJLWFqbEEfi3HuwSrZBJxELm7BuselIjSuL%2BCdNUmB5MetDTuBedPXoYbHVaOwZyrlLdGeRAKt95p1P8VdAlND1cMAyol7FWlTvj9ojPXvrff4fHji3yf2cApvpYEnFafr05aukz%2F8ppC5zdhGc6bjQSxFiH4dGqzpnCyhbmvAOgvHZdWA0vabVSF1mcPfSiRaZLnjon%2Bd6ZjRBE74X1Pf&X-Amz-Signature=45e5c37ae0ec2cb024940994ea9a42f010838a4bba6d24d4c7604404546405a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







>>>>>>> 67e2e8ba81abbca0065a5254fe8b7b646ead6176
