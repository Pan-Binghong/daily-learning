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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSX5JIQ6%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICCSaBolgIECCYWzdxAeYm%2FUPkSYBKwe%2BaXip%2B3I4Yk%2BAiBwJqOuVwlLQbHGzb%2BSVmJ0SgqRsUQgqBHjvccbB3aHLir%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIM0j5WmghE7%2F53WiYcKtwDOdk4jZwXxKWHyqlEjUOoGP3y2WqUXvJ00eGVM2pWORoEIfqMFqdRBOh4Jr4AhSl6QiE4mw0DVxscQa%2BZ6bAn0VsHusNftkP0I0TPBz8upl8W3G99vjb0dO89wVZOoLQwb4NhFVKmkB4%2FLWCta7ku8ZQi6bPBC81koKZAVLU%2BOB%2FEr28%2FpdiGxniDy5O5is5UZjYsT%2ByHmvwhiTNi0hW3c1W1LfQKmpW1xQZnIfqrUNeEquUlY%2Befd3DH8Cb4PNAolzngERJSsWvqj9gSewyLfejvSulmWc8PuZsVJOHiUEm6x2Pwsl7FsMeB2We1NAqB2h83BFfaGb0B8DFKfCcZyckLhi9hvti18Oc8fHtKJchFgXRuLve6a5nhzwaUzyKtY4ehb%2BAluc%2FNlnN1rw0vHK3J4DjRB4orOtPlr6334VGDeVkmpud79gMd70uBRO1G%2FcyGAuUq4K7KLaRyUgRr0B01e97i8YunD9RkdM01FT8piEb4CyWrV7q%2B43K1iD78DxTLiKSHvJDMKi6AGBNQi9PUy5atS4S7wSRy0G0qY%2FbQnt0WuG9gbge3muJsNDJP2veqA2P2CqO4WSgkVMbe9Gmq8nfvEYv1PTUTQc4H7aaCK7F7UWBHDOpDsHEw%2Ba69zgY6pgGKGo5mEbc3IZ1T3EL4GRl5cdkRCCHCSoxD7%2FtHFIVqDJnT4tPqUMys3w2p8IUhSpAcajZulEATL3nmS75X1SA535%2FQP%2BNixJpeY34hC2Tu7WDIE3eFawlcPPUJl9TBMrNaoVnpL1nRb4RTb%2BQmF7jySoScvYeLRTUAFoCav6fFMlnBVKfnfh%2BlRLgrUO%2FD9hdIOpsLOZMdwWLNodK4DtSr4A7MvNtK&X-Amz-Signature=b755065579fe0bc2bf09355031d6580dad3626ce88ff6dee9828a9f618868552&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSX5JIQ6%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICCSaBolgIECCYWzdxAeYm%2FUPkSYBKwe%2BaXip%2B3I4Yk%2BAiBwJqOuVwlLQbHGzb%2BSVmJ0SgqRsUQgqBHjvccbB3aHLir%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIM0j5WmghE7%2F53WiYcKtwDOdk4jZwXxKWHyqlEjUOoGP3y2WqUXvJ00eGVM2pWORoEIfqMFqdRBOh4Jr4AhSl6QiE4mw0DVxscQa%2BZ6bAn0VsHusNftkP0I0TPBz8upl8W3G99vjb0dO89wVZOoLQwb4NhFVKmkB4%2FLWCta7ku8ZQi6bPBC81koKZAVLU%2BOB%2FEr28%2FpdiGxniDy5O5is5UZjYsT%2ByHmvwhiTNi0hW3c1W1LfQKmpW1xQZnIfqrUNeEquUlY%2Befd3DH8Cb4PNAolzngERJSsWvqj9gSewyLfejvSulmWc8PuZsVJOHiUEm6x2Pwsl7FsMeB2We1NAqB2h83BFfaGb0B8DFKfCcZyckLhi9hvti18Oc8fHtKJchFgXRuLve6a5nhzwaUzyKtY4ehb%2BAluc%2FNlnN1rw0vHK3J4DjRB4orOtPlr6334VGDeVkmpud79gMd70uBRO1G%2FcyGAuUq4K7KLaRyUgRr0B01e97i8YunD9RkdM01FT8piEb4CyWrV7q%2B43K1iD78DxTLiKSHvJDMKi6AGBNQi9PUy5atS4S7wSRy0G0qY%2FbQnt0WuG9gbge3muJsNDJP2veqA2P2CqO4WSgkVMbe9Gmq8nfvEYv1PTUTQc4H7aaCK7F7UWBHDOpDsHEw%2Ba69zgY6pgGKGo5mEbc3IZ1T3EL4GRl5cdkRCCHCSoxD7%2FtHFIVqDJnT4tPqUMys3w2p8IUhSpAcajZulEATL3nmS75X1SA535%2FQP%2BNixJpeY34hC2Tu7WDIE3eFawlcPPUJl9TBMrNaoVnpL1nRb4RTb%2BQmF7jySoScvYeLRTUAFoCav6fFMlnBVKfnfh%2BlRLgrUO%2FD9hdIOpsLOZMdwWLNodK4DtSr4A7MvNtK&X-Amz-Signature=9d030c0cfbe1cab0c1e4be971be0e8576967ab1aadb8ce0ebe35b5eff0b91c6a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







