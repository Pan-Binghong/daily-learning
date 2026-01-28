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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BEA3GIN%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFlQmiX6abDEn9%2BKBXywzK30VqPA6WkRbw44cAGuPdnCAiAgyHtwxyY9lsdld97me8VpEfoFq4mCNmQyCcUH3LqaHCr%2FAwhhEAAaDDYzNzQyMzE4MzgwNSIMfMN54pfL8ZQcmS21KtwDqanzThAQVKccANuZnsj4D2k9N90p2nVxa%2FtUjZKfdOd3A3mWlHdlHrRKN4Yh%2FpxSvCiIJLKhN%2BfyYfB6lEN1QyhCfR5aDrWvfWe4w9m%2FH6W2DgfZSCRzlcwsMjsIBaU6VZSputGShLfQ3QN1RUfehPW8T9gx%2Ft8Hs84qklouT%2BjUkBTwapWRIkFDk3ejePRD2xNgg5vOWmp6okaPuCfHLlwgxZbZ1cJL9iF621hjv3lBoc5rkh3o5sH0V8aWPulmie9yvx8Kq80CRBrgmlVq0e3kEvbYudfG2%2BkjnBYHmyA5e%2Ftm52Klwpzd9Livf7SBHTAwBOCxLAnjaHI%2Be%2FqAoIVc%2BG1xBbgLBBtfh2Hfxz5pG64jvSuQIjQKk%2BjBE04wYcqAYf9OpvGJKGHhwa5WyMdkmi3PIH7r5rQ0NkFnxsCs5X0JpiFTir6LOEjxzvC52Y6eigcn9WR9MumVTPtd4Su0NksU5enu34CequycysWihEz0uDtcsqBL6hLPu%2B5rt0vHRlq8obMkkjJMYmHvZqLowBEcMWF1IZqyQnG50dop8aFDLDngqqtyKUzx3hoqE0xHtYdplkIbuMJXc6auphCEea0q8%2F9nG%2B7cOtH6mgMxtOdFsWRRNt%2Bnb0Mw5pblywY6pgHVbaJsVHeXmFAw%2FtWxMkgCydQhSO%2F%2FsaQMt5pH7PxZiyFRZ0q7fBsL29KiuIvtJoi4bEzJH7K1JB8DEbevAigVWfbSZXgSImy9Yt8zdk9x9HwyjKmbnPevYvLXw0bclmipvCp8b7L0rf7oI5Ont6WE13gYixAj61ymeC4SX77N9ZYwvaWXYBMZEoN9WNNnZCyHgcUHFoIFGjJPr69hMji%2FUG%2FNCfk9&X-Amz-Signature=e1e5e973a5403627723371ea8b43926d220d41c858cb8ce273975cbd36f386aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BEA3GIN%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFlQmiX6abDEn9%2BKBXywzK30VqPA6WkRbw44cAGuPdnCAiAgyHtwxyY9lsdld97me8VpEfoFq4mCNmQyCcUH3LqaHCr%2FAwhhEAAaDDYzNzQyMzE4MzgwNSIMfMN54pfL8ZQcmS21KtwDqanzThAQVKccANuZnsj4D2k9N90p2nVxa%2FtUjZKfdOd3A3mWlHdlHrRKN4Yh%2FpxSvCiIJLKhN%2BfyYfB6lEN1QyhCfR5aDrWvfWe4w9m%2FH6W2DgfZSCRzlcwsMjsIBaU6VZSputGShLfQ3QN1RUfehPW8T9gx%2Ft8Hs84qklouT%2BjUkBTwapWRIkFDk3ejePRD2xNgg5vOWmp6okaPuCfHLlwgxZbZ1cJL9iF621hjv3lBoc5rkh3o5sH0V8aWPulmie9yvx8Kq80CRBrgmlVq0e3kEvbYudfG2%2BkjnBYHmyA5e%2Ftm52Klwpzd9Livf7SBHTAwBOCxLAnjaHI%2Be%2FqAoIVc%2BG1xBbgLBBtfh2Hfxz5pG64jvSuQIjQKk%2BjBE04wYcqAYf9OpvGJKGHhwa5WyMdkmi3PIH7r5rQ0NkFnxsCs5X0JpiFTir6LOEjxzvC52Y6eigcn9WR9MumVTPtd4Su0NksU5enu34CequycysWihEz0uDtcsqBL6hLPu%2B5rt0vHRlq8obMkkjJMYmHvZqLowBEcMWF1IZqyQnG50dop8aFDLDngqqtyKUzx3hoqE0xHtYdplkIbuMJXc6auphCEea0q8%2F9nG%2B7cOtH6mgMxtOdFsWRRNt%2Bnb0Mw5pblywY6pgHVbaJsVHeXmFAw%2FtWxMkgCydQhSO%2F%2FsaQMt5pH7PxZiyFRZ0q7fBsL29KiuIvtJoi4bEzJH7K1JB8DEbevAigVWfbSZXgSImy9Yt8zdk9x9HwyjKmbnPevYvLXw0bclmipvCp8b7L0rf7oI5Ont6WE13gYixAj61ymeC4SX77N9ZYwvaWXYBMZEoN9WNNnZCyHgcUHFoIFGjJPr69hMji%2FUG%2FNCfk9&X-Amz-Signature=db6923a5976549fa4875137e1df2a1af75be7bfcd4012accb71c14284d4aa02e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







