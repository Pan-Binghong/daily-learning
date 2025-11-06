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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLJCKMSB%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDST7o9R06HtJ1ZoB%2BHmqMgMKt8%2Bvy3qD8kTp%2FJRhPqIAiEAwLh1dDZhqffHQAhyFDstrJHksFDzzY%2BfP2jcp0YkTXMqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP8gobuWqekeWU059CrcA5WDb9W8b8%2BJY8B%2BCT1mswliDF4Tg6nxwMS7VTWdXHBX%2BUddNTToQoyakqYl4wpE3t10bF8D2X9T6nCY4Nx430TOCCoa0Axp9ypXpwMGDGp4IVo%2B10eIgkbRO%2FahLT1Iy6dxoGPsTvQMOFDejLefMc8mVr22jedl4hjDpJub%2B0DRH99zKjyzWimAN4ezSInf%2B%2F%2Bp5YwyLUlah9PxlIxmMSrUKD34v0MO1%2BPxcf5%2Bd0ulUVLk5DkBQA2%2BNsTJaENrmcKWAGSC3nFJGQnVNTV0G5aNqtaZD3%2F6%2BqVC602Ll0YJsTjMJwljfKP%2Bqg2v1owJ%2BDHto9i5l58CSLtapMjAPdB9lJf1WyQ5agXDrNgWr%2FNHVBMEhuZZ2WWX83eN%2BXg8%2FvDJx0UlT8EBhCwd33PTqbtX%2FKLPa%2FXu7D24ZVSl8PGRAMF%2F9sXCBrrfUs41jJQUrYdZtxNxddTX8HIw6z59Nc1MSoe0wlp40m25j%2BIHnIHWmDYY5onSthw2EOgtNuJ2EMdDy6gAM9LK1s%2F7adxr9JCxa4C%2BCubO%2FfhsIlY1uFEo%2B9k2W1yNO08lH%2FgmDJiK5Hy9tCvRA3i%2Bo54JS4YoW3qHwbZzQlDlIOPvL8UpvZGHEZMkuQfm2W1XvWJWMJTxr8gGOqUBEXA23bj9cQYNmwp86hDhTDdtSs6zT6DF2hF9oRsTcoggDpct%2BVNJtUuP%2FfaCUKL5sYTDLoS4SYmjCUUzHd7QoV67lr0k%2FK65gcOWApY3TWEyh13RNVAE%2BArd6pqNEwUt%2BqBAVX6A%2B%2BoHo9UE5fjNV%2FwnlUSavNEgyFXHc5kOAFOUh28yA4p21XZvlf7%2Bb6d8oFG7ZYgeULSrz7azOIdoS9tbbBmF&X-Amz-Signature=580d2e84247a6495034817f55726fe4792a85431324b7d1c8292ae1329684f89&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLJCKMSB%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDST7o9R06HtJ1ZoB%2BHmqMgMKt8%2Bvy3qD8kTp%2FJRhPqIAiEAwLh1dDZhqffHQAhyFDstrJHksFDzzY%2BfP2jcp0YkTXMqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP8gobuWqekeWU059CrcA5WDb9W8b8%2BJY8B%2BCT1mswliDF4Tg6nxwMS7VTWdXHBX%2BUddNTToQoyakqYl4wpE3t10bF8D2X9T6nCY4Nx430TOCCoa0Axp9ypXpwMGDGp4IVo%2B10eIgkbRO%2FahLT1Iy6dxoGPsTvQMOFDejLefMc8mVr22jedl4hjDpJub%2B0DRH99zKjyzWimAN4ezSInf%2B%2F%2Bp5YwyLUlah9PxlIxmMSrUKD34v0MO1%2BPxcf5%2Bd0ulUVLk5DkBQA2%2BNsTJaENrmcKWAGSC3nFJGQnVNTV0G5aNqtaZD3%2F6%2BqVC602Ll0YJsTjMJwljfKP%2Bqg2v1owJ%2BDHto9i5l58CSLtapMjAPdB9lJf1WyQ5agXDrNgWr%2FNHVBMEhuZZ2WWX83eN%2BXg8%2FvDJx0UlT8EBhCwd33PTqbtX%2FKLPa%2FXu7D24ZVSl8PGRAMF%2F9sXCBrrfUs41jJQUrYdZtxNxddTX8HIw6z59Nc1MSoe0wlp40m25j%2BIHnIHWmDYY5onSthw2EOgtNuJ2EMdDy6gAM9LK1s%2F7adxr9JCxa4C%2BCubO%2FfhsIlY1uFEo%2B9k2W1yNO08lH%2FgmDJiK5Hy9tCvRA3i%2Bo54JS4YoW3qHwbZzQlDlIOPvL8UpvZGHEZMkuQfm2W1XvWJWMJTxr8gGOqUBEXA23bj9cQYNmwp86hDhTDdtSs6zT6DF2hF9oRsTcoggDpct%2BVNJtUuP%2FfaCUKL5sYTDLoS4SYmjCUUzHd7QoV67lr0k%2FK65gcOWApY3TWEyh13RNVAE%2BArd6pqNEwUt%2BqBAVX6A%2B%2BoHo9UE5fjNV%2FwnlUSavNEgyFXHc5kOAFOUh28yA4p21XZvlf7%2Bb6d8oFG7ZYgeULSrz7azOIdoS9tbbBmF&X-Amz-Signature=dd49bba9baf9ae21d23454d7e1915c58fb406eafa7cbc9fe8e53a5fb6d3ae9d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







