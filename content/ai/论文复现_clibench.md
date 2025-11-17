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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZ4F4HKJ%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsdzEZEFS3IdQ%2ByWwEJvCiAAD554LfvrduOf6SDRiWfAIgLRbK4%2BxqHUxFjTTVdT7K3Rr%2BWMNNzWC9RNEBxcew0x4qiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGGPce%2FeK7WvyTHpiyrcA%2B8emZvQ%2BPjS6WtNH4LnobkGulrDGPHRBSS%2FFPIyVcGjC68qkwrQiD08sxF%2BUDylxtlEUSrgsAKLhPuSRVh4bdtAOw0sjaOgMPIQc9g1Mi1xPcrgBtUpeG%2BHAmL1Aqx2xiM2S2N8I0XPB8A9N9sUhMtugoQC3aUtsrTx0SCuLKHaYdpLw282L6yf5AdIWcReDQOckGarrr7IBWBut1svAvWnqZ6%2Fv%2FTxEe7pn9Ksapik2%2FaJCYtNxh4JOleBAwL792pzF2KfJzQGvLzp7%2FsUycUJ1Ixsz5i1n9Bzs%2BIg1ZXjGHhiLo1Racn%2Bc2PtCI3QaFUnEK0qlg2vCfxEgPROgNVHoYbfoo9fwBm17vRYPIVaVmIEbyWQAR%2B75Xvd39f7NGLb9qn8zGhE52094UK2F%2Bnta%2Fj8nOTqAnCjRzH8gu%2BA3JRL47jjSVLZHggcOIdAg5bBBFBUhzu874tFksfDCHG%2FtPyunjl0TCxY70xjcConLsfh9LPf4Q2qsTCYzwZ8jzRoYWglx0T7HFqHtFvFHQ4KET88U9jwLwwKKhISK3C8vzWwvgaqthalw1sLD8J6rS3bjxF86GEYW5WMxAhxp7DuwXDmJVY7Vwt5I0ajK0dNONEqSyPiYCb5aAPrMLaH6sgGOqUBeQYKF4VCheexGugDY1hxex%2BM3KdxVBdnuttwxBfm7dp%2BogcNnMVG6Tid9LKRE29r2TRr4WNjB8nOUhgbz2rAoi80w%2FLP%2FBkLMcWCtxwJBkFl6SSBH2I4WhZ3w3Sblks4yWwRANHcogtkE1jBp%2BT4D%2FwcnNf0Px96bhP%2FB2i3oPgUc74prTOYqudyGZcykeXns899o4Mg8zc9cEr%2Btm6VNl1f9zcD&X-Amz-Signature=04137be0e24b5405857b85f1bb2f87682a6738af4a690d21edae380e081df533&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZ4F4HKJ%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsdzEZEFS3IdQ%2ByWwEJvCiAAD554LfvrduOf6SDRiWfAIgLRbK4%2BxqHUxFjTTVdT7K3Rr%2BWMNNzWC9RNEBxcew0x4qiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGGPce%2FeK7WvyTHpiyrcA%2B8emZvQ%2BPjS6WtNH4LnobkGulrDGPHRBSS%2FFPIyVcGjC68qkwrQiD08sxF%2BUDylxtlEUSrgsAKLhPuSRVh4bdtAOw0sjaOgMPIQc9g1Mi1xPcrgBtUpeG%2BHAmL1Aqx2xiM2S2N8I0XPB8A9N9sUhMtugoQC3aUtsrTx0SCuLKHaYdpLw282L6yf5AdIWcReDQOckGarrr7IBWBut1svAvWnqZ6%2Fv%2FTxEe7pn9Ksapik2%2FaJCYtNxh4JOleBAwL792pzF2KfJzQGvLzp7%2FsUycUJ1Ixsz5i1n9Bzs%2BIg1ZXjGHhiLo1Racn%2Bc2PtCI3QaFUnEK0qlg2vCfxEgPROgNVHoYbfoo9fwBm17vRYPIVaVmIEbyWQAR%2B75Xvd39f7NGLb9qn8zGhE52094UK2F%2Bnta%2Fj8nOTqAnCjRzH8gu%2BA3JRL47jjSVLZHggcOIdAg5bBBFBUhzu874tFksfDCHG%2FtPyunjl0TCxY70xjcConLsfh9LPf4Q2qsTCYzwZ8jzRoYWglx0T7HFqHtFvFHQ4KET88U9jwLwwKKhISK3C8vzWwvgaqthalw1sLD8J6rS3bjxF86GEYW5WMxAhxp7DuwXDmJVY7Vwt5I0ajK0dNONEqSyPiYCb5aAPrMLaH6sgGOqUBeQYKF4VCheexGugDY1hxex%2BM3KdxVBdnuttwxBfm7dp%2BogcNnMVG6Tid9LKRE29r2TRr4WNjB8nOUhgbz2rAoi80w%2FLP%2FBkLMcWCtxwJBkFl6SSBH2I4WhZ3w3Sblks4yWwRANHcogtkE1jBp%2BT4D%2FwcnNf0Px96bhP%2FB2i3oPgUc74prTOYqudyGZcykeXns899o4Mg8zc9cEr%2Btm6VNl1f9zcD&X-Amz-Signature=ccf30c36cc91f9f5bc0c23a043613eedf2e0cb2bc840f87467feca98dfc6e107&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







