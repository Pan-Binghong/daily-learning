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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZI5FBXZ6%2F20260206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260206T033330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIHfvJPmptivvYRwjD7D8z0CPA6v5LpmGiYwNq8yu7qXlAiA8GrQRxeHRrSxh3HBvqpJa%2BbuO8RnREWl2fTfJuE4coyr%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMuW%2Fvo2chUQd%2BbHiiKtwDS7iNfeV8m3baMlECMJ2k85u6BEF%2FdQy%2FqMXlIXgYvz5l%2BrgrTkZ2bTagkL7LnUuV4344unyb9%2FKlrhTNICEJrk8jUH1HWGdy3VSyoBidYKkPouv5dxYCmJXy4tDgKVZp9EKVWj%2FAuyKyYvL2sTluGxzyEZEXSopxgWaeTMfigyswXqutA2hz4pcSRPPJeYKvd11WMbig2dgy5LJAqRLfHSFdOzjGSoIFMCF02SiikfMS56zylYrKzSc6uJ2UGCteKwJp2%2BDqDvJGz6knDQd0sB9cmiPh8TbcKf9OwEH8cB4yxX%2F7ZPJWteOVJBq7b1RE%2FzC9HuSLYPnEBMp9aDycYujgJCxXqK6FbcVOyN4d54pGnzdWARJ7qZ%2BP3yn9Ti5t4UsseEG2j3hCJQ%2F9YHuzIEy9DqoFBXCyZwD27JUgukLEmj%2BQm9IP0kl3fDJyXqvCRBBZzN7fJt64adbXKTQTaFjjr9J7IrW4T1rrxIrtc6O8Wu%2B4zx9lIffiTM7tbpA1hBQgz%2FhnKiPu9Z6qPpyQAdnT6J360%2BZfQ6TIalwTk5ZQYt8oT84u12ykYWyi18MoT3LnQk80ooZgd%2B2PCQJuN0s8BziTcPeW447CAlgzRDioTIezCS5sWJZLW6Ew3ruVzAY6pgGCmN1tsO3l9UgkYRQHoebf8mWBMNxjEY6OIoj0Y1BtdI0ETrKGietKs7D3JQ6JlvD5v6wHTsyMRe95rDtn1z8m%2F1Rp8qhCR9aJYr%2BcWWzIIc22FHjnyhL2Jui6HnCAqybAV9TvWfs7zfXP94Ale31ovxeEgUKXOXcQOuDoQk8qzQ37uNXoLQle3tjbo6W4KNf0ZTZlsln6hn0GQdE2Pu7y4ujwkSXE&X-Amz-Signature=10e707ff1f2c8c63ca15fbd5538011d55313aeb1738dc6ecc4960ca646891f3d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZI5FBXZ6%2F20260206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260206T033330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIHfvJPmptivvYRwjD7D8z0CPA6v5LpmGiYwNq8yu7qXlAiA8GrQRxeHRrSxh3HBvqpJa%2BbuO8RnREWl2fTfJuE4coyr%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMuW%2Fvo2chUQd%2BbHiiKtwDS7iNfeV8m3baMlECMJ2k85u6BEF%2FdQy%2FqMXlIXgYvz5l%2BrgrTkZ2bTagkL7LnUuV4344unyb9%2FKlrhTNICEJrk8jUH1HWGdy3VSyoBidYKkPouv5dxYCmJXy4tDgKVZp9EKVWj%2FAuyKyYvL2sTluGxzyEZEXSopxgWaeTMfigyswXqutA2hz4pcSRPPJeYKvd11WMbig2dgy5LJAqRLfHSFdOzjGSoIFMCF02SiikfMS56zylYrKzSc6uJ2UGCteKwJp2%2BDqDvJGz6knDQd0sB9cmiPh8TbcKf9OwEH8cB4yxX%2F7ZPJWteOVJBq7b1RE%2FzC9HuSLYPnEBMp9aDycYujgJCxXqK6FbcVOyN4d54pGnzdWARJ7qZ%2BP3yn9Ti5t4UsseEG2j3hCJQ%2F9YHuzIEy9DqoFBXCyZwD27JUgukLEmj%2BQm9IP0kl3fDJyXqvCRBBZzN7fJt64adbXKTQTaFjjr9J7IrW4T1rrxIrtc6O8Wu%2B4zx9lIffiTM7tbpA1hBQgz%2FhnKiPu9Z6qPpyQAdnT6J360%2BZfQ6TIalwTk5ZQYt8oT84u12ykYWyi18MoT3LnQk80ooZgd%2B2PCQJuN0s8BziTcPeW447CAlgzRDioTIezCS5sWJZLW6Ew3ruVzAY6pgGCmN1tsO3l9UgkYRQHoebf8mWBMNxjEY6OIoj0Y1BtdI0ETrKGietKs7D3JQ6JlvD5v6wHTsyMRe95rDtn1z8m%2F1Rp8qhCR9aJYr%2BcWWzIIc22FHjnyhL2Jui6HnCAqybAV9TvWfs7zfXP94Ale31ovxeEgUKXOXcQOuDoQk8qzQ37uNXoLQle3tjbo6W4KNf0ZTZlsln6hn0GQdE2Pu7y4ujwkSXE&X-Amz-Signature=f0f098ab524e3c02378afe379999aaeba3f57c587d6801d6f79c7ec882ffbb32&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







