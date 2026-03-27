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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466276KUC3B%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQDqWHnpM6nn7otl2QvLG5cT%2BAj%2BtlA1E4aEc6wg%2BLRRtAIhAI7nRVjaXXwS6WfSPNsTRVNycphcRyJvX24h%2Fki9gVQJKogECM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxOIkr9wtOL6No4gbUq3ANbMigsqNP6rZMaIZZFH%2FEmRqMIT5dH8y1nxIGnYFZ%2BnW4tAgLu%2BfFnkqd9YfTXb05h6RMwETBKFnSfrLY6QQFStbp%2B%2FIHEQATTGOPgXPPGpY%2FOxS424SA0wy772%2B19FDZE7zvpPT7rOMOWPGeX9IzOqCeU7SB4hfjZxHivQ1snZP%2FIivfjfo4rZUv0XfM8sqpS49sJYpszschn%2FByZdAzIibY%2F3STIYtaY6Hsv9v6%2FVxTJ6CGZHwylBhS4uGmVFc3QQDL54M4DkCHWpS47MSciIMGP5dGQUk0zMZUQ5E53TaNEUtWnElZgBEht%2FhxD%2FI5m7PXJyO1oWAWYs2I%2By69nxYDkHYb9rNiJlj3d3S4vIPxI6oQ2jUilKwTKPyW3duiHc1%2BQjHN%2B1ZKzSS8BULRGDkshnTyyuONbP9jodB8B6AORmxSuBaIXiWZmxlW3fHG%2B3VOlo8%2FP56XrFOiS9hA9%2FvheKyDgUD%2BEiTgbrA3160cg9t4ukiKW9%2BHfeAeWu4ZdLYxg1ro5MneV8xtPMtDSGOkFEy6CiHzl1kJA5%2BOdWYDUfKukAEt8LO%2Bo9sjdMM%2BxNfX9zPR0NztUmAja5D%2BVvW0AyJGyvlH4nXoQE4ALK5ML5o7uyILV8eZ9FzCz2JbOBjqkAf31zwXmqk30kvTW3w2e9VLQzgYu%2FfswhAg8aUCiTGZYAXhNBA7vtjNTxyPdv%2B62f8OUBy3QQQSMykJZq6aGhBS8Mp5yj7drFVwI0b5LHIGBuNNfQhheERK0Br0QEZy8huJwz4utzRtgbMxRiqFkSSa7EEpYm0ID%2Bjer16b%2BVQUJZwj6irDTXAm1kk0B2Vk%2FGD7bUbJ7476swYk6XyP0dB%2FEfHa1&X-Amz-Signature=9ae0989a16996bd8571ca51fcb111de5fd829c4a96c1bd22d5735d4d5ff499bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466276KUC3B%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJIMEYCIQDqWHnpM6nn7otl2QvLG5cT%2BAj%2BtlA1E4aEc6wg%2BLRRtAIhAI7nRVjaXXwS6WfSPNsTRVNycphcRyJvX24h%2Fki9gVQJKogECM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxOIkr9wtOL6No4gbUq3ANbMigsqNP6rZMaIZZFH%2FEmRqMIT5dH8y1nxIGnYFZ%2BnW4tAgLu%2BfFnkqd9YfTXb05h6RMwETBKFnSfrLY6QQFStbp%2B%2FIHEQATTGOPgXPPGpY%2FOxS424SA0wy772%2B19FDZE7zvpPT7rOMOWPGeX9IzOqCeU7SB4hfjZxHivQ1snZP%2FIivfjfo4rZUv0XfM8sqpS49sJYpszschn%2FByZdAzIibY%2F3STIYtaY6Hsv9v6%2FVxTJ6CGZHwylBhS4uGmVFc3QQDL54M4DkCHWpS47MSciIMGP5dGQUk0zMZUQ5E53TaNEUtWnElZgBEht%2FhxD%2FI5m7PXJyO1oWAWYs2I%2By69nxYDkHYb9rNiJlj3d3S4vIPxI6oQ2jUilKwTKPyW3duiHc1%2BQjHN%2B1ZKzSS8BULRGDkshnTyyuONbP9jodB8B6AORmxSuBaIXiWZmxlW3fHG%2B3VOlo8%2FP56XrFOiS9hA9%2FvheKyDgUD%2BEiTgbrA3160cg9t4ukiKW9%2BHfeAeWu4ZdLYxg1ro5MneV8xtPMtDSGOkFEy6CiHzl1kJA5%2BOdWYDUfKukAEt8LO%2Bo9sjdMM%2BxNfX9zPR0NztUmAja5D%2BVvW0AyJGyvlH4nXoQE4ALK5ML5o7uyILV8eZ9FzCz2JbOBjqkAf31zwXmqk30kvTW3w2e9VLQzgYu%2FfswhAg8aUCiTGZYAXhNBA7vtjNTxyPdv%2B62f8OUBy3QQQSMykJZq6aGhBS8Mp5yj7drFVwI0b5LHIGBuNNfQhheERK0Br0QEZy8huJwz4utzRtgbMxRiqFkSSa7EEpYm0ID%2Bjer16b%2BVQUJZwj6irDTXAm1kk0B2Vk%2FGD7bUbJ7476swYk6XyP0dB%2FEfHa1&X-Amz-Signature=71d7f643709dd0d58e774de47aa32d8b172d941f6119132eba8f0c4acbb3c8b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







