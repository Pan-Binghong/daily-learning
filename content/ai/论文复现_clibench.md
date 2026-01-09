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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644QZDWIT%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICVYY%2B6qCVQztC7Tp2aLLJPscbh5ZbIJf2T%2BPFAO7l4HAiEAp%2B4aw%2FQVyTH00seAfeI064Fdhbxj2zASdTWrno2sQPQqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMqyNXCH71c0Sg62jSrcA5jonq39ouWRchBr1FkEcAyewVtbhZqTWmOI7BwCxtIKrm9IxXkbq5MZ36I52Md%2Fn3kelWmqCZFFST9tRWWslusmXzlE%2FTHeQzBFcKzde9x1Ph%2FGFFu5tVDXgAHxc5MxbD9P4KW%2BEc%2BRrKlytZ3%2BdmUPSXo7REuO3EHhKHfFxdbq95GrSqKSQJjgDsYdvoOamXBZ6VBhwb8LauzyIHoq6CGAPasHQyxnmw7vwKV3AySeljWy1DWiYW8TtzvcjYbxHmLC50AWAw0ESp9CSkeIYALSaNtRVZ2y4sxcyxElvcSXJFcXdnCkwkk9H%2FVytPJfgV%2BX%2BIPNLO55dfQn7Wv%2FTY94n2ZyyOJ0LhFs3W%2FfKlH3Ow2EkJReSySuLX5EVdDIki2ZzLAYSIwq6KC0iH8tn5S%2FGfqnjHb2w1wiXJcJK8NaJAR7A%2FETJMPdwya3prfJ%2FaNyYJB4r2pVaUqj0h6%2Fqh0Jwzyj6qAjRaHhP22Rg%2BA35bqw8F8puFOS8shUgNU3BNcOFE4Xm0NLwFz%2FiayGPqG2fr9AAkHL7hBZ3lrX%2BTH0uTShF1XYLw8Tk%2BXZHTkTvCmoeSp4r78V1tqDVnhSys1P9kxqq4YMPX8ftu7yxGBcDmFF5nEemYJ9Mdp3MOPEgcsGOqUBMpot4t%2FiUpAcAmeucvoHQQhAbYmwMYIDA8FC8L5Pn%2Fr8oJrtFyqlkw4PMtHL%2BSYktxMN2WlwL9b6BIgBlebjKNdQubzl1B5BEY3CcAtjVS5tX2IIdnx0ZuoJdkWvYGAbQP7aysvA0xPRPB3LQNW%2FpNLCBt%2BoaIx3UDP0UGZ7VVd3GtwVKxWwhs7floex%2BxYlCnUCsM1gGsRVJId56fi4iVh%2BZ%2Bmr&X-Amz-Signature=a583e378230d8f9f9dd8e567fb083edd5fa3e977a5c264c451953db0692be96e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644QZDWIT%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICVYY%2B6qCVQztC7Tp2aLLJPscbh5ZbIJf2T%2BPFAO7l4HAiEAp%2B4aw%2FQVyTH00seAfeI064Fdhbxj2zASdTWrno2sQPQqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMqyNXCH71c0Sg62jSrcA5jonq39ouWRchBr1FkEcAyewVtbhZqTWmOI7BwCxtIKrm9IxXkbq5MZ36I52Md%2Fn3kelWmqCZFFST9tRWWslusmXzlE%2FTHeQzBFcKzde9x1Ph%2FGFFu5tVDXgAHxc5MxbD9P4KW%2BEc%2BRrKlytZ3%2BdmUPSXo7REuO3EHhKHfFxdbq95GrSqKSQJjgDsYdvoOamXBZ6VBhwb8LauzyIHoq6CGAPasHQyxnmw7vwKV3AySeljWy1DWiYW8TtzvcjYbxHmLC50AWAw0ESp9CSkeIYALSaNtRVZ2y4sxcyxElvcSXJFcXdnCkwkk9H%2FVytPJfgV%2BX%2BIPNLO55dfQn7Wv%2FTY94n2ZyyOJ0LhFs3W%2FfKlH3Ow2EkJReSySuLX5EVdDIki2ZzLAYSIwq6KC0iH8tn5S%2FGfqnjHb2w1wiXJcJK8NaJAR7A%2FETJMPdwya3prfJ%2FaNyYJB4r2pVaUqj0h6%2Fqh0Jwzyj6qAjRaHhP22Rg%2BA35bqw8F8puFOS8shUgNU3BNcOFE4Xm0NLwFz%2FiayGPqG2fr9AAkHL7hBZ3lrX%2BTH0uTShF1XYLw8Tk%2BXZHTkTvCmoeSp4r78V1tqDVnhSys1P9kxqq4YMPX8ftu7yxGBcDmFF5nEemYJ9Mdp3MOPEgcsGOqUBMpot4t%2FiUpAcAmeucvoHQQhAbYmwMYIDA8FC8L5Pn%2Fr8oJrtFyqlkw4PMtHL%2BSYktxMN2WlwL9b6BIgBlebjKNdQubzl1B5BEY3CcAtjVS5tX2IIdnx0ZuoJdkWvYGAbQP7aysvA0xPRPB3LQNW%2FpNLCBt%2BoaIx3UDP0UGZ7VVd3GtwVKxWwhs7floex%2BxYlCnUCsM1gGsRVJId56fi4iVh%2BZ%2Bmr&X-Amz-Signature=6a33c287fcb3c64aac6de1778ffceea4f8f83f5268ed38ea588abd1bb9dcd8a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







