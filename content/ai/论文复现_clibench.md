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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667T5HES6Q%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T043530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIFejnvW6RMeeL7aoMLgR1wCr4w8v9mb2tPpT3yB2yCGEAiAFH8V1KNkhMiM%2F6gLEmefE4YlC9jAPq5JZDcffc5Wm6iqIBAjV%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdduQQ%2BR9B7QVDnt%2BKtwD11g35AmJacFFwzTHx2EYArD874dhsmNIDeMkISyWAnQfHtkZqu9T9Icn4h9HBvIK5b%2FmE8r%2BClXiSnpCHdkR5SgeW%2FxXi2kny%2BWmSVJUcU%2BQy9AVBnLqAHxqc7DSkxD81xAMjljfe3a81ZOvPVlR7Q6bK9wlbtM2L5b79ELRBe%2BDBr3TQ%2BUJOHVLVRT2phv0cMTvZET%2FIcyIt4UM1e%2FgDgMAdyuz4hnuguU8vYzR9Ze%2BbeE%2BeCToV24EHAjjvmvcp84mzU7%2FKqhcaHu%2Fm3D0BfOXEpHI3%2Fp7x2J3ZNwOyuF1hopTXiosBUBp2SbwZfrxvnRhDQunH8ITpS2y2ayfDMi5D80IOHMibL2yYOBBwyb7T%2BaZv97u92oyPJyenlDMn%2FRewHNMHGzDvNO3F5NvnFRAJPo7KjO8bjwQ4QlaPbvzBKI%2BaKQLOylo3rB4szs7voQA48jHgm45m5Y9Q01bdpKyVr5YQQdxcEM2KKJUANs6yRpQwQ0x865PUQlfiBuIyWptjnWr%2FaRzBTF8bxfGTNO3b33pMzaFauVOnuj0eU2v9eRI2sGf9497qyU%2FfeVapVbXO%2B%2FQ8%2FwS0HcxNDfHMBgKd58SqtB%2FOHYJJEW41Eha0t9NWtd2re6OmQsw7%2BzAzwY6pgHX%2BxS41xvacSSBe8KhPBfAM6wF6p0wrGixN40ld68wG6nEOP6Kpr34pBfiSHFurWlkYndxS39MdcGVs827qJanYbLnHRiO9uBc8INOE6gEMyytq5M1QgAs%2BMwsapspvYRomyl3zdVBoPCRjfQS9AX5xry0e%2FDh%2F%2FW%2BHzrGczL4R9TbDttSKLyLchMp1JnQLMCqQ1kr9h7dTuhpmnbpZg11B8vTgSVc&X-Amz-Signature=4783d8bf67ea7baec8218cadf90a57aa09262b3bac3907fcd31de1dd038bf045&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667T5HES6Q%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T043530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIFejnvW6RMeeL7aoMLgR1wCr4w8v9mb2tPpT3yB2yCGEAiAFH8V1KNkhMiM%2F6gLEmefE4YlC9jAPq5JZDcffc5Wm6iqIBAjV%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMdduQQ%2BR9B7QVDnt%2BKtwD11g35AmJacFFwzTHx2EYArD874dhsmNIDeMkISyWAnQfHtkZqu9T9Icn4h9HBvIK5b%2FmE8r%2BClXiSnpCHdkR5SgeW%2FxXi2kny%2BWmSVJUcU%2BQy9AVBnLqAHxqc7DSkxD81xAMjljfe3a81ZOvPVlR7Q6bK9wlbtM2L5b79ELRBe%2BDBr3TQ%2BUJOHVLVRT2phv0cMTvZET%2FIcyIt4UM1e%2FgDgMAdyuz4hnuguU8vYzR9Ze%2BbeE%2BeCToV24EHAjjvmvcp84mzU7%2FKqhcaHu%2Fm3D0BfOXEpHI3%2Fp7x2J3ZNwOyuF1hopTXiosBUBp2SbwZfrxvnRhDQunH8ITpS2y2ayfDMi5D80IOHMibL2yYOBBwyb7T%2BaZv97u92oyPJyenlDMn%2FRewHNMHGzDvNO3F5NvnFRAJPo7KjO8bjwQ4QlaPbvzBKI%2BaKQLOylo3rB4szs7voQA48jHgm45m5Y9Q01bdpKyVr5YQQdxcEM2KKJUANs6yRpQwQ0x865PUQlfiBuIyWptjnWr%2FaRzBTF8bxfGTNO3b33pMzaFauVOnuj0eU2v9eRI2sGf9497qyU%2FfeVapVbXO%2B%2FQ8%2FwS0HcxNDfHMBgKd58SqtB%2FOHYJJEW41Eha0t9NWtd2re6OmQsw7%2BzAzwY6pgHX%2BxS41xvacSSBe8KhPBfAM6wF6p0wrGixN40ld68wG6nEOP6Kpr34pBfiSHFurWlkYndxS39MdcGVs827qJanYbLnHRiO9uBc8INOE6gEMyytq5M1QgAs%2BMwsapspvYRomyl3zdVBoPCRjfQS9AX5xry0e%2FDh%2F%2FW%2BHzrGczL4R9TbDttSKLyLchMp1JnQLMCqQ1kr9h7dTuhpmnbpZg11B8vTgSVc&X-Amz-Signature=01a5dbded56e82f56a24971c7e70269e4ced56241118363d53c53dfbbcab6e71&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







