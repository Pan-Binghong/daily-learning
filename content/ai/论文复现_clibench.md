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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRZV2SZZ%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJGMEQCIA9zp5MP9jVxqVjql4XeuBMGV7u%2B2p7WwpEiXYXaZR%2FdAiBO0xuRQ9VGLwkOM1l7nt4po7Z4U9pvN91AjlW9Pgy9sCr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMRgtXtonl1ZdICqqgKtwDWrtW1IUP3IlgsND1b3%2FkhSzBuH2r3FIiX5YB724LhZLat4sPQl6fx0u4RkljjnzRBrF%2BBRogz1ZH%2FeoFss60C%2BxoYlTBrG6ZTObigBBoTgdy8oyoSTTNCsl28CXF1aB4eMyt2KXORy%2FG7549AMpA8yKxKJILgKGLulkPgeFgx6aeB4UNrtbVzTNXVjTx%2BXqhcQxLoKFMUqHZ60w0FnRvfaZ7RZJQktviQCqqSTEAInDoqM7%2BYcC8L94Yo9q4yL8AGd1SeDEdlFONoZw4nB7h%2BfPdT5IU6EVu5ElX5ZzeWYyLeIqYXOjgmCQilY0%2BtpFLrjXfgx9B08P9lJjM9fGjBZPxDMDGbPl0oqwpQVUcrvOpYBDkGHVdW92sT8RhlJFsB%2FVaVivhq3PsOj%2B7asQSvso%2FCWSgtjuKUITym6ngxUwctDl3M99669P41eHaULX%2FtvUHPOrl9Aq6hgM4i2bCvcM%2BywUqYc11JIqaQEG9vT6FlcqsaGs8vRvt%2FHZtIHJXVmtsjA%2BP0Oea21viGKh1piXcVfiVAUhL8SuEg%2FqcPXp%2BL%2Frk%2FwP2PV2kkQRRJRYAZ%2FpKC3t8Z2VhfVzAkDQeThfNPlRvvZI5cid9On1LaNQzh6MlHwb5dFMkvygwofCbywY6pgH1Rh5mtLDeYgQv2NIcC0MtfcWPIKK5kFC47IwnilVdz5k1ryD5H1zO910%2F7LnVBpz6tDaCFOs6lbbYEuroE0pfKufGXFkTPEuv9zOe6DU1cQuGk5rgFs5j4MCnKyrOnWSlcpqtLZw50P73fCPSSCAyEn5Zr2iCkMnfzP5Hflq6jnaRYE3Kzm3GzsbN%2FzqW8me5Fl7VYbDmLwDjgXJV9ZDbMgyB%2BUgn&X-Amz-Signature=58e2a9461355ec790d252ef9671c61e3417ba9d1624559d41622f3f0a57d76b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRZV2SZZ%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJGMEQCIA9zp5MP9jVxqVjql4XeuBMGV7u%2B2p7WwpEiXYXaZR%2FdAiBO0xuRQ9VGLwkOM1l7nt4po7Z4U9pvN91AjlW9Pgy9sCr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMRgtXtonl1ZdICqqgKtwDWrtW1IUP3IlgsND1b3%2FkhSzBuH2r3FIiX5YB724LhZLat4sPQl6fx0u4RkljjnzRBrF%2BBRogz1ZH%2FeoFss60C%2BxoYlTBrG6ZTObigBBoTgdy8oyoSTTNCsl28CXF1aB4eMyt2KXORy%2FG7549AMpA8yKxKJILgKGLulkPgeFgx6aeB4UNrtbVzTNXVjTx%2BXqhcQxLoKFMUqHZ60w0FnRvfaZ7RZJQktviQCqqSTEAInDoqM7%2BYcC8L94Yo9q4yL8AGd1SeDEdlFONoZw4nB7h%2BfPdT5IU6EVu5ElX5ZzeWYyLeIqYXOjgmCQilY0%2BtpFLrjXfgx9B08P9lJjM9fGjBZPxDMDGbPl0oqwpQVUcrvOpYBDkGHVdW92sT8RhlJFsB%2FVaVivhq3PsOj%2B7asQSvso%2FCWSgtjuKUITym6ngxUwctDl3M99669P41eHaULX%2FtvUHPOrl9Aq6hgM4i2bCvcM%2BywUqYc11JIqaQEG9vT6FlcqsaGs8vRvt%2FHZtIHJXVmtsjA%2BP0Oea21viGKh1piXcVfiVAUhL8SuEg%2FqcPXp%2BL%2Frk%2FwP2PV2kkQRRJRYAZ%2FpKC3t8Z2VhfVzAkDQeThfNPlRvvZI5cid9On1LaNQzh6MlHwb5dFMkvygwofCbywY6pgH1Rh5mtLDeYgQv2NIcC0MtfcWPIKK5kFC47IwnilVdz5k1ryD5H1zO910%2F7LnVBpz6tDaCFOs6lbbYEuroE0pfKufGXFkTPEuv9zOe6DU1cQuGk5rgFs5j4MCnKyrOnWSlcpqtLZw50P73fCPSSCAyEn5Zr2iCkMnfzP5Hflq6jnaRYE3Kzm3GzsbN%2FzqW8me5Fl7VYbDmLwDjgXJV9ZDbMgyB%2BUgn&X-Amz-Signature=c1dd32f3252f513a29156b560033f3a2a7713557536c6ea77f39c3d7b2c4518f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







