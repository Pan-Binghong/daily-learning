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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUZE3NCO%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgObH7kvioJr0Kx6oQjO0reep1o7LvssdoofzI9gum5wIgTXSHCCRtChD2EyhRgYrszZAeJWJJ0OmEvAQ0POQoui0qiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGzR0WSqh7yCo5a2IyrcA4eAwxwBpo1nN%2FLhf5I8RZoLqq3sAbPaCi2ja4VGiVt6k71AwJHgxnUdRlsJ6hTHl4l5NB2qhAmjw9gHM5aNVUoin7c3w6c2R0908K2Rz8Lgf0JE4TMIQYU%2B61VosZ1J7wY6rFwve3lDKDPkk4FyawdI8h2YN6NURyId8hrF46IVEpswz44LUUNgrm3oaLx8bDp74%2BlgWz52YRdPVNPb8pCOfabtGOvSiUk0XK%2Bn6GyYm%2BsvdubutYgJGQ29UScni2Hg1LOD58KZZyLPwAgAFn3dHICKtA2WJm1ymDcM2Bp9K7xPJH%2BZb3RNamDGiK7ao7IxaHyN7IyJMgvftB7%2FfCjkCZY3fOfoBRJ9lvw2j2yQIOmeh39K%2BIXfC1tcHoMQcc%2Fumn5MmidksJBho5pdngqPI77e56l19vHYq9sEgbHlVrjDtPsCfnKZWdIoGEiHESM3Z5m12lMKVMQRy%2F5TC3Vk2l0x3XswGXYojxFlmhbcxjWH0rfy5SrSP2jRBNCHn2Z4WZpJkRFCDtjSlzvDaGDhxpoRjaglqliovbQKQv8oMJ793rzid2hVMnuv6dkmKlwuedR0zU0u1tYC8pPj4YcTMfxKd9S8%2FiUImWsDTuG1ZEQXMSW8MBXNYiZkMIaZ78gGOqUBdHmM2XSum4RlHApw7vKe3Ug%2Buhh1wrTMpcwK6Gl7MupyqnG9Z%2BFn6r2S8vb34oLU03ZF9ZupBiYKIWP7DQJ968vfTpzlfZUmEDpfNx1FOVhnjC5uAzCnhUYCbQiMgfWH06RhryauCtsSaf4dOQgN%2FRMfQi4LolUXLVwTMnB3vVXfWz%2BXtO9s30nXB7b8d%2BJu56dCJNN7AnsMS6RD8KOSdKZqJt%2BD&X-Amz-Signature=147dd9ab15a47f24793efb1913e7de31d391df9d332d066e1794eea1443816eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUZE3NCO%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgObH7kvioJr0Kx6oQjO0reep1o7LvssdoofzI9gum5wIgTXSHCCRtChD2EyhRgYrszZAeJWJJ0OmEvAQ0POQoui0qiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGzR0WSqh7yCo5a2IyrcA4eAwxwBpo1nN%2FLhf5I8RZoLqq3sAbPaCi2ja4VGiVt6k71AwJHgxnUdRlsJ6hTHl4l5NB2qhAmjw9gHM5aNVUoin7c3w6c2R0908K2Rz8Lgf0JE4TMIQYU%2B61VosZ1J7wY6rFwve3lDKDPkk4FyawdI8h2YN6NURyId8hrF46IVEpswz44LUUNgrm3oaLx8bDp74%2BlgWz52YRdPVNPb8pCOfabtGOvSiUk0XK%2Bn6GyYm%2BsvdubutYgJGQ29UScni2Hg1LOD58KZZyLPwAgAFn3dHICKtA2WJm1ymDcM2Bp9K7xPJH%2BZb3RNamDGiK7ao7IxaHyN7IyJMgvftB7%2FfCjkCZY3fOfoBRJ9lvw2j2yQIOmeh39K%2BIXfC1tcHoMQcc%2Fumn5MmidksJBho5pdngqPI77e56l19vHYq9sEgbHlVrjDtPsCfnKZWdIoGEiHESM3Z5m12lMKVMQRy%2F5TC3Vk2l0x3XswGXYojxFlmhbcxjWH0rfy5SrSP2jRBNCHn2Z4WZpJkRFCDtjSlzvDaGDhxpoRjaglqliovbQKQv8oMJ793rzid2hVMnuv6dkmKlwuedR0zU0u1tYC8pPj4YcTMfxKd9S8%2FiUImWsDTuG1ZEQXMSW8MBXNYiZkMIaZ78gGOqUBdHmM2XSum4RlHApw7vKe3Ug%2Buhh1wrTMpcwK6Gl7MupyqnG9Z%2BFn6r2S8vb34oLU03ZF9ZupBiYKIWP7DQJ968vfTpzlfZUmEDpfNx1FOVhnjC5uAzCnhUYCbQiMgfWH06RhryauCtsSaf4dOQgN%2FRMfQi4LolUXLVwTMnB3vVXfWz%2BXtO9s30nXB7b8d%2BJu56dCJNN7AnsMS6RD8KOSdKZqJt%2BD&X-Amz-Signature=2f1bc10130ed88979730de563112e78abae674a2bd524121a5b697f9d31d1ac6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







