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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVDVQNTF%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T034916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCOYdlpT3Rx68o7PhpPuCvuy8OKuYp%2FVtsATvkOgie2BwIgd7R%2Byr3gFMeQTrCn1kmSBMJSMYS0t5aTExCInySbcpoqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBL0c2Mx6waCodIrRircA0fhnoqmsnGy1yJadr%2BYjhFDOJ0QhE5KVIoiq8LC1gyPPrOFsoxdSk1Ll3v1S%2FaJGoDP8eVsEACGnZMeaCZ2HI8FcOfPDcqz5EeEJF0K8%2Byp0fRx7xk%2Fh2xxNcTuLy%2B2vNtr8TDOIJXXq01vNJVZyOSnLtUcjEPlRba0KTGAgEZ5D4iZJ2pV6bdzwTvP7URaEEdorKyzB9jSoOb7gDrpBNUh3ZNYfioDerqMEIrgQST8Nar3TefYCbG2J8BM3bMR%2BUgjF48sLwOESfxzZtBRYNMSg%2BdM2z64EnPyMJX6xHmpAdfRK066dMOToX430QqDS7G0WlIUBLdFF%2FZ4z%2BicAQamu14MGYL38sBmodYCRhtrhgl1eUOPxqN51FC42%2FjWrbP4FQS6KCuUxxwc1UQWiPJEBNf6XLUgUqtBly5YpPZoS%2Bkjdnh6yqzFs48xQ0Naar3KWcHGBpz94BtDSqyCyrFj2xpzWfPFbcu75PP1vY%2BYM0okjO7nNraw57dc6vbL9FCv68XaCXkrdoDz6BCAaK6dsR6WBQnT1GZKtrftgcGpXO4rmQVSBGG9DNdRtN7MXybTpiShdFT6yP6SJrBQdlDlFvOPOSe0xhVZZLWe%2F%2FvEggFez7x2Pfazjao%2FMKTLr8wGOqUBmBZeX8SvMHNJCizkjqOyfT8zCy8oqw5b18aXajaGPhFtcUiiQ0WkQIREtAv17uSGjoLrF3oJdiUR2jOLiY8SWwUrlSyKgXJGeX8HYOJPvhtbQchHUBNbyyiLgs%2Fd%2B7jwEC%2BvwRrtAaoxlmdCs8UeDBEeTl5vW%2BWcqKOeTCk1KlWjgJ46HYsYHQa%2F92L7urFajX6UdvcaZtO7mSZRGhkV%2B02wdHJt&X-Amz-Signature=da5a672a584112f39529aa2167ee709e25ba59cc43013613ffdea6dbd6ae9f06&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVDVQNTF%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T034916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCOYdlpT3Rx68o7PhpPuCvuy8OKuYp%2FVtsATvkOgie2BwIgd7R%2Byr3gFMeQTrCn1kmSBMJSMYS0t5aTExCInySbcpoqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBL0c2Mx6waCodIrRircA0fhnoqmsnGy1yJadr%2BYjhFDOJ0QhE5KVIoiq8LC1gyPPrOFsoxdSk1Ll3v1S%2FaJGoDP8eVsEACGnZMeaCZ2HI8FcOfPDcqz5EeEJF0K8%2Byp0fRx7xk%2Fh2xxNcTuLy%2B2vNtr8TDOIJXXq01vNJVZyOSnLtUcjEPlRba0KTGAgEZ5D4iZJ2pV6bdzwTvP7URaEEdorKyzB9jSoOb7gDrpBNUh3ZNYfioDerqMEIrgQST8Nar3TefYCbG2J8BM3bMR%2BUgjF48sLwOESfxzZtBRYNMSg%2BdM2z64EnPyMJX6xHmpAdfRK066dMOToX430QqDS7G0WlIUBLdFF%2FZ4z%2BicAQamu14MGYL38sBmodYCRhtrhgl1eUOPxqN51FC42%2FjWrbP4FQS6KCuUxxwc1UQWiPJEBNf6XLUgUqtBly5YpPZoS%2Bkjdnh6yqzFs48xQ0Naar3KWcHGBpz94BtDSqyCyrFj2xpzWfPFbcu75PP1vY%2BYM0okjO7nNraw57dc6vbL9FCv68XaCXkrdoDz6BCAaK6dsR6WBQnT1GZKtrftgcGpXO4rmQVSBGG9DNdRtN7MXybTpiShdFT6yP6SJrBQdlDlFvOPOSe0xhVZZLWe%2F%2FvEggFez7x2Pfazjao%2FMKTLr8wGOqUBmBZeX8SvMHNJCizkjqOyfT8zCy8oqw5b18aXajaGPhFtcUiiQ0WkQIREtAv17uSGjoLrF3oJdiUR2jOLiY8SWwUrlSyKgXJGeX8HYOJPvhtbQchHUBNbyyiLgs%2Fd%2B7jwEC%2BvwRrtAaoxlmdCs8UeDBEeTl5vW%2BWcqKOeTCk1KlWjgJ46HYsYHQa%2F92L7urFajX6UdvcaZtO7mSZRGhkV%2B02wdHJt&X-Amz-Signature=088036b9336d54e770393291ee8cc55677ba2d30902526b4997c0f2b5041ff7f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







