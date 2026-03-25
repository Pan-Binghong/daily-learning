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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOZIGGQ7%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T033939Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDbA2mx6kjKMX7AUkm9HQTUygWtiQqWWYOM1fIdVNTeUAIgKGDFtnvxOiDclNbuvWJis%2FedlpE%2FHfGnNBqG4P%2BwZyMqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLEJA5lQlz%2FGi17XNircA%2Ffbl6iUa2YCpLAauKZTt27XqggwEQxnc9RdUZ6rSznpJfNXMhUhwkupjuBtOIrzOK8EYb1MirtoBIHkJ4w9i36cY95Z30L7v1oHVSapyiUHdQpdTxFA4RUG4zeEMDtlsvTNKuw%2BbGbNzD97XZmbCX0PPGggzaxgqTdw4lN8AesSNSfq%2BdmabyEhxBp3V7YrXLcMnFjQ1m9AEJp7uuNpD2YK3YP%2FOVOmETYBX3pWnba%2FIxlzrDbG2tKmBGE9EiGfJ8d1%2FOIi8iN6LI27WQGiZUsteMnZVDjdNt5G7O3lADNJjveSOc7R9O51rZlvD1EaZXVcYahx3KJays9Uof0%2FMcY06dK5ldgdXjGW%2Bx%2FbPePk2SOVVek9oCHw3TjU07s%2FYucOH7NdSobSs4JIjYKlPVwAOO%2BzmH3NiYCVj2T1MiXBqx%2FOeWSdbvedZKB6z8j3tw8Q4oJYRdjUO8rNA%2F9AaCHgohTHrZVL7cd90vrMdoM4vhb2twgqM1DRSRIV3VctTNLpiiwolvoPvzg5T03WXuxqvIxIozhw8duJnKFYCxySvKMRMKE2kmt%2B9L5qfSb013OumqH9avYTE8T%2F3w%2BRpvdLSKmGZZcwwS9dl3mhO1vF4IgHGYoYRV0F6VGrMO%2Bnjc4GOqUBonZogSYtS%2FU7FRlouEAM6x34j%2Be0UsgCJF6mT3qQ9uIzvCuNNhoSyPQjHF%2FVp1gKtmfNqF950eB0mr5ct2Gm7DwoQZ7cudKZhdxqQWgsnXlzhGoO0oIRkK9gg1kEhHZILL794a7HlBrg2rADxH%2FtnJtVTCadYn9RFM%2F911uPkCXyTBV%2Fj8U20X9MSSNxAcnk4vGFdYwaE7rKWFCNAq1eJ2gopxNw&X-Amz-Signature=c9cc72157729a6f7d3f6d129a19f0c82ffa156d2981434f66d5d7e88e4d37621&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOZIGGQ7%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T033939Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDbA2mx6kjKMX7AUkm9HQTUygWtiQqWWYOM1fIdVNTeUAIgKGDFtnvxOiDclNbuvWJis%2FedlpE%2FHfGnNBqG4P%2BwZyMqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLEJA5lQlz%2FGi17XNircA%2Ffbl6iUa2YCpLAauKZTt27XqggwEQxnc9RdUZ6rSznpJfNXMhUhwkupjuBtOIrzOK8EYb1MirtoBIHkJ4w9i36cY95Z30L7v1oHVSapyiUHdQpdTxFA4RUG4zeEMDtlsvTNKuw%2BbGbNzD97XZmbCX0PPGggzaxgqTdw4lN8AesSNSfq%2BdmabyEhxBp3V7YrXLcMnFjQ1m9AEJp7uuNpD2YK3YP%2FOVOmETYBX3pWnba%2FIxlzrDbG2tKmBGE9EiGfJ8d1%2FOIi8iN6LI27WQGiZUsteMnZVDjdNt5G7O3lADNJjveSOc7R9O51rZlvD1EaZXVcYahx3KJays9Uof0%2FMcY06dK5ldgdXjGW%2Bx%2FbPePk2SOVVek9oCHw3TjU07s%2FYucOH7NdSobSs4JIjYKlPVwAOO%2BzmH3NiYCVj2T1MiXBqx%2FOeWSdbvedZKB6z8j3tw8Q4oJYRdjUO8rNA%2F9AaCHgohTHrZVL7cd90vrMdoM4vhb2twgqM1DRSRIV3VctTNLpiiwolvoPvzg5T03WXuxqvIxIozhw8duJnKFYCxySvKMRMKE2kmt%2B9L5qfSb013OumqH9avYTE8T%2F3w%2BRpvdLSKmGZZcwwS9dl3mhO1vF4IgHGYoYRV0F6VGrMO%2Bnjc4GOqUBonZogSYtS%2FU7FRlouEAM6x34j%2Be0UsgCJF6mT3qQ9uIzvCuNNhoSyPQjHF%2FVp1gKtmfNqF950eB0mr5ct2Gm7DwoQZ7cudKZhdxqQWgsnXlzhGoO0oIRkK9gg1kEhHZILL794a7HlBrg2rADxH%2FtnJtVTCadYn9RFM%2F911uPkCXyTBV%2Fj8U20X9MSSNxAcnk4vGFdYwaE7rKWFCNAq1eJ2gopxNw&X-Amz-Signature=a29ff4089c8cc59d7250994d05b67353b6527cfa2a8ae49fa8d66b8431f20f05&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







