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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TS6JWO3C%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032820Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDMAOBBCzjXdojYD0WilD8N5WUUuB9N63HOKVSlWa06uwIhALmBP6ei%2BVniY5gcXbKNVSJXFkoD38d7sLSFiOd6D5%2B3Kv8DCHwQABoMNjM3NDIzMTgzODA1IgwbkwlILKSwG86ipM0q3AN3UHxJBeFrGcK6X%2Bmsicrp%2BCQ8OUY8PScZ1%2F0CnxJPR45bEqswTi3uvS0wcEzGAkhqvCCfdhYhjk%2FFtg2Exy0%2F2HcwK8YYu8B%2BOEIiW8uTBOj5E99cxGCScqMD0oyqTxXHdxP%2B00gQ%2FqsHitugLu1clSSodXqjURjTrT2jdHlMZT%2F3SDjmkVqxmHEZFCKL9K%2BDG108vWDRlK9wiYMc7LWZ8BC2NbuWORWts86qVcKtVKdRtlRGqfWjZn6a70y0d3rUaIt0FraOfuSYoFYFlu2jgyGcnmwkJRvTF%2FVbMUMfVRZmOw2CQfg2xEzMvbZZo460JNmDjY7taKJmubjlSFYS74uSV2Lj%2B7ykmF40%2BOsbGjLb5gLJfihzQMfNDsnN7SeOr%2BTADNjcuZfAbWiYLDKft3r3qPOA%2FWXPTEkfbLvr6h0%2BKmjlg5eBdssDQDEyIbyc4FP%2BgKr4DG18fEOnOMcg0Rjt68nYfrIHv1tmnm3yI%2FCo1cVCd3dWd04X4OTpvr%2BTD8IqbkgYNqV3N02UH3JZyWsqnUfenFO5Ube6s8fjcH56hCvaM8edUwmavwIuePJOBCxDsfmBeGtdELimhKolUsCnDbh8O0eg%2FZEeT%2B0hPTZ0RWooNEd0838GljCAouvLBjqkAaOvr7lgpztLwCxZeh72FJkwnj4NWE5tVKrSlSClGh6Z9a7DkFe50RDyA8S2CO7cp50DDROG1FezaHBfy%2F2FyFAZxKug6CuJsT4GvD4qRuPGTDnz1VsD%2FGTuRhKqls5OAduloinaZxa%2BmPq2od5QYyjql0m74nGT8BnldIWavhIDurYzbj8rhgEaTTPaeXk%2FFQcwFigSjLXZxaq6sazT%2BYkPm0uD&X-Amz-Signature=902e48a081db41dcf38319a2d13fac058270e9c36c179e0e2de4b7cec3b7ba60&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TS6JWO3C%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032820Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDMAOBBCzjXdojYD0WilD8N5WUUuB9N63HOKVSlWa06uwIhALmBP6ei%2BVniY5gcXbKNVSJXFkoD38d7sLSFiOd6D5%2B3Kv8DCHwQABoMNjM3NDIzMTgzODA1IgwbkwlILKSwG86ipM0q3AN3UHxJBeFrGcK6X%2Bmsicrp%2BCQ8OUY8PScZ1%2F0CnxJPR45bEqswTi3uvS0wcEzGAkhqvCCfdhYhjk%2FFtg2Exy0%2F2HcwK8YYu8B%2BOEIiW8uTBOj5E99cxGCScqMD0oyqTxXHdxP%2B00gQ%2FqsHitugLu1clSSodXqjURjTrT2jdHlMZT%2F3SDjmkVqxmHEZFCKL9K%2BDG108vWDRlK9wiYMc7LWZ8BC2NbuWORWts86qVcKtVKdRtlRGqfWjZn6a70y0d3rUaIt0FraOfuSYoFYFlu2jgyGcnmwkJRvTF%2FVbMUMfVRZmOw2CQfg2xEzMvbZZo460JNmDjY7taKJmubjlSFYS74uSV2Lj%2B7ykmF40%2BOsbGjLb5gLJfihzQMfNDsnN7SeOr%2BTADNjcuZfAbWiYLDKft3r3qPOA%2FWXPTEkfbLvr6h0%2BKmjlg5eBdssDQDEyIbyc4FP%2BgKr4DG18fEOnOMcg0Rjt68nYfrIHv1tmnm3yI%2FCo1cVCd3dWd04X4OTpvr%2BTD8IqbkgYNqV3N02UH3JZyWsqnUfenFO5Ube6s8fjcH56hCvaM8edUwmavwIuePJOBCxDsfmBeGtdELimhKolUsCnDbh8O0eg%2FZEeT%2B0hPTZ0RWooNEd0838GljCAouvLBjqkAaOvr7lgpztLwCxZeh72FJkwnj4NWE5tVKrSlSClGh6Z9a7DkFe50RDyA8S2CO7cp50DDROG1FezaHBfy%2F2FyFAZxKug6CuJsT4GvD4qRuPGTDnz1VsD%2FGTuRhKqls5OAduloinaZxa%2BmPq2od5QYyjql0m74nGT8BnldIWavhIDurYzbj8rhgEaTTPaeXk%2FFQcwFigSjLXZxaq6sazT%2BYkPm0uD&X-Amz-Signature=466cb59b1a4e4b9db595ef5749e22649b7b278d5d0dc03b78bb6a48b48df7b80&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







