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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623ZHY2IA%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCIERT9bamkfJaxb1pVL99plwb73YidJqzKTW0NHQhaKe0AiEArNitvrr2Sei5xnl4kUUbwK01Hq%2FaJU5xaN3X9mPdadYqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLLjmrD14TO9AnHbgCrcAws13Uq1cUAzGfeRcFYcE7dqb9tis7KFyJPjpqw2h81Ihv0qpsTTqXrbM0GbtNKn2lsx4vNGQprWYD7%2BpoAlSwvPGd5kkeog%2BmF15PTW7UTltbMiHOfwk21J2ElwcXzd2j0mtBcNT1FVW%2FARFmXgAhGexr9cUHHGsd%2FfO8AYv53s7EfiPaLmWvpcO5GP4K1bfmO0X%2Fohqla2bYUrVsV9DwNpPuLr3aO1F%2F0gvaIKEP2iPAeDAzgEr%2FSNtuipjmc0Hpvu40VM9b3%2FTZ09R4vAy%2FjSrO9MsUQNPaiFogf0qEwVfv1h6cwPyqtC%2F96l2N%2FNT%2FbWD1vTZuDg8Qy4HVOgUnRrpeadzcFmTRLYVyW2AhnN1KdJ31nDnEGifQX%2BuOYK5xZHU1FzbTT7qh7OFKTkD%2FCs2IxokUiQkvagkdkS8TgKsDY7UEU%2B7XI4tqXaCOii9Qqm%2BPh9DBaSIdJf2XhrMFTcdqkE4Scqwamt%2BLDwdKgOG%2FwyYt0BMPKVGMHxtzIoz7tf2ZTNlXP%2FM8ES2jDqYUnxemknOFx9e68D9YV8mGDJLGhvPIYzmgXjJCqRO4f31B0%2FHwGmo4qnDFi%2BzMMzgHUZZul3CojG51R0VyqvJGJXuBDrX09052GRLl4RMOjYhcwGOqUB0Zd%2FH3yPnET0uUVFJsWoWTCEhkGYMSDMHLo2CltMdQ0hGPHt8%2F7yNLruX%2BosasLMkuxMiHyHg4eahSDylf88iRD5HW1Jc%2B6QFEhCHZXF8RRycIw3IXho3Ev%2BdM%2F0ZsaITRmWsiXQ%2F1BlaxE6kg8E5QklXNf202BmOOwyDMkVxstqDKL10IOlwwPEtLBJEdpwnkPLRh3l3g4Virm16PUv3fZzxxKq&X-Amz-Signature=b4e7dd63530d833505dada16f85bbc849c1b61740300fd7cb4752e3610d9b0eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623ZHY2IA%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCIERT9bamkfJaxb1pVL99plwb73YidJqzKTW0NHQhaKe0AiEArNitvrr2Sei5xnl4kUUbwK01Hq%2FaJU5xaN3X9mPdadYqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLLjmrD14TO9AnHbgCrcAws13Uq1cUAzGfeRcFYcE7dqb9tis7KFyJPjpqw2h81Ihv0qpsTTqXrbM0GbtNKn2lsx4vNGQprWYD7%2BpoAlSwvPGd5kkeog%2BmF15PTW7UTltbMiHOfwk21J2ElwcXzd2j0mtBcNT1FVW%2FARFmXgAhGexr9cUHHGsd%2FfO8AYv53s7EfiPaLmWvpcO5GP4K1bfmO0X%2Fohqla2bYUrVsV9DwNpPuLr3aO1F%2F0gvaIKEP2iPAeDAzgEr%2FSNtuipjmc0Hpvu40VM9b3%2FTZ09R4vAy%2FjSrO9MsUQNPaiFogf0qEwVfv1h6cwPyqtC%2F96l2N%2FNT%2FbWD1vTZuDg8Qy4HVOgUnRrpeadzcFmTRLYVyW2AhnN1KdJ31nDnEGifQX%2BuOYK5xZHU1FzbTT7qh7OFKTkD%2FCs2IxokUiQkvagkdkS8TgKsDY7UEU%2B7XI4tqXaCOii9Qqm%2BPh9DBaSIdJf2XhrMFTcdqkE4Scqwamt%2BLDwdKgOG%2FwyYt0BMPKVGMHxtzIoz7tf2ZTNlXP%2FM8ES2jDqYUnxemknOFx9e68D9YV8mGDJLGhvPIYzmgXjJCqRO4f31B0%2FHwGmo4qnDFi%2BzMMzgHUZZul3CojG51R0VyqvJGJXuBDrX09052GRLl4RMOjYhcwGOqUB0Zd%2FH3yPnET0uUVFJsWoWTCEhkGYMSDMHLo2CltMdQ0hGPHt8%2F7yNLruX%2BosasLMkuxMiHyHg4eahSDylf88iRD5HW1Jc%2B6QFEhCHZXF8RRycIw3IXho3Ev%2BdM%2F0ZsaITRmWsiXQ%2F1BlaxE6kg8E5QklXNf202BmOOwyDMkVxstqDKL10IOlwwPEtLBJEdpwnkPLRh3l3g4Virm16PUv3fZzxxKq&X-Amz-Signature=9eedbdf59178ebf4cf5ca0f0babdf7b853180674f23789118d8197b1d66260df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







