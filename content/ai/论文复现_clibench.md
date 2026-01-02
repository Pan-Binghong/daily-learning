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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FAZ6GWS%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T025954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIDHXWm38CMBdodYbqWjU%2BBemmToxS3L37SLteV8P8%2F0%2FAiBtAv2%2F%2Fad8erS7yknhRvc9EgHdU1CXqQ1Uz30tcejRjSqIBAjy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcbN7hm1I7O4ksZUCKtwDKEWN9YhHPuezwcOH6oKxj0jdj3Be7IKfjena7myA1W5PXf2hAJPd0KU84mn0RHA3YsP2EyeTnfGfWDUKp0za66zp4Oc%2FLlYQiU76pBc5T%2FHkL0cN60dg5PQfrELu8dbHkKs1YmOCuzmxhq1XuttFk2XVxGKJPi9nEy3CGtzHzeuVO8JPqFJQ43FvFqhBBF%2F5ZGUwFKtt1ay2jfpqXScStNYUVF0GykmFMfSDE1lgs3yEzWumoMQF9%2Fc1mXDc6t72gtIyjhC7w57lgq6%2BkmPAVPY%2BcfjGKIZPmcK%2BgF53xB0osKmoQySv9%2FnxEQfSqz78bnxB0HEfrGOcYKIV42F1kmVrTXWuUmAqaCG87ySvwB7X2ydeaLeOnXWeOW1nYc%2FNmaGcaN3GVQhL2UcLqc1%2FmnOCwP%2BsCy8XRXvXe%2B0iTu40RQa0%2BU0SAKT1SiWmKtWoGxGzJdjdx5%2FtoZFoSVCRlPyb9fKUhicNB308tBGFtrdNq5csKHkBABQb2oh4ZpZHbUM3dJH2KJ%2FQT4vFbaZ3Ely46vxsqD%2F9RrHALbg5uh6y3V4ORVGh2VH6BA%2BjM2S453V8yOVbwj4XDCMeSlO%2Bhz9Hw6fEuavEONBMA6Du57CyvljwdoJb1VGTc%2BUwx73cygY6pgErM38ojujI7LzFNPpAGEBZfu9zlLpODYC0am4ljlIO9QeeAQc49i0VTMcaT4BaraB6K8u8GjyRtLzYpMSAVPZgFFu9AgEMc1wnpfABQW%2BgH3cpAG4GvILXuZUC5tkdNJ%2BCotEKDZrTthubpz3jBtEuNe4EtUFHJehJT%2FRvDwx2T7dCrgvME2SzVRguVTWTwox%2BxjQvejESxaDlXWYzSsiTcx5qVkqw&X-Amz-Signature=8f1fbb5bbee29aa062a9437d93ab233f85655781ce7d18d22b3fca19945f13a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664FAZ6GWS%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T025954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIDHXWm38CMBdodYbqWjU%2BBemmToxS3L37SLteV8P8%2F0%2FAiBtAv2%2F%2Fad8erS7yknhRvc9EgHdU1CXqQ1Uz30tcejRjSqIBAjy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcbN7hm1I7O4ksZUCKtwDKEWN9YhHPuezwcOH6oKxj0jdj3Be7IKfjena7myA1W5PXf2hAJPd0KU84mn0RHA3YsP2EyeTnfGfWDUKp0za66zp4Oc%2FLlYQiU76pBc5T%2FHkL0cN60dg5PQfrELu8dbHkKs1YmOCuzmxhq1XuttFk2XVxGKJPi9nEy3CGtzHzeuVO8JPqFJQ43FvFqhBBF%2F5ZGUwFKtt1ay2jfpqXScStNYUVF0GykmFMfSDE1lgs3yEzWumoMQF9%2Fc1mXDc6t72gtIyjhC7w57lgq6%2BkmPAVPY%2BcfjGKIZPmcK%2BgF53xB0osKmoQySv9%2FnxEQfSqz78bnxB0HEfrGOcYKIV42F1kmVrTXWuUmAqaCG87ySvwB7X2ydeaLeOnXWeOW1nYc%2FNmaGcaN3GVQhL2UcLqc1%2FmnOCwP%2BsCy8XRXvXe%2B0iTu40RQa0%2BU0SAKT1SiWmKtWoGxGzJdjdx5%2FtoZFoSVCRlPyb9fKUhicNB308tBGFtrdNq5csKHkBABQb2oh4ZpZHbUM3dJH2KJ%2FQT4vFbaZ3Ely46vxsqD%2F9RrHALbg5uh6y3V4ORVGh2VH6BA%2BjM2S453V8yOVbwj4XDCMeSlO%2Bhz9Hw6fEuavEONBMA6Du57CyvljwdoJb1VGTc%2BUwx73cygY6pgErM38ojujI7LzFNPpAGEBZfu9zlLpODYC0am4ljlIO9QeeAQc49i0VTMcaT4BaraB6K8u8GjyRtLzYpMSAVPZgFFu9AgEMc1wnpfABQW%2BgH3cpAG4GvILXuZUC5tkdNJ%2BCotEKDZrTthubpz3jBtEuNe4EtUFHJehJT%2FRvDwx2T7dCrgvME2SzVRguVTWTwox%2BxjQvejESxaDlXWYzSsiTcx5qVkqw&X-Amz-Signature=a969eee0cbc9b78bed83f682fa2d68a50bd87cf76bdb807f33844d2916b40739&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







