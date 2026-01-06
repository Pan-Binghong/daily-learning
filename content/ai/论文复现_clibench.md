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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4433IWJ%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T025858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQClOBKezEG7oxy2RxmKnnkn0vXUMl41Z0EPxQ0%2FtiLqfQIgO0WNCLxO2Obt9BooXzx%2Br7VbYHKv%2FsOmVH%2Bq8%2BAAalMq%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDKyRbroMJirHyg5JuircAxUvY%2Fc4VzlTGgdEOJ2WpWI1mbSpovtt26MiNZ0FXSHpBBOemY%2BLtCCAu4lAtKIlp34FDqQfjv8pzovZApZ8vOvCb0yMwm4O2%2Bf3KTHh07tePAqEhOxsW26mb8cmpWZBBA%2Bv06ruIejUKX7Mr9zDyA48wTMjp%2B89ApjEniP9Gr9%2BO%2F51rziSlugQIsFEf%2Bt1tBrOAGElzOGRIqKOx4KbzCu4ukdcVZcJsRsOfxq7taqTj%2FfK481M6QBJHRNuVd701BTdH0CFT13YiIa8dI5KX9Ktni3NSpM7VoDIg9CkULLbYfEz1k1f7Nl26Z0pNs3WdIysV2t%2BusGndfzyUeKNGsR%2BxqD4dBX4WXmRAjV0qufWQubbaFmIj3t%2F5jChP2MG%2Bmm2xBCIdKn2P7ESAdD2KVUvnI9bOv4LIYhaS%2FEJ2rpI25OA%2By5jHRAmHhTqf6wzfObdYB88wbzY%2BcXYgziFE%2FGW9kCNc78m7z6BwU%2FMeaU9wQCkReidg7mFcROavZUkjUVsP8MJ86TDoXOJM3B4X%2BiYe1kyFkjUvyyYTqwoeMjUyl%2Bbr0tGNAVIacszoezYshEyTvyHKp4l9AxQvDob13W8vMEVMcdKZ%2BibXCVPoNFpMRU60n%2FhO0I4%2FagEMMzy8coGOqUBU1b23yfZz5GOHqveFC0vzmKy4qkkLXji519gDV8vPxDb9%2FJHZyjzOpyWrqG0L3QhsQBvG7c3CY%2FEsAXXa6dn7NgZ4IJ3GlRv5DG61svmYMOL2cewXzqVf4AZgIpK7GxfMmrqajDmOot%2FXN0LtqFtauCFtDdVdM7NsVLIBLJMPOSTdsZw3LX%2FFD%2FSka9hI2EgRRVQXkiiXdjaK2deeop3b4JcNlzM&X-Amz-Signature=28a5177242e3cc7d12c96921347f980f34c6ee1ac52f4f9a1dcc5a2d02e474c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4433IWJ%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T025858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQClOBKezEG7oxy2RxmKnnkn0vXUMl41Z0EPxQ0%2FtiLqfQIgO0WNCLxO2Obt9BooXzx%2Br7VbYHKv%2FsOmVH%2Bq8%2BAAalMq%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDKyRbroMJirHyg5JuircAxUvY%2Fc4VzlTGgdEOJ2WpWI1mbSpovtt26MiNZ0FXSHpBBOemY%2BLtCCAu4lAtKIlp34FDqQfjv8pzovZApZ8vOvCb0yMwm4O2%2Bf3KTHh07tePAqEhOxsW26mb8cmpWZBBA%2Bv06ruIejUKX7Mr9zDyA48wTMjp%2B89ApjEniP9Gr9%2BO%2F51rziSlugQIsFEf%2Bt1tBrOAGElzOGRIqKOx4KbzCu4ukdcVZcJsRsOfxq7taqTj%2FfK481M6QBJHRNuVd701BTdH0CFT13YiIa8dI5KX9Ktni3NSpM7VoDIg9CkULLbYfEz1k1f7Nl26Z0pNs3WdIysV2t%2BusGndfzyUeKNGsR%2BxqD4dBX4WXmRAjV0qufWQubbaFmIj3t%2F5jChP2MG%2Bmm2xBCIdKn2P7ESAdD2KVUvnI9bOv4LIYhaS%2FEJ2rpI25OA%2By5jHRAmHhTqf6wzfObdYB88wbzY%2BcXYgziFE%2FGW9kCNc78m7z6BwU%2FMeaU9wQCkReidg7mFcROavZUkjUVsP8MJ86TDoXOJM3B4X%2BiYe1kyFkjUvyyYTqwoeMjUyl%2Bbr0tGNAVIacszoezYshEyTvyHKp4l9AxQvDob13W8vMEVMcdKZ%2BibXCVPoNFpMRU60n%2FhO0I4%2FagEMMzy8coGOqUBU1b23yfZz5GOHqveFC0vzmKy4qkkLXji519gDV8vPxDb9%2FJHZyjzOpyWrqG0L3QhsQBvG7c3CY%2FEsAXXa6dn7NgZ4IJ3GlRv5DG61svmYMOL2cewXzqVf4AZgIpK7GxfMmrqajDmOot%2FXN0LtqFtauCFtDdVdM7NsVLIBLJMPOSTdsZw3LX%2FFD%2FSka9hI2EgRRVQXkiiXdjaK2deeop3b4JcNlzM&X-Amz-Signature=ad8841e40c1c76a3f27ed26e68aa008fe34997a17cba19da16b785c5ee1b3749&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







