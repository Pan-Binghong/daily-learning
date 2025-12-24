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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6TIAREL%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQCMBlixsKxs5QWEtAAQIx0%2F4TCpErNyMs%2FPFHeEVfxopwIgbiTEXiBrQuO5iI8RdXnaadbXy9irsfbHiyWmiyZ14k8q%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDKkMZZjDYMdb04wu5yrcA8MiqIr1eCREfFUtXpJ7Dg1R3weg3NQ%2FEsZqX5LftsT0%2B5jYJwARdn%2Fj8qS135SgbiF6qo%2FprX5B%2BYs5HUQsWoYepYN9qTdJuPt9BjUjTd4dvYakM17peOLDIbNAUIv8FFTmYI6puLXh4cnsRT93ZNSk00oNR26OKxsbTZwbLAKowV85Jtk2jysPCJ%2FlOAdARgg559hdWmUBzmFnv2TEfw4sDMnMW3lr96v7r8qN3ilmpdx%2BE0rwf1zh7m6Y0GNYbIO6dVzWZOIyntQsPiggezF7oAVB7sJ1AQI4zzXU0YgxJQ%2Fpcq3yuifNS%2F1JSU0utsixo3MP%2B4Jv2NwMx05oqCsEISZEZ5cNQq4xI%2BwyQza3k26xE2RjDprP4gVIdKfxsz59CUDQRBpa0kzxL2Zn%2Foh52wd7YZVzdvkTUAJxi1m1KSZ9f2ttXoeXxzMIpXN1DtYHQP7DM6qynTh1s16wKljHbKG%2BJYmGwCZm9UpdbzyFl9CObvyFHnCUwSCVGIGQFbgCh%2F0%2F%2FqU3sBSa5iYreHOmMYjeEI2LqmJpmkscZSJh7GJTkw7l6rCjXmOmy2yLjjk93bM5gTdcocL9B7%2BpIZRs54ZsFy0VKyrFM9sNtu7MAZBP1GnJd8KtFAPZMN3grMoGOqUBv6Pno%2B9oPvyhTM4T5U2oK3vq%2B2JzkI5HgtUVFyjk2sv%2FCm65BNflCKxRJIsID6oVjr0vDCKnc0dxPjnkRYQlywXJKpDJh3k64PFWrkXCdD%2B3F8Pq13ko3nR4vTfOnO%2FPZf803XR6uGqJvm9pkAxeIMs%2BMkVicIq%2Fo5axJ9lPqG2i2BRv7VR0fTpqKbqNzvMq6t0AUUF4UC6TFcUCrsZ4brQI3YGM&X-Amz-Signature=4f253a3f8f347ea3bd1adc9e76160aa1bfbc913efbed27510624b0a769869da3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6TIAREL%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQCMBlixsKxs5QWEtAAQIx0%2F4TCpErNyMs%2FPFHeEVfxopwIgbiTEXiBrQuO5iI8RdXnaadbXy9irsfbHiyWmiyZ14k8q%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDKkMZZjDYMdb04wu5yrcA8MiqIr1eCREfFUtXpJ7Dg1R3weg3NQ%2FEsZqX5LftsT0%2B5jYJwARdn%2Fj8qS135SgbiF6qo%2FprX5B%2BYs5HUQsWoYepYN9qTdJuPt9BjUjTd4dvYakM17peOLDIbNAUIv8FFTmYI6puLXh4cnsRT93ZNSk00oNR26OKxsbTZwbLAKowV85Jtk2jysPCJ%2FlOAdARgg559hdWmUBzmFnv2TEfw4sDMnMW3lr96v7r8qN3ilmpdx%2BE0rwf1zh7m6Y0GNYbIO6dVzWZOIyntQsPiggezF7oAVB7sJ1AQI4zzXU0YgxJQ%2Fpcq3yuifNS%2F1JSU0utsixo3MP%2B4Jv2NwMx05oqCsEISZEZ5cNQq4xI%2BwyQza3k26xE2RjDprP4gVIdKfxsz59CUDQRBpa0kzxL2Zn%2Foh52wd7YZVzdvkTUAJxi1m1KSZ9f2ttXoeXxzMIpXN1DtYHQP7DM6qynTh1s16wKljHbKG%2BJYmGwCZm9UpdbzyFl9CObvyFHnCUwSCVGIGQFbgCh%2F0%2F%2FqU3sBSa5iYreHOmMYjeEI2LqmJpmkscZSJh7GJTkw7l6rCjXmOmy2yLjjk93bM5gTdcocL9B7%2BpIZRs54ZsFy0VKyrFM9sNtu7MAZBP1GnJd8KtFAPZMN3grMoGOqUBv6Pno%2B9oPvyhTM4T5U2oK3vq%2B2JzkI5HgtUVFyjk2sv%2FCm65BNflCKxRJIsID6oVjr0vDCKnc0dxPjnkRYQlywXJKpDJh3k64PFWrkXCdD%2B3F8Pq13ko3nR4vTfOnO%2FPZf803XR6uGqJvm9pkAxeIMs%2BMkVicIq%2Fo5axJ9lPqG2i2BRv7VR0fTpqKbqNzvMq6t0AUUF4UC6TFcUCrsZ4brQI3YGM&X-Amz-Signature=f0bbe006633df8256be3b7e304612bff6ea3626316945d7c0914f93b96fd3225&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







