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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3PSBAS5%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T032821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQDiX9zCt8J84159GzNmxL7EJvReobI6uZ1r9o0aP3NOqgIgYapMd95OMPou212VpI945UIbH1Vbk7MokX%2BtpTknJ7kqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM27Wc72e%2FnGC6jToCrcA27R%2F7SjEklqxvgK%2BH8tCtCVajv03mtl7rWbcb%2FSi2eI4I%2BneklxEbmX35rCW5nala9irh1FUyxUFyeM5a9znN4%2FlYuyjZSBf%2BURABM1SbaMKRL%2BmQoMnWFWUxs6rrazKb1pRcTzeNG9d5J9OF8BCldBmc8G%2FI2lC7SkiwJ%2BQY2UaJAbvDJsxMl6IjyGajqnbmYSi64I7S4YHMTpafwSX2uZoIoPZjxN1qR7ReS5v0XNQfznmIaontRNE0HQ%2Fp5FAuFH8RMOmmUQFFfcTJaoG8XfyR8nMXdvFNSr9Ki4nfS8PjFU4CstGG2i91wQpcBNH4mp6Fig31jhfXyVvlu2vcOvdIbBCXrPPomNWhOBXdOsZhpssM6QA3vUH6XSmYXAyr9ibfTblwJMSEgYcZHpGPX0HHPjx8xsQLpu8%2BXvS7iZmnfr18TqsKyCfuCBg72lfvaZ%2B7AkquHXI3ywZuBQ0lM6FRggPpBFOJMe957fd9YLqMSamsG5iwVoKNZehISlikyvp6X%2FvmAme4DWtJd%2F2aYGduu6HTtiuwlOSPcm6jCKM890TH7YUmPNSMkyTi30mmLP%2FQcwlPANeFgSeVfYPAmQQfvSOGgPP9G%2Figq7ifykb33Rh2vRhQPDLmZuMMzPqM0GOqUBjtvh789qOe56Vp8TxfxQtZ4la5h%2B2e%2B5yH5I5bTvgk%2FIcy3tfttvvbSWv0TObY7VbuAne3GVDP9a1i2n5lD8T%2FmqyGbVRawmlYAwqhPA3ZlXZ39Cnq2nOdEbHts1Rld79j08ufaZRk3lnX30C8WGws%2Bt6YwTTXptCjvZ5jySlL%2F%2F6W5TDauq29Kcd8QDQ3Etlea8YL189Tpcogi41s0bfkcdY0hs&X-Amz-Signature=fa7502569c62e24b093f592bb2e329f431b59f9f3e6c94cb5c5f0215fdc09bf0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3PSBAS5%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T032821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQDiX9zCt8J84159GzNmxL7EJvReobI6uZ1r9o0aP3NOqgIgYapMd95OMPou212VpI945UIbH1Vbk7MokX%2BtpTknJ7kqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM27Wc72e%2FnGC6jToCrcA27R%2F7SjEklqxvgK%2BH8tCtCVajv03mtl7rWbcb%2FSi2eI4I%2BneklxEbmX35rCW5nala9irh1FUyxUFyeM5a9znN4%2FlYuyjZSBf%2BURABM1SbaMKRL%2BmQoMnWFWUxs6rrazKb1pRcTzeNG9d5J9OF8BCldBmc8G%2FI2lC7SkiwJ%2BQY2UaJAbvDJsxMl6IjyGajqnbmYSi64I7S4YHMTpafwSX2uZoIoPZjxN1qR7ReS5v0XNQfznmIaontRNE0HQ%2Fp5FAuFH8RMOmmUQFFfcTJaoG8XfyR8nMXdvFNSr9Ki4nfS8PjFU4CstGG2i91wQpcBNH4mp6Fig31jhfXyVvlu2vcOvdIbBCXrPPomNWhOBXdOsZhpssM6QA3vUH6XSmYXAyr9ibfTblwJMSEgYcZHpGPX0HHPjx8xsQLpu8%2BXvS7iZmnfr18TqsKyCfuCBg72lfvaZ%2B7AkquHXI3ywZuBQ0lM6FRggPpBFOJMe957fd9YLqMSamsG5iwVoKNZehISlikyvp6X%2FvmAme4DWtJd%2F2aYGduu6HTtiuwlOSPcm6jCKM890TH7YUmPNSMkyTi30mmLP%2FQcwlPANeFgSeVfYPAmQQfvSOGgPP9G%2Figq7ifykb33Rh2vRhQPDLmZuMMzPqM0GOqUBjtvh789qOe56Vp8TxfxQtZ4la5h%2B2e%2B5yH5I5bTvgk%2FIcy3tfttvvbSWv0TObY7VbuAne3GVDP9a1i2n5lD8T%2FmqyGbVRawmlYAwqhPA3ZlXZ39Cnq2nOdEbHts1Rld79j08ufaZRk3lnX30C8WGws%2Bt6YwTTXptCjvZ5jySlL%2F%2F6W5TDauq29Kcd8QDQ3Etlea8YL189Tpcogi41s0bfkcdY0hs&X-Amz-Signature=b570debcaf467158516f5e07f59e57e4a48e6568b4ef0a5704f67a3b04064f6a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







