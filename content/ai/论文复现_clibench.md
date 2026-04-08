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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663G23SIN7%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQDMy4FauihtMNeuiXG2bXNtCvWol%2BUy1d9%2BP1oa9RyecwIgHSHauhQmmXjj88Qwnk15vJCMKfvdlJaqqahka0rSaF0qiAQI9P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPZgZNyczF4iuvd4pircAxHvSGfsV9Y%2BObD6X7hUtCXJcRuZCf8AAh2ydw6e7SgzMjYgn8PEPrOrqQIcCNLQ7VzSWJpuAgRTlYQUT32rRNolp44dkSvMC3aCahuyHtju%2BgSC1ui2XLv1uVnNcXMP8y%2Fv%2FksA%2F8NilxF1ii1L%2FP7mI8K4eHOPe3E3%2FH49qg6ifP3UAPne9czkNnzm4Vxfk8BPylvwbT5%2BwtqgASGBjrCnRMMhyFDtkhx8L727eB7FmhPM3LfaifU21OxTTPZyvRHXbLZpuF8nB8mQMl6TeSY6j4umpm7xj2DYBujd5kDIlg4LXQ5V6HqGmr4Gbs0h0gOJs5ln47SLUYdiN1fVDX7pYQp6mvCzJ5XJ3MQPb6oAiGFfOMdUU2ZfzIvn%2Fe0NFL3gi6Byy38Q0jIXkl0HmPuY3yekUNvP4nHnE4bGtSW%2Fn6OQv0Y%2B2JMKv24S87gfb%2FeJcPJCkM4km2VsqgzkKl74mioRQb9sjkUdHs4%2BLuI108CFbBftzCxp2JF2%2B07Yx%2BrU%2FRH4A5ZyINqmQBTp8I0qw735ESWy%2FCeF7ohhwH896AOrrpe0Bb560o2jw23V%2FkB1%2FNkmCA3rezhfPbpDSoCkfPGui1bExFrruwwrgkmeMrvOTOXtdhK5ftf0MKqI184GOqUBtim5yv32lSoUhholPtCGxxpl5NXYg1er5lhlaa20mYn6JL9zA7zNz85lMMaQcEHWU6XkIITElXwnXic5dceSZbik%2By9tN67QsfbHAcCsW4tKk2wy96Z0KsRcbXXoNZsZpQ%2BLsLVtqRwtDWUT18LP9VoRrQ3oqdcp6674brcs967DbPf1c%2FYUC3kVbsoHY%2FOR7IQMAWASScpRi%2Fu25anU4G%2Ba%2BXSA&X-Amz-Signature=a50be3e21ccd907b2c41b7cda25bc6d8227beeaad84c6e32b1ab7b4f75506d03&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663G23SIN7%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQDMy4FauihtMNeuiXG2bXNtCvWol%2BUy1d9%2BP1oa9RyecwIgHSHauhQmmXjj88Qwnk15vJCMKfvdlJaqqahka0rSaF0qiAQI9P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPZgZNyczF4iuvd4pircAxHvSGfsV9Y%2BObD6X7hUtCXJcRuZCf8AAh2ydw6e7SgzMjYgn8PEPrOrqQIcCNLQ7VzSWJpuAgRTlYQUT32rRNolp44dkSvMC3aCahuyHtju%2BgSC1ui2XLv1uVnNcXMP8y%2Fv%2FksA%2F8NilxF1ii1L%2FP7mI8K4eHOPe3E3%2FH49qg6ifP3UAPne9czkNnzm4Vxfk8BPylvwbT5%2BwtqgASGBjrCnRMMhyFDtkhx8L727eB7FmhPM3LfaifU21OxTTPZyvRHXbLZpuF8nB8mQMl6TeSY6j4umpm7xj2DYBujd5kDIlg4LXQ5V6HqGmr4Gbs0h0gOJs5ln47SLUYdiN1fVDX7pYQp6mvCzJ5XJ3MQPb6oAiGFfOMdUU2ZfzIvn%2Fe0NFL3gi6Byy38Q0jIXkl0HmPuY3yekUNvP4nHnE4bGtSW%2Fn6OQv0Y%2B2JMKv24S87gfb%2FeJcPJCkM4km2VsqgzkKl74mioRQb9sjkUdHs4%2BLuI108CFbBftzCxp2JF2%2B07Yx%2BrU%2FRH4A5ZyINqmQBTp8I0qw735ESWy%2FCeF7ohhwH896AOrrpe0Bb560o2jw23V%2FkB1%2FNkmCA3rezhfPbpDSoCkfPGui1bExFrruwwrgkmeMrvOTOXtdhK5ftf0MKqI184GOqUBtim5yv32lSoUhholPtCGxxpl5NXYg1er5lhlaa20mYn6JL9zA7zNz85lMMaQcEHWU6XkIITElXwnXic5dceSZbik%2By9tN67QsfbHAcCsW4tKk2wy96Z0KsRcbXXoNZsZpQ%2BLsLVtqRwtDWUT18LP9VoRrQ3oqdcp6674brcs967DbPf1c%2FYUC3kVbsoHY%2FOR7IQMAWASScpRi%2Fu25anU4G%2Ba%2BXSA&X-Amz-Signature=f84fd9e46d20cfdcf04ec2a925461e6fe334ca29d95a51870ccee18cf1c930eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







