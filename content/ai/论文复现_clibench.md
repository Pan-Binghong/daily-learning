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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665S3JWC6Z%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025110Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDS48qCwdqAT%2BxSz023QM8TlZIvCp%2B0JgreQIHCY8ObAQIgLEl9waEdb8vQaAEaZBBESdWCjOmZzPiErvs%2BmvrXHoUqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCNV7w0VdgroxiV35SrcAx7GNBtHooQXlJwk%2FPiK6bm6yf3MgaEkRMV%2BZHsPkcmUDL0%2Bn0KqpymJUG%2FePBR%2BMduA%2FSkDzadP0Fxv9nW26AS6IsAPd59yfwYT6BAj9FoyUFJetf8%2B5eXSB2QEBJ2M%2FFYn%2BTF1YhTkrvYz3hTBzhnvyy1nsVbxbUiGXt5k%2BKGuC%2Fl3TjTKcgkgvcpVzgTHYV5yjQBe6e1zOuN0EnQrDQCuMOR3mGHo9j0t1RaVnPNNjwAYdSKb9jZMYQSzMTZQjZZDFA6cfyayUTWVlnp1UNnALeKRK1GX15X8VM0gZ2apOlMDEyBqbm%2BweUWhd28u52%2BHizODDfe0j1NlvSc4lg4h%2F70TN1vVoQEZrf2XhE%2FK2wL2SD%2FGTFIfBvf1%2B%2B%2BHViN9SvUIMFf6mPYeiN4Z3wQTuF91F%2FkxiDBwE%2B9WNPMWV4B7OgbnSm%2BJHRly3OJQ70NVvE8zxjpRpsMkrxrM4qV0Xx1JRs0CMvqp3ys7mrqNhigB78wrIumXFDXadZI7xu5uOIKGXoSz1%2F5fm3ydHIkNx95LLtyyYiJrW%2Bn7vF5kD3mhJGWIw2bi5Syrbb1r3N%2FkA4oE3RssV9dY%2BoLl1717XUms1O46QmiYhGucicXoZArotcodqIbYlijpMKLJjcoGOqUBz%2BdrOiVaaZ1j5pnIVWlN5YpCGOHgeLjLjDvLxBJ%2FFzKwdmW8jIZ1j4CsL5sqTRYRm%2FAAQWx5%2Bpr38rPxTNGynXRF2ohVz6qrrNC%2FeYYYlbvXE7NRmQHcjQRna7EILI7BKTEd3SRoxcIUYLACW%2B81dkC7S%2BUgfcjMwRvYHXsAcxli7bUoGttYUVxJmbWwUE2kDRV%2FseFfzUf6Nlc18FeWwbVkaSe2&X-Amz-Signature=25800049a32598f142a5b9d4542f4a8ceba9c39891b5422da596d3e9fbed3142&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665S3JWC6Z%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025110Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDS48qCwdqAT%2BxSz023QM8TlZIvCp%2B0JgreQIHCY8ObAQIgLEl9waEdb8vQaAEaZBBESdWCjOmZzPiErvs%2BmvrXHoUqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCNV7w0VdgroxiV35SrcAx7GNBtHooQXlJwk%2FPiK6bm6yf3MgaEkRMV%2BZHsPkcmUDL0%2Bn0KqpymJUG%2FePBR%2BMduA%2FSkDzadP0Fxv9nW26AS6IsAPd59yfwYT6BAj9FoyUFJetf8%2B5eXSB2QEBJ2M%2FFYn%2BTF1YhTkrvYz3hTBzhnvyy1nsVbxbUiGXt5k%2BKGuC%2Fl3TjTKcgkgvcpVzgTHYV5yjQBe6e1zOuN0EnQrDQCuMOR3mGHo9j0t1RaVnPNNjwAYdSKb9jZMYQSzMTZQjZZDFA6cfyayUTWVlnp1UNnALeKRK1GX15X8VM0gZ2apOlMDEyBqbm%2BweUWhd28u52%2BHizODDfe0j1NlvSc4lg4h%2F70TN1vVoQEZrf2XhE%2FK2wL2SD%2FGTFIfBvf1%2B%2B%2BHViN9SvUIMFf6mPYeiN4Z3wQTuF91F%2FkxiDBwE%2B9WNPMWV4B7OgbnSm%2BJHRly3OJQ70NVvE8zxjpRpsMkrxrM4qV0Xx1JRs0CMvqp3ys7mrqNhigB78wrIumXFDXadZI7xu5uOIKGXoSz1%2F5fm3ydHIkNx95LLtyyYiJrW%2Bn7vF5kD3mhJGWIw2bi5Syrbb1r3N%2FkA4oE3RssV9dY%2BoLl1717XUms1O46QmiYhGucicXoZArotcodqIbYlijpMKLJjcoGOqUBz%2BdrOiVaaZ1j5pnIVWlN5YpCGOHgeLjLjDvLxBJ%2FFzKwdmW8jIZ1j4CsL5sqTRYRm%2FAAQWx5%2Bpr38rPxTNGynXRF2ohVz6qrrNC%2FeYYYlbvXE7NRmQHcjQRna7EILI7BKTEd3SRoxcIUYLACW%2B81dkC7S%2BUgfcjMwRvYHXsAcxli7bUoGttYUVxJmbWwUE2kDRV%2FseFfzUf6Nlc18FeWwbVkaSe2&X-Amz-Signature=b9ffde4335c25edcb4f7c6959f4f7b3dd1aab4ec551a6c9a290cb3afa7ff7292&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







