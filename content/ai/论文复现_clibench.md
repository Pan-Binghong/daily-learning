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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNPFMY5R%2F20251122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251122T022630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJHMEUCIQDLdAjtTWtAkphVIO9P1JmS36f%2F6VRaz8NfLG%2B0N2vYwAIgeKyKIkTviSWdHU0Un31lVTS5wGeuKXxrMdCmvc0JFIIq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDKW0kXK0OGywNLWA2yrcA4k0VlzXMjPE%2BzyXlwLYTF59en%2FCWY%2F38jYjxCRScdIMQzOUaPx3AvuItdUWy5LpgYg0I1yUSpIBpACie5N6HuRaHzewfdRaQRGpgSdeu1sB35hxy7io8AxVsWHG5Tj2%2B6hrieHCtCx9VPAspaJVhifo9BjS0qn9rrxGs5YNUp0waIo1uz%2B8aNyfpm0dV2%2B6iAe04%2FmsfrgJUf8Yo3qK8FzjUMAgATQzmlE7TzN%2Fd7Y6TkamiNWI0%2BtNAm8IF%2F1cFuZTBEbEfc1dyiG8wn732%2BlGVBYEZkNk73WcDUxm5YNRnC6fZ3L1MN%2BHIQnGU9EVyLzv5PLM4kg%2FCwlrZQdb%2BZPWzR709N5lU8ipWMGusdBQXg231HqMVlT0S7GiN2CLC4bs20ohnQ1%2B%2BwvSdd0R2QhhzPqpXumtN6RRoZw5t0B7tB9GRJTnYU4Fy9CtNGiJLxmT%2BTkkGaFtoinVwOOA1w51xCbbo1jZ1OV7la7AclRgoyuCPVsWKTDcgMdch444gGRjwqUEYW8mS07QqesE9PAAkBQewPCAO8abEB72fmaOrnzQO61%2B2307lWOEis5kZGlJWaI4Wu5FkF%2BfYXl8tzhyx45KplCJZsYirNk1grLSC%2BZR%2BNzgumlW%2FDrOMLahhMkGOqUBo%2FjuXOt%2FcMhev6gogbcTLiieE0rV12JMoIWACJXpGm3duw6MhMtf4jBXEHkw%2BO2bHxKVVtifT793h6L1%2BMG9kQPjXvGxvG3LFH%2FX8etG7wk4pcdSnYmQMLf1hJ5O0ay%2BNKjFLtOfbFwwznmRYzRoJMMBlSJBvKQte8ajXfaPX5Pm0kOxlk8Hsa0X%2FxhwCJh5b7yKzwm1CMLJN5kXPODP9BR1Yz%2Bm&X-Amz-Signature=3764a0ae91bc96e0d72ba3398085d8f060200be1b7dfcd852acaa62b4ef0ffa0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNPFMY5R%2F20251122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251122T022630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJHMEUCIQDLdAjtTWtAkphVIO9P1JmS36f%2F6VRaz8NfLG%2B0N2vYwAIgeKyKIkTviSWdHU0Un31lVTS5wGeuKXxrMdCmvc0JFIIq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDKW0kXK0OGywNLWA2yrcA4k0VlzXMjPE%2BzyXlwLYTF59en%2FCWY%2F38jYjxCRScdIMQzOUaPx3AvuItdUWy5LpgYg0I1yUSpIBpACie5N6HuRaHzewfdRaQRGpgSdeu1sB35hxy7io8AxVsWHG5Tj2%2B6hrieHCtCx9VPAspaJVhifo9BjS0qn9rrxGs5YNUp0waIo1uz%2B8aNyfpm0dV2%2B6iAe04%2FmsfrgJUf8Yo3qK8FzjUMAgATQzmlE7TzN%2Fd7Y6TkamiNWI0%2BtNAm8IF%2F1cFuZTBEbEfc1dyiG8wn732%2BlGVBYEZkNk73WcDUxm5YNRnC6fZ3L1MN%2BHIQnGU9EVyLzv5PLM4kg%2FCwlrZQdb%2BZPWzR709N5lU8ipWMGusdBQXg231HqMVlT0S7GiN2CLC4bs20ohnQ1%2B%2BwvSdd0R2QhhzPqpXumtN6RRoZw5t0B7tB9GRJTnYU4Fy9CtNGiJLxmT%2BTkkGaFtoinVwOOA1w51xCbbo1jZ1OV7la7AclRgoyuCPVsWKTDcgMdch444gGRjwqUEYW8mS07QqesE9PAAkBQewPCAO8abEB72fmaOrnzQO61%2B2307lWOEis5kZGlJWaI4Wu5FkF%2BfYXl8tzhyx45KplCJZsYirNk1grLSC%2BZR%2BNzgumlW%2FDrOMLahhMkGOqUBo%2FjuXOt%2FcMhev6gogbcTLiieE0rV12JMoIWACJXpGm3duw6MhMtf4jBXEHkw%2BO2bHxKVVtifT793h6L1%2BMG9kQPjXvGxvG3LFH%2FX8etG7wk4pcdSnYmQMLf1hJ5O0ay%2BNKjFLtOfbFwwznmRYzRoJMMBlSJBvKQte8ajXfaPX5Pm0kOxlk8Hsa0X%2FxhwCJh5b7yKzwm1CMLJN5kXPODP9BR1Yz%2Bm&X-Amz-Signature=f0a50295a1b903b3b75a6af36e37d6c18d464810216ba59c073e9b890672fdbd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







