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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QE7LEIPF%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031007Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIQC%2F81WPt1T8dBH7PI6MqGqLGYGUVYlGecSx7AudMFPOeAIgUlDaJ4fTjrVYSryNIOVUMtw%2BWuEDGiOI9gU7jwsL96kq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDHGsG5eWrj7ISN7sdircA9P1vKXUFhTcJgVYh1mLY2zMTzd5tFThnmE3PZgQiQ73TR9QdqsOeC0IgPNLWLoHvL3hMyyZoBnr4bZ%2BVAtappXX2kIOjfw6E497hY8fVOQFZ%2F60HayDPAsqBgi8SkQ3uEyVZm9%2BeWLxN7vRUi0tbtHvUbsTUYgK5yV4PX4V327kxg0S%2Bmr8QjC48U9oE3%2Fr3coT0UfLC7G7DqJ%2Fw5CiQTlbPdy5%2F53OdMC9Q9qCmJMZm8DrTvmbN7ZOBBWCsq32fA2b9lFsfotjHjcFMeWzAmHZHQ12ApyARnwlLSaciGe6GjSHc7voznM2oLYpgCXPZE4Xu3RjfaDq2aPnf6sro54ywsbzkdVx5HPooVIRR1jI9%2BsCNzMY4iSgXczKUVIZYUbIKyHeZ21yQ%2BHi1efNVxvAQNQJ313CkiCH6J1%2FZhnyg%2FPctMVLMJ7TIMf44zt54RcMEPduHZmTTh6%2FGK1DqSUrtnC0j4H06gybOpyNN4fnW4%2BgqOUyvhWkQVKPFvQPY9E0rQZUwgCX8V9zUVK3Pp%2F0S8tsE6tnhUiolN9TDxpp02bMMz%2FiNcRSd%2BOfYpqygWmwVVbip6g7lZYLf8taQfqnq30JCCZVTwrXsK2oYrZJ36EhFRhA0wqLr%2FH9MPaX5soGOqUBXfAYbZ7D55HFvRqaUWr5ZbeLeYMgjp0oAvHvWmgH%2B5mSYbGWq67xJXR7XcoIosl3M%2Bhj2SceyGUAYew2vd%2BqavtYp4DqOzrQ9Avi9oRxVizHSo4qcG9APDP9E8BE6vFMnjYTdN%2BJ2tkZiQXXOf2T0te3i5JqdZYx09vJoKZr42yslu1nN%2FiFuFFsx4q4F%2FcpLcw2BuKXZhRSxkjqnS62wZasktGH&X-Amz-Signature=1d9e2804d8ba85e85b86ddb2dc4b08f355f8f78c88e9ca659c8c480d9e7a77bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QE7LEIPF%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031007Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIQC%2F81WPt1T8dBH7PI6MqGqLGYGUVYlGecSx7AudMFPOeAIgUlDaJ4fTjrVYSryNIOVUMtw%2BWuEDGiOI9gU7jwsL96kq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDHGsG5eWrj7ISN7sdircA9P1vKXUFhTcJgVYh1mLY2zMTzd5tFThnmE3PZgQiQ73TR9QdqsOeC0IgPNLWLoHvL3hMyyZoBnr4bZ%2BVAtappXX2kIOjfw6E497hY8fVOQFZ%2F60HayDPAsqBgi8SkQ3uEyVZm9%2BeWLxN7vRUi0tbtHvUbsTUYgK5yV4PX4V327kxg0S%2Bmr8QjC48U9oE3%2Fr3coT0UfLC7G7DqJ%2Fw5CiQTlbPdy5%2F53OdMC9Q9qCmJMZm8DrTvmbN7ZOBBWCsq32fA2b9lFsfotjHjcFMeWzAmHZHQ12ApyARnwlLSaciGe6GjSHc7voznM2oLYpgCXPZE4Xu3RjfaDq2aPnf6sro54ywsbzkdVx5HPooVIRR1jI9%2BsCNzMY4iSgXczKUVIZYUbIKyHeZ21yQ%2BHi1efNVxvAQNQJ313CkiCH6J1%2FZhnyg%2FPctMVLMJ7TIMf44zt54RcMEPduHZmTTh6%2FGK1DqSUrtnC0j4H06gybOpyNN4fnW4%2BgqOUyvhWkQVKPFvQPY9E0rQZUwgCX8V9zUVK3Pp%2F0S8tsE6tnhUiolN9TDxpp02bMMz%2FiNcRSd%2BOfYpqygWmwVVbip6g7lZYLf8taQfqnq30JCCZVTwrXsK2oYrZJ36EhFRhA0wqLr%2FH9MPaX5soGOqUBXfAYbZ7D55HFvRqaUWr5ZbeLeYMgjp0oAvHvWmgH%2B5mSYbGWq67xJXR7XcoIosl3M%2Bhj2SceyGUAYew2vd%2BqavtYp4DqOzrQ9Avi9oRxVizHSo4qcG9APDP9E8BE6vFMnjYTdN%2BJ2tkZiQXXOf2T0te3i5JqdZYx09vJoKZr42yslu1nN%2FiFuFFsx4q4F%2FcpLcw2BuKXZhRSxkjqnS62wZasktGH&X-Amz-Signature=65582ed2bb5d94a7d561f4fe256d5421ccb01e6b42ce3740158ea7e1f623f5e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







