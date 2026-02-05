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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4IW3X2U%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJGMEQCIEhzkt6yQTjnJXC9otFWh4uneYz4G8EDHNThJOjhM1iFAiAduFsrvrQnRjvKLI%2BAfUdRBrQUpPhW%2FIwWSad%2B40aTxSr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMv%2Fsf8YfekVQIanPcKtwD9LigTcLn7hbYo8ht2ZNmV2oLHb9TAyBNS5NIYN4HP2YingnCVsSZyqsbvY%2BDvlA2EN5D9iJf8HnseVEn7Zngwkh1txqRzRl5GwKf5xCpxWh%2FsYXPTtV0cG%2Fkl5iMeom6hkhVsyxs%2B3GddlVbVNISkc9l%2Faw3lbJJ9vvDbjQEIqbn5xEBrueDkR6WIkhnd5Q7eVuyJOfUPStAHxhPYRFP2IzSHfZ4xZ8FX694dqcYmsOklzTunEAnGQvjJDcVZjAEVsAdr03Vk%2FT2d5XP0LMlDCMm0KKqoGa4ULtfbP6S7NFLoekphTMT5WZGEteTJ8Ep15Ow11hjc3W2AqCAhG4L%2Bw%2FpGwwaLZ977XY2k85hy14gDtGmQm5r7RbQ9z9i7iDdv9UG431xvaX3ZVF6VQAKVV4cdF69u3Pea42llk%2BnjZfOnfKVoW%2FCZBI5c0oy7ZHXoG4jnSBFIwHj7BBKxqWAEdp7wHOvZfFA0%2FrZJNBRI81hxEsevJmbTheRDXBVlDtyDjMvQuGK3obx%2B%2F1XHS6RivZyrepTQBcK4L8c1tC00WJXa68UTPopRHB7LEPQjssdqBWIX84eDW5p4NcdAFqc7t5B5jglljxOi9QB%2Fv5a%2FmE00pmSgReg52R1mvswmpSQzAY6pgEP%2BxpmEI9AedIt1yzqHiGjqthZ8KJcHzA8RQ0rnIMcbYOPSdOnFlCVTjg6X2QQ5BSaiONgTw4DXlLjUpQBt0ZUkI0kqPfxjO4eWCapDaEOnOCGG4FrgNqb5SQjTNAv3PCOhv8ckZjj9DNzPK1CrAPeq%2BM6uGF9IjzDHHMYIz4DioOr5g%2F7wdofCDF%2BxQoPRQFJ2%2BqAKfCOLXVvP4kG6PyyQVrWcwWT&X-Amz-Signature=3f86b7b27ce68d228035957c962e7abcc58fb6db40e2e488edfdd596134195f5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4IW3X2U%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJGMEQCIEhzkt6yQTjnJXC9otFWh4uneYz4G8EDHNThJOjhM1iFAiAduFsrvrQnRjvKLI%2BAfUdRBrQUpPhW%2FIwWSad%2B40aTxSr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMv%2Fsf8YfekVQIanPcKtwD9LigTcLn7hbYo8ht2ZNmV2oLHb9TAyBNS5NIYN4HP2YingnCVsSZyqsbvY%2BDvlA2EN5D9iJf8HnseVEn7Zngwkh1txqRzRl5GwKf5xCpxWh%2FsYXPTtV0cG%2Fkl5iMeom6hkhVsyxs%2B3GddlVbVNISkc9l%2Faw3lbJJ9vvDbjQEIqbn5xEBrueDkR6WIkhnd5Q7eVuyJOfUPStAHxhPYRFP2IzSHfZ4xZ8FX694dqcYmsOklzTunEAnGQvjJDcVZjAEVsAdr03Vk%2FT2d5XP0LMlDCMm0KKqoGa4ULtfbP6S7NFLoekphTMT5WZGEteTJ8Ep15Ow11hjc3W2AqCAhG4L%2Bw%2FpGwwaLZ977XY2k85hy14gDtGmQm5r7RbQ9z9i7iDdv9UG431xvaX3ZVF6VQAKVV4cdF69u3Pea42llk%2BnjZfOnfKVoW%2FCZBI5c0oy7ZHXoG4jnSBFIwHj7BBKxqWAEdp7wHOvZfFA0%2FrZJNBRI81hxEsevJmbTheRDXBVlDtyDjMvQuGK3obx%2B%2F1XHS6RivZyrepTQBcK4L8c1tC00WJXa68UTPopRHB7LEPQjssdqBWIX84eDW5p4NcdAFqc7t5B5jglljxOi9QB%2Fv5a%2FmE00pmSgReg52R1mvswmpSQzAY6pgEP%2BxpmEI9AedIt1yzqHiGjqthZ8KJcHzA8RQ0rnIMcbYOPSdOnFlCVTjg6X2QQ5BSaiONgTw4DXlLjUpQBt0ZUkI0kqPfxjO4eWCapDaEOnOCGG4FrgNqb5SQjTNAv3PCOhv8ckZjj9DNzPK1CrAPeq%2BM6uGF9IjzDHHMYIz4DioOr5g%2F7wdofCDF%2BxQoPRQFJ2%2BqAKfCOLXVvP4kG6PyyQVrWcwWT&X-Amz-Signature=c3b7dc986a3c46d673f865e6cc6ea0397870049b7b81841eb9cc56805d30b1f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







