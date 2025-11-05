---
title: 论文复现_CliBench
date: '2024-11-13T02:07:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
标签:
- LLMs
- Paper
categories:
- AI
---

> 💡 对大型语言模型在诊断、手术、实验室测试订单和处方等临床决策中的多方面评估。

## 文章介绍

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUDKIH2C%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAZlDl6p5GVRvOVmGVp1bryVyIAzfDDg54YSOKI3j0oMAiEA7lgY2ZZJlql9mP7XX2eetBGk3cIP%2FiaD29gteHXDq6UqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAOaXyJrVxwI8z30NyrcA6n7p0giq5KpJINwBqnoBuhFeIbK%2FNfPvy77jFC6jlHwm7oIKE94%2BT2X0uffdlJlSD5KzexgH8BmtxxohgF%2BRKn9mgUant7SXq59a6LuC0u%2F5scwKmoVL0BJex8HLz%2BY0jTJeKPeOyMIG1JRzdO7v1NcDRc6mUDwIsOl5Gf0W7Wc4EWcPKOOAS8dSmoGDMsh9ASsoiUCeo8EYiLFCDCGvE722W%2BdhOR8IvlcdnJWZy5nGGDGZdSQ%2FCL2uEXur9P00BTxh2gRjJlZ1k86n4%2FxliYHxnyVsuOFLwHFg78yX33THXzP0Ukrtb93KVuS7FAg44ySKJ7sOuTJOAMnkDe%2FDXqU4nJDfssK2eP03Qa%2FZeNdhhNxZhflpCMot3QO%2FfGHyOWShB2lbT2quTmeLuIVEoYFEzhkvB0%2FgCUVAZnAkPHS%2BGgQPkd%2BHs4ADyEseVZJV0B25Ypt1IqRqSB%2Bp0qmQ32ztqQiJyqwf25J6tLxa23cCqtk6SRu1v0u%2FBnsYJooDp3bhvnX8OKwrZ2hFGXIW%2BGrwvS9grOtJSR2ksvNKOt4UxJv01Ohy7Ux7SmlEsr9l8Z%2BeYYtNbBLQcrbvdLdxZEciUvJdVUUy038I7xRZRDthhREIf78QciKIA5jMOGirMgGOqUBn%2BdIR6o9DjRcw5Q3XRlZZiqU3XlcxIsU9g%2F8rJGgU3rlHuIGAj%2BY0zqPkE2emb3XWqjLgoQM9ltgFh2FntzyIacMCrXDPAQa5ZY4c2acOSfdWES4kTAB9iZqViHN%2F874g4ndjWeM0KHQExNxWn3lq3o6%2FTHnRQvp95f%2BP%2BIe0FZkSEOgC4UkJuncMTHC9AjpwzCJXu8mDmVWll%2F3ZQm6pI6g6%2BJ3&X-Amz-Signature=e4e88c2669336b4c98f88e5e08ca74c469d07c522793f6ee612f9d30a2041fcc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUDKIH2C%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAZlDl6p5GVRvOVmGVp1bryVyIAzfDDg54YSOKI3j0oMAiEA7lgY2ZZJlql9mP7XX2eetBGk3cIP%2FiaD29gteHXDq6UqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAOaXyJrVxwI8z30NyrcA6n7p0giq5KpJINwBqnoBuhFeIbK%2FNfPvy77jFC6jlHwm7oIKE94%2BT2X0uffdlJlSD5KzexgH8BmtxxohgF%2BRKn9mgUant7SXq59a6LuC0u%2F5scwKmoVL0BJex8HLz%2BY0jTJeKPeOyMIG1JRzdO7v1NcDRc6mUDwIsOl5Gf0W7Wc4EWcPKOOAS8dSmoGDMsh9ASsoiUCeo8EYiLFCDCGvE722W%2BdhOR8IvlcdnJWZy5nGGDGZdSQ%2FCL2uEXur9P00BTxh2gRjJlZ1k86n4%2FxliYHxnyVsuOFLwHFg78yX33THXzP0Ukrtb93KVuS7FAg44ySKJ7sOuTJOAMnkDe%2FDXqU4nJDfssK2eP03Qa%2FZeNdhhNxZhflpCMot3QO%2FfGHyOWShB2lbT2quTmeLuIVEoYFEzhkvB0%2FgCUVAZnAkPHS%2BGgQPkd%2BHs4ADyEseVZJV0B25Ypt1IqRqSB%2Bp0qmQ32ztqQiJyqwf25J6tLxa23cCqtk6SRu1v0u%2FBnsYJooDp3bhvnX8OKwrZ2hFGXIW%2BGrwvS9grOtJSR2ksvNKOt4UxJv01Ohy7Ux7SmlEsr9l8Z%2BeYYtNbBLQcrbvdLdxZEciUvJdVUUy038I7xRZRDthhREIf78QciKIA5jMOGirMgGOqUBn%2BdIR6o9DjRcw5Q3XRlZZiqU3XlcxIsU9g%2F8rJGgU3rlHuIGAj%2BY0zqPkE2emb3XWqjLgoQM9ltgFh2FntzyIacMCrXDPAQa5ZY4c2acOSfdWES4kTAB9iZqViHN%2F874g4ndjWeM0KHQExNxWn3lq3o6%2FTHnRQvp95f%2BP%2BIe0FZkSEOgC4UkJuncMTHC9AjpwzCJXu8mDmVWll%2F3ZQm6pI6g6%2BJ3&X-Amz-Signature=49b4bbc54a61fb9a4a941e410e4625444729c8da18fbef05331236404d3643d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







