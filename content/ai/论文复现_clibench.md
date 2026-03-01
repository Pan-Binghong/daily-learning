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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S475QS4F%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCc%2BmkPIKTEMvJ0Z%2F6Fag7wus7o899WWkvbzNFUi3XZ%2BAIhAPiouSX%2FGOaME%2FZWbz9rbIZImtK2QOj7xj3kUF35c2Z0Kv8DCGQQABoMNjM3NDIzMTgzODA1IgxFvdKQA9RY8gAvE4Mq3ANkKBzkyEhJdnqcGdjdBPOUC1sayWVRiZbOizqEFfOb%2BX8hW%2FEKu6ahZWEfVAGcWy5HWyqEEKR1hrdKW3gPP0kg0tYEIJorNzJTTgx%2BxHTVD77Srw72isPaXGCBHGK8fWVdPTyF4UmBVCC1rGD0IaDfLI%2F8ZkiksNz3kFVsPwi1M2ToCfk1hHG5r3twQnfYQAt3n%2BVnJXaUgEqDpXwpEkD5azkuzY5yVtUwTD9zjkjFCdeSwNCONBABa%2FD3mJCzMKFSU%2FcWB5y%2BhyGpYFYWTuJO9BRkJanrAnqRtp4CAZvn0yUF0AxGzQJPoo2OpHdKlnNjuJoSzym4uO%2BUjeSnmZjUwfKnbkn%2B2x6NuFqp1LBqqYjUB50hGAblZrDELtp1F1zfn8j8tlap3IBwKFJazsQvhmlXnezdAFq6eF6J2eNiTPpa%2BYezi38z0Dmc0YdbMXOm1HXMW7I6lGYmx8G0iVc%2FKSQYkiVAavZAQJA0E281L021Wm7zVtBooc%2Bk5BEExYtnp3XslYg0EedKsOQ8wP%2BxKGijOKcgmeu1WSCpbeJjetSvUiY5KgYffPXaWgQqYtUBsiLa7mNhMKyCpB7VqSbrQCnsudwVcWmDn05KRnmt5%2BSmme7jSOSERix%2B4zCSzY7NBjqkAXrJ9DOkvKmi25YMx8%2Fovi%2BVsQbPHAgDSdXm%2F6gm5Wm0xC68AnSXyMv63640p5HJIwrrJW8%2B029BRBStwjDWwu6hV%2FRXqL5yknHOGbIAHe%2FY7pUSsgOAyoHs31r9iW5hs8KPunMSkfbHbJjaqNqixoHS4Lsvp5jJXpESdRfwuR90IynV47bVwtCV5pkCJEce93LReVnO3LJgm6UmFNm%2Fffcm4cNU&X-Amz-Signature=bd0eed6fb48878ce9bc182f20f53ef0b99c147dc22fb61c6e627e5cb077806be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S475QS4F%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCc%2BmkPIKTEMvJ0Z%2F6Fag7wus7o899WWkvbzNFUi3XZ%2BAIhAPiouSX%2FGOaME%2FZWbz9rbIZImtK2QOj7xj3kUF35c2Z0Kv8DCGQQABoMNjM3NDIzMTgzODA1IgxFvdKQA9RY8gAvE4Mq3ANkKBzkyEhJdnqcGdjdBPOUC1sayWVRiZbOizqEFfOb%2BX8hW%2FEKu6ahZWEfVAGcWy5HWyqEEKR1hrdKW3gPP0kg0tYEIJorNzJTTgx%2BxHTVD77Srw72isPaXGCBHGK8fWVdPTyF4UmBVCC1rGD0IaDfLI%2F8ZkiksNz3kFVsPwi1M2ToCfk1hHG5r3twQnfYQAt3n%2BVnJXaUgEqDpXwpEkD5azkuzY5yVtUwTD9zjkjFCdeSwNCONBABa%2FD3mJCzMKFSU%2FcWB5y%2BhyGpYFYWTuJO9BRkJanrAnqRtp4CAZvn0yUF0AxGzQJPoo2OpHdKlnNjuJoSzym4uO%2BUjeSnmZjUwfKnbkn%2B2x6NuFqp1LBqqYjUB50hGAblZrDELtp1F1zfn8j8tlap3IBwKFJazsQvhmlXnezdAFq6eF6J2eNiTPpa%2BYezi38z0Dmc0YdbMXOm1HXMW7I6lGYmx8G0iVc%2FKSQYkiVAavZAQJA0E281L021Wm7zVtBooc%2Bk5BEExYtnp3XslYg0EedKsOQ8wP%2BxKGijOKcgmeu1WSCpbeJjetSvUiY5KgYffPXaWgQqYtUBsiLa7mNhMKyCpB7VqSbrQCnsudwVcWmDn05KRnmt5%2BSmme7jSOSERix%2B4zCSzY7NBjqkAXrJ9DOkvKmi25YMx8%2Fovi%2BVsQbPHAgDSdXm%2F6gm5Wm0xC68AnSXyMv63640p5HJIwrrJW8%2B029BRBStwjDWwu6hV%2FRXqL5yknHOGbIAHe%2FY7pUSsgOAyoHs31r9iW5hs8KPunMSkfbHbJjaqNqixoHS4Lsvp5jJXpESdRfwuR90IynV47bVwtCV5pkCJEce93LReVnO3LJgm6UmFNm%2Fffcm4cNU&X-Amz-Signature=0e7c5192243268aca18f4e8d2cc1862f42a44c9a52c1541f92fe081c21569da4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







