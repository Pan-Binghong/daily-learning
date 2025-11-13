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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTZ2O44V%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T024643Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJIMEYCIQDCP9GGYZsG%2Fw8pwGQl%2F54FnoudluSwqrZE6gMuS7ipDgIhAMVmAsx%2FyJbXGRNTpHbtEmA0SvDKx40htmVyf5dmH5VMKv8DCEMQABoMNjM3NDIzMTgzODA1IgzINqoT%2FYflaglk1qoq3APRJlwonH2vPJ23Jgb8XKbKG506L8xFI3X5tyVKpwZHLcJLScYCThJOxm165tOeP%2BXqgp9ZDdpXYKS5K8kEv%2FGSJ3Z35qQkQGtQnjs3GsaST1sHDbBS3iONizq5qHBY7d6jgD3YObyTjT2Zo4kLrt6D2aaAkPKPM9vEx4S4PZWI5xUOH1wgVSPhV%2Fddp%2F74YBDxw5r03iCgmWCDc0%2Bmy9ShWGS489SMYyiMdqa%2F2ZpWPVmj6o2HnwRg%2FueC3Jhrxhlha4Rz9L%2FFFosOCBxjleoDyiffMHsFwR1owtSP3bimD3qTMhsjPKxwajBnmxka7j%2FsWlp3HiVm6SRf6OI%2B9GCgZzRRPK9zvw8nqMKQk7xCamNLcRdrLobunONK04NshYv4eWVrFax7qyhqeByIDrg7PT%2BFsOkWnI%2FQ3b6wb6xsaeMOUcKhbGlHLXz8NL%2Bo64jCmCP1xR%2FbRcpNVqNCbMDo70TWjgj25b%2Fy672rViz7boteXQ5wduN8Iz3Hl%2BUzqfLxgzBdguBR8eF0mt1Yqouv9FVFe4pzU6KULdF5mj8hwwB7r%2FxyJMu430LBEM3Dje9ZzJRVdM1gJReH5rTVZBvhZ%2FaNPXw%2FCakAHj%2BuoSTGcahKkGlCE5sMF1GpVDCv8dTIBjqkAVmGP2tH4H6%2FVXy6B%2Fp%2BkbhZy8lXlV6Doe5nvGOOPdaS4SyaucYATpU6%2FB6VP2x2hh29nno7y235Exc0O56c43oEMACsigWOmHDM5k0015d%2Fig0fLix7My1UQSe73xUg94wbB1YiSbWSybLPWt018qAfZN87E7k0YFp8%2BKGGDpuzO1D6Jap7k4vkRSMvLek4Q2nqAXeRN4Re0vH1hIcKwYdX97z4&X-Amz-Signature=830b8185f76cdedb3fbf632e786521767b1fb50573e9935046f7144e142d8e3a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTZ2O44V%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T024643Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJIMEYCIQDCP9GGYZsG%2Fw8pwGQl%2F54FnoudluSwqrZE6gMuS7ipDgIhAMVmAsx%2FyJbXGRNTpHbtEmA0SvDKx40htmVyf5dmH5VMKv8DCEMQABoMNjM3NDIzMTgzODA1IgzINqoT%2FYflaglk1qoq3APRJlwonH2vPJ23Jgb8XKbKG506L8xFI3X5tyVKpwZHLcJLScYCThJOxm165tOeP%2BXqgp9ZDdpXYKS5K8kEv%2FGSJ3Z35qQkQGtQnjs3GsaST1sHDbBS3iONizq5qHBY7d6jgD3YObyTjT2Zo4kLrt6D2aaAkPKPM9vEx4S4PZWI5xUOH1wgVSPhV%2Fddp%2F74YBDxw5r03iCgmWCDc0%2Bmy9ShWGS489SMYyiMdqa%2F2ZpWPVmj6o2HnwRg%2FueC3Jhrxhlha4Rz9L%2FFFosOCBxjleoDyiffMHsFwR1owtSP3bimD3qTMhsjPKxwajBnmxka7j%2FsWlp3HiVm6SRf6OI%2B9GCgZzRRPK9zvw8nqMKQk7xCamNLcRdrLobunONK04NshYv4eWVrFax7qyhqeByIDrg7PT%2BFsOkWnI%2FQ3b6wb6xsaeMOUcKhbGlHLXz8NL%2Bo64jCmCP1xR%2FbRcpNVqNCbMDo70TWjgj25b%2Fy672rViz7boteXQ5wduN8Iz3Hl%2BUzqfLxgzBdguBR8eF0mt1Yqouv9FVFe4pzU6KULdF5mj8hwwB7r%2FxyJMu430LBEM3Dje9ZzJRVdM1gJReH5rTVZBvhZ%2FaNPXw%2FCakAHj%2BuoSTGcahKkGlCE5sMF1GpVDCv8dTIBjqkAVmGP2tH4H6%2FVXy6B%2Fp%2BkbhZy8lXlV6Doe5nvGOOPdaS4SyaucYATpU6%2FB6VP2x2hh29nno7y235Exc0O56c43oEMACsigWOmHDM5k0015d%2Fig0fLix7My1UQSe73xUg94wbB1YiSbWSybLPWt018qAfZN87E7k0YFp8%2BKGGDpuzO1D6Jap7k4vkRSMvLek4Q2nqAXeRN4Re0vH1hIcKwYdX97z4&X-Amz-Signature=e5ecf46441a03552ce0313aeb6283c76b073e160b90278ffb1d30865cead0e3c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







