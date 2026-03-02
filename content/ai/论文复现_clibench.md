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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCDEJ5HC%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033158Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHg%2FHonyte8KF3cwQJgC7qpkfz%2BSfuXD3QKPSva4F4vhAiEA3qo8c3RsznNPZKb1obz1PgZHigtv201mCGsedEsvoQ0q%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDP23al6yqhSv2x%2FcWCrcA1SHkOchW7E7BMLFvmj6Fvncw6%2B%2FXoq0xPHp8Pb8OaCt5YMSI3igDusSH%2BPgNz9bdtiGBwjz93y%2FhkB55IcCVTLEXKGtJ8bsDfCgECijrHnBqSIWKtq5f8sAhqlTy5%2BGE9nWOQQtHVGRNqUW7oQiZ%2BdwhmbxLXcLD0iD%2B4zjXyHViEe51xX4Y6lav%2FsztsJbrMfTor9FoAIYB9DeGctaPhyabVkbh%2FeM653E0N6Js8ildaPK%2Fw2ozfuyeh3zJtjRI9ZtJ8ZyTPzRqGfdzvx06ygSI8nwyaId1vOXEsVhM0T0Fv34TaWvlDT6ntcsHGDPJyAZjx0A1fQgZHFvsze8jC3Ef4bFFXLftSzUlPj0ec5T9leGB2e25mWCWmX3xQEYFAnzV6NlIONz1hFsDhxVmRzVxdHaNt%2FVr1iyb5yonhDIZtVFskzycXsCx4PdQNoUez96kpHqmyocy8gXZ8YZwi1ZyIKFqVAui0uwaBEUt9HJcToGJcv6hpn%2FlhT04%2BoCGPqKXeBvpzEXpO9oFBhrzj5f9PnhuPZmRatekbiywenrJ6s6r401l2bjLm2tycarMeZ5C9s9VNPv%2B%2B7qsATeLrmnzbTlaM4txJ0LMG9gDEm%2BjJHJAw65hUOBR1h2MIb%2Bk80GOqUBam1O9gA9NY4CwG8go54Rrht0vYW6zNQEruNdPfgdWqLW3htq4%2BUKHeCh%2BC8U9ScOXBLk2Nd7a%2BrJ55i8GNsyHq%2FFBHMQtHam4wSrXvQy8iGp27hiWN79kpDpSVKtBsas2y%2FXQY0xEkrUQXDj%2BeoZVcuZYtlCklXMY5%2FR0%2FCwfSU8wpP2FxFGnzSsxy6iDZXjH%2FQE2veskYG1EtIe5kEf2gdl5VRG&X-Amz-Signature=ec8ac4a686ddfecbc835206c28afad4dfb6f29d2392d3212b981ff18c5fc30db&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCDEJ5HC%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033158Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHg%2FHonyte8KF3cwQJgC7qpkfz%2BSfuXD3QKPSva4F4vhAiEA3qo8c3RsznNPZKb1obz1PgZHigtv201mCGsedEsvoQ0q%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDP23al6yqhSv2x%2FcWCrcA1SHkOchW7E7BMLFvmj6Fvncw6%2B%2FXoq0xPHp8Pb8OaCt5YMSI3igDusSH%2BPgNz9bdtiGBwjz93y%2FhkB55IcCVTLEXKGtJ8bsDfCgECijrHnBqSIWKtq5f8sAhqlTy5%2BGE9nWOQQtHVGRNqUW7oQiZ%2BdwhmbxLXcLD0iD%2B4zjXyHViEe51xX4Y6lav%2FsztsJbrMfTor9FoAIYB9DeGctaPhyabVkbh%2FeM653E0N6Js8ildaPK%2Fw2ozfuyeh3zJtjRI9ZtJ8ZyTPzRqGfdzvx06ygSI8nwyaId1vOXEsVhM0T0Fv34TaWvlDT6ntcsHGDPJyAZjx0A1fQgZHFvsze8jC3Ef4bFFXLftSzUlPj0ec5T9leGB2e25mWCWmX3xQEYFAnzV6NlIONz1hFsDhxVmRzVxdHaNt%2FVr1iyb5yonhDIZtVFskzycXsCx4PdQNoUez96kpHqmyocy8gXZ8YZwi1ZyIKFqVAui0uwaBEUt9HJcToGJcv6hpn%2FlhT04%2BoCGPqKXeBvpzEXpO9oFBhrzj5f9PnhuPZmRatekbiywenrJ6s6r401l2bjLm2tycarMeZ5C9s9VNPv%2B%2B7qsATeLrmnzbTlaM4txJ0LMG9gDEm%2BjJHJAw65hUOBR1h2MIb%2Bk80GOqUBam1O9gA9NY4CwG8go54Rrht0vYW6zNQEruNdPfgdWqLW3htq4%2BUKHeCh%2BC8U9ScOXBLk2Nd7a%2BrJ55i8GNsyHq%2FFBHMQtHam4wSrXvQy8iGp27hiWN79kpDpSVKtBsas2y%2FXQY0xEkrUQXDj%2BeoZVcuZYtlCklXMY5%2FR0%2FCwfSU8wpP2FxFGnzSsxy6iDZXjH%2FQE2veskYG1EtIe5kEf2gdl5VRG&X-Amz-Signature=9f73d7d0c7a556f3a801985cc008b7550a177b70e787b9ce2793a54c71d0e33d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







