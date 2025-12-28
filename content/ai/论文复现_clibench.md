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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663I2UM72U%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDIGUb630Zb690XG3wwB4C2cLnxgHTXEAl6FYoQBDTMtQIgcu8L4wUNrZzp86JKOol7So5V87GvXRw18NUwqTGi75Yq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDO1ZVas9fCXLsEJJhircA1O%2FrxtjVSm4k90Kf9TR6VqVw4o4Uloi67VRYkwQxB5aoXQt%2FSCdBsOnAG1LOp6l0D07VPVK1q7HoNpqSzOR9LsZp0s7XpUpYsXEwxiUU5M%2FTZs5qBbQBNFff3HsfiNjoKQeiaeuRP7en8Ew4iJZq4uh3f8Zgf6uMryH7VSSymCHVGxN3Gs9u6V3xTNIzjkA7y%2BdIorzte4entCy9NWHgBSZRB%2Fw83yF4yaEkTwvhmebiuxXoWjdfuJM2ktwLgzttSmButEwU%2FmOQNWtPjF%2Fcy2mP3KacaxNdSd07rIbeOe%2B1UrBUmXQKyZbe2NKgvEG9m7LmKb7fHd8AnZFYrcceeBBSBomL9ay79WtMFnJt7cCx0sSIbfEhT2J%2BtBsATGD6VqAmv%2BEPBngKlU2jh1Vv5ia6pakmhTgdcvnbtUqo%2BMuWfI2h8Pq3eSAopRyqtc1P1hEwWlBofZwIY%2BdZooXD784ChDhyWIee6yDEqQRNCbWXQJD2Vm7Gi%2F%2B5S2EEHre33pJuNOMAcY1mR5NhYiqLw5%2Bq1V8%2Bz54%2Bnfr2WTjFb0mGzRf%2FtdHJCYHQ0VVZ3I9H2hbaB1NmdaMUxpRA9JnX2zBQUtYpRb%2B%2Fd9l2Au%2FIkZ8kgoaL8bEbos8OThaMLbpwcoGOqUBkegl3ANV8R5ITZ8jhUcMyyJlvlXFrACgeZX5G21muFw5TtuHY6ZNc6W1eQC0ufYQDjz6l63LFCvqtKvAKbOx%2Bs1Cx28ltsi7LFNuCSdtZPi3wIn1mqZs7xzTi%2BQ%2BH5uYDLZhxAMTpY%2FQ%2FgLMtFwvZegO4UkHf0QeWt4WbhROczFzwOLgA2crggouMdkQtsh%2F%2Fgi8V34zK%2FfA5cIV1uPwauuoNpcZ&X-Amz-Signature=903ef4489ab16937dbb91bb9c1c5a698be927227f66577cf1711d74598029f07&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663I2UM72U%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDIGUb630Zb690XG3wwB4C2cLnxgHTXEAl6FYoQBDTMtQIgcu8L4wUNrZzp86JKOol7So5V87GvXRw18NUwqTGi75Yq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDO1ZVas9fCXLsEJJhircA1O%2FrxtjVSm4k90Kf9TR6VqVw4o4Uloi67VRYkwQxB5aoXQt%2FSCdBsOnAG1LOp6l0D07VPVK1q7HoNpqSzOR9LsZp0s7XpUpYsXEwxiUU5M%2FTZs5qBbQBNFff3HsfiNjoKQeiaeuRP7en8Ew4iJZq4uh3f8Zgf6uMryH7VSSymCHVGxN3Gs9u6V3xTNIzjkA7y%2BdIorzte4entCy9NWHgBSZRB%2Fw83yF4yaEkTwvhmebiuxXoWjdfuJM2ktwLgzttSmButEwU%2FmOQNWtPjF%2Fcy2mP3KacaxNdSd07rIbeOe%2B1UrBUmXQKyZbe2NKgvEG9m7LmKb7fHd8AnZFYrcceeBBSBomL9ay79WtMFnJt7cCx0sSIbfEhT2J%2BtBsATGD6VqAmv%2BEPBngKlU2jh1Vv5ia6pakmhTgdcvnbtUqo%2BMuWfI2h8Pq3eSAopRyqtc1P1hEwWlBofZwIY%2BdZooXD784ChDhyWIee6yDEqQRNCbWXQJD2Vm7Gi%2F%2B5S2EEHre33pJuNOMAcY1mR5NhYiqLw5%2Bq1V8%2Bz54%2Bnfr2WTjFb0mGzRf%2FtdHJCYHQ0VVZ3I9H2hbaB1NmdaMUxpRA9JnX2zBQUtYpRb%2B%2Fd9l2Au%2FIkZ8kgoaL8bEbos8OThaMLbpwcoGOqUBkegl3ANV8R5ITZ8jhUcMyyJlvlXFrACgeZX5G21muFw5TtuHY6ZNc6W1eQC0ufYQDjz6l63LFCvqtKvAKbOx%2Bs1Cx28ltsi7LFNuCSdtZPi3wIn1mqZs7xzTi%2BQ%2BH5uYDLZhxAMTpY%2FQ%2FgLMtFwvZegO4UkHf0QeWt4WbhROczFzwOLgA2crggouMdkQtsh%2F%2Fgi8V34zK%2FfA5cIV1uPwauuoNpcZ&X-Amz-Signature=64e86899a34dda07f784ab0ed202b28d75cd47dfe718c61ea275ebe2be3ba595&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







