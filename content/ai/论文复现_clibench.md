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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCMQMITM%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020047Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6J%2F%2BSJNYXvm09MA1lhwebryP8BDImQpJT9hesNHil5wIgM08ejnMKZL5AUsdMmT6xvZ7eGogVdU%2BBd0xWC3znOJMqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC4MTFPt5kSESWKcZCrcA4BjFr2xSVXUEcrJmtR40HYaqG28m3yTjjeGh5SV8CFruz7dxNVQRDuYusWqUfX9ugn1H5yencFJI8i8QzuVuJXRpyB72ylXOHN95E2RZ63041cSK1Kx3eXapEjdWkt0K7%2Fpo4FvJ3cQbE5nTakoSDGS%2F93GctrLGyb3odayCMk4ng9Ng05F%2BHs1G0W2BMX0Wc38VwoZSqKfVqgx3PltArCFdHVN%2FbqEDvZ%2FEPaikRUz74uu4g%2FD0Q%2F%2FIkgTXekDVYWkIViUOJq8f2f4mRGODWHgdll9MH%2FpVuGH6wqN7pt%2Bh9s%2FuCMruvsBx8TePe0Vznf4JmIGowA9RnQu8zSSb0166sXHL%2F5MCrZc4%2FAVQCrPiksreBOOLQjdW7ZoEsfLyNlW%2FFpj1F0BX201gUaaZ07ZigPA0epuWSzxTsKm6CEtdFC4Ni2hWgDmkS%2FKjDYKEDWlGEjf05uavl2gE7rugMgfcD9nCgRw0nvGzeFG%2B4bpRSklaOwzDj5cDLBm5mbrupXxRuaE0qhwksXM8zA1Xj5o%2BSol2eSIJzKOcOlCm3GIYEjjfn1TEg%2FB1o5IdbEvryp0Zyj2ai3pEQvx8ztEbNrqKmAl6VlQRf1zz3uNKued1H15SXNmG5or4tBPMJLwr8gGOqUBBNkXwIG1g06w5FYe5UCpvvdJuRVTPPKQQS0GlWSPYDefem68YhbPgS3y5uMutLHrRxQo47Uu6gVsZ5bJ9a0Jdxc%2BVl%2F%2FhEZS47JP5cMu%2B2yZNgFEtOwwoGs%2FPLi6vRGruyxVOk%2FTx2dFIkk0yEonqqO2pDp46S89gBpaZscxxm0%2BGxwq9SKaGqwZR5qhLjc48IQk6FCovDh40GqvGidx80NxEl2x&X-Amz-Signature=a28822adac85351461b1c492a8fd330d17c8ebc0ce567dcf6d2380a324311311&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YCMQMITM%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020047Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6J%2F%2BSJNYXvm09MA1lhwebryP8BDImQpJT9hesNHil5wIgM08ejnMKZL5AUsdMmT6xvZ7eGogVdU%2BBd0xWC3znOJMqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC4MTFPt5kSESWKcZCrcA4BjFr2xSVXUEcrJmtR40HYaqG28m3yTjjeGh5SV8CFruz7dxNVQRDuYusWqUfX9ugn1H5yencFJI8i8QzuVuJXRpyB72ylXOHN95E2RZ63041cSK1Kx3eXapEjdWkt0K7%2Fpo4FvJ3cQbE5nTakoSDGS%2F93GctrLGyb3odayCMk4ng9Ng05F%2BHs1G0W2BMX0Wc38VwoZSqKfVqgx3PltArCFdHVN%2FbqEDvZ%2FEPaikRUz74uu4g%2FD0Q%2F%2FIkgTXekDVYWkIViUOJq8f2f4mRGODWHgdll9MH%2FpVuGH6wqN7pt%2Bh9s%2FuCMruvsBx8TePe0Vznf4JmIGowA9RnQu8zSSb0166sXHL%2F5MCrZc4%2FAVQCrPiksreBOOLQjdW7ZoEsfLyNlW%2FFpj1F0BX201gUaaZ07ZigPA0epuWSzxTsKm6CEtdFC4Ni2hWgDmkS%2FKjDYKEDWlGEjf05uavl2gE7rugMgfcD9nCgRw0nvGzeFG%2B4bpRSklaOwzDj5cDLBm5mbrupXxRuaE0qhwksXM8zA1Xj5o%2BSol2eSIJzKOcOlCm3GIYEjjfn1TEg%2FB1o5IdbEvryp0Zyj2ai3pEQvx8ztEbNrqKmAl6VlQRf1zz3uNKued1H15SXNmG5or4tBPMJLwr8gGOqUBBNkXwIG1g06w5FYe5UCpvvdJuRVTPPKQQS0GlWSPYDefem68YhbPgS3y5uMutLHrRxQo47Uu6gVsZ5bJ9a0Jdxc%2BVl%2F%2FhEZS47JP5cMu%2B2yZNgFEtOwwoGs%2FPLi6vRGruyxVOk%2FTx2dFIkk0yEonqqO2pDp46S89gBpaZscxxm0%2BGxwq9SKaGqwZR5qhLjc48IQk6FCovDh40GqvGidx80NxEl2x&X-Amz-Signature=285d87ce134ecf7141061da103905e3c5dd1ed7477a709024c89225b59690684&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







