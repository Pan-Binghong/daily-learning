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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPNSGPT6%2F20260312%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260312T033345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAcQrAzb6UlSjl3uUR0I8O59JIrQZ9V3Ex737R4fl2b6AiBAGxkhB%2FHYwnatUI9fYdzAdnHzfCRHDFH3nZBEvlaOASr%2FAwhrEAAaDDYzNzQyMzE4MzgwNSIMK%2FzoaTqP8T5ku%2FMrKtwDw7cps4UKiVZG6Yb9sU7i3ShIoHzZahj20Xglf7HaAYcWZxR7SQLT%2BdleIUZOjhP1tnblYEJceRVMKZGpM7IaIT8CX6DBA7kptsXyILYQlx00SLsiMVHGMTGWP3CoNHWqL3wcCOYMH2iPKLn%2BLOFYs5by6qIi%2BKqopeNknDk6cMEk0rrgTAypv36zKhj5k0pvmBuvzOhvksCfofm1g741oR8i8RKpVrmRKI%2FEECmsv1QI0Zbd2meafVKO6VpyjjYsSaTsULisxxOdcD9XDa9FMOY2ocQs3rAJ%2FZnLz2wMwwI9N2AnmULqQwgEiBR2UaGTk1W4uYWrzqCt0akb57azsUvTCkD44HukPgfudAWmKPg%2F11f9ehFFnurcwjFbj29eCnZxlWlOtIUaYZjBB2O0IxhLDxgKun9reT0cEsPMSO0Frpri5Nj6cPv0syvDB0cIi10m9zVe6RU%2BdF4Cs9JpOUHh%2Fdh0F6KwwJRXGAdGJ80cQ5sgfyJU3iYKXXLB8Q6VtJn%2BSEElgORBJJcaqHrjn5KpP69ylNAvvYcAvNL2MGslerPi8ZCii2usJs%2BC6ayDCCk141Qqxu840lE%2BKrHmERuDqOF1D%2FKDXzCvo4kSlf0KgpHpd5py3dg%2FKXwwkbLIzQY6pgHiupjrEi5r2ojSREZpbXReDuiZpR9An3qWgnqcbWSIkDRvxWUYYFLss4qM356bhFwP%2FjwunHK5djeFAcqIR8ThY7IvV%2BYiwUsBo5TQxE8QCYynG0cglABURnPAztvvCxx6s70rQ262pnmGA%2F2dzlhaxej6Sx%2BEp8lZGzWhJBpzcXRSI1xTf%2BqCTTfAaiQf4kGXfPHF1Xr3uH%2FAhKHIJ5sp39n8m7MI&X-Amz-Signature=789a259fa089b9f0366627d4902e1824b5ad38acc44378b8e6e15ebf079c0714&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPNSGPT6%2F20260312%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260312T033345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAcQrAzb6UlSjl3uUR0I8O59JIrQZ9V3Ex737R4fl2b6AiBAGxkhB%2FHYwnatUI9fYdzAdnHzfCRHDFH3nZBEvlaOASr%2FAwhrEAAaDDYzNzQyMzE4MzgwNSIMK%2FzoaTqP8T5ku%2FMrKtwDw7cps4UKiVZG6Yb9sU7i3ShIoHzZahj20Xglf7HaAYcWZxR7SQLT%2BdleIUZOjhP1tnblYEJceRVMKZGpM7IaIT8CX6DBA7kptsXyILYQlx00SLsiMVHGMTGWP3CoNHWqL3wcCOYMH2iPKLn%2BLOFYs5by6qIi%2BKqopeNknDk6cMEk0rrgTAypv36zKhj5k0pvmBuvzOhvksCfofm1g741oR8i8RKpVrmRKI%2FEECmsv1QI0Zbd2meafVKO6VpyjjYsSaTsULisxxOdcD9XDa9FMOY2ocQs3rAJ%2FZnLz2wMwwI9N2AnmULqQwgEiBR2UaGTk1W4uYWrzqCt0akb57azsUvTCkD44HukPgfudAWmKPg%2F11f9ehFFnurcwjFbj29eCnZxlWlOtIUaYZjBB2O0IxhLDxgKun9reT0cEsPMSO0Frpri5Nj6cPv0syvDB0cIi10m9zVe6RU%2BdF4Cs9JpOUHh%2Fdh0F6KwwJRXGAdGJ80cQ5sgfyJU3iYKXXLB8Q6VtJn%2BSEElgORBJJcaqHrjn5KpP69ylNAvvYcAvNL2MGslerPi8ZCii2usJs%2BC6ayDCCk141Qqxu840lE%2BKrHmERuDqOF1D%2FKDXzCvo4kSlf0KgpHpd5py3dg%2FKXwwkbLIzQY6pgHiupjrEi5r2ojSREZpbXReDuiZpR9An3qWgnqcbWSIkDRvxWUYYFLss4qM356bhFwP%2FjwunHK5djeFAcqIR8ThY7IvV%2BYiwUsBo5TQxE8QCYynG0cglABURnPAztvvCxx6s70rQ262pnmGA%2F2dzlhaxej6Sx%2BEp8lZGzWhJBpzcXRSI1xTf%2BqCTTfAaiQf4kGXfPHF1Xr3uH%2FAhKHIJ5sp39n8m7MI&X-Amz-Signature=a802fb9b6cfdc5668a3b9a98dcf0d55053d11ba85ea1ae60efb5363897bd76d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







