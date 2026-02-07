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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EC6F6JB%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVN%2FdmYfDd3M4AwGuhRMKle5qISCpSsvgPgs9BrjTu%2FQIgUCzOmzHd%2BLC3LKXhF3c%2B%2BZaVbmMgFDW0Gu%2FvRPEO3MUq%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDDvkPRWEj5I4OSNV5SrcAyZshFAFSLwtYb7tXrotUF5%2BoCGwCQZhtaHaHMsoA01QNXw3uFgAHirMlF77SXZIH8OG9RDtxATrDtM5SfAj8UapX3oINEpjQ7RjJU27%2BZiFcTQaOlWLY%2FNYDkMJDTiGCgHWjTDoA3TklTQS3OiuBHwE5nY1FamorQiyxfavuZMr0pfQVRbhr1PSegtIj5QbuY4Aq8HCHDUX3m0Yw8O2BsazJhrSlCwd6azNzMEaN5OX%2BPUQA8xXzqCefFgBes9JqlhCQ%2F%2FRfPjblC6ezZfYeUqUFhlFKSkKiyrwAJ2aLlg46gac5%2BO81%2BA5Ob8nzPerQeDMMCEvd04ouJWZASmjtjybDk70m4lnWnwbTgJVHFAGGj%2Bg2tJtXPD%2Fnq7bXTaPeWRQGcprymQIQeOFmWl9vQa6dq%2FxWf8paH1LdDUEfpW10E%2FpXgSYZIyVsBATEqJUv%2BY%2BRcdEk3FTshm5rc0U%2B8Hg1BwT%2BXe1lbHNEvfcQt22b0P8lJPLxUf6YnscJfVCbitfL3VyQB02Ace192EBZGH1aZpKo7ZuEUWyOGg4XyvsglW65CVo5KX%2F64i9%2FFv%2FqvCP7ARB8kAopxoJXzOMCpn2HJtOR2iUgsKrSpFdwDEpjGv08PoMyqoAKCBCML%2FEmswGOqUB6VDb3LUZhdF0iREgnjlGHTKQQv%2BG03m6WCtlvpoVU2haVBb%2BMOL0oCu1P%2B2f%2Bqlp1M9K%2Bzvf53e723%2Fdm8tTw2hi4EMo0mhCVFN9VLOfmKcHy7LiDJloEWnopAuyPhgUZ6Rezdn9fCy6KT46zZcssn7P6M4f2OqNzcR5T5epIzwJD8bybCsYYhf7920BFm6Da0mJOZVLvoRErnTzFXCn7f8Gb2UI&X-Amz-Signature=e0964848925f41138e0e4443597333188b5df6f7e6c8e5dec3e01761bb28fc72&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EC6F6JB%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVN%2FdmYfDd3M4AwGuhRMKle5qISCpSsvgPgs9BrjTu%2FQIgUCzOmzHd%2BLC3LKXhF3c%2B%2BZaVbmMgFDW0Gu%2FvRPEO3MUq%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDDvkPRWEj5I4OSNV5SrcAyZshFAFSLwtYb7tXrotUF5%2BoCGwCQZhtaHaHMsoA01QNXw3uFgAHirMlF77SXZIH8OG9RDtxATrDtM5SfAj8UapX3oINEpjQ7RjJU27%2BZiFcTQaOlWLY%2FNYDkMJDTiGCgHWjTDoA3TklTQS3OiuBHwE5nY1FamorQiyxfavuZMr0pfQVRbhr1PSegtIj5QbuY4Aq8HCHDUX3m0Yw8O2BsazJhrSlCwd6azNzMEaN5OX%2BPUQA8xXzqCefFgBes9JqlhCQ%2F%2FRfPjblC6ezZfYeUqUFhlFKSkKiyrwAJ2aLlg46gac5%2BO81%2BA5Ob8nzPerQeDMMCEvd04ouJWZASmjtjybDk70m4lnWnwbTgJVHFAGGj%2Bg2tJtXPD%2Fnq7bXTaPeWRQGcprymQIQeOFmWl9vQa6dq%2FxWf8paH1LdDUEfpW10E%2FpXgSYZIyVsBATEqJUv%2BY%2BRcdEk3FTshm5rc0U%2B8Hg1BwT%2BXe1lbHNEvfcQt22b0P8lJPLxUf6YnscJfVCbitfL3VyQB02Ace192EBZGH1aZpKo7ZuEUWyOGg4XyvsglW65CVo5KX%2F64i9%2FFv%2FqvCP7ARB8kAopxoJXzOMCpn2HJtOR2iUgsKrSpFdwDEpjGv08PoMyqoAKCBCML%2FEmswGOqUB6VDb3LUZhdF0iREgnjlGHTKQQv%2BG03m6WCtlvpoVU2haVBb%2BMOL0oCu1P%2B2f%2Bqlp1M9K%2Bzvf53e723%2Fdm8tTw2hi4EMo0mhCVFN9VLOfmKcHy7LiDJloEWnopAuyPhgUZ6Rezdn9fCy6KT46zZcssn7P6M4f2OqNzcR5T5epIzwJD8bybCsYYhf7920BFm6Da0mJOZVLvoRErnTzFXCn7f8Gb2UI&X-Amz-Signature=d73fa30c6445bd97c5e6d683b2568298dd5842983e776599df95590f9be170b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







