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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URNPBWYA%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030254Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCylRLcvFQqkUAeiSXxsTTyS63VTHpZJ4BHz45%2FneCBVQIhAMvk%2FxJkJa7F7X%2FQsrLeqOCeoB4dtHBfGODsx%2Fo87D03KogECKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgytsJ38cO4GB9Yk2nYq3AMwx7R6Z1rhtpem3NM%2BDZJM3fPylGH1NDRtaFXmjIiV3w0ajR0ofvOPtqCTl%2BGCRKE1Zia6gaoP3418RwAaVQ%2FGoH4T%2B7I%2BWKC62POAPEzcclsFyAMe7LuFhPOt9Whcfo46hyKKZh160svBg5UTXRKG90pErwjA51BX4MD3w%2F%2FgMLUY8qZjlsI3%2FINgG4El44YyaUHTnEBe0%2B59IgQYP%2B0W%2FYeqocQsKRNCtxkxdx6ljyNL0NQnHoFl%2BLnCse62pwikXUtYvXCd9pZbzx6trQNeVFXqDs1e4FgAfYm2BOY3sdJqGYZ4yj%2F4fb8x5DtOoMHQYp8cDCMF06nm1i2G6G8WS0pDo3CHLt8Rx2fiGYv12zAc6aedEGmQD7M0RrmViHENHc%2F7kJydTMcr7i5Vhpvz%2F3DlhLdxy%2F0%2BqUgQvUxX8zzglpdmPP%2BMGDWiBWAttH%2FA17UjqK7TsiMJuJFdCxljDn%2B87Fjk4Y%2FcS48Uzc1yq4hslxMOt7oDqt4V7MTikczswcq0oe3sW4eeGfc1i%2FCGzi31cMXydClShvGizi74V7%2B%2BPsdQpIa%2Be1PoecQ44XeoaF6RmtvlDbQ3n78DIUrVnjTl%2BF%2FzTw2FAYbniONfXEOoN178MydVLwFX7jDz9LrLBjqkAUmEQBXhzSTSO3T0snaGbEDE%2B%2BEjqOaum8YvdK5SSGu%2B%2BPWyXM8fhFUm%2BAqZdzTTsYxL0k0aZQ53siJyMKVkXeGdx3goWDB8KtqJTUPO8KzGKmyH5o5t0A0Kv5A0bjaDT7YjBt7g1P6udBUPZGQ9fYa3HINmF%2FfTWLlr2MEKy%2Fh1vQV2PFM0tsTMXJuU35rN4g1hqb1usa9Ir1H7Tg5zB1%2Fadcm2&X-Amz-Signature=4a0f9d14665151ec0cb93c7e0a2553929320ab3c10636912844c9c16d40946ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URNPBWYA%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030254Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCylRLcvFQqkUAeiSXxsTTyS63VTHpZJ4BHz45%2FneCBVQIhAMvk%2FxJkJa7F7X%2FQsrLeqOCeoB4dtHBfGODsx%2Fo87D03KogECKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgytsJ38cO4GB9Yk2nYq3AMwx7R6Z1rhtpem3NM%2BDZJM3fPylGH1NDRtaFXmjIiV3w0ajR0ofvOPtqCTl%2BGCRKE1Zia6gaoP3418RwAaVQ%2FGoH4T%2B7I%2BWKC62POAPEzcclsFyAMe7LuFhPOt9Whcfo46hyKKZh160svBg5UTXRKG90pErwjA51BX4MD3w%2F%2FgMLUY8qZjlsI3%2FINgG4El44YyaUHTnEBe0%2B59IgQYP%2B0W%2FYeqocQsKRNCtxkxdx6ljyNL0NQnHoFl%2BLnCse62pwikXUtYvXCd9pZbzx6trQNeVFXqDs1e4FgAfYm2BOY3sdJqGYZ4yj%2F4fb8x5DtOoMHQYp8cDCMF06nm1i2G6G8WS0pDo3CHLt8Rx2fiGYv12zAc6aedEGmQD7M0RrmViHENHc%2F7kJydTMcr7i5Vhpvz%2F3DlhLdxy%2F0%2BqUgQvUxX8zzglpdmPP%2BMGDWiBWAttH%2FA17UjqK7TsiMJuJFdCxljDn%2B87Fjk4Y%2FcS48Uzc1yq4hslxMOt7oDqt4V7MTikczswcq0oe3sW4eeGfc1i%2FCGzi31cMXydClShvGizi74V7%2B%2BPsdQpIa%2Be1PoecQ44XeoaF6RmtvlDbQ3n78DIUrVnjTl%2BF%2FzTw2FAYbniONfXEOoN178MydVLwFX7jDz9LrLBjqkAUmEQBXhzSTSO3T0snaGbEDE%2B%2BEjqOaum8YvdK5SSGu%2B%2BPWyXM8fhFUm%2BAqZdzTTsYxL0k0aZQ53siJyMKVkXeGdx3goWDB8KtqJTUPO8KzGKmyH5o5t0A0Kv5A0bjaDT7YjBt7g1P6udBUPZGQ9fYa3HINmF%2FfTWLlr2MEKy%2Fh1vQV2PFM0tsTMXJuU35rN4g1hqb1usa9Ir1H7Tg5zB1%2Fadcm2&X-Amz-Signature=78cc491ce2a081e2eb024429fb357e5780bb789332a474529093ffbb05657e61&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







