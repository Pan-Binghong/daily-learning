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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVDME3V5%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD8ZWm1p0dbg3hxwH7YqwAgs%2F5mtJikQVxyNfzNXoeAvQIhAOFZS%2FeYJSVy7t4i6EKTp9Ln5%2B%2FpllF6np19YyS6%2B3JlKogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxCoZfDoPI9iVd%2FDZ8q3AP7HAJ7QBDKMUd3SLJaTHZK0lYmdv0DO7jShZC6T01f0jzM8BjszngCsso9cfoNgkeT4RPipvW1dvrzX%2BKWU1kZTW%2FMmwtJ8bp%2F3JyHyAQWeNYEgihT85GZmLDntMxQg%2FfG8qAeut%2BNSMHdjPVLOtLt0TNNxJnmOLWvVdDJBW2eLJOxIDVN2R8OnE%2ByaWoWKC6gXpmbYVH0Y7Wzlwm7bAjy9JhWfROV%2FSm2Qrjgn80Y8Lb9xp%2BH4Ic6HLtW6xjyaIfUUdTKdw5PQPLTRS6UA09W0yVJTuJ6gGxzlxw%2FCe%2BXcWkEI%2F8OpNLs0O2eTmcgE%2FpUh3KjVOgg7f64D3oIhhZxKnhlVFh44w4w0kIUO%2BSr73nuIPz%2B8p8Ie7sr7j8YQUqX1ygHFdCC%2F8OAVTy4G23zLTF9WX09Ld8N%2BnamCaarcdZErTD1PllTQUlkun%2BlfstH2vJ9ksQHotSPvem4LflfQRjCtdeXqVmBa0pv%2FKTbL8IQy9YMZLhXDEgrZCEUHaIHSdyJ%2BknHlJT6FIaNoq0WNvokZLQhEA8EG9WzjBiAamF%2Fb9fa86ld%2ByndJBJ5viUal5PlOkRk2vgq7J1QD76wYI8OrWdLI0oqY%2B%2BqnzSfWJCmdNZz%2B5i3Hu245TCdj7bPBjqkAQrZ6NEZHdGjFOIkcMXBoxdyljT5HqBIdSuzk3pwWQgJaJozEkkGMrhVIxx4s3QcFlWHr8sg8M83ZpLpGhYc7p4wW3WB%2FukNkZx6uIcLvnppUTKU7LsLPxGfDxRmCFwd8XRCC0rULrcLLYjCu2g%2F0jRdsGtXfipIemNXaxAPOY6pfwZP%2FOyFc7Gh4EbYr9xgNw8b0C0twtfrrpAfjL4djzbnCH8W&X-Amz-Signature=af8d71104e8612c725ba083c2f1be8ddffc04eb39407c667b6c6bc82736dd0f2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVDME3V5%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD8ZWm1p0dbg3hxwH7YqwAgs%2F5mtJikQVxyNfzNXoeAvQIhAOFZS%2FeYJSVy7t4i6EKTp9Ln5%2B%2FpllF6np19YyS6%2B3JlKogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxCoZfDoPI9iVd%2FDZ8q3AP7HAJ7QBDKMUd3SLJaTHZK0lYmdv0DO7jShZC6T01f0jzM8BjszngCsso9cfoNgkeT4RPipvW1dvrzX%2BKWU1kZTW%2FMmwtJ8bp%2F3JyHyAQWeNYEgihT85GZmLDntMxQg%2FfG8qAeut%2BNSMHdjPVLOtLt0TNNxJnmOLWvVdDJBW2eLJOxIDVN2R8OnE%2ByaWoWKC6gXpmbYVH0Y7Wzlwm7bAjy9JhWfROV%2FSm2Qrjgn80Y8Lb9xp%2BH4Ic6HLtW6xjyaIfUUdTKdw5PQPLTRS6UA09W0yVJTuJ6gGxzlxw%2FCe%2BXcWkEI%2F8OpNLs0O2eTmcgE%2FpUh3KjVOgg7f64D3oIhhZxKnhlVFh44w4w0kIUO%2BSr73nuIPz%2B8p8Ie7sr7j8YQUqX1ygHFdCC%2F8OAVTy4G23zLTF9WX09Ld8N%2BnamCaarcdZErTD1PllTQUlkun%2BlfstH2vJ9ksQHotSPvem4LflfQRjCtdeXqVmBa0pv%2FKTbL8IQy9YMZLhXDEgrZCEUHaIHSdyJ%2BknHlJT6FIaNoq0WNvokZLQhEA8EG9WzjBiAamF%2Fb9fa86ld%2ByndJBJ5viUal5PlOkRk2vgq7J1QD76wYI8OrWdLI0oqY%2B%2BqnzSfWJCmdNZz%2B5i3Hu245TCdj7bPBjqkAQrZ6NEZHdGjFOIkcMXBoxdyljT5HqBIdSuzk3pwWQgJaJozEkkGMrhVIxx4s3QcFlWHr8sg8M83ZpLpGhYc7p4wW3WB%2FukNkZx6uIcLvnppUTKU7LsLPxGfDxRmCFwd8XRCC0rULrcLLYjCu2g%2F0jRdsGtXfipIemNXaxAPOY6pfwZP%2FOyFc7Gh4EbYr9xgNw8b0C0twtfrrpAfjL4djzbnCH8W&X-Amz-Signature=01d1914bf1c989990194df33ac62085328e4ef83defc11ff2743a418feaf3bb2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







