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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RNQW5WX%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCRTTdgVpFFpEmaW5Des5FtRMF1tIPuS%2Bvy7VCH6NayyQIgOOpcDr8zI0vB9dQNkrWHLRrD9P%2BTQLNoETlFS8hwSnMqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF0uCe0SCk3%2B1gqCKircA4MA6YR90OaBZKUtEINVhO4ILVhLHz3uLBiRPP4d%2FNWEg9P2xzaUsJGPhbMHwfWMTpfL58CGtJB%2BF7AE8jJe1iEVNP1cjw6VbJvdGu2CtvNRcyJAtDaUoFuBKleEVbWvLcosCM1gQArwtdbewY638UzvP8vEw%2BXMfYlLh%2F2WMcqmoeGlX7jEieEQjsoxmwTYjEAUqOgoi8uI7C%2Fyb%2Bv%2FevConS4wnnNKEmks4n24Q3GtQtmEbLCWwkoiJEYOkS21abVEe%2BOwhH1gCPB9lLh437P490spAhdA8ncN22CnQfpGnJtkCEz1RTiNm9qOgisDoMMHkBam%2B8Zcg0HmGhbvR5AEzRUI6G4kejHtmNtW3K2ufTf5qlkOxqG3S3UwqJKdMGauymgnDPWeiU4NffAza7X%2BeJepq1UVRIlaRF0f%2BbCez2DBIlgU0t1klzfDEx%2BMs2S5E6YbBvqFzbaSrPJjcSo5Z%2BuyRSy1A%2FQRnuHfQZ%2B5H5CWCKruafipUAjSZE93xyA4rg7%2FywfeRIICWaJpaXBF%2BhOjfPPlE9KgZy5JlIoUNjpXZOlLd%2Frhtysx6N%2Fo3dDOmQ3w5Bq4om7sf3B2ifnky41aOw9hn6kKiHkgU9syoVN2QiqKxCvR4DQ2MM%2FM6cwGOqUB%2BwFdOLBW8Rr%2BZztjmPfDpR5daHE%2FZ1qsg3Gn1MoVdz90ZekGQH4VRgr8OTjf4H5SXGxXSS2F%2FGCyM%2FN%2FsSOHGYh9%2BymKCcrbH7zhyv6R8RveFpI36UHhuhUgoKUAspvIyO%2BvZnZf9evNkXuHux%2Fn3XJTVy%2BTFtZHMo%2Fn9id2KNKu7UxEs1Jm2SbqDaAwE6HDH%2FHLncry74HQ54bID62Xbr9Ob2ij&X-Amz-Signature=1abfc45749544ce3ed34cef6ca83976e6eccb3bf08a5a0c84a8c1b625991aff5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RNQW5WX%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCRTTdgVpFFpEmaW5Des5FtRMF1tIPuS%2Bvy7VCH6NayyQIgOOpcDr8zI0vB9dQNkrWHLRrD9P%2BTQLNoETlFS8hwSnMqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF0uCe0SCk3%2B1gqCKircA4MA6YR90OaBZKUtEINVhO4ILVhLHz3uLBiRPP4d%2FNWEg9P2xzaUsJGPhbMHwfWMTpfL58CGtJB%2BF7AE8jJe1iEVNP1cjw6VbJvdGu2CtvNRcyJAtDaUoFuBKleEVbWvLcosCM1gQArwtdbewY638UzvP8vEw%2BXMfYlLh%2F2WMcqmoeGlX7jEieEQjsoxmwTYjEAUqOgoi8uI7C%2Fyb%2Bv%2FevConS4wnnNKEmks4n24Q3GtQtmEbLCWwkoiJEYOkS21abVEe%2BOwhH1gCPB9lLh437P490spAhdA8ncN22CnQfpGnJtkCEz1RTiNm9qOgisDoMMHkBam%2B8Zcg0HmGhbvR5AEzRUI6G4kejHtmNtW3K2ufTf5qlkOxqG3S3UwqJKdMGauymgnDPWeiU4NffAza7X%2BeJepq1UVRIlaRF0f%2BbCez2DBIlgU0t1klzfDEx%2BMs2S5E6YbBvqFzbaSrPJjcSo5Z%2BuyRSy1A%2FQRnuHfQZ%2B5H5CWCKruafipUAjSZE93xyA4rg7%2FywfeRIICWaJpaXBF%2BhOjfPPlE9KgZy5JlIoUNjpXZOlLd%2Frhtysx6N%2Fo3dDOmQ3w5Bq4om7sf3B2ifnky41aOw9hn6kKiHkgU9syoVN2QiqKxCvR4DQ2MM%2FM6cwGOqUB%2BwFdOLBW8Rr%2BZztjmPfDpR5daHE%2FZ1qsg3Gn1MoVdz90ZekGQH4VRgr8OTjf4H5SXGxXSS2F%2FGCyM%2FN%2FsSOHGYh9%2BymKCcrbH7zhyv6R8RveFpI36UHhuhUgoKUAspvIyO%2BvZnZf9evNkXuHux%2Fn3XJTVy%2BTFtZHMo%2Fn9id2KNKu7UxEs1Jm2SbqDaAwE6HDH%2FHLncry74HQ54bID62Xbr9Ob2ij&X-Amz-Signature=e2f13c891b1a7b645d4d5d8956c6782060f6e55611a5ba148c44d6b53a4b135b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







