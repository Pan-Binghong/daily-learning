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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMHTWOHH%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDnwXriI67kUdNd25%2FYUEyKnBJdVuILC39c%2FTCxvgNTwIgIlWpE2BWcZXRWMuyPEoOACJ01zQ0QXfLprVL3WRF9tYqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJAf4Nnsr6%2Baf0hIHyrcAwiLKmal5SW2T6jOG5O5sjf0ahmYbxv15AVejdr8Dwu1HdGEFGsTHeLlnRs3lcweuHLpW34kCyPiYBb%2BhMIKbRlOfZ1o%2Bv7Swb7qruM7PwXQwh%2BwGITVTzZHKe7sholwSvvHG1eRWVO0Dbf6egXfEcd3oRFD9FeujhaXBKkgc6LrhMWSKKdfZPyz3Zun4z63qO3e4OYncvu2ro70VxOa8X8s2UxAj6M8lIe7hC%2F3fHLisnJYIp%2BnVtNzMubrmmTOJrZpUORTZp4xP8B%2BFsO6DtWJFBoJ9WzLman7HppvvhiLwUpzSNfBTFyKL0CTjp98i%2FqY%2FDDIgDWLmuijSqXQpCQtVDoiUn3CdXXp0KqK%2BNuLYL7XoQprhis79%2B7kdCsS0lVkwsY5lv8aIN7RE%2FOeMDOScDPN75TISPFJSlNHl5UqpTSdR72AhGIU70XJN%2Biu0H8Rs99KNHMsMPuf7ZP25wZifELTohljq5sruVEmQ%2BNjFbeD%2BBcJh0T58fbhcHp8Q6uw4crXlbrc8wu13nsn0dpEv9FoKsvNDdy9wkvuGTojPBB320ryYigqfnFltyraeyRGp56JB5qZYc7jtcH1w%2FROswPpz37uwV%2Fw7dcxpB0XQ4q7BPJv9I4BFWGTMMDzh84GOqUBe6H50A99X05MmyoCFmPa5T%2FAszbwmkRNDmXk%2F0cggSevsuyGM0LrYfunIP%2F%2B2N87JliMOMAFeAbwboV6EyDAgKsyCU6IoWOEJNbNnM994NcNDNObiFo92%2FGgVtvNx32jW6sEbK4Z3mTVX1noX85qlFDWopMMrEIdAuPGN%2BtAPyC2jtfVD2PBkhRY4CJKIOdEdpWzxuA0xSZYkt0hawP7dsbQqLVy&X-Amz-Signature=d0249234123769c92f9006596387a1e9c1bca2b07a59a957bfe0152e6fb4751a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMHTWOHH%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDnwXriI67kUdNd25%2FYUEyKnBJdVuILC39c%2FTCxvgNTwIgIlWpE2BWcZXRWMuyPEoOACJ01zQ0QXfLprVL3WRF9tYqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJAf4Nnsr6%2Baf0hIHyrcAwiLKmal5SW2T6jOG5O5sjf0ahmYbxv15AVejdr8Dwu1HdGEFGsTHeLlnRs3lcweuHLpW34kCyPiYBb%2BhMIKbRlOfZ1o%2Bv7Swb7qruM7PwXQwh%2BwGITVTzZHKe7sholwSvvHG1eRWVO0Dbf6egXfEcd3oRFD9FeujhaXBKkgc6LrhMWSKKdfZPyz3Zun4z63qO3e4OYncvu2ro70VxOa8X8s2UxAj6M8lIe7hC%2F3fHLisnJYIp%2BnVtNzMubrmmTOJrZpUORTZp4xP8B%2BFsO6DtWJFBoJ9WzLman7HppvvhiLwUpzSNfBTFyKL0CTjp98i%2FqY%2FDDIgDWLmuijSqXQpCQtVDoiUn3CdXXp0KqK%2BNuLYL7XoQprhis79%2B7kdCsS0lVkwsY5lv8aIN7RE%2FOeMDOScDPN75TISPFJSlNHl5UqpTSdR72AhGIU70XJN%2Biu0H8Rs99KNHMsMPuf7ZP25wZifELTohljq5sruVEmQ%2BNjFbeD%2BBcJh0T58fbhcHp8Q6uw4crXlbrc8wu13nsn0dpEv9FoKsvNDdy9wkvuGTojPBB320ryYigqfnFltyraeyRGp56JB5qZYc7jtcH1w%2FROswPpz37uwV%2Fw7dcxpB0XQ4q7BPJv9I4BFWGTMMDzh84GOqUBe6H50A99X05MmyoCFmPa5T%2FAszbwmkRNDmXk%2F0cggSevsuyGM0LrYfunIP%2F%2B2N87JliMOMAFeAbwboV6EyDAgKsyCU6IoWOEJNbNnM994NcNDNObiFo92%2FGgVtvNx32jW6sEbK4Z3mTVX1noX85qlFDWopMMrEIdAuPGN%2BtAPyC2jtfVD2PBkhRY4CJKIOdEdpWzxuA0xSZYkt0hawP7dsbQqLVy&X-Amz-Signature=3cf81c9f193fba5ea00050fc6870b72e4cd7d9fd8e00d703e12602c8b0a6532a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







