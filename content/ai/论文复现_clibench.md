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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676CDXZRY%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025805Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBoHAkl61iHS8amKUQZF9jnJPbDiCCtzu9ny5lERgCRVAiBqdzJGWkBXhP8tWlpnHIChwvZpT8yTrMHv5NMDt4jxsiqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOmpzrI%2F2jJJtRaGhKtwDuL91PhxUUFaSrqLYsgkmB1BPLmjRSh7MpxfivFn91WRJDsI4RL2wikxsQnRtHU4R9HpqoY8EHQffGnTcWwCwF%2Bwi24%2FOj%2BV1OCmwg7e13quiXZ6ZRnQo6461auoNwPnZWf6E1jEKxdfZFYkH4MOJyYdJUySrC8fPXr7hIeoO4lNkJoLVGoT%2B9MT4WlXLE3ZLn%2BYCG2%2B3sTLAqOKK%2Fcj78ASGnFELG9uqXPrsDVjsDiirpSsBNUGyU3IwYkIcIq2XUMHNBQluty3T2WhVhbiLr%2FqkAfuwfXLD1IEgfSAhErKyyfDWcha6jAeN23FKNdlJiKViBb0nmvwtx39msUpd7DzkMOgOMN2QgV1oh39pC2%2BIYr9sonUhXHABkCZC06PboTeLO86MsqxdtEiYm7oE1A%2B45X8hKF2BMaK1Ovq3QKuLnFKj0xNPj1isLzQdTZ3303qlUqJ97F063fUcBqQcUd7iVZEH9pzdKB3lumobn4nxy6NweGTBVNXsORqhSqnz90aCK6zmC2B2kPvZl%2F9sRvqff4w5xBKFJ3G3LHM1%2BYurkYsNtlITx1GDCErBAKXXvTP4vtPX%2Fta4K%2FzHBCwpCmMEU%2BEiWjvr3C7Y1qaIDfVtL%2Fk7IiGSpC9Q4Jkwjf7SyQY6pgGRfCv1dGt46kAoqMNAtiCjp6MwPR93cG7H%2BRVz1Axx3mEjE7VjevtarZgEm44Y2gvq6vtSAxLdxnCi5TeE%2FxRB%2BUW%2FDxMjK%2FrgNS5dMffGS5heSZf4TIBjzncEzGnn9HUOroSXBktmCSE5QXWzfbJIQDOD1d2tfAMCG09pZK%2FPwjiX%2FN63ZpPB4kg5bRN6QQ2krP1cwAaY1KeCBRhWQmD7gWPErGhl&X-Amz-Signature=0f3c1fc1bc8131d2f1ee0f70fe4151c83f8233ae5440d9fd1418123d76862a6b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676CDXZRY%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025805Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBoHAkl61iHS8amKUQZF9jnJPbDiCCtzu9ny5lERgCRVAiBqdzJGWkBXhP8tWlpnHIChwvZpT8yTrMHv5NMDt4jxsiqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOmpzrI%2F2jJJtRaGhKtwDuL91PhxUUFaSrqLYsgkmB1BPLmjRSh7MpxfivFn91WRJDsI4RL2wikxsQnRtHU4R9HpqoY8EHQffGnTcWwCwF%2Bwi24%2FOj%2BV1OCmwg7e13quiXZ6ZRnQo6461auoNwPnZWf6E1jEKxdfZFYkH4MOJyYdJUySrC8fPXr7hIeoO4lNkJoLVGoT%2B9MT4WlXLE3ZLn%2BYCG2%2B3sTLAqOKK%2Fcj78ASGnFELG9uqXPrsDVjsDiirpSsBNUGyU3IwYkIcIq2XUMHNBQluty3T2WhVhbiLr%2FqkAfuwfXLD1IEgfSAhErKyyfDWcha6jAeN23FKNdlJiKViBb0nmvwtx39msUpd7DzkMOgOMN2QgV1oh39pC2%2BIYr9sonUhXHABkCZC06PboTeLO86MsqxdtEiYm7oE1A%2B45X8hKF2BMaK1Ovq3QKuLnFKj0xNPj1isLzQdTZ3303qlUqJ97F063fUcBqQcUd7iVZEH9pzdKB3lumobn4nxy6NweGTBVNXsORqhSqnz90aCK6zmC2B2kPvZl%2F9sRvqff4w5xBKFJ3G3LHM1%2BYurkYsNtlITx1GDCErBAKXXvTP4vtPX%2Fta4K%2FzHBCwpCmMEU%2BEiWjvr3C7Y1qaIDfVtL%2Fk7IiGSpC9Q4Jkwjf7SyQY6pgGRfCv1dGt46kAoqMNAtiCjp6MwPR93cG7H%2BRVz1Axx3mEjE7VjevtarZgEm44Y2gvq6vtSAxLdxnCi5TeE%2FxRB%2BUW%2FDxMjK%2FrgNS5dMffGS5heSZf4TIBjzncEzGnn9HUOroSXBktmCSE5QXWzfbJIQDOD1d2tfAMCG09pZK%2FPwjiX%2FN63ZpPB4kg5bRN6QQ2krP1cwAaY1KeCBRhWQmD7gWPErGhl&X-Amz-Signature=8afe5943c14c797efa89c181e3b1e1c51dee054bba81f1f14596182138b757e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







