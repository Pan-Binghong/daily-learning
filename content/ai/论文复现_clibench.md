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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPAVXETL%2F20260317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260317T033517Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQDzfbDI3aJuPVy4QaJYF3oWsx7i9i6ncMvfxsBPne7kMAIhANe9hZyYZQeo82t74m97FhVX0eUVRUSu5nHsft263RscKogECOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyG%2BQFUNruaUI3sISMq3AOZBZOUqcwmusuSIUwx1lFuUpBg%2F2Q3w%2FiexX5DTj%2BmgxmO396J0njjkuxOEYMaZLhTPe7CU%2BLyBxAauxq5DOrcFubMgJEowLKj0V56nSEMbcxP9o946Szt0vIj7HQmRsfW76WRGWyLmGg%2FyZ8jKAoBvPXmnzez7nFt4Cd8BQpOgyk12e%2BXrJHwL4QyHiCBnhYobiygzfAhtW1t1lX4KXOxuJTdLUdoK%2FP9qAspObl82o3tDHwnT4gso%2FLuuIqcOu9JVUHBkit59jCZIt9%2FCReKLeik4gLqxXSyezkuauGD1x85JSosRiVoL0mipzabpXpFBHPTuqXYGGv5IxYvLs%2FOZs%2F8DvMIlVG1WoR0OGvtFLjbN5XAEDFdRVfi84enhBK9L9uV7uOFEkZ%2Bcah%2FfkUI4Hu4M3OK55bwww0pSusAutg%2BtXl4Km4V6Y0kWU2J7axGqcflApWZHkfQYK4Dpoxlyve7Japv9o1x1mBZQA5xeyFTy94B9heKxUWKNV01A09QoLAF3NYZT%2FzAyolUgHs4Xz4AFhXkhj3hkQzg3DGncreCbNKEiBlXtPPH%2BwpYKX5v5ubAzN9LOo7owT7KmJZWBDFxsaB2qAY8osvgZNNSLiIFHWDylAb4gy7qXTDx5%2BLNBjqkAX3Xm%2BDePxv2qMIvR8oNR00999eoc8hK%2Fnt%2BMD7jJRXhX6%2FHakNR0ZrazxIfdhPI4v0%2FKv%2FotOBykBQt0F8L%2BqUqjAPYMQvcJZ1rtynkhSemFQFFnWx4XGm1yib1O1hU4NoKX3Ad12zYGfvYzxB8VpkQABcWie%2Ff6OAg76IgSciJ48DRpI%2FV394sNvXVr2mzRnti50gl70bEp30brgfs8m%2B%2BY39I&X-Amz-Signature=4680d1befa5fb0d6653a94bb5981a23268c1e2d0a4c6bca50a0e5e3289eab9b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QPAVXETL%2F20260317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260317T033517Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQDzfbDI3aJuPVy4QaJYF3oWsx7i9i6ncMvfxsBPne7kMAIhANe9hZyYZQeo82t74m97FhVX0eUVRUSu5nHsft263RscKogECOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyG%2BQFUNruaUI3sISMq3AOZBZOUqcwmusuSIUwx1lFuUpBg%2F2Q3w%2FiexX5DTj%2BmgxmO396J0njjkuxOEYMaZLhTPe7CU%2BLyBxAauxq5DOrcFubMgJEowLKj0V56nSEMbcxP9o946Szt0vIj7HQmRsfW76WRGWyLmGg%2FyZ8jKAoBvPXmnzez7nFt4Cd8BQpOgyk12e%2BXrJHwL4QyHiCBnhYobiygzfAhtW1t1lX4KXOxuJTdLUdoK%2FP9qAspObl82o3tDHwnT4gso%2FLuuIqcOu9JVUHBkit59jCZIt9%2FCReKLeik4gLqxXSyezkuauGD1x85JSosRiVoL0mipzabpXpFBHPTuqXYGGv5IxYvLs%2FOZs%2F8DvMIlVG1WoR0OGvtFLjbN5XAEDFdRVfi84enhBK9L9uV7uOFEkZ%2Bcah%2FfkUI4Hu4M3OK55bwww0pSusAutg%2BtXl4Km4V6Y0kWU2J7axGqcflApWZHkfQYK4Dpoxlyve7Japv9o1x1mBZQA5xeyFTy94B9heKxUWKNV01A09QoLAF3NYZT%2FzAyolUgHs4Xz4AFhXkhj3hkQzg3DGncreCbNKEiBlXtPPH%2BwpYKX5v5ubAzN9LOo7owT7KmJZWBDFxsaB2qAY8osvgZNNSLiIFHWDylAb4gy7qXTDx5%2BLNBjqkAX3Xm%2BDePxv2qMIvR8oNR00999eoc8hK%2Fnt%2BMD7jJRXhX6%2FHakNR0ZrazxIfdhPI4v0%2FKv%2FotOBykBQt0F8L%2BqUqjAPYMQvcJZ1rtynkhSemFQFFnWx4XGm1yib1O1hU4NoKX3Ad12zYGfvYzxB8VpkQABcWie%2Ff6OAg76IgSciJ48DRpI%2FV394sNvXVr2mzRnti50gl70bEp30brgfs8m%2B%2BY39I&X-Amz-Signature=33480a735c913d6b31a3580183e80c0448aef456d7ca7e4e7c836513c10c5314&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







