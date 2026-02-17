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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOXUAIYC%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T033731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJIMEYCIQDnhhy83V3aAn%2BP1UrWd39g5udeZtOiZ03wH1pf3JDmEwIhALeA11bpKki%2FrY0Ojw8qDUjMZsmE6RVGQ0AuLGa12oyAKv8DCEUQABoMNjM3NDIzMTgzODA1IgyybzxiVuVm4gahPP8q3AOP9ga7kFCT3SvqtvH5d%2FX6D2%2BObifF5FETajjDQMYaOTaGbWS4SuoSnwm%2FM26zUP%2BBhgW8W2GDz7Ws%2Bo7%2Bb%2Fp02jdbElBqJcQicOGA9l3hEC4ZnkVNMYpTExwUXj8l%2F3GhKcBWOs9YIAmnaukRgGJy1SlqASn%2FYlwc7j7uC%2BcVMl28%2FiQJcAUMAuRr0eRHKmMFbj1E3OxF8LY02C9sIF31e2WUNoVcu9gSpCXF3l9xgTwhsnKvWBKCal9jBEJY4GaWwZY3FD978NQtCJNq1adXsicS%2BrWQlXeQS%2FSHuqENdjpv70ID0SDGonDRm8rWkZfxpbbzOa%2FzyaU7CN7dG5AJD1dBMSiKtluDIrNtbMGzl5n4K%2FGtX%2FY32Ix0Kdz1GeqE4JvmLkvVkmNEjWpaqkeBG%2FHK2W9pAv4U3aODb9ork6igqmGF9F%2Bf8Xu2XhsApJHNfWzvGU%2BrhxYsaBFEvZMWIN7cHSm7Sig8BMuc%2FxU0%2BzKktU2NqtgK7g4GgvC5tf6EozBoxXfuUP4CX%2BO4G9mon9LAvlaZLpC5Da%2BpO7bF8XVHDbMrz7uK9o%2Fh5RliYzmPps%2BouxK6ecT7VHS2Un8tL14ZMoBq9hxPIsKYG%2B8Qpz1HmYmUpLh1gmj6lTDZv8%2FMBjqkAfXhM5drnRSWspd5BQO%2FcWR66V1Rj9tKiPguiyaDGKRnpHmYLbAdUyZDCS7tUxJx7jhkD38yMXlpgaIn0kSsXhDwKKRYdppMn%2FhJ47PsIZtAvZZzqdEyt23Y2bQ2MyCi%2Fq6dtHfoKaY1jQ32pIyOOsXQZOcHDCwMZg2JVb1kxJba0o1hHLbepe6BK4OuilrNXojEUrP%2FnQuLTyRfT%2F9hoHJOhwY6&X-Amz-Signature=fea3288edfa3dd813d2063f349e35cf84ca46c81aaa5607ab58e0e723b5f5503&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOXUAIYC%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T033731Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJIMEYCIQDnhhy83V3aAn%2BP1UrWd39g5udeZtOiZ03wH1pf3JDmEwIhALeA11bpKki%2FrY0Ojw8qDUjMZsmE6RVGQ0AuLGa12oyAKv8DCEUQABoMNjM3NDIzMTgzODA1IgyybzxiVuVm4gahPP8q3AOP9ga7kFCT3SvqtvH5d%2FX6D2%2BObifF5FETajjDQMYaOTaGbWS4SuoSnwm%2FM26zUP%2BBhgW8W2GDz7Ws%2Bo7%2Bb%2Fp02jdbElBqJcQicOGA9l3hEC4ZnkVNMYpTExwUXj8l%2F3GhKcBWOs9YIAmnaukRgGJy1SlqASn%2FYlwc7j7uC%2BcVMl28%2FiQJcAUMAuRr0eRHKmMFbj1E3OxF8LY02C9sIF31e2WUNoVcu9gSpCXF3l9xgTwhsnKvWBKCal9jBEJY4GaWwZY3FD978NQtCJNq1adXsicS%2BrWQlXeQS%2FSHuqENdjpv70ID0SDGonDRm8rWkZfxpbbzOa%2FzyaU7CN7dG5AJD1dBMSiKtluDIrNtbMGzl5n4K%2FGtX%2FY32Ix0Kdz1GeqE4JvmLkvVkmNEjWpaqkeBG%2FHK2W9pAv4U3aODb9ork6igqmGF9F%2Bf8Xu2XhsApJHNfWzvGU%2BrhxYsaBFEvZMWIN7cHSm7Sig8BMuc%2FxU0%2BzKktU2NqtgK7g4GgvC5tf6EozBoxXfuUP4CX%2BO4G9mon9LAvlaZLpC5Da%2BpO7bF8XVHDbMrz7uK9o%2Fh5RliYzmPps%2BouxK6ecT7VHS2Un8tL14ZMoBq9hxPIsKYG%2B8Qpz1HmYmUpLh1gmj6lTDZv8%2FMBjqkAfXhM5drnRSWspd5BQO%2FcWR66V1Rj9tKiPguiyaDGKRnpHmYLbAdUyZDCS7tUxJx7jhkD38yMXlpgaIn0kSsXhDwKKRYdppMn%2FhJ47PsIZtAvZZzqdEyt23Y2bQ2MyCi%2Fq6dtHfoKaY1jQ32pIyOOsXQZOcHDCwMZg2JVb1kxJba0o1hHLbepe6BK4OuilrNXojEUrP%2FnQuLTyRfT%2F9hoHJOhwY6&X-Amz-Signature=a6f719b88e59ef4b1ad648fc40daf20d3f23aa4881e1d626c790430ea92f3101&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







