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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627P7PYOE%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFNgXWwF7aQMD%2FZDhrsugF3E1B9skth2PLi7sQ1g9uKsAiEA6QtyvMhLdO0xjKE4WpdmXJ6kOT2uMbhvFvGCp3wQNS0qiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBlL0pEOtKbKW7HcNircA1jhjZ%2Bg1aAx8tNFTd6L9rCYcPtLkuZrNg1txuxTbXQd%2BhsenLRCEydOHF2pCJhbGriHxzU7aSdWh03do7HrBDsRIA3XfiaazFDTv%2BirT%2FOkTn0ZOc9mZrQjLWTP28pFc6Q9dbWDydnz1jLa79lGOCWe5LVAA4k%2FFok%2BlCZrFgCJ1562FRKn312ltLWmbb3XQ7ZLh%2FjafOfDC1MXgDacqb4AFwYbSY7nofh1hDhXFBsH1ROqVVjBKaGkw0oLr5Lgm0148gp9sFYVzw8uqMbM9LcvMn2yFgBfKhF9j%2F3wYA0mxtVj8SrCKo%2BtmWIQwry3w5epNJB0OCFQIQtwc3pUySanthy4XfuN3AJJNoe24UqehYw%2BXuEe3EdOHFtmJ5UymJXE9fmRdgGrdyd19xttoDRTXa%2FZUatMXeUGKVbiLPE3SuAEnLpLA9SN9PmgRsTXa77WL838TAMhUCx7z45f3rRhU7wn0Ea4Xgxhlb%2FVQ3nnVaZSSQlOiLiBhPxnit9XbaTqra769M%2FcGRlyo%2BNLM07OZ%2FEx%2B9hs8VYf2bXiv0AFaONYBFUcFLs0iFjJo2OnxmVro58338tbTQz3dvoMCw%2Ff0KHIYEHAWU15C5CGkfskC2hYCbnJTd%2FnG%2B40MIi95MwGOqUBQtgOPjS31lESimaA9pcHhKTcKhE3LmHkYdQhMKl2tpGA2JxB7QqgI89YoBxKvMKUGehjZ0CfhA%2FvJlj4%2Fey2GbpYEd%2F2ZxliPfRGrJCXL43UJUWqufs%2BnCYB3E2jj875yq9iEQi%2FceL1NvI8uBa%2Btz3s%2BKiaoyI%2Bl%2B3Fh%2BU9t7PODa1n6dNdTglqSHrUN6QylYMXb%2FsPO9ln%2F1chXqHO4fE34D6R&X-Amz-Signature=ca9c3fc4a690537f4e5c338fb5e24086106e040135216e42c4f00f9105de6014&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627P7PYOE%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFNgXWwF7aQMD%2FZDhrsugF3E1B9skth2PLi7sQ1g9uKsAiEA6QtyvMhLdO0xjKE4WpdmXJ6kOT2uMbhvFvGCp3wQNS0qiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBlL0pEOtKbKW7HcNircA1jhjZ%2Bg1aAx8tNFTd6L9rCYcPtLkuZrNg1txuxTbXQd%2BhsenLRCEydOHF2pCJhbGriHxzU7aSdWh03do7HrBDsRIA3XfiaazFDTv%2BirT%2FOkTn0ZOc9mZrQjLWTP28pFc6Q9dbWDydnz1jLa79lGOCWe5LVAA4k%2FFok%2BlCZrFgCJ1562FRKn312ltLWmbb3XQ7ZLh%2FjafOfDC1MXgDacqb4AFwYbSY7nofh1hDhXFBsH1ROqVVjBKaGkw0oLr5Lgm0148gp9sFYVzw8uqMbM9LcvMn2yFgBfKhF9j%2F3wYA0mxtVj8SrCKo%2BtmWIQwry3w5epNJB0OCFQIQtwc3pUySanthy4XfuN3AJJNoe24UqehYw%2BXuEe3EdOHFtmJ5UymJXE9fmRdgGrdyd19xttoDRTXa%2FZUatMXeUGKVbiLPE3SuAEnLpLA9SN9PmgRsTXa77WL838TAMhUCx7z45f3rRhU7wn0Ea4Xgxhlb%2FVQ3nnVaZSSQlOiLiBhPxnit9XbaTqra769M%2FcGRlyo%2BNLM07OZ%2FEx%2B9hs8VYf2bXiv0AFaONYBFUcFLs0iFjJo2OnxmVro58338tbTQz3dvoMCw%2Ff0KHIYEHAWU15C5CGkfskC2hYCbnJTd%2FnG%2B40MIi95MwGOqUBQtgOPjS31lESimaA9pcHhKTcKhE3LmHkYdQhMKl2tpGA2JxB7QqgI89YoBxKvMKUGehjZ0CfhA%2FvJlj4%2Fey2GbpYEd%2F2ZxliPfRGrJCXL43UJUWqufs%2BnCYB3E2jj875yq9iEQi%2FceL1NvI8uBa%2Btz3s%2BKiaoyI%2Bl%2B3Fh%2BU9t7PODa1n6dNdTglqSHrUN6QylYMXb%2FsPO9ln%2F1chXqHO4fE34D6R&X-Amz-Signature=dd3aea3307d03334215f40a49eb10cc3783a95593142c55355e69a59f0449e7d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







