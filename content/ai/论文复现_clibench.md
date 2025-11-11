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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QF6FU4Q2%2F20251111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251111T024441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIQCMx7kY57xgAsxvrUfsGiKwB1SCHv3xu7J8%2F5t8Hf7DFQIgMa298oLSxbrJH%2BK3yH2vU5%2BBY5XHSEp52CAO6ZPRtv8q%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDG0xVuHWeg1BB7YgwircA54coPHb0KHfRstEja%2FRfve77KYhkva0x1XQ%2BslJayPZYAxjH8p01C0KoQFd8ynoDvmoPRbUe02ywT7mMMMsCVQRaAlw2RuFYC31d4aNG5jGE9qDdWqxMYbB1umztlN6FVdR%2FkQeW1eo9xEt1D2wVIg8NPdZMaJyem%2FUYDQqALNClx2pJwELE%2F6vDmbolBMBY1UTX1NarIAPw0AY%2B3OuBC8KdsXkzfpLD05eptEI79haJk5CZJfXkwWq6Nvx6ZJmJcKENw0HZgC52%2BLlaAXTMZ8cuYjbQWrSCjEqRs7is1kygNP1bvOgIAHlQn0dOIPHcW50267PgjG4EofP%2FB7e1WwwT70g%2BMA2SvhEDbfWdnap%2BvIjtLJ%2BsMxu28JkRR1YJL1E1jfIHty0VpcpOAgNO8A5XO9QRaBGJ%2Bd%2B4N8xwnLOFPxao1bnhKEhi%2B%2B%2BSzp%2FGa1p8x41ocUGzi24ohPm%2FQ0sEXXHxh7ySL9LqUmPNlrAhwz97f3%2BjZ9TORiYSCzsZNvs1gdbDc7mgG9MC2HxJcCHhA%2F6vBGSnoEd4XW81e%2BTa%2BhtjzG%2Bk0Erb7MITVITx%2BGq3tGP0e%2FcZHcf%2BCzGtuuSH7QwtEhtAWpcQkdpTY6KmED28PrLx4AWe4FGMMe9ysgGOqUBx8jGq6fOElm6EpWnv%2FglljqimYSVYjsxWS%2BVt2LxbqC2Vbs9ypunWQbPbVkIlpwKDN4inNX%2FIPzHhWEVb1mnV8pMBd6jZ1JTl4d2qxs0T4UkigY9difDJvzCckqcDAXD34On7SXf%2BD3SwBj1cumS7A5j4WJbuqwBbcesZQCz%2F1iuwZLubZgqPTB5lhN7uRWOO%2BjuY4aRYCSSp3NGwSXyzJHV3y36&X-Amz-Signature=51b3564d086138cb3e8100519ae51a5d92247636681931f7c1d5a9df2474ff07&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QF6FU4Q2%2F20251111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251111T024441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIQCMx7kY57xgAsxvrUfsGiKwB1SCHv3xu7J8%2F5t8Hf7DFQIgMa298oLSxbrJH%2BK3yH2vU5%2BBY5XHSEp52CAO6ZPRtv8q%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDG0xVuHWeg1BB7YgwircA54coPHb0KHfRstEja%2FRfve77KYhkva0x1XQ%2BslJayPZYAxjH8p01C0KoQFd8ynoDvmoPRbUe02ywT7mMMMsCVQRaAlw2RuFYC31d4aNG5jGE9qDdWqxMYbB1umztlN6FVdR%2FkQeW1eo9xEt1D2wVIg8NPdZMaJyem%2FUYDQqALNClx2pJwELE%2F6vDmbolBMBY1UTX1NarIAPw0AY%2B3OuBC8KdsXkzfpLD05eptEI79haJk5CZJfXkwWq6Nvx6ZJmJcKENw0HZgC52%2BLlaAXTMZ8cuYjbQWrSCjEqRs7is1kygNP1bvOgIAHlQn0dOIPHcW50267PgjG4EofP%2FB7e1WwwT70g%2BMA2SvhEDbfWdnap%2BvIjtLJ%2BsMxu28JkRR1YJL1E1jfIHty0VpcpOAgNO8A5XO9QRaBGJ%2Bd%2B4N8xwnLOFPxao1bnhKEhi%2B%2B%2BSzp%2FGa1p8x41ocUGzi24ohPm%2FQ0sEXXHxh7ySL9LqUmPNlrAhwz97f3%2BjZ9TORiYSCzsZNvs1gdbDc7mgG9MC2HxJcCHhA%2F6vBGSnoEd4XW81e%2BTa%2BhtjzG%2Bk0Erb7MITVITx%2BGq3tGP0e%2FcZHcf%2BCzGtuuSH7QwtEhtAWpcQkdpTY6KmED28PrLx4AWe4FGMMe9ysgGOqUBx8jGq6fOElm6EpWnv%2FglljqimYSVYjsxWS%2BVt2LxbqC2Vbs9ypunWQbPbVkIlpwKDN4inNX%2FIPzHhWEVb1mnV8pMBd6jZ1JTl4d2qxs0T4UkigY9difDJvzCckqcDAXD34On7SXf%2BD3SwBj1cumS7A5j4WJbuqwBbcesZQCz%2F1iuwZLubZgqPTB5lhN7uRWOO%2BjuY4aRYCSSp3NGwSXyzJHV3y36&X-Amz-Signature=e08a9d8415152ec299a9f0ed947aa6c5ebed1729e5d128486fd81bf60de4b751&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







