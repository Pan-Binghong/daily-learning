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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662K7ZD35R%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T094216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEp%2FSC%2F7jwJSaJH79wZ2CB%2FivB5U%2BGhfwqZAftDO%2BjXgAiEAlSoxc%2F99j2git4bZ0cSolvCDP%2FggUA%2FcdnvHonAV%2FvsqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLs1Qdg0RucZao26VircAxBIRdb0aFsEVrn0xODabGsMMxuk25Y0cGE44y3%2FN4m6I2x8FHUxytz45iSaFMLfNqzjnvA3sskQliGUfxTI7w37pWuJmJotr37z5ziTh%2BkA6RfcdtZQO0uJSqxqGumaU2SzakAUfKG8KEH7VNYqeizlzq2QULtCX%2Bxt0of1QObDmHXjnbCo0XfyplxZNFUHjg2xGJxAP6%2FWZAKKTN9Q75XMznD3GqTIypQRkfBkyelWDf89Vz7M2PnSJm5TsmnFpDoC%2F9y2%2BuWldxBckJHtUcRVDsR8fTHh2vl8t4%2FmWnu7gp64ZuVVHfWZhF%2BY51hSy3Fh08RGKvHbaXZC%2BfQl5rpWdG6Wcfar9Ku9PbKfHubMpzP2UVrhHKF4ezkON2Sal8L4ErV2MVu1r%2BP8z2x5Efn46PJ1yzi417xf6tRAf6JI3JBSBSObOJ4a3hoCWg14rg6YJj4YyrEfa6nrR7AeErhLhUndhs4FWpILNEBxkO4EUjMhO3T8MdUKAqEGPIS37gn5ON8rq%2B4PH0OSM6o2hgLKK8CXD6SyJzmtSIVJCTxBDK7PA8351URZma053Hp5ohGPFNdRcNdq4dbaQ9NhEY17xcMX3TP5uR1WirjwaFXNvg5w9GdeSvoQvuCxMNDXjs4GOqUBV9obDROGLmTjhEaliS9q3XqRamzTx5YUD6HuGuBJ%2FSCWrRz5LDptsihb66vrfcgXWH9kp9tV36dtEFHLmKcpKhuA%2Fwf033uyCmSeBtabt%2BgWsxuatD9rnY%2BlPyguGtmtn%2FNWG%2BGOF41zi%2BlWGAtAGGaCxZlmEnGyTacpsKjGDhTG9Ge%2Bji9l1asBPHmcGvME6CBUaumELORcE6cRU7V4o2YjVR4e&X-Amz-Signature=3a568d574bd7de5a38160876af50581672bf1a9bea34374ba3ea0b9782b48608&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662K7ZD35R%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T094216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEp%2FSC%2F7jwJSaJH79wZ2CB%2FivB5U%2BGhfwqZAftDO%2BjXgAiEAlSoxc%2F99j2git4bZ0cSolvCDP%2FggUA%2FcdnvHonAV%2FvsqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLs1Qdg0RucZao26VircAxBIRdb0aFsEVrn0xODabGsMMxuk25Y0cGE44y3%2FN4m6I2x8FHUxytz45iSaFMLfNqzjnvA3sskQliGUfxTI7w37pWuJmJotr37z5ziTh%2BkA6RfcdtZQO0uJSqxqGumaU2SzakAUfKG8KEH7VNYqeizlzq2QULtCX%2Bxt0of1QObDmHXjnbCo0XfyplxZNFUHjg2xGJxAP6%2FWZAKKTN9Q75XMznD3GqTIypQRkfBkyelWDf89Vz7M2PnSJm5TsmnFpDoC%2F9y2%2BuWldxBckJHtUcRVDsR8fTHh2vl8t4%2FmWnu7gp64ZuVVHfWZhF%2BY51hSy3Fh08RGKvHbaXZC%2BfQl5rpWdG6Wcfar9Ku9PbKfHubMpzP2UVrhHKF4ezkON2Sal8L4ErV2MVu1r%2BP8z2x5Efn46PJ1yzi417xf6tRAf6JI3JBSBSObOJ4a3hoCWg14rg6YJj4YyrEfa6nrR7AeErhLhUndhs4FWpILNEBxkO4EUjMhO3T8MdUKAqEGPIS37gn5ON8rq%2B4PH0OSM6o2hgLKK8CXD6SyJzmtSIVJCTxBDK7PA8351URZma053Hp5ohGPFNdRcNdq4dbaQ9NhEY17xcMX3TP5uR1WirjwaFXNvg5w9GdeSvoQvuCxMNDXjs4GOqUBV9obDROGLmTjhEaliS9q3XqRamzTx5YUD6HuGuBJ%2FSCWrRz5LDptsihb66vrfcgXWH9kp9tV36dtEFHLmKcpKhuA%2Fwf033uyCmSeBtabt%2BgWsxuatD9rnY%2BlPyguGtmtn%2FNWG%2BGOF41zi%2BlWGAtAGGaCxZlmEnGyTacpsKjGDhTG9Ge%2Bji9l1asBPHmcGvME6CBUaumELORcE6cRU7V4o2YjVR4e&X-Amz-Signature=5d8c39d1706bef7bf0474ce0d62a09e9ec2a5792e45792b8f6581e57db6675c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







