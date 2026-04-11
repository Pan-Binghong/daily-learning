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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667II7JAWJ%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T033920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCIGSuMcxG2wAfO47X70zC0llr5K%2FhHPLWrG0VH90MQ0k8AiAWQCj21I%2BRf%2Bu8ae%2FIhyemHFjN8l32J69OAGv%2FNGCniyr%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMaMQ43BUAg4TbFLcKKtwDsom0H1zRfe2I6KqP%2BMx1o75lYWVEELhUJ8yDAmCOMp5Av%2FXQ1ozNk%2FvF7UvC7Y9%2FPVrh6LmRczx3vJ0Hj2WN02iZuAddHFj8tztRzc4JNhdzswpPeK0jU6HpU5ykiJT6NiwtswSBLADnDkQJCRufRPjJNJmcsM%2F0ZbDk0e98XpsVKcF6pPB6%2BZG7PEuPIpfZdP3%2BxjauPOkwogD7NAWonGCHNdVEmfs%2BM%2FxnUGMFDF00Sp2%2Fow%2B99KqA088Fr2BuTm0VOgjJDQn64C7lsGClbh2KgpqAhT4Vol2Ult2%2Btfk3QF1YGKHXiUmVkqwqCKrK%2FO%2FJEIU%2FTWqa66NoKHEN2kwz%2Bv5xxlXbQ2ZHpZBjMIhHUZvCR0NfwrhNI6nr%2FiHbZmG8gGj5Dt6dzqv%2FtFbEZ9pcNxSIJ%2B%2Fe5qj5wWFB%2BNDlu%2FtmmgdrWGoHEDI8efFPXmvFUfFZ4OWJhldwkY9s5%2BoPQRfX%2BKBUbtirUMwhlMqOLENoaL0FWzSaKd3XTyUpO3EeXM2SSVUTiwEG4uwfL0fkwKxizmDte3gtSM11VVKnNYg%2Bn26MSBW3rZde9OuZY4wIXP6ASdNGwajU0h6%2FjqB6BtQ%2Bvnb5skVDS%2FW7DFUzaVLPXXphhdNzVYkw2ermzgY6pgFqnU9C8VFoOQLGDojSirB4bBIrvw77TeXbuUNhVLuQzF1Cb73lbZDEo9d3NsJ8b5vREMEySIxXlsOrh1FI7i3fqD1P1e4gaPw%2B%2FTc%2BLb2ESjtY%2Fj6GRqvuML4ThgaywzelQgarxRrXuxPQnCzHFGBwH9MYwqNwYoFNhHNP%2Fs%2BGFelIlFGZdrCc%2F6cTeZaIPskL%2FsJTDamXnT7ZGNSay5K%2FoTg1HUWg&X-Amz-Signature=2945af1310d6c8edb15b8b6bd7eed08ee10059dde863d56d03129cf7f8864f40&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667II7JAWJ%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T033920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCIGSuMcxG2wAfO47X70zC0llr5K%2FhHPLWrG0VH90MQ0k8AiAWQCj21I%2BRf%2Bu8ae%2FIhyemHFjN8l32J69OAGv%2FNGCniyr%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMaMQ43BUAg4TbFLcKKtwDsom0H1zRfe2I6KqP%2BMx1o75lYWVEELhUJ8yDAmCOMp5Av%2FXQ1ozNk%2FvF7UvC7Y9%2FPVrh6LmRczx3vJ0Hj2WN02iZuAddHFj8tztRzc4JNhdzswpPeK0jU6HpU5ykiJT6NiwtswSBLADnDkQJCRufRPjJNJmcsM%2F0ZbDk0e98XpsVKcF6pPB6%2BZG7PEuPIpfZdP3%2BxjauPOkwogD7NAWonGCHNdVEmfs%2BM%2FxnUGMFDF00Sp2%2Fow%2B99KqA088Fr2BuTm0VOgjJDQn64C7lsGClbh2KgpqAhT4Vol2Ult2%2Btfk3QF1YGKHXiUmVkqwqCKrK%2FO%2FJEIU%2FTWqa66NoKHEN2kwz%2Bv5xxlXbQ2ZHpZBjMIhHUZvCR0NfwrhNI6nr%2FiHbZmG8gGj5Dt6dzqv%2FtFbEZ9pcNxSIJ%2B%2Fe5qj5wWFB%2BNDlu%2FtmmgdrWGoHEDI8efFPXmvFUfFZ4OWJhldwkY9s5%2BoPQRfX%2BKBUbtirUMwhlMqOLENoaL0FWzSaKd3XTyUpO3EeXM2SSVUTiwEG4uwfL0fkwKxizmDte3gtSM11VVKnNYg%2Bn26MSBW3rZde9OuZY4wIXP6ASdNGwajU0h6%2FjqB6BtQ%2Bvnb5skVDS%2FW7DFUzaVLPXXphhdNzVYkw2ermzgY6pgFqnU9C8VFoOQLGDojSirB4bBIrvw77TeXbuUNhVLuQzF1Cb73lbZDEo9d3NsJ8b5vREMEySIxXlsOrh1FI7i3fqD1P1e4gaPw%2B%2FTc%2BLb2ESjtY%2Fj6GRqvuML4ThgaywzelQgarxRrXuxPQnCzHFGBwH9MYwqNwYoFNhHNP%2Fs%2BGFelIlFGZdrCc%2F6cTeZaIPskL%2FsJTDamXnT7ZGNSay5K%2FoTg1HUWg&X-Amz-Signature=0ec01ff478a30519ad80ab119dadd22f5a2bfec16d94d7f3d19eb722135cad3d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







