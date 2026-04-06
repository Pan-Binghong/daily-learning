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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCEXRSVG%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T040845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCvN304NCsxH0GFDUj6aZb3bSFv%2BozLR%2FTcPP%2FX8yKXvAIgQ789NDptLRaYfIzG3n6WGHULJyS6QSR3%2FGtq7V1Y0VUqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJy0euinhP02jyMNrSrcA24TqVzZbPqrlYNC4ZeNfGRmSihEy2v4hKZ15rqOr%2FrPoyfvlI5C6jQ04XtcKW%2F9imUgAVXeBaddZh1Tksi8dlKUKB2v09xmnnWarij8y4T5wKufJkKUgwLbZWQoGp2%2F3k7sswe6bI1Jvqo7aG4dhfZrxwGE94PDjiRUPqChSr7f7SfBdRk4OscKhB4UJDvgDNvSTaBT8HhpabCYtqa3Oulx%2Bz8E8ZMaCzCxrN8yR9iHi6Z6py9Du%2B3hFka2Ioqdsf5n29vuK37OuSNIOGiMwf4Ke1dyz4Ynu9JXh4lw3tBtTHkcdewFegBfojeyiviyWdSvrxt9%2BYlE73yZMkmhj4TYPfr9vufjc8OZZO%2BSHFHgCoOHKUssCTSE19XsYXpkd731rDFE%2Br5i3WmmtXBnIzAn8XSLxcpAoYGZX3HpMy4il2cYQuFzLbIbKNhAChGSLLf4%2B5PN2m1OhJlbmRXUo7cFGwTB3%2FApTPAWbvjBkQfol78bRFsNy76wIxeJU4BQh1mqOO%2FD0LE2CWSn6%2Fcr7%2Fsa2JAuwryJ7x7dvMD%2BTwWV6UZ2MztfPv4wnp1UKXcotR0OAlLigjVzBxMd1mpg1zfVj3rBu1GUfS3tTQ%2FSbxVOJ1PFman0fh18gACPMO%2ByzM4GOqUB8BNCyZPqkJYZJYBZRRRgVrkvRm5i2TYs94V343Q%2BTmotGgoljXkD5Vc%2FsBrmnC8LifFRKhElELwrcquWAhm2QNxTAw7PY0PBMRlemcLTDj6Insyeon4ZYQr8GHVogsHHevcw%2BHfVZDQoVwz3ZnM59X5oc6rUs1ma2hRDcwke4Tp%2B4VtJvA1rGGEKnac7RoCOiuxIQe28Bkq2kcyZaacB2RJKUO%2BD&X-Amz-Signature=cf29a16373c3b5203c5c4a0d59420db6fed9407ebdc13cef591f71213cedf6e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TCEXRSVG%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T040845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCvN304NCsxH0GFDUj6aZb3bSFv%2BozLR%2FTcPP%2FX8yKXvAIgQ789NDptLRaYfIzG3n6WGHULJyS6QSR3%2FGtq7V1Y0VUqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJy0euinhP02jyMNrSrcA24TqVzZbPqrlYNC4ZeNfGRmSihEy2v4hKZ15rqOr%2FrPoyfvlI5C6jQ04XtcKW%2F9imUgAVXeBaddZh1Tksi8dlKUKB2v09xmnnWarij8y4T5wKufJkKUgwLbZWQoGp2%2F3k7sswe6bI1Jvqo7aG4dhfZrxwGE94PDjiRUPqChSr7f7SfBdRk4OscKhB4UJDvgDNvSTaBT8HhpabCYtqa3Oulx%2Bz8E8ZMaCzCxrN8yR9iHi6Z6py9Du%2B3hFka2Ioqdsf5n29vuK37OuSNIOGiMwf4Ke1dyz4Ynu9JXh4lw3tBtTHkcdewFegBfojeyiviyWdSvrxt9%2BYlE73yZMkmhj4TYPfr9vufjc8OZZO%2BSHFHgCoOHKUssCTSE19XsYXpkd731rDFE%2Br5i3WmmtXBnIzAn8XSLxcpAoYGZX3HpMy4il2cYQuFzLbIbKNhAChGSLLf4%2B5PN2m1OhJlbmRXUo7cFGwTB3%2FApTPAWbvjBkQfol78bRFsNy76wIxeJU4BQh1mqOO%2FD0LE2CWSn6%2Fcr7%2Fsa2JAuwryJ7x7dvMD%2BTwWV6UZ2MztfPv4wnp1UKXcotR0OAlLigjVzBxMd1mpg1zfVj3rBu1GUfS3tTQ%2FSbxVOJ1PFman0fh18gACPMO%2ByzM4GOqUB8BNCyZPqkJYZJYBZRRRgVrkvRm5i2TYs94V343Q%2BTmotGgoljXkD5Vc%2FsBrmnC8LifFRKhElELwrcquWAhm2QNxTAw7PY0PBMRlemcLTDj6Insyeon4ZYQr8GHVogsHHevcw%2BHfVZDQoVwz3ZnM59X5oc6rUs1ma2hRDcwke4Tp%2B4VtJvA1rGGEKnac7RoCOiuxIQe28Bkq2kcyZaacB2RJKUO%2BD&X-Amz-Signature=8995e7414f7635889b5e2042add0c49f03161e217494e63c9e82e7b85d574bcc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







