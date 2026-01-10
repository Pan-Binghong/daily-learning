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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMGNWWXO%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHK7BsQUAIE2788vC9bssCP%2BMiD9ddyZ0RpZQGMzcxaYAiEAysN7z3wVxl5H3nc%2BAbY4A5VmdGmXnhqkl0xxhE37nhsqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFs7sgA9bEF7qhUHpyrcA4i%2FHQvYtWmOgFGeUki7aHz9ZhRWCZmHH2MhPFTHBkSqNGJnEbGTkaA7towNY8%2FG%2BoX6cxSMCU5nvnyduJ2%2Bzqm2nyRyN0YVZRJLsiARqY%2FDdF%2F6CrkmU%2BUulA1GjEBp0NoY9%2BTFUdOyc9n5MgzhUsyvTuI4S%2F4Wihmo4B49zttoMhOcYM%2FHuEHD%2B6HROhSoWeiEMjgXh%2B4k3aftdr9GMtIJGWJ42Stfuc2ji1OmymK36N6Fjwoyqll5A9r6GEyVrOWuIMgV0CCoviGT2kWpXtfc%2FY%2Bmk8Mx%2FzIcM%2FLViymdME5GgFAazJauJxhMdenIbPCDjqR0bBzcaYagRQoTVhv5z%2BqqN6gWohB6HS1CMO%2Bt4ylhBdgA7STU%2BH%2Fyppfw8Hsp4O1zwzYMwcNXXIdX4ekA7zTcrT2AC5IyS973UQ9fl%2FYwqx9sZzxKzZ9akwXXqcKsKLET6AsPURwnCxrDSxucJYvro7LtOU9PbQZUy1Qo4ftYzip1fKHViHoVM%2FK2wLiZC45EEKqFNVJbeFMxN792sIsAluKPSs0cqgstXgtrNquz4t1641gbFZ5wsvpVaSOpFRUHOsNcts32E855msIl%2BWXR7hKdQkcR8GMGhFsBorpgBo49yx%2F5ByKmMNn5hssGOqUBSpGDpW542tq%2BDaLEHfzQPdK%2FrH2W%2Fi8GVIR%2Fdj%2BFlhg6z%2F3SsXAzGGvDMNiOgugoFMV08ayvJ5fc1KE%2F5Seu61623LSW70X4L1kjqEvo3Wqw48PppDdFzHQnpCPV0dsssoVb393Ofc%2BkxR7EOeVhG1f8d0FtvP2r62x9e7Ik9dFBzvkMO%2F6W9qtf%2BDGRYo482sAZdsMpyEBlokmG67NbxuIEJYk2&X-Amz-Signature=42cf6153b4f1de18100b241a04bdf74fb562fa7f4ce20b40744f82eee61e9620&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMGNWWXO%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHK7BsQUAIE2788vC9bssCP%2BMiD9ddyZ0RpZQGMzcxaYAiEAysN7z3wVxl5H3nc%2BAbY4A5VmdGmXnhqkl0xxhE37nhsqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFs7sgA9bEF7qhUHpyrcA4i%2FHQvYtWmOgFGeUki7aHz9ZhRWCZmHH2MhPFTHBkSqNGJnEbGTkaA7towNY8%2FG%2BoX6cxSMCU5nvnyduJ2%2Bzqm2nyRyN0YVZRJLsiARqY%2FDdF%2F6CrkmU%2BUulA1GjEBp0NoY9%2BTFUdOyc9n5MgzhUsyvTuI4S%2F4Wihmo4B49zttoMhOcYM%2FHuEHD%2B6HROhSoWeiEMjgXh%2B4k3aftdr9GMtIJGWJ42Stfuc2ji1OmymK36N6Fjwoyqll5A9r6GEyVrOWuIMgV0CCoviGT2kWpXtfc%2FY%2Bmk8Mx%2FzIcM%2FLViymdME5GgFAazJauJxhMdenIbPCDjqR0bBzcaYagRQoTVhv5z%2BqqN6gWohB6HS1CMO%2Bt4ylhBdgA7STU%2BH%2Fyppfw8Hsp4O1zwzYMwcNXXIdX4ekA7zTcrT2AC5IyS973UQ9fl%2FYwqx9sZzxKzZ9akwXXqcKsKLET6AsPURwnCxrDSxucJYvro7LtOU9PbQZUy1Qo4ftYzip1fKHViHoVM%2FK2wLiZC45EEKqFNVJbeFMxN792sIsAluKPSs0cqgstXgtrNquz4t1641gbFZ5wsvpVaSOpFRUHOsNcts32E855msIl%2BWXR7hKdQkcR8GMGhFsBorpgBo49yx%2F5ByKmMNn5hssGOqUBSpGDpW542tq%2BDaLEHfzQPdK%2FrH2W%2Fi8GVIR%2Fdj%2BFlhg6z%2F3SsXAzGGvDMNiOgugoFMV08ayvJ5fc1KE%2F5Seu61623LSW70X4L1kjqEvo3Wqw48PppDdFzHQnpCPV0dsssoVb393Ofc%2BkxR7EOeVhG1f8d0FtvP2r62x9e7Ik9dFBzvkMO%2F6W9qtf%2BDGRYo482sAZdsMpyEBlokmG67NbxuIEJYk2&X-Amz-Signature=1e52bb4ad2bd9a4293c7b30fdbfcffcc8f7454057f107e59e715ff703743b587&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







