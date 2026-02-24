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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLICJ47V%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJGMEQCIA8GrqcJCdn%2BpHp5sztIs0O7xaemvpkJREnT8dM%2FXzToAiA8L6CN8MJx1LYWcgfp5hWyzGDTmGCdvJZCLx2vzGfSVCqIBAjs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIqQMbkNiDJh3XpUaKtwDUdvmj80ydh0tVfHkDg7y0gDN0xGeebLOaXpua5R4je8nDJ0Kar8%2BfFPd7%2FL9%2BQLULJyPuq4tBYoMiK1OF2uCt2XUWnhIdcTZkAvqvMNM5pm%2F883s867DzppyyBcPe3AlfEoqQD8AnZZKLjSVh8Xwh6rQqrW3nLfQ79DKsRqykBZKXwKQH1fdEzn4v5z8Zv4qyCtE5lsgmX6fAJpdX0kNewKuHeQE77x2jTh4uKpH6RhsHR%2FWnvmo0lvkE78IDZE42Uvk2WRCvUMPWvvWDWO99JNbbRIv34ruaP%2F8nMrhSxqpMHPVkmg%2Fx3CLAiATmaTcUtL5MvqOAYGUbzcC1ny7HEe5WfiIy%2B7ahuOw7aGhW1ur5oqIJSaenxAPTEJp3lT0iCM%2FeM818ePQkN6B%2BiIj7CGzeX7FbMWPMy%2BnbjFLL%2FoFHvm7xuwAvyoAta29kT4860uuxV%2F6NL6vBxeXRM903Io3vn1y1Wti6WEpZ6xkGIFc7baozl8UQ2KvAhrw5xqakRxItvSpYlPLH8%2FstyvGiTBWZNpwo53G5ba%2BtAtDBsxRLqQR8vxIT19ZQPoNVhR4rtzy57vDeyAKULoHVFf%2Fn40ecbx5e8tiTjdgggK2YIbRzKSSQcgY2NSEdfww7bT0zAY6pgEun3RC8B6gOE1oJJJatymWZ3uJdXdCpZ6stcLrdhM9yQ4o9DHFhOwCGIB45kcvQaFincGzrG2Runb2aBf3HKdblKMIQKOvcIceNo7iTRZqUKtKlBSbovxiUTAZf99Wy66XX0wqEBDQT9vXym6z0eIPLBoMCTfh3GtShzTr9ikt8SO5L8Dmt%2B693gKW3IZQ%2B%2FvFUrfjmZPkzIHjWWMa%2F1F%2B2NhD2Ujw&X-Amz-Signature=f09b12d0518010d11b56a26526c80c5892fb06cc2d49d4753ec28c07c15abe81&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLICJ47V%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJGMEQCIA8GrqcJCdn%2BpHp5sztIs0O7xaemvpkJREnT8dM%2FXzToAiA8L6CN8MJx1LYWcgfp5hWyzGDTmGCdvJZCLx2vzGfSVCqIBAjs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMIqQMbkNiDJh3XpUaKtwDUdvmj80ydh0tVfHkDg7y0gDN0xGeebLOaXpua5R4je8nDJ0Kar8%2BfFPd7%2FL9%2BQLULJyPuq4tBYoMiK1OF2uCt2XUWnhIdcTZkAvqvMNM5pm%2F883s867DzppyyBcPe3AlfEoqQD8AnZZKLjSVh8Xwh6rQqrW3nLfQ79DKsRqykBZKXwKQH1fdEzn4v5z8Zv4qyCtE5lsgmX6fAJpdX0kNewKuHeQE77x2jTh4uKpH6RhsHR%2FWnvmo0lvkE78IDZE42Uvk2WRCvUMPWvvWDWO99JNbbRIv34ruaP%2F8nMrhSxqpMHPVkmg%2Fx3CLAiATmaTcUtL5MvqOAYGUbzcC1ny7HEe5WfiIy%2B7ahuOw7aGhW1ur5oqIJSaenxAPTEJp3lT0iCM%2FeM818ePQkN6B%2BiIj7CGzeX7FbMWPMy%2BnbjFLL%2FoFHvm7xuwAvyoAta29kT4860uuxV%2F6NL6vBxeXRM903Io3vn1y1Wti6WEpZ6xkGIFc7baozl8UQ2KvAhrw5xqakRxItvSpYlPLH8%2FstyvGiTBWZNpwo53G5ba%2BtAtDBsxRLqQR8vxIT19ZQPoNVhR4rtzy57vDeyAKULoHVFf%2Fn40ecbx5e8tiTjdgggK2YIbRzKSSQcgY2NSEdfww7bT0zAY6pgEun3RC8B6gOE1oJJJatymWZ3uJdXdCpZ6stcLrdhM9yQ4o9DHFhOwCGIB45kcvQaFincGzrG2Runb2aBf3HKdblKMIQKOvcIceNo7iTRZqUKtKlBSbovxiUTAZf99Wy66XX0wqEBDQT9vXym6z0eIPLBoMCTfh3GtShzTr9ikt8SO5L8Dmt%2B693gKW3IZQ%2B%2FvFUrfjmZPkzIHjWWMa%2F1F%2B2NhD2Ujw&X-Amz-Signature=000d2667d441744481ee68b741afd55f00b69aa44f2afe5147cc1e97413b9d52&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







