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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UQEZIU5%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQCkH2Jqx0Qr5l5szXwV1BZw8Xasw8v%2BcEVgTOvE1Xi%2BMAIgCizlcgWOgIXJIn6%2BuU%2F4Ox15Pokz8wwWRtO%2Fvs6CqMcq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDDgPBNsj96%2BNzXzBwircA6BL%2FompJD1jlp8GpabQvowFQTcqjaRud2QExnhxWr0SXN30oLNqaHMASvvkAdMAcjWTwq2414z4aINJNDmdRo8dD0o%2Fdy%2Bvu0m477kE0%2BfHpTG3RC4Udw9SnF1Qvz4LEnzwE9ReV9JsrlaW27bMnYfIUvHqqpcKwJuus4wYY6OmEOsBgV5L6Gd2XcOrmsVaPhxYVeAsCea99BBpwRc%2FsAG0yp%2BT9bUDdYFnBY2pdbRs9ErgMhblUITPQUCdgKh%2F5%2BAUSx8kf8IRRkRAnbT1dv3Q9%2FJwK8V3Zsvgy%2BcdnwUZtVwmiba3g3QlGBErtXVEJFWFHWlnJsLZzkD4sfkoe%2B%2Fi%2BF8aRxw%2BkIiB%2FUNopZ2z4TWHabZH8ZfUuez2ypZT4np0rvBjZgGgz375C4lzEFsXJ%2BzxZapTXgCyxNReZDHoMZdr2MmWXbyD45VlMb3XWvw60iYL8LikD6TAKWNrBoV5ziC86%2Fkl3PsYsGg%2B1YjX1c7eeGtEqnaLXAWUj0g9GLpvTcR0Fet0uY4vDCTcX%2BHtSt0fywiEDPi5uXYcJA1J3qU%2FfDAtxxAWPH0gNnd0o3k54XtGJ3E6gAN%2FrLQi1PZpIRAE3rxFcAs686Pi0sRGYHCpuTXm8sIqHqEhMJyUyswGOqUB2CtMJCnRwfA9XyTPYK5jXLDbGdJ054DUWMIcZ4XkrcmmjY3bHY4TQJWT4KPPeGX42ClQWQsd%2FCPak%2B%2BFID%2FMRxYDyzrsZd1gTiC2%2BSGFGMg2HSlxWprXe1yv31kG2TfS1SF81szYpn6zbs0sKnXnDtlYl89pvVvY3IpkvezV%2FdFkHgXuJTIj5udzkgycT8qUDl%2FBaoMnNS4Gvj8inT5SIt0fFZbE&X-Amz-Signature=28fc0c1185b23ee0e303e4345f70b217f0fc00b12a3199159e0b97b165d5c507&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UQEZIU5%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQCkH2Jqx0Qr5l5szXwV1BZw8Xasw8v%2BcEVgTOvE1Xi%2BMAIgCizlcgWOgIXJIn6%2BuU%2F4Ox15Pokz8wwWRtO%2Fvs6CqMcq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDDgPBNsj96%2BNzXzBwircA6BL%2FompJD1jlp8GpabQvowFQTcqjaRud2QExnhxWr0SXN30oLNqaHMASvvkAdMAcjWTwq2414z4aINJNDmdRo8dD0o%2Fdy%2Bvu0m477kE0%2BfHpTG3RC4Udw9SnF1Qvz4LEnzwE9ReV9JsrlaW27bMnYfIUvHqqpcKwJuus4wYY6OmEOsBgV5L6Gd2XcOrmsVaPhxYVeAsCea99BBpwRc%2FsAG0yp%2BT9bUDdYFnBY2pdbRs9ErgMhblUITPQUCdgKh%2F5%2BAUSx8kf8IRRkRAnbT1dv3Q9%2FJwK8V3Zsvgy%2BcdnwUZtVwmiba3g3QlGBErtXVEJFWFHWlnJsLZzkD4sfkoe%2B%2Fi%2BF8aRxw%2BkIiB%2FUNopZ2z4TWHabZH8ZfUuez2ypZT4np0rvBjZgGgz375C4lzEFsXJ%2BzxZapTXgCyxNReZDHoMZdr2MmWXbyD45VlMb3XWvw60iYL8LikD6TAKWNrBoV5ziC86%2Fkl3PsYsGg%2B1YjX1c7eeGtEqnaLXAWUj0g9GLpvTcR0Fet0uY4vDCTcX%2BHtSt0fywiEDPi5uXYcJA1J3qU%2FfDAtxxAWPH0gNnd0o3k54XtGJ3E6gAN%2FrLQi1PZpIRAE3rxFcAs686Pi0sRGYHCpuTXm8sIqHqEhMJyUyswGOqUB2CtMJCnRwfA9XyTPYK5jXLDbGdJ054DUWMIcZ4XkrcmmjY3bHY4TQJWT4KPPeGX42ClQWQsd%2FCPak%2B%2BFID%2FMRxYDyzrsZd1gTiC2%2BSGFGMg2HSlxWprXe1yv31kG2TfS1SF81szYpn6zbs0sKnXnDtlYl89pvVvY3IpkvezV%2FdFkHgXuJTIj5udzkgycT8qUDl%2FBaoMnNS4Gvj8inT5SIt0fFZbE&X-Amz-Signature=b02c4ee8d1424ac43f42f890ec5c6bd982efc652b742c4515fcfa8da15b0ab34&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







