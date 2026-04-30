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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UP4BCT3Q%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T043411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIHzEIi%2B6AeB8VB5rLiMiZcLtZaM97EbFazPb3OZI5rflAiEA1EbrnK3cQAZ%2F%2FxLugv66%2BQRfXg0qEwcTZqk5VT5rhu4q%2FwMIBhAAGgw2Mzc0MjMxODM4MDUiDPYvikb63%2Feqp3JYUircAzU2fG%2B5Fo3HP1QGLk0krDkDM7Q%2BmYTpkh%2FcXmRru5dr86epZfhd1Ya3cRmsOVKpRfYHYkBIAeUDOmyAttKzXDP3MEdj%2BzvCYxP4a%2FgvFVqX92LboijbDc9C2W4xZ7GiaQ8%2BJcjps0rMA09%2BqxiQowC6frDBVLs4GsJgD18MVQCLs7TPU6uTqI6EeKXdFbkaaOgqM31YF2YEd9VBvcDdvw4zWAOFNCNQAkIwlkHfK18A7L4sb4RsPb0je%2FZztKU9ItTO5tIoP0ZKCNrIGD3MHxR%2Binaeh1M3q4rqySksQqELABOdIxCGt1y8jHCjl9DvUhV%2FlJ%2BTeLYsYSmbkpK5USMN7cAqTi7elWKz5jyE8GKcdAFmo7hWQYUWjNOBbSkyE%2Bt3pa2LTKnQ7pi3ugqG90bwkKStouTLKdsAx3JHmopbjLARlgO8Hf87jLtcjNIp%2FhPhZe16SsJMiFkph79WMCTuIjO9YbnGqpxouI6h777e6uNGHc8%2BnWjpWkyh5H7%2BosRd89kCPE%2F%2FkeokW7tf56Y9P7D2sn%2FmB67QW7rvD%2BD3nevGyJk9QL3Lg9%2FmcMnbbe5arrnUwLWCixH%2B3YOJObxwGOnXn%2BK2BU0kxueVhRI0G6QCelc%2FngOg8XGdML2zy88GOqUBkHyhDzdMuP4Tb3gVnd9IBbg2wICP6Byz%2BsEmSKcxSi55zkHThwr%2BcvIzOQTNl6zHiZOc7rAaqb8tIjhOvX%2F8zo9RZAeg11L35DU53B7SiRR8DJzbcxp00aPVGC2T%2BdmH5rYQFqRU5yxpXrk0FGIOPpaAO6H%2FUH7fDKkcSQnc9wl8AXLYX1AXeioybH9V0OYdNOKSRZG2VosV53f88Tbn8eyqpZU0&X-Amz-Signature=04bb12731c26bfcd187fcf38cd0e2f41df7b73db45bf9a4e91e7a8d39e769227&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UP4BCT3Q%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T043411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIHzEIi%2B6AeB8VB5rLiMiZcLtZaM97EbFazPb3OZI5rflAiEA1EbrnK3cQAZ%2F%2FxLugv66%2BQRfXg0qEwcTZqk5VT5rhu4q%2FwMIBhAAGgw2Mzc0MjMxODM4MDUiDPYvikb63%2Feqp3JYUircAzU2fG%2B5Fo3HP1QGLk0krDkDM7Q%2BmYTpkh%2FcXmRru5dr86epZfhd1Ya3cRmsOVKpRfYHYkBIAeUDOmyAttKzXDP3MEdj%2BzvCYxP4a%2FgvFVqX92LboijbDc9C2W4xZ7GiaQ8%2BJcjps0rMA09%2BqxiQowC6frDBVLs4GsJgD18MVQCLs7TPU6uTqI6EeKXdFbkaaOgqM31YF2YEd9VBvcDdvw4zWAOFNCNQAkIwlkHfK18A7L4sb4RsPb0je%2FZztKU9ItTO5tIoP0ZKCNrIGD3MHxR%2Binaeh1M3q4rqySksQqELABOdIxCGt1y8jHCjl9DvUhV%2FlJ%2BTeLYsYSmbkpK5USMN7cAqTi7elWKz5jyE8GKcdAFmo7hWQYUWjNOBbSkyE%2Bt3pa2LTKnQ7pi3ugqG90bwkKStouTLKdsAx3JHmopbjLARlgO8Hf87jLtcjNIp%2FhPhZe16SsJMiFkph79WMCTuIjO9YbnGqpxouI6h777e6uNGHc8%2BnWjpWkyh5H7%2BosRd89kCPE%2F%2FkeokW7tf56Y9P7D2sn%2FmB67QW7rvD%2BD3nevGyJk9QL3Lg9%2FmcMnbbe5arrnUwLWCixH%2B3YOJObxwGOnXn%2BK2BU0kxueVhRI0G6QCelc%2FngOg8XGdML2zy88GOqUBkHyhDzdMuP4Tb3gVnd9IBbg2wICP6Byz%2BsEmSKcxSi55zkHThwr%2BcvIzOQTNl6zHiZOc7rAaqb8tIjhOvX%2F8zo9RZAeg11L35DU53B7SiRR8DJzbcxp00aPVGC2T%2BdmH5rYQFqRU5yxpXrk0FGIOPpaAO6H%2FUH7fDKkcSQnc9wl8AXLYX1AXeioybH9V0OYdNOKSRZG2VosV53f88Tbn8eyqpZU0&X-Amz-Signature=1242893bba8b096ce2491a6f6bf517022aae79f763384ab3f7200f09ba939c46&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







