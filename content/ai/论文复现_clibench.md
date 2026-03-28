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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666INCXF2I%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T033948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIE3O5RdtiGBZTLWVr%2Fs1yz7kcb%2FLYHW%2FYd03MgewcxJpAiEAvfDoADN7NCK85WHjo5u1zX5yPAYPPYq%2Ftwv43lQ0m%2BwqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFCnwAxB5p85vKebUSrcA7X4krrWjI6wRJs%2F1dUXqDKDkwYeh0UpeybDeJCQh%2FiY1v2BDk6RkuWq0MFZSnO4zQPOmqaTNR41Ks7iGs33o5pRHUhQoS%2BEYHSoJfqR1isert9ljJ3ummLfrNwZ%2BewAhq4iuCqyegS2fagH5EfajaFbKhf3eYVBebdt8OQtYw%2B0q69s6P%2FaaqIMTFsjMR3Sk76JTBoo%2BUcij7OtGEDfOfdow72tvCXaXwVRwtAveYOgvMiIrWZLdf%2BHW5MmpySsQvllGZLtFR2fEjni3Ca%2FtqR0WSpgcEw2W00ov75tR5yC6za1CQEwtccviUFEONIr%2Fy8IrWm2sN6hgYPr%2FxJKMiNGWs7YWe5EJE%2FL8DnHnXf9nqI4S3APZPu0tDInQ6XWs9NJfspkWW3Vx%2BKwt8w9Czk4RKKORYlyytR7piXHeRwSuQ5Tk2TYZv%2BSSYMt96zJfsQ9xcx5wruvsGt0SBjNiafFPm37CKBAEuKltcu36rc0ul6CFFEMXQh7I0wgKbSZ735f7r6S96rWlu9SpJSEPKnVcSevfsBDCUmhUgzWSwtX83df6Skld9V7j6Cow%2B5mEutB3Hd%2FU%2FYLUy5UbFXqWOC2paYUPBLpIA7g52pgLA8I7piuGzCpRbEILL6lMITtnM4GOqUB0NAMxxMUwL8gHcKLOODHTDTCt7TgfTwWbMrJ58%2FdoGf8ekwSJiV1ymqDpEeYfeI5Wc22mJkMKrVTCsXn30Cre%2Bwh0t6U3z%2BxyVzRflHfFF0gTrAKUaNl%2F8ZeYPxusVmybgf07WIbAewNrr4sK34VNVwsVmgOtl4n5LFYOlZSSDdkgAed50sWyLf3OnYkJ3c5Qe9zCFwT2HHImzVFtSo7h%2BqpQ8xb&X-Amz-Signature=8e024170cbd8ba80ee32ea7a4d718865b9745316da45682b4ff159bec97b8e20&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666INCXF2I%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T033948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIE3O5RdtiGBZTLWVr%2Fs1yz7kcb%2FLYHW%2FYd03MgewcxJpAiEAvfDoADN7NCK85WHjo5u1zX5yPAYPPYq%2Ftwv43lQ0m%2BwqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFCnwAxB5p85vKebUSrcA7X4krrWjI6wRJs%2F1dUXqDKDkwYeh0UpeybDeJCQh%2FiY1v2BDk6RkuWq0MFZSnO4zQPOmqaTNR41Ks7iGs33o5pRHUhQoS%2BEYHSoJfqR1isert9ljJ3ummLfrNwZ%2BewAhq4iuCqyegS2fagH5EfajaFbKhf3eYVBebdt8OQtYw%2B0q69s6P%2FaaqIMTFsjMR3Sk76JTBoo%2BUcij7OtGEDfOfdow72tvCXaXwVRwtAveYOgvMiIrWZLdf%2BHW5MmpySsQvllGZLtFR2fEjni3Ca%2FtqR0WSpgcEw2W00ov75tR5yC6za1CQEwtccviUFEONIr%2Fy8IrWm2sN6hgYPr%2FxJKMiNGWs7YWe5EJE%2FL8DnHnXf9nqI4S3APZPu0tDInQ6XWs9NJfspkWW3Vx%2BKwt8w9Czk4RKKORYlyytR7piXHeRwSuQ5Tk2TYZv%2BSSYMt96zJfsQ9xcx5wruvsGt0SBjNiafFPm37CKBAEuKltcu36rc0ul6CFFEMXQh7I0wgKbSZ735f7r6S96rWlu9SpJSEPKnVcSevfsBDCUmhUgzWSwtX83df6Skld9V7j6Cow%2B5mEutB3Hd%2FU%2FYLUy5UbFXqWOC2paYUPBLpIA7g52pgLA8I7piuGzCpRbEILL6lMITtnM4GOqUB0NAMxxMUwL8gHcKLOODHTDTCt7TgfTwWbMrJ58%2FdoGf8ekwSJiV1ymqDpEeYfeI5Wc22mJkMKrVTCsXn30Cre%2Bwh0t6U3z%2BxyVzRflHfFF0gTrAKUaNl%2F8ZeYPxusVmybgf07WIbAewNrr4sK34VNVwsVmgOtl4n5LFYOlZSSDdkgAed50sWyLf3OnYkJ3c5Qe9zCFwT2HHImzVFtSo7h%2BqpQ8xb&X-Amz-Signature=ffd32daf940e58f4a36df16b0e67a5a03529dc8b3d7403746cd83344fc29859d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







