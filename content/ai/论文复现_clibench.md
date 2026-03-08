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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RBZ7OAI%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033154Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJIMEYCIQC1ojdghHChB1AA9%2FPUYSFsHXW89bHEbzYgdAVKE%2BvNSAIhAPswtvCOWlMLt02KjHtP01hnO9K6SpQslurNvs%2F1Mpm3Kv8DCAwQABoMNjM3NDIzMTgzODA1IgxRxFbbMrsc%2FvVRU0Yq3APKF8SErMWcilkPySVGhOhzGePjjN2g0KZUliQnD8j6s68SMlKnDcOc7QCwsIq2HtFlMA4StmS8YH%2BAet0%2F3pR8gsPfaVVKhaYbx1G7SRPhXtsFtcnIcyT4AQpx07E372CzbSRBXJlyntWAbJhx0QLzdPs8w%2BHxTij8KSkEhlRQKP8d7jaFC4s95s%2F94W4KHEgwz1kfuYcV%2FzLP4XVh6UUycpX9MNgLRq8Vz4JVXEW%2Ff9IiKm0T82z9zXMycp%2BD12IkYiws48MBf1fWydKZ9TLftsAODR%2FhQKOXZlNeSxQQRo%2FcaTGatcY%2FV4%2FCsYjXn3tUCL0ZvJ1%2BAvmtiotHc7ECdEOG1lkz8aQOyX7RqYFwxEPKj08GSGpRXgfp6cn42cdbRLGg3oMqlnPBKnJFwWfjn73lLZJrG8TJll4RwjgV4qIKJ8z%2BWQW3G5VToGqq%2BOljDTkMCvI73k9bFc2010RayIcdkSOlm5%2BEctlzLNLhmyyiuCJt7TnGsXnwiM8vQB%2BurHqgmAnFNLujW2F%2BAHcX%2BZ2II%2BVUQHGek8yhLiS4yeh8bvghUrCEIO%2FkTf56%2FHLJ02R3W7k2T2kGMTMhJzuJeaKeaPJyJ0iDgYouAKCwGOlxJn0h9ed%2F33ykmTDdwrPNBjqkAUPb6dO6RH5I6cWxOCDxbVOFjM%2BaHTFJzrALRcNV0pw9AM5iZ0kzjV4Ln2%2FgwDhqc0%2BHYIcSW6pQPFWxczv9HyiiGsyaC6j%2BGmRNiClzCmFr5bNq5SQYUqweWkfktjiEUP5a288bjLoF4rA%2BzYYxzxD9tJiK85J3dRgmxHAx%2FwxWEfVhrDI%2FF9URRc7Dt55qAlE1ok5afqek58H8vtk4CJJC%2BOgh&X-Amz-Signature=627a417f9340ae00d713f89df902d5d4652a89c56f2fc478a6e418bfdb0e80d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RBZ7OAI%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033154Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJIMEYCIQC1ojdghHChB1AA9%2FPUYSFsHXW89bHEbzYgdAVKE%2BvNSAIhAPswtvCOWlMLt02KjHtP01hnO9K6SpQslurNvs%2F1Mpm3Kv8DCAwQABoMNjM3NDIzMTgzODA1IgxRxFbbMrsc%2FvVRU0Yq3APKF8SErMWcilkPySVGhOhzGePjjN2g0KZUliQnD8j6s68SMlKnDcOc7QCwsIq2HtFlMA4StmS8YH%2BAet0%2F3pR8gsPfaVVKhaYbx1G7SRPhXtsFtcnIcyT4AQpx07E372CzbSRBXJlyntWAbJhx0QLzdPs8w%2BHxTij8KSkEhlRQKP8d7jaFC4s95s%2F94W4KHEgwz1kfuYcV%2FzLP4XVh6UUycpX9MNgLRq8Vz4JVXEW%2Ff9IiKm0T82z9zXMycp%2BD12IkYiws48MBf1fWydKZ9TLftsAODR%2FhQKOXZlNeSxQQRo%2FcaTGatcY%2FV4%2FCsYjXn3tUCL0ZvJ1%2BAvmtiotHc7ECdEOG1lkz8aQOyX7RqYFwxEPKj08GSGpRXgfp6cn42cdbRLGg3oMqlnPBKnJFwWfjn73lLZJrG8TJll4RwjgV4qIKJ8z%2BWQW3G5VToGqq%2BOljDTkMCvI73k9bFc2010RayIcdkSOlm5%2BEctlzLNLhmyyiuCJt7TnGsXnwiM8vQB%2BurHqgmAnFNLujW2F%2BAHcX%2BZ2II%2BVUQHGek8yhLiS4yeh8bvghUrCEIO%2FkTf56%2FHLJ02R3W7k2T2kGMTMhJzuJeaKeaPJyJ0iDgYouAKCwGOlxJn0h9ed%2F33ykmTDdwrPNBjqkAUPb6dO6RH5I6cWxOCDxbVOFjM%2BaHTFJzrALRcNV0pw9AM5iZ0kzjV4Ln2%2FgwDhqc0%2BHYIcSW6pQPFWxczv9HyiiGsyaC6j%2BGmRNiClzCmFr5bNq5SQYUqweWkfktjiEUP5a288bjLoF4rA%2BzYYxzxD9tJiK85J3dRgmxHAx%2FwxWEfVhrDI%2FF9URRc7Dt55qAlE1ok5afqek58H8vtk4CJJC%2BOgh&X-Amz-Signature=259afea54a4e55811a44afb8436ee9d0c2b07cc890286eea064e4670b34cccf7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







