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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLYSCVZT%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCKgN5v17jGD0ibdgyzMkuipmsoD8Tt1agPcPxAYv%2BWFAIhAPZLYZ2RVH9q1lvBJju74KTYiXL7tOhBJSYjTeCkis5LKv8DCHQQABoMNjM3NDIzMTgzODA1IgyNfc5aWYenDTVfl%2B4q3ANtekgVSSdDjLVJnp25QZAahgM9AXVGT80Lky2P2PFyJJT5FKGfIBACTBPjCzn4Bgw%2FSoo%2F%2BqN%2BlRtpHv1xjv%2FhmwayeNJQ%2FAlPwM4vKGd5bz%2BpW4dPNmlLrOf2eZrer2D%2B4JG37B5yT084r5yWNNgJtwJd%2Fhj3hZ4%2FjN%2FogAQ7anGvJo8Oh44rpoGRA5rGqKcYPCL2OM2y4CwP34nYVPHNyMudMvw0e0IVqt12tI9JD3v60dRF%2FNrNkxB0esK6R3udQ4l5eKVk%2FsGQqDokfkhSVnaUVi%2BeCBMJ7yJCE4l7jdoqfnmtXMc%2BKL5wR6Ddbm7OhEVcIyPRNqsq1g0CpR3aQP0Aic8JK04bsuVk7819NPtWZ8Swkv256QCjkB7FjPM3YNMy0OKMISnsVWyMpjPPRq8Q6uRVRd1ocKuacMdlUDeICM97z%2B92DhHf22kLrG0%2FRAt7tiDuqiV87vfiK0sSUUTE1xYxOyzHJuadtdIb812rrpSpTYMv9tuAgEumgJEtcpFs3cxOJ61FGMJr3dirYBJMDRX5q51HADXxMWr0NaKi9%2FWsljH%2ByQ8AgRNPere%2FsCl%2BMWJHwPsrlkfiANpTo6FEhjweu%2Fk6wX9nVs3A10qgSpVzRCh5hnyf9TDB5ILOBjqkAdhL8SzmKAYnmGMVwBT9wRdB4B3iWvygzOrN4phNIFDXa7tm2zOoWXjYF5qOsQvMkgXuntaPfxlDkMfp23UQV45ertlp6ZjEHng84QPjaRm0%2BsDTh%2FQ02VVH8YIAfbPExR1Q5Zu2ItweMrMM5VbLv2l%2FF6FmcXr8lTDHfmNF2b7qaun%2FqD5AtyeyeKajvd7XLOpcFrxR%2BVwekolBD5Ec%2FCBmakUs&X-Amz-Signature=a153d2c59aa16bcaac7ed5fad7dc0936cdb298b0e61b3a0700de24ea32354609&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLYSCVZT%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCKgN5v17jGD0ibdgyzMkuipmsoD8Tt1agPcPxAYv%2BWFAIhAPZLYZ2RVH9q1lvBJju74KTYiXL7tOhBJSYjTeCkis5LKv8DCHQQABoMNjM3NDIzMTgzODA1IgyNfc5aWYenDTVfl%2B4q3ANtekgVSSdDjLVJnp25QZAahgM9AXVGT80Lky2P2PFyJJT5FKGfIBACTBPjCzn4Bgw%2FSoo%2F%2BqN%2BlRtpHv1xjv%2FhmwayeNJQ%2FAlPwM4vKGd5bz%2BpW4dPNmlLrOf2eZrer2D%2B4JG37B5yT084r5yWNNgJtwJd%2Fhj3hZ4%2FjN%2FogAQ7anGvJo8Oh44rpoGRA5rGqKcYPCL2OM2y4CwP34nYVPHNyMudMvw0e0IVqt12tI9JD3v60dRF%2FNrNkxB0esK6R3udQ4l5eKVk%2FsGQqDokfkhSVnaUVi%2BeCBMJ7yJCE4l7jdoqfnmtXMc%2BKL5wR6Ddbm7OhEVcIyPRNqsq1g0CpR3aQP0Aic8JK04bsuVk7819NPtWZ8Swkv256QCjkB7FjPM3YNMy0OKMISnsVWyMpjPPRq8Q6uRVRd1ocKuacMdlUDeICM97z%2B92DhHf22kLrG0%2FRAt7tiDuqiV87vfiK0sSUUTE1xYxOyzHJuadtdIb812rrpSpTYMv9tuAgEumgJEtcpFs3cxOJ61FGMJr3dirYBJMDRX5q51HADXxMWr0NaKi9%2FWsljH%2ByQ8AgRNPere%2FsCl%2BMWJHwPsrlkfiANpTo6FEhjweu%2Fk6wX9nVs3A10qgSpVzRCh5hnyf9TDB5ILOBjqkAdhL8SzmKAYnmGMVwBT9wRdB4B3iWvygzOrN4phNIFDXa7tm2zOoWXjYF5qOsQvMkgXuntaPfxlDkMfp23UQV45ertlp6ZjEHng84QPjaRm0%2BsDTh%2FQ02VVH8YIAfbPExR1Q5Zu2ItweMrMM5VbLv2l%2FF6FmcXr8lTDHfmNF2b7qaun%2FqD5AtyeyeKajvd7XLOpcFrxR%2BVwekolBD5Ec%2FCBmakUs&X-Amz-Signature=7ec5038ef54897314d9f9ea7b544046578ab3232dc7c1805bbb0907101c8cf18&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







