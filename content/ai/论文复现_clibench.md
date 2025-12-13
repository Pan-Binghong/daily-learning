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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLBHC2U6%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIQC8wgEjOvteYOrIq%2BdaXeRVzz78AUAI3s6y%2FZqT2yzmvgIgKe8f1ALeT%2FyIiJ8822IpFSw%2Beg10PwAECzO4l%2BDewZwq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDKVLh267KpH317mFaSrcA6JWMxpvpcOcd%2B1OdGlT%2BB6s34C1jl6Z2Gm92oVq3kTqANkGTkHTw%2FpCc0RtezTpNEH5D%2BUIFkOM62lNwLQuhfgN%2Fy2ZgsWil4%2Fr%2BA0Im1d7TEaOK89HF9BAPxEoaANVwlylZt7MLW7ht08dUbZwc9YF0YmJibOu2%2BZcBhF1IKufQAoF2AQ92XMDLD0tDqnH7SUp2Kdbec0WxUWcqkaDPBTugKW8NN6M4gBOA9PKnLs8f46NJSVXJcwG%2FXh0ndlUYpyhnc1NHSB9rgoWv%2BMipgYKpczfqIcUEgVLK1flXkqBWdjqoL9kCSGcT1uWYCAIyJ2fWccQndUtIQ%2Fzy9%2BGANE5EGBC0ZB5mXboMmu2VQ4lhmBuA2JbSEA0WNQQc4hlEWlimKTIiiRzHSL4LHAgrS8a32uIwgHWz0FJ8uz5TYMYfL4OzlYri994qrOUNpCSXSco7Dl80x7193jGht5PL04gxrKXl8Bu7IjccYmjFeV5Guk33brj%2BVtB1MEBUuFduMB8Tlo0WwPKxxfw78E27BvyqYtoWVXmJgRgDz65Cl3CKGPCwneHbMpniuDRKhb0Ls8EDq4j8bW0RyQP3tH6LWFijmsXMvHoND3p23K%2B%2B9A3w%2Fr0JzCATfHcg6OIML2N88kGOqUB%2FhgTXb9fvJqMtsuzpWVdO%2FdVm5hF%2Beruc0dviIsxeF7RAOu1AlVl2dMqG43g18bXjobTXL2wYmJStW45yCvZ7nkgEkP5nB7MvnmrS9DGitGOqS2NDICgmJKMyOkfPNalaJthdKkXOu7KgklZi7DogmQ5pQuCngxNabmlPQ809on%2BUEpm5TsvxQt9EuR5frrNChkLlLjq0v0B9czGh0Zl7WN5kuTB&X-Amz-Signature=b08aece95d2688b7183a1c6f292e871211474cb2997b95bb72533cee1be5ea38&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLBHC2U6%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIQC8wgEjOvteYOrIq%2BdaXeRVzz78AUAI3s6y%2FZqT2yzmvgIgKe8f1ALeT%2FyIiJ8822IpFSw%2Beg10PwAECzO4l%2BDewZwq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDKVLh267KpH317mFaSrcA6JWMxpvpcOcd%2B1OdGlT%2BB6s34C1jl6Z2Gm92oVq3kTqANkGTkHTw%2FpCc0RtezTpNEH5D%2BUIFkOM62lNwLQuhfgN%2Fy2ZgsWil4%2Fr%2BA0Im1d7TEaOK89HF9BAPxEoaANVwlylZt7MLW7ht08dUbZwc9YF0YmJibOu2%2BZcBhF1IKufQAoF2AQ92XMDLD0tDqnH7SUp2Kdbec0WxUWcqkaDPBTugKW8NN6M4gBOA9PKnLs8f46NJSVXJcwG%2FXh0ndlUYpyhnc1NHSB9rgoWv%2BMipgYKpczfqIcUEgVLK1flXkqBWdjqoL9kCSGcT1uWYCAIyJ2fWccQndUtIQ%2Fzy9%2BGANE5EGBC0ZB5mXboMmu2VQ4lhmBuA2JbSEA0WNQQc4hlEWlimKTIiiRzHSL4LHAgrS8a32uIwgHWz0FJ8uz5TYMYfL4OzlYri994qrOUNpCSXSco7Dl80x7193jGht5PL04gxrKXl8Bu7IjccYmjFeV5Guk33brj%2BVtB1MEBUuFduMB8Tlo0WwPKxxfw78E27BvyqYtoWVXmJgRgDz65Cl3CKGPCwneHbMpniuDRKhb0Ls8EDq4j8bW0RyQP3tH6LWFijmsXMvHoND3p23K%2B%2B9A3w%2Fr0JzCATfHcg6OIML2N88kGOqUB%2FhgTXb9fvJqMtsuzpWVdO%2FdVm5hF%2Beruc0dviIsxeF7RAOu1AlVl2dMqG43g18bXjobTXL2wYmJStW45yCvZ7nkgEkP5nB7MvnmrS9DGitGOqS2NDICgmJKMyOkfPNalaJthdKkXOu7KgklZi7DogmQ5pQuCngxNabmlPQ809on%2BUEpm5TsvxQt9EuR5frrNChkLlLjq0v0B9czGh0Zl7WN5kuTB&X-Amz-Signature=7480cdeef1ba9f80d16cb7d44309c89b2d7a2903373ea2670d550eae70e01eda&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







