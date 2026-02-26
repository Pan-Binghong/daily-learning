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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZCP2WBZ%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIErFJSImPmQqq4tOeJrpQ9FpeMPf3LCZo8O8QYQRm8ZQAiEAxw3Yd4eE1%2FvzURRI1UkEMZBpwkGK1daJYvnccVQj734q%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDF%2BxENYVon7kU0enVyrcAxTXfxs69%2F5BPVv0R%2F5bHUngI%2BGthIqTp%2FTPyCJBKrYpCs9mnvoagZTsh1mzjIMLH6kLl9P8N2soTOzRoFZkYaZThNrt8VeBOP%2BqTYEA3A6bugA5CmpeLx07EvuUdE2FXL9arVU9kMGb22IMwpRzsbLaWKlAEFYKUZ85HuGHp82X3THcXD6etGazZ0Wua7AjK0U0UOaleI9Vi0ZeEGR2jZvkdRJr6d8sXsmqevid%2BZVjlZB%2B4ZXRQ%2FpaWmNmyScDdj%2Fslr4p9VlSW5tn6hzhZ%2B9MXxt%2FBZnv4JitfepU6Px2EWMNZ4wi30NFh2cJ%2B6CqTSt0DBR%2BRsrE35mFD0%2BcymIW0Al5H3TflA5peX%2BaXdt%2F5elHoZkdDNUnUkyN11%2F%2BY1dtmxoUu0K%2Fvf90PJXQSQZqdEhCyutsyz5hLIK7ZoLJo0UVWPZyAr%2Fbw4mPlfRd2Kg1zGYUa0QB%2BVDCdiawl5ITfai6qSNVdjzB5PTcoYOBYyDbr24ewgc7A4LVJtAgk2CvbQ0bunRB0wzNvRp2DUq78Yq%2FMInWHW6yhZSG3ARsJ8uypxJK6L2xxAZYFCQ%2BRBSB2LJU4fqIL53qUXt%2FVvutT10O7c7ZbrN9SHD0lgHtpNJKUREB%2F4XYW99XMJn2%2FswGOqUB%2FQtcR51OdprDTwRwGu2YWgxsTiPsXabVjrh%2BONm443KSZRf%2FhGhgvIWyzvP6v3H1xR7P300pHK%2FX6VMBEHvTXVP%2BRiIR8rdg85OC1Gg%2FCxbMlEOO4UHNCQuT5NW1AADDM98Q2eEJ2jU87t2%2BuGaSopOmOTiZd%2FzhAUSscVdXNk%2FR9ojxC1iDtcJn36yQIA7Xerqedp%2BHFr%2BwCi5BB9ad8cLJiwLd&X-Amz-Signature=7306414b411c4aa3d11867b0711f47b8f9fa2c7073a80e1acf307c6b2d764025&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZCP2WBZ%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIErFJSImPmQqq4tOeJrpQ9FpeMPf3LCZo8O8QYQRm8ZQAiEAxw3Yd4eE1%2FvzURRI1UkEMZBpwkGK1daJYvnccVQj734q%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDF%2BxENYVon7kU0enVyrcAxTXfxs69%2F5BPVv0R%2F5bHUngI%2BGthIqTp%2FTPyCJBKrYpCs9mnvoagZTsh1mzjIMLH6kLl9P8N2soTOzRoFZkYaZThNrt8VeBOP%2BqTYEA3A6bugA5CmpeLx07EvuUdE2FXL9arVU9kMGb22IMwpRzsbLaWKlAEFYKUZ85HuGHp82X3THcXD6etGazZ0Wua7AjK0U0UOaleI9Vi0ZeEGR2jZvkdRJr6d8sXsmqevid%2BZVjlZB%2B4ZXRQ%2FpaWmNmyScDdj%2Fslr4p9VlSW5tn6hzhZ%2B9MXxt%2FBZnv4JitfepU6Px2EWMNZ4wi30NFh2cJ%2B6CqTSt0DBR%2BRsrE35mFD0%2BcymIW0Al5H3TflA5peX%2BaXdt%2F5elHoZkdDNUnUkyN11%2F%2BY1dtmxoUu0K%2Fvf90PJXQSQZqdEhCyutsyz5hLIK7ZoLJo0UVWPZyAr%2Fbw4mPlfRd2Kg1zGYUa0QB%2BVDCdiawl5ITfai6qSNVdjzB5PTcoYOBYyDbr24ewgc7A4LVJtAgk2CvbQ0bunRB0wzNvRp2DUq78Yq%2FMInWHW6yhZSG3ARsJ8uypxJK6L2xxAZYFCQ%2BRBSB2LJU4fqIL53qUXt%2FVvutT10O7c7ZbrN9SHD0lgHtpNJKUREB%2F4XYW99XMJn2%2FswGOqUB%2FQtcR51OdprDTwRwGu2YWgxsTiPsXabVjrh%2BONm443KSZRf%2FhGhgvIWyzvP6v3H1xR7P300pHK%2FX6VMBEHvTXVP%2BRiIR8rdg85OC1Gg%2FCxbMlEOO4UHNCQuT5NW1AADDM98Q2eEJ2jU87t2%2BuGaSopOmOTiZd%2FzhAUSscVdXNk%2FR9ojxC1iDtcJn36yQIA7Xerqedp%2BHFr%2BwCi5BB9ad8cLJiwLd&X-Amz-Signature=d2271ab3f2066d840756fb6249ae5d6bb796c9545b2a4b68657c5606d508f59b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







