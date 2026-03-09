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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLONNSEJ%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJIMEYCIQDYCIRqY3XLHDN0GHZ9Rudv3f%2BeuRPuBkPUzrbGGjp6BAIhAI9fzUCe3%2BHI0J0ICJXO25vfn73S%2F1u%2F%2FQ4Rf4TJmu%2B%2BKv8DCCUQABoMNjM3NDIzMTgzODA1Igy%2F5ogt3KYESJqGwNUq3AMyRdWUYdPE0pYDMq%2B7GlPp54aKZFsVXGwUQXkySXKODGwudQnNeWCEJh9UnNmBP41vup3dtmdpLs8qCYGikxbrwE1tsocCLR4v3wku%2FHd1rDmzRkDdLAuyRv83bjPb3Fxlr9ZvGHJgdHibHoa35YDEluaccCqOZok33l6aA5UnUk%2FK6qhq7f119c02rqk7XeqTUojUjzhUthoiEnzEmHlPgs7n7WF3FVaHfh9TkRkn%2BB0WFVJ%2FqW%2BB7Km9pZQCI201Wk%2BLigeDb9XPCttSofP8Z0P84UomcCNRiZPiddC%2FRAnwEKytUxTBp%2BZ%2Fs3u7A1kLMCeOkFz%2FWoOsTp%2FcxUvSCQANeK85qGT9RCJuc%2FCmzBZ5XXr6ciIdgu8TzLtrVeo5WemlhfwH1rspWjPAnhgBso35HWFFsnyfKEhB2Z94XU%2B8sipKKQpkeNavfRC87iqAGMrYxPzM63ldla7RYYPE0xJiBWBTvCTpTQcNIkPfFvaX7kU6AEyx3h7U8WIFWTgAjow62X1t7GPCY2kqN13lO2KzI7a9hRslQQ43K%2FtKb1nHkQSBCEQ9LotNUEs6dWj2bX4b0%2F%2BjMq%2FybSrFNWXcWoKEevZCT6dLb6K3fFBR2G8zz2hiytcJ9B4cDzCW%2FbjNBjqkAf33mPEc6aCMI%2FivjTk8xs7OyBWWlnEmFqkWol%2Bxnuf%2Fz3h37X4BFPHCg6kvh8XtqkA1cwxPIFRaLm63RxvjSmyrYoflKdJTi0boSasYaA9IkV3iaINb2wVaEj2cBPihgPnxDgpJWFH%2FxQKF862qVOcTY8ea%2FBdNkQi8rvBXRvCs6aELRnhacDmGcJbqbeOeXK4EWzg%2F7hfwf7GDnzP7AXyd4dVC&X-Amz-Signature=886ac8c0e68e944597c64b459875592e4970dec913293f5e0dfd687d53af38b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLONNSEJ%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJIMEYCIQDYCIRqY3XLHDN0GHZ9Rudv3f%2BeuRPuBkPUzrbGGjp6BAIhAI9fzUCe3%2BHI0J0ICJXO25vfn73S%2F1u%2F%2FQ4Rf4TJmu%2B%2BKv8DCCUQABoMNjM3NDIzMTgzODA1Igy%2F5ogt3KYESJqGwNUq3AMyRdWUYdPE0pYDMq%2B7GlPp54aKZFsVXGwUQXkySXKODGwudQnNeWCEJh9UnNmBP41vup3dtmdpLs8qCYGikxbrwE1tsocCLR4v3wku%2FHd1rDmzRkDdLAuyRv83bjPb3Fxlr9ZvGHJgdHibHoa35YDEluaccCqOZok33l6aA5UnUk%2FK6qhq7f119c02rqk7XeqTUojUjzhUthoiEnzEmHlPgs7n7WF3FVaHfh9TkRkn%2BB0WFVJ%2FqW%2BB7Km9pZQCI201Wk%2BLigeDb9XPCttSofP8Z0P84UomcCNRiZPiddC%2FRAnwEKytUxTBp%2BZ%2Fs3u7A1kLMCeOkFz%2FWoOsTp%2FcxUvSCQANeK85qGT9RCJuc%2FCmzBZ5XXr6ciIdgu8TzLtrVeo5WemlhfwH1rspWjPAnhgBso35HWFFsnyfKEhB2Z94XU%2B8sipKKQpkeNavfRC87iqAGMrYxPzM63ldla7RYYPE0xJiBWBTvCTpTQcNIkPfFvaX7kU6AEyx3h7U8WIFWTgAjow62X1t7GPCY2kqN13lO2KzI7a9hRslQQ43K%2FtKb1nHkQSBCEQ9LotNUEs6dWj2bX4b0%2F%2BjMq%2FybSrFNWXcWoKEevZCT6dLb6K3fFBR2G8zz2hiytcJ9B4cDzCW%2FbjNBjqkAf33mPEc6aCMI%2FivjTk8xs7OyBWWlnEmFqkWol%2Bxnuf%2Fz3h37X4BFPHCg6kvh8XtqkA1cwxPIFRaLm63RxvjSmyrYoflKdJTi0boSasYaA9IkV3iaINb2wVaEj2cBPihgPnxDgpJWFH%2FxQKF862qVOcTY8ea%2FBdNkQi8rvBXRvCs6aELRnhacDmGcJbqbeOeXK4EWzg%2F7hfwf7GDnzP7AXyd4dVC&X-Amz-Signature=74da51dac495a8764d402ca6749c55dd83bd4d5c1dce68f7eb693d2ea8f1f888&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







