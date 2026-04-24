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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667V3IRJ5H%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCWBHB61tn7huGdkGZww5Do1wHCz80YzzDLdYWUUUprSwIgR258DyzoOyzvBvLjUiPAkb6KVfZuhCOwg9shcGG4ryQq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDLC4tKAr%2B7G58fg7kCrcA0eYBO2%2F4g2pk9UxJvgDRNXf4I%2F7P6o3XDYu5Ki6GQsteHs4RY7taGWCZ%2BLYpCer2MiY0k6DPoDC8XQ2vgDTEHCAdQ5pyt2lpQL6Gg3H9RLiq4EtDH9b4hR6YIGi1ujwoK6lnLuCaX4Myx6ekTGQ3r2srgPSzXpwNI9rb6HxHrGGG4KNCC1km3A90M0NMpk5Kg1Jl59ymfygT04BjojU4rfLeQERZehablxSHSe6NVwV4EsB%2FH2zNRK4gQWnGMGPxjtxXE0YdUXJiTxUapcM4q%2FT55VaxQbkyEUSQlp7WuuoySpOFocR5RXQ9pmCLIuzURnc1KchfOoZhYH%2B1tc7BeTZPcsMVmSYhYwPhcMOrgpUOXZP%2FiItpnK7fTpdJlnOeewNXEVOJfZqKXrSduHq%2BBds3wKGvgz83oy1qcxxhrcmam3ymjHDEvTFMLSxDeWd4Q7yTSwZyzjgWbf8Mese1HQAvWwxBPXZgfmuRHXx8Noq%2Blr%2BqEFbXJffiPjIm33h%2FuhJGEKJX83X6Y4aki52fwhv7jow0BIMen%2FzkP%2FBqV%2FHGxhoAW%2F99%2BASMssaZk1FQzgE1J5ZXjamNku9dlbIHcbXQoy8ILkkw1ppdUhbSCSvr5p61igJ909M7milMLOvq88GOqUBLfMSoaI0HfWdedFx7OdTLOAkgj72tUe1Dy1FLmyRsk%2BMYym9untQnr5sG7JWdDTqJJJz%2B0keMwK7wr0l59oHNN%2BYcca6UiuU2b%2FE20543zX0jBUJM%2BJcPojDFBPMsaynqBZAQk3ZCWLtRatPMi%2BghrW7KFyDAW14GMpZjKeZyYGjNXQxupqikO4l2f%2FwbtpyS8kRoHZEI8dALnuQiM8dRgMqf95d&X-Amz-Signature=6e921885282ee51a27ea94f876aa2fd1111d4e577eca6dc9cd5a9e890ca717a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667V3IRJ5H%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCWBHB61tn7huGdkGZww5Do1wHCz80YzzDLdYWUUUprSwIgR258DyzoOyzvBvLjUiPAkb6KVfZuhCOwg9shcGG4ryQq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDLC4tKAr%2B7G58fg7kCrcA0eYBO2%2F4g2pk9UxJvgDRNXf4I%2F7P6o3XDYu5Ki6GQsteHs4RY7taGWCZ%2BLYpCer2MiY0k6DPoDC8XQ2vgDTEHCAdQ5pyt2lpQL6Gg3H9RLiq4EtDH9b4hR6YIGi1ujwoK6lnLuCaX4Myx6ekTGQ3r2srgPSzXpwNI9rb6HxHrGGG4KNCC1km3A90M0NMpk5Kg1Jl59ymfygT04BjojU4rfLeQERZehablxSHSe6NVwV4EsB%2FH2zNRK4gQWnGMGPxjtxXE0YdUXJiTxUapcM4q%2FT55VaxQbkyEUSQlp7WuuoySpOFocR5RXQ9pmCLIuzURnc1KchfOoZhYH%2B1tc7BeTZPcsMVmSYhYwPhcMOrgpUOXZP%2FiItpnK7fTpdJlnOeewNXEVOJfZqKXrSduHq%2BBds3wKGvgz83oy1qcxxhrcmam3ymjHDEvTFMLSxDeWd4Q7yTSwZyzjgWbf8Mese1HQAvWwxBPXZgfmuRHXx8Noq%2Blr%2BqEFbXJffiPjIm33h%2FuhJGEKJX83X6Y4aki52fwhv7jow0BIMen%2FzkP%2FBqV%2FHGxhoAW%2F99%2BASMssaZk1FQzgE1J5ZXjamNku9dlbIHcbXQoy8ILkkw1ppdUhbSCSvr5p61igJ909M7milMLOvq88GOqUBLfMSoaI0HfWdedFx7OdTLOAkgj72tUe1Dy1FLmyRsk%2BMYym9untQnr5sG7JWdDTqJJJz%2B0keMwK7wr0l59oHNN%2BYcca6UiuU2b%2FE20543zX0jBUJM%2BJcPojDFBPMsaynqBZAQk3ZCWLtRatPMi%2BghrW7KFyDAW14GMpZjKeZyYGjNXQxupqikO4l2f%2FwbtpyS8kRoHZEI8dALnuQiM8dRgMqf95d&X-Amz-Signature=6990b4c106c7bc44ffbd215c6666e33cee849102fa8c277f9a66dbd3d32c7a10&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







