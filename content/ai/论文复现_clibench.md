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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SVY5EK5%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033928Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHWv7ZRzgwuKuqeiBmBPOZemOjmnnYE8xcfvyPFN2EzUAiBRJomARKiwhzLwGM4ce3kOAlnGZtQgsqnZ1%2FH8L2YsNCr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMdHkgK8g%2F7A09h2ZBKtwD4CKLbg3M4OZ%2Fu28FOwA3tfKpkWrmfRXwnqRAtT1rDYuQqLp9pmOtUfSmyG0rKHOE0%2BDf8xua2XD8En9xRTdXPsF85eAD78bHn24Pd7VHxPmwp1tewaatFvJQZPSOHfDvJU969A6L1gLkrBm8%2F%2FafABx85yKuHwN6Jm%2BGSOxO3ZL4ukB6LmU1gPb5hKCwn%2Bicy1MmlMV2xxSFOlJhsSi5K%2FneovJPBw6L%2Bee6K8ReygUDsKn0P4LV0IQa%2BIeQHOaUDQ9JKGCBr%2BO8vE%2BhswNF0aSpTDwq%2BGXGVHjpz%2FYqN6ewGNFSanKD68x9lGo7AWtW%2BwZ%2BsrEih9HLT6GasAfrqMbXdil84fV07hWMI4ve6gKYR3lNhFdGNmq61AtOCRBc79UK7q0LYuANHX6o3Z7L5GwJqLuUl6x0ihr1gUrlPPkBKmkjdYRok5apfFOe2BWV2uWFT8kFcktoxOelw%2BYTd1%2BKXlwNSqYCXdUGwPMivjbi7yKVg0NUcr9vhs6QnFjUHv166ztk7RatVjbWT%2B%2BlgAeK5x3IfjwNaf00nG0VrbnUluv%2BrZF1nXMTIMp0P0NmljOY94LmUC47O8IVRqfKUE8fqA3DIxOOR2ytmTjDhPhQjTFOK5B3LCcwi2kw2fLZzAY6pgEnG9lQOQNWzEpgGet3ZYfjY0OSqug1RP3Xhtaui3ITqa9BiTvcLGBYR34Muzk%2BNdU7kszN7VCbTk3lEeQ43h0cQWhfElTkSS1uISnk%2FTi8R38qG4IeHmYYV6H1Ddn2wyVEtqP3fU7RxgA05ZQoobUHySmFSJGtvFtHnwrsgSobZ1tKJ95I4QR0M9c4bZIYkl%2FsrpvrQBHB7KeJ0npqsfpEK%2FDyo3gT&X-Amz-Signature=06bb41fe752fac2dc55b93ad2168647a3e1fd94912e4a88de035614a534e5fee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SVY5EK5%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033928Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHWv7ZRzgwuKuqeiBmBPOZemOjmnnYE8xcfvyPFN2EzUAiBRJomARKiwhzLwGM4ce3kOAlnGZtQgsqnZ1%2FH8L2YsNCr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMdHkgK8g%2F7A09h2ZBKtwD4CKLbg3M4OZ%2Fu28FOwA3tfKpkWrmfRXwnqRAtT1rDYuQqLp9pmOtUfSmyG0rKHOE0%2BDf8xua2XD8En9xRTdXPsF85eAD78bHn24Pd7VHxPmwp1tewaatFvJQZPSOHfDvJU969A6L1gLkrBm8%2F%2FafABx85yKuHwN6Jm%2BGSOxO3ZL4ukB6LmU1gPb5hKCwn%2Bicy1MmlMV2xxSFOlJhsSi5K%2FneovJPBw6L%2Bee6K8ReygUDsKn0P4LV0IQa%2BIeQHOaUDQ9JKGCBr%2BO8vE%2BhswNF0aSpTDwq%2BGXGVHjpz%2FYqN6ewGNFSanKD68x9lGo7AWtW%2BwZ%2BsrEih9HLT6GasAfrqMbXdil84fV07hWMI4ve6gKYR3lNhFdGNmq61AtOCRBc79UK7q0LYuANHX6o3Z7L5GwJqLuUl6x0ihr1gUrlPPkBKmkjdYRok5apfFOe2BWV2uWFT8kFcktoxOelw%2BYTd1%2BKXlwNSqYCXdUGwPMivjbi7yKVg0NUcr9vhs6QnFjUHv166ztk7RatVjbWT%2B%2BlgAeK5x3IfjwNaf00nG0VrbnUluv%2BrZF1nXMTIMp0P0NmljOY94LmUC47O8IVRqfKUE8fqA3DIxOOR2ytmTjDhPhQjTFOK5B3LCcwi2kw2fLZzAY6pgEnG9lQOQNWzEpgGet3ZYfjY0OSqug1RP3Xhtaui3ITqa9BiTvcLGBYR34Muzk%2BNdU7kszN7VCbTk3lEeQ43h0cQWhfElTkSS1uISnk%2FTi8R38qG4IeHmYYV6H1Ddn2wyVEtqP3fU7RxgA05ZQoobUHySmFSJGtvFtHnwrsgSobZ1tKJ95I4QR0M9c4bZIYkl%2FsrpvrQBHB7KeJ0npqsfpEK%2FDyo3gT&X-Amz-Signature=e787e03a02a21e483589fce560fd49087b1474e408781d57c4db9d56c44e87dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







