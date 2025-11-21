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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QES52W4G%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIQCiv4HrO4wO4LYSD5wEHrbkmR%2FJzrElM4Wh81uKw5R3WQIgci8F9CMoUp7XHnozEQq7AHuSq27IY98%2FqC3IYRMOF7Yq%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDDlk6fyzALkAh10FFircAyAspoehT8QV8GC%2B35JqBBtakQYreEfnM1cehu4FRPPBQwCAPYxVA1Pkh%2F3FS6HTOHwM01RAq61%2B3u3ZHbu7pX2FsFAkiaIo8SrAu%2BxV%2B3VuHyleXd0%2F%2F8Jb7nEC2h6aokpX8Tqm0UKOvUJItp9QVEI2w2kguZT4%2B0sblfTZyUh72zrgbOMSdO7DqcsChUNvHw%2FSyxe3aHF5SqHYf2%2F%2BxqGugSWaGTENqGjmvWut2AGHer6nXrffc3wf8vPKgpJG7THI3z3X9CbjHzv%2BBPbrhd6UCUDf5LDPw5FkFYgdAr%2BaJmY6EZ0ns%2Fe%2FyrbdkM65ysNZWsXiS3Ov2HgETpIPndX7J0RFSvOJxYNpNKF%2BMURyNypdj79U%2BM1Utrg9hSmxZ%2BqkO331FfHIBTSI0vl%2FQG%2F1xAF%2FoZ6B6C%2BP5A5XQ8aGvdoC%2BqVmdU0wV2jIu8UX5yjFKtPpP8JY76Hs%2FTlsiDHMvLnq2pB7qBOzth32Z2iFA%2Bow5CrOjdTL9W7p3yU0zre9v0KPrIsM%2BI9ztz%2F5t%2F3hLTmxfEmu4td2Pqavmu6B02tGta%2F9KLhw2xOeyFl4BpQL69kQ12bDRKlJTpBw7O7CW4v1qnAMxZcbalb9nskeGa3zPMiwSbPGTR%2B6MOSf%2F8gGOqUBBLsy5Nc7oq67ChONq0njeIoDhuBNQuXerjVWiGN9KE22j%2B8I0E0eW1FEhVpZIpjST%2B02fjJPtVMkl2uh8%2BRNAoh5YDtR0BXV9pbg2DqDJrUSqupnLdWeZwibknbyEbRyKoaP%2BQh0K%2BCxf3DG8XrOALTqWWRtg%2BhU5qrr8Mg%2FrOrHG0SYauiJWD0Q0VEnz2oMAvun1ciXs29SIyTXd5r0UdEaNprl&X-Amz-Signature=eb73fe192595d44a99d89776bc504255c7c104e02cf0b05699bd2eb2ff40afdb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QES52W4G%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIQCiv4HrO4wO4LYSD5wEHrbkmR%2FJzrElM4Wh81uKw5R3WQIgci8F9CMoUp7XHnozEQq7AHuSq27IY98%2FqC3IYRMOF7Yq%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDDlk6fyzALkAh10FFircAyAspoehT8QV8GC%2B35JqBBtakQYreEfnM1cehu4FRPPBQwCAPYxVA1Pkh%2F3FS6HTOHwM01RAq61%2B3u3ZHbu7pX2FsFAkiaIo8SrAu%2BxV%2B3VuHyleXd0%2F%2F8Jb7nEC2h6aokpX8Tqm0UKOvUJItp9QVEI2w2kguZT4%2B0sblfTZyUh72zrgbOMSdO7DqcsChUNvHw%2FSyxe3aHF5SqHYf2%2F%2BxqGugSWaGTENqGjmvWut2AGHer6nXrffc3wf8vPKgpJG7THI3z3X9CbjHzv%2BBPbrhd6UCUDf5LDPw5FkFYgdAr%2BaJmY6EZ0ns%2Fe%2FyrbdkM65ysNZWsXiS3Ov2HgETpIPndX7J0RFSvOJxYNpNKF%2BMURyNypdj79U%2BM1Utrg9hSmxZ%2BqkO331FfHIBTSI0vl%2FQG%2F1xAF%2FoZ6B6C%2BP5A5XQ8aGvdoC%2BqVmdU0wV2jIu8UX5yjFKtPpP8JY76Hs%2FTlsiDHMvLnq2pB7qBOzth32Z2iFA%2Bow5CrOjdTL9W7p3yU0zre9v0KPrIsM%2BI9ztz%2F5t%2F3hLTmxfEmu4td2Pqavmu6B02tGta%2F9KLhw2xOeyFl4BpQL69kQ12bDRKlJTpBw7O7CW4v1qnAMxZcbalb9nskeGa3zPMiwSbPGTR%2B6MOSf%2F8gGOqUBBLsy5Nc7oq67ChONq0njeIoDhuBNQuXerjVWiGN9KE22j%2B8I0E0eW1FEhVpZIpjST%2B02fjJPtVMkl2uh8%2BRNAoh5YDtR0BXV9pbg2DqDJrUSqupnLdWeZwibknbyEbRyKoaP%2BQh0K%2BCxf3DG8XrOALTqWWRtg%2BhU5qrr8Mg%2FrOrHG0SYauiJWD0Q0VEnz2oMAvun1ciXs29SIyTXd5r0UdEaNprl&X-Amz-Signature=eb92ea89e166e7057e54afc4efe45f000a7b4bda0238b44a27d39249b0c3f771&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







