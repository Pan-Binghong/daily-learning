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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLK4TSEV%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032711Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDB59e8frEhKGfPYykI1n1cl9t9HybQOynpSQGffOGClQIhAM4O93uGoNqu0Lko2YGWzH2X4a8RzJgK4SU2Awp52bTCKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwYqh1NQwN1CrmGruMq3AM6nXkhGin5mz67sFvFqkZDJ8zkr%2FRlxLZ%2Fz1YDtbiqBBSEOBR8ergekgXg1Xqw0m7%2FDoSx43itFwSBv7NjmfkcIa%2BrP9KIbFeG4Jt5CmYhryQ1kvtkfRqwIAuLQv%2BpFkTmU5NUV1iBPDXzEAqM2kkGe7CkRp1qiPIP%2FJDPaHsBPXy2q5wIqMZBimaXaGFIR%2BEoj8UICQF74RnYUuKzLLo5Et8F%2BXK67aBoLW%2BRb0TOGLE%2B9ioTp8GU1SCQS7cKRxO5dnyHpbyQAvVsLETNOnvF9pN4uHy%2BVjwiEsrWjVsFj2tI4aMJVyR3wdgJH8inKvTkPTegNrsML%2BwhgXhcBG8ZbcMAI%2FKpUWD%2B46%2FWvvB9OAFa3wwVMaUO1o3ldrYx83uuO9lZBVUVIyIm0bN%2FFMvswmC21du65neFmNPVbpj1L741B42RgSpFKzP3eZ4Wiu0hJR4b%2BI1q%2FhvsLES26qnbFG4ImKoJKVK%2BO%2FnG%2BU7wZiZGaGzakuD8tX4xw1Jjt2%2FCq10cHkZlCfGBW0jhOit%2FBdgZPBpdSDKGDo8ixSUcwp2lAbdI%2F2kUGG3HHl3Tgg4Y0y3GZE4uFWR%2FAEzRbkxyX0pC3b8JyBV3yG%2Bsqpz8m18TyR6UULXBWwxNIjDamZ7NBjqkAWtgvwOeetQDs1Ko6iT7gNK4A813RNl5IwYl%2FpPDjryQN7YDhHNVoklxkikQe%2FFup7zr6h8NlhVdhq4ISq0X%2BId8qyBO%2FUcm0EY2bVwbFujuGaFSrE%2FjIF5t9nkm3rbYzAw7xnDxzgYRULjM3fSew3Fb8Gj7hg%2BnUB5bbHV85y4qtvt%2FiGkK0eOlAyr1CCeOB9lAzBcwO7ur0ekrEHrHv8w29teh&X-Amz-Signature=4b655b4147ed4e3d344997bc6c1383193ea3d510e2b77982549e478c0b218311&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLK4TSEV%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032711Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDB59e8frEhKGfPYykI1n1cl9t9HybQOynpSQGffOGClQIhAM4O93uGoNqu0Lko2YGWzH2X4a8RzJgK4SU2Awp52bTCKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwYqh1NQwN1CrmGruMq3AM6nXkhGin5mz67sFvFqkZDJ8zkr%2FRlxLZ%2Fz1YDtbiqBBSEOBR8ergekgXg1Xqw0m7%2FDoSx43itFwSBv7NjmfkcIa%2BrP9KIbFeG4Jt5CmYhryQ1kvtkfRqwIAuLQv%2BpFkTmU5NUV1iBPDXzEAqM2kkGe7CkRp1qiPIP%2FJDPaHsBPXy2q5wIqMZBimaXaGFIR%2BEoj8UICQF74RnYUuKzLLo5Et8F%2BXK67aBoLW%2BRb0TOGLE%2B9ioTp8GU1SCQS7cKRxO5dnyHpbyQAvVsLETNOnvF9pN4uHy%2BVjwiEsrWjVsFj2tI4aMJVyR3wdgJH8inKvTkPTegNrsML%2BwhgXhcBG8ZbcMAI%2FKpUWD%2B46%2FWvvB9OAFa3wwVMaUO1o3ldrYx83uuO9lZBVUVIyIm0bN%2FFMvswmC21du65neFmNPVbpj1L741B42RgSpFKzP3eZ4Wiu0hJR4b%2BI1q%2FhvsLES26qnbFG4ImKoJKVK%2BO%2FnG%2BU7wZiZGaGzakuD8tX4xw1Jjt2%2FCq10cHkZlCfGBW0jhOit%2FBdgZPBpdSDKGDo8ixSUcwp2lAbdI%2F2kUGG3HHl3Tgg4Y0y3GZE4uFWR%2FAEzRbkxyX0pC3b8JyBV3yG%2Bsqpz8m18TyR6UULXBWwxNIjDamZ7NBjqkAWtgvwOeetQDs1Ko6iT7gNK4A813RNl5IwYl%2FpPDjryQN7YDhHNVoklxkikQe%2FFup7zr6h8NlhVdhq4ISq0X%2BId8qyBO%2FUcm0EY2bVwbFujuGaFSrE%2FjIF5t9nkm3rbYzAw7xnDxzgYRULjM3fSew3Fb8Gj7hg%2BnUB5bbHV85y4qtvt%2FiGkK0eOlAyr1CCeOB9lAzBcwO7ur0ekrEHrHv8w29teh&X-Amz-Signature=17c2599c94d5fb5a12c25e31dfea5ebcfadc5a4e797670bf5cdb1a80f89dd108&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







