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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYERTQ5H%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID9F%2FFzpLgYsBeRpiQ3oD50v0%2Flf6nw1NJ99yCeycbV1AiAzkVNB4I2CV8KQ4IdBvqxE1iw4fqTVSod%2FFasSoFi%2Foyr%2FAwhcEAAaDDYzNzQyMzE4MzgwNSIM7h5fm1ah4B8gAmB3KtwDij3o2fmgny%2BKtQA3ji2xvLaMYhpgHluUNYilW1GKVByVjZsOFXCTqmzp0ap6N2aAXrEOPhPNBGO76F%2BD4BRq1U4SrZaq%2FhUwOe8cBpy48bgz%2FIe4F3%2BAbiOZwC1MfQREXb9%2Bq3wtXmWlenowfTmO7o5ic0pZSIH7h2RU9YRQiXFAQDvSR0XSRpb%2B0XKjzuGi8RkIRp0hIRSm3pVrjMnY3bbKIxC5c7G6ddMCnjO9S3c7Zar0RUbc5L8sCDys8jwXoRbHmHVRBvCRYWIUKCqVbtXgutbCp3Cpf2%2BDI7u1t5edH9o5VaZdJVqHcY6%2BxlYlcwN2%2But2GtJzQVTnvs0Vp%2ButDgENqT0FiwRhL0Jurlqx%2BXqWAGI0rv6oSMWWS%2FaoOMrx%2FyIuoY7keRB1NXZaQ0vghHCmY%2B81VR9p%2FmVOFlAyBr4N3JnNUAMZPphTpJ0FeAy%2BD9gGxbPIUmOcm5jNVRoaqVVoe6%2FcHMpAqF%2Bl7grWQoExC8O1YFVP97DW2Aw6K9o%2BV91Wi7HcC%2BZySiTzQMo5pekkmg81CUsBXk%2FDIEvRlnmpJK3I1HgcpngeSQJHphLDpv9k%2Fixo3Jj58cQgMYdF%2BKnPqLT%2BwAVnzItSNqzAScdKBvPnitk4FaEw7az9zQY6pgFYuNW7Yoy3OOP40eJlBkkIL9BxQWN6JQ4EkhfD7%2FuZsxjn1NzIDy7FAuAo49xr3gNaJms7h%2BQvmeX4Xqk1l%2F0p%2FX%2FJst%2F8GwNjhfr3YYa9fUUM2jhaavm%2BsV4Xl6%2Bho88xBim8w6FZAx7msioaG88CLmL8nfCKGd3R54U4%2BcutQmAPsJzV%2B0pN1fGufMPk7df2ImdQKwaYIv%2BApKrRLmpfkuIvMMdW&X-Amz-Signature=af51e9aa83713136984c2298dbaaf59a10f56d565afd0d26b0a4e273aab26e26&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYERTQ5H%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID9F%2FFzpLgYsBeRpiQ3oD50v0%2Flf6nw1NJ99yCeycbV1AiAzkVNB4I2CV8KQ4IdBvqxE1iw4fqTVSod%2FFasSoFi%2Foyr%2FAwhcEAAaDDYzNzQyMzE4MzgwNSIM7h5fm1ah4B8gAmB3KtwDij3o2fmgny%2BKtQA3ji2xvLaMYhpgHluUNYilW1GKVByVjZsOFXCTqmzp0ap6N2aAXrEOPhPNBGO76F%2BD4BRq1U4SrZaq%2FhUwOe8cBpy48bgz%2FIe4F3%2BAbiOZwC1MfQREXb9%2Bq3wtXmWlenowfTmO7o5ic0pZSIH7h2RU9YRQiXFAQDvSR0XSRpb%2B0XKjzuGi8RkIRp0hIRSm3pVrjMnY3bbKIxC5c7G6ddMCnjO9S3c7Zar0RUbc5L8sCDys8jwXoRbHmHVRBvCRYWIUKCqVbtXgutbCp3Cpf2%2BDI7u1t5edH9o5VaZdJVqHcY6%2BxlYlcwN2%2But2GtJzQVTnvs0Vp%2ButDgENqT0FiwRhL0Jurlqx%2BXqWAGI0rv6oSMWWS%2FaoOMrx%2FyIuoY7keRB1NXZaQ0vghHCmY%2B81VR9p%2FmVOFlAyBr4N3JnNUAMZPphTpJ0FeAy%2BD9gGxbPIUmOcm5jNVRoaqVVoe6%2FcHMpAqF%2Bl7grWQoExC8O1YFVP97DW2Aw6K9o%2BV91Wi7HcC%2BZySiTzQMo5pekkmg81CUsBXk%2FDIEvRlnmpJK3I1HgcpngeSQJHphLDpv9k%2Fixo3Jj58cQgMYdF%2BKnPqLT%2BwAVnzItSNqzAScdKBvPnitk4FaEw7az9zQY6pgFYuNW7Yoy3OOP40eJlBkkIL9BxQWN6JQ4EkhfD7%2FuZsxjn1NzIDy7FAuAo49xr3gNaJms7h%2BQvmeX4Xqk1l%2F0p%2FX%2FJst%2F8GwNjhfr3YYa9fUUM2jhaavm%2BsV4Xl6%2Bho88xBim8w6FZAx7msioaG88CLmL8nfCKGd3R54U4%2BcutQmAPsJzV%2B0pN1fGufMPk7df2ImdQKwaYIv%2BApKrRLmpfkuIvMMdW&X-Amz-Signature=e9177624f1a0a9e851ec70b9544d28326adb969741f9b6553554f73f2d1799be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







