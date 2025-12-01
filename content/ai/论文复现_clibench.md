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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BZT55XK%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T030907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIB%2BxRLQS9aNoF40MZc1g9S3%2FRJrCQmMBJY%2FHZhCkDXu9AiEAld47IvdTuGRYnfsoqgllJ3isFnfGNqc%2BnI6uf95eZT4qiAQI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAFPKia65zuMg2aGdircA%2FoHTk5NohQ91u%2BcK7UNn0ioF9meWRjHa5XYjtBH9uIR%2Be14faM8PNhOu0c8Rdi42OVie%2FmThasHDrAfniSJLe7aBNDuMrWTyX1PtH5dD4p9GSDRaw7lBwO6oCOKhxztiyrWiwbkPKnnadCQC097Y%2F1moZ4birGLrlfY58bQ5oR8yKV8uaQzEkGu8LbdanhF7SnD1l5IttQHE%2BS7CjOIgpMj311RuPCLiJIHXK3bPYtNVLCc9EIDd5p1vOVHnb8Cg9UxY2v3rzOZQaVYKJuHswRCxOxmnpI8LLctbOPE2J1OmgelEZUWOHdrPgXEKrQhuhL9gE03N5LZr40sXoOdfx5LpUR4W%2F85rs23CMD46EGvpsWn%2FBiZwegVtpnGW1YhKbGYPw0Hv2pR2Uby%2FGRRltHDz2wlEWqPYroK6Yd68lszlDHzE1QxBrUfJYMKdsDoNY2azqqvYhWeNUNLVo2UzCmyEApcbaUOaCh0ucBsqvT8dNYjjIPW7WovRrVy7OX%2BBuRmrEp%2FHQ%2F%2BfVFQcK%2FrDQGLp%2BlM7sQ%2FhTA3a0Yv3V0pMNNH%2BVIh1CzkhxcZoNKf3eEx7y28S5EKEhdoQtQX2%2B6Vm1LmwPXCp4dFdcD17nJwW7fP4eKXeuurDK%2BIMNGBs8kGOqUB3g%2BqPy8f%2BZfEyyScav91pSTIpv4hihIQTmHO3wJjwwfeXBNuX6Qy5qNw0FUP%2F79KiipERh4DTbycYiC%2Blsct6yIpYa1GIJZ5lgkacHhFXsrdPwO1KR8%2F5mMVlf5TFweAgTV8KQHEmZcXsC9fxBA6oUpECP5F4XEfsBERoTZlnWPBsJoW%2F0iWXolyrrqJ698iGnuXGHm14dofUTZjA2NF0wvI29LP&X-Amz-Signature=b196d6e0f9b504e4a8c5dd42ed9baf88ed77a3667e68e2c2a0b6062ac91538f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BZT55XK%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T030907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJHMEUCIB%2BxRLQS9aNoF40MZc1g9S3%2FRJrCQmMBJY%2FHZhCkDXu9AiEAld47IvdTuGRYnfsoqgllJ3isFnfGNqc%2BnI6uf95eZT4qiAQI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAFPKia65zuMg2aGdircA%2FoHTk5NohQ91u%2BcK7UNn0ioF9meWRjHa5XYjtBH9uIR%2Be14faM8PNhOu0c8Rdi42OVie%2FmThasHDrAfniSJLe7aBNDuMrWTyX1PtH5dD4p9GSDRaw7lBwO6oCOKhxztiyrWiwbkPKnnadCQC097Y%2F1moZ4birGLrlfY58bQ5oR8yKV8uaQzEkGu8LbdanhF7SnD1l5IttQHE%2BS7CjOIgpMj311RuPCLiJIHXK3bPYtNVLCc9EIDd5p1vOVHnb8Cg9UxY2v3rzOZQaVYKJuHswRCxOxmnpI8LLctbOPE2J1OmgelEZUWOHdrPgXEKrQhuhL9gE03N5LZr40sXoOdfx5LpUR4W%2F85rs23CMD46EGvpsWn%2FBiZwegVtpnGW1YhKbGYPw0Hv2pR2Uby%2FGRRltHDz2wlEWqPYroK6Yd68lszlDHzE1QxBrUfJYMKdsDoNY2azqqvYhWeNUNLVo2UzCmyEApcbaUOaCh0ucBsqvT8dNYjjIPW7WovRrVy7OX%2BBuRmrEp%2FHQ%2F%2BfVFQcK%2FrDQGLp%2BlM7sQ%2FhTA3a0Yv3V0pMNNH%2BVIh1CzkhxcZoNKf3eEx7y28S5EKEhdoQtQX2%2B6Vm1LmwPXCp4dFdcD17nJwW7fP4eKXeuurDK%2BIMNGBs8kGOqUB3g%2BqPy8f%2BZfEyyScav91pSTIpv4hihIQTmHO3wJjwwfeXBNuX6Qy5qNw0FUP%2F79KiipERh4DTbycYiC%2Blsct6yIpYa1GIJZ5lgkacHhFXsrdPwO1KR8%2F5mMVlf5TFweAgTV8KQHEmZcXsC9fxBA6oUpECP5F4XEfsBERoTZlnWPBsJoW%2F0iWXolyrrqJ698iGnuXGHm14dofUTZjA2NF0wvI29LP&X-Amz-Signature=db40c76ea6b8e261e51f45c36a09953f3c75bfa447fa729716c2592fd85541b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







