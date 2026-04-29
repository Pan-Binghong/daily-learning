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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJRZMKFC%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043142Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJIMEYCIQDuOyAuMKIqoZkxEIpM%2BUo24R6mkhBWEOxxuYnBk492ngIhAMi%2BWf0tYhEw%2FJUxn9DXMmjaprh7O0lV9A7w7a2SA8ouKogECOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyN8s4JVaFjUmd7drcq3APtuMXy8ua6w%2FFXIElV9CL1o9rFFRHcX85QPft1Q5u786mSMdBwcCNYXSww1O4LgzRcp2KsWizgQ5UOu%2FYMJBJd2ySc4Mv6Te4mx0FPT6z%2FI1YYK%2BZJ%2FS7iH4myBLVQ7b0g2kVmnFgY3U5tpOT4PREh3EJjT9HgvXA%2F%2Bq%2FvKgcUTAeHW9v5rbw1S0blukKspoh3GvXp7GBkr63QgBxWCscq%2FwGK0PLSBt97Fo54pPx8rcsI85ZpmXI4aRt09do5C1zrP1gbpSTkp3piMtqdPK0mqCc4Y0Ly%2Fc96m4qhj%2Fa1JEmGAN0vLWlq%2B5eBkzcRFaFXQ7tgLDgpctcaADupkY2DFxda8G3JuDmTmtL8mn%2FN%2BX7TIl%2FGVd1KND1cW6sP9X4D%2B5dKoV0UtuavtikdN6j7TbNmVpBY7%2F0PptdKDr2uSOiUn0tHrffhWGiWdN3%2BiTLCJuH2q68QRH3hup1jC5PCoYGiWviwZF3cTHS71VVb1dJL3Za96BQftemuVvr8%2Bskt0dfd2bD5ADJhx6BDMP0GEbC1hb6bIMk6kc3%2FuVNsT2COnIHATrlbAMkaaYdtlOnCYnq%2Bhl%2Fc7BrvUIfz%2Fqlz%2FCIKLzcGnKMg7G8wNlz6o%2BSRRbnPPZv%2BpCcLSTC97cXPBjqkAZtkZC%2Fs%2BXJPs34nfowQqvd25NDCxOVl4xkPN5mTkYEjcOjv4yp23hoJUUrR2E006htL8xRaLxTvsslqZow144oxyKc6%2BDZZLLcz0pSd8eX7aOnfKnG0z4pEYtqRXvbvZsAej2vgOJ3sDDmoYh3vIo9OnvesLH1WGO5vU%2FQfgKIk2GAGhJgKrT41gUNA6xWne9kYGJFzL%2FgD%2FUf1dpKm7UHHkHIw&X-Amz-Signature=e9ad8b20069b18d3d982b0dfc9bed5bfa18ed0d85eb237af11478a7e3509fac0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJRZMKFC%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043142Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJIMEYCIQDuOyAuMKIqoZkxEIpM%2BUo24R6mkhBWEOxxuYnBk492ngIhAMi%2BWf0tYhEw%2FJUxn9DXMmjaprh7O0lV9A7w7a2SA8ouKogECOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyN8s4JVaFjUmd7drcq3APtuMXy8ua6w%2FFXIElV9CL1o9rFFRHcX85QPft1Q5u786mSMdBwcCNYXSww1O4LgzRcp2KsWizgQ5UOu%2FYMJBJd2ySc4Mv6Te4mx0FPT6z%2FI1YYK%2BZJ%2FS7iH4myBLVQ7b0g2kVmnFgY3U5tpOT4PREh3EJjT9HgvXA%2F%2Bq%2FvKgcUTAeHW9v5rbw1S0blukKspoh3GvXp7GBkr63QgBxWCscq%2FwGK0PLSBt97Fo54pPx8rcsI85ZpmXI4aRt09do5C1zrP1gbpSTkp3piMtqdPK0mqCc4Y0Ly%2Fc96m4qhj%2Fa1JEmGAN0vLWlq%2B5eBkzcRFaFXQ7tgLDgpctcaADupkY2DFxda8G3JuDmTmtL8mn%2FN%2BX7TIl%2FGVd1KND1cW6sP9X4D%2B5dKoV0UtuavtikdN6j7TbNmVpBY7%2F0PptdKDr2uSOiUn0tHrffhWGiWdN3%2BiTLCJuH2q68QRH3hup1jC5PCoYGiWviwZF3cTHS71VVb1dJL3Za96BQftemuVvr8%2Bskt0dfd2bD5ADJhx6BDMP0GEbC1hb6bIMk6kc3%2FuVNsT2COnIHATrlbAMkaaYdtlOnCYnq%2Bhl%2Fc7BrvUIfz%2Fqlz%2FCIKLzcGnKMg7G8wNlz6o%2BSRRbnPPZv%2BpCcLSTC97cXPBjqkAZtkZC%2Fs%2BXJPs34nfowQqvd25NDCxOVl4xkPN5mTkYEjcOjv4yp23hoJUUrR2E006htL8xRaLxTvsslqZow144oxyKc6%2BDZZLLcz0pSd8eX7aOnfKnG0z4pEYtqRXvbvZsAej2vgOJ3sDDmoYh3vIo9OnvesLH1WGO5vU%2FQfgKIk2GAGhJgKrT41gUNA6xWne9kYGJFzL%2FgD%2FUf1dpKm7UHHkHIw&X-Amz-Signature=266ba758baa6482e9d146485cb5fa593a3353f062e77a6a388ccafd349a4c6c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







