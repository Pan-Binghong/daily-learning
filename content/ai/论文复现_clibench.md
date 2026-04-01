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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WG7Z4KKE%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVczC4Wd7w6DYGru1aGdkFSh1feeaEsHY%2FuoAnmjN%2BDgIgSZOGWSseoZL%2BqW57AK4ShdywkQuw86rSGNcIi1eg2CEq%2FwMITRAAGgw2Mzc0MjMxODM4MDUiDCsNQs1daRrsxTt%2BoyrcAwQ5j3G7Y2m91zN11j%2F6oROHVC4m9sn8EXSMqEurpryeIsZsVYgRNR%2F%2FSZ%2Fe7WFZKSh0LEinoB9xJOJxtG8sg8L%2B00eN3UCgi7%2FeBkLzgD%2FhjMOP0y32J0uQ3LJDAJdS6tBVkw3KC8z%2BxXXw8cCWYwWq4UDNpkYmvm0WPOUHoYut4xrtoCvGgCuTUeTsUELzrr8ykPxy0dvH4Cyq0brX8RCJgYTLlEZAQ6cMlcsfOr6opK0pMGK9lDsZOWiD9j4lHNAGZJQWb1gJSBpBVmoJeCAgCkpX0djrvEJ03QPE7goL%2B2JXHQAX8R57hj%2F73fgSxQ3zYHVZtK670jwwg9fn5SZxfBvJZt1ICVctoBFo%2BloTLlFYbo3%2F1h2NQfYbzPUqFicbSybRsCOXCXCz%2FO3qlIlAXQsiBrIH%2BY6UvQ0CKc9vEaXUmWH8in9uFUftG22V3bgcWni%2BgzgPk6jBzumK7lutaoQxfHLeEJCiOGkpf5pAAGRiBl6PL0npsjq95L6%2FOpixw0P1ynZbZnRXi9XGVt%2BsMCLLwS56ZnSWSEbd9Nj5b%2Bo06ZcJNFRDqbkYVAUL0S2z9vQyu4vst4DK0PjnxUcp%2FGahWKGFIVSRJ5S3hedphnBEc83avRfLmxtVMKShss4GOqUB%2F08t%2FYssS73PIkcnkYP%2FGS3FdelNmjbSwHNfDdN1VPUqHtStL8P0uoYHf38Es%2B0%2BW7G4BmB%2FKO8hPA%2B0tZ6mjrELnJ%2BdC1vtICVWscO%2FI77ze0vDYM2zW3UH9ckToo5XSSfmRxj6KpgQNCzOmoy6siOzzJC9lS3G7T8UIfT5WD7DmdD9CbvZeA5%2BHOBq09YFi65M7isFZCazvBuauR%2FWuI6sksh2&X-Amz-Signature=9d791be12be0da731760e63b19d6989942460c203cfbf7ed7ed74cf6c672b606&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WG7Z4KKE%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVczC4Wd7w6DYGru1aGdkFSh1feeaEsHY%2FuoAnmjN%2BDgIgSZOGWSseoZL%2BqW57AK4ShdywkQuw86rSGNcIi1eg2CEq%2FwMITRAAGgw2Mzc0MjMxODM4MDUiDCsNQs1daRrsxTt%2BoyrcAwQ5j3G7Y2m91zN11j%2F6oROHVC4m9sn8EXSMqEurpryeIsZsVYgRNR%2F%2FSZ%2Fe7WFZKSh0LEinoB9xJOJxtG8sg8L%2B00eN3UCgi7%2FeBkLzgD%2FhjMOP0y32J0uQ3LJDAJdS6tBVkw3KC8z%2BxXXw8cCWYwWq4UDNpkYmvm0WPOUHoYut4xrtoCvGgCuTUeTsUELzrr8ykPxy0dvH4Cyq0brX8RCJgYTLlEZAQ6cMlcsfOr6opK0pMGK9lDsZOWiD9j4lHNAGZJQWb1gJSBpBVmoJeCAgCkpX0djrvEJ03QPE7goL%2B2JXHQAX8R57hj%2F73fgSxQ3zYHVZtK670jwwg9fn5SZxfBvJZt1ICVctoBFo%2BloTLlFYbo3%2F1h2NQfYbzPUqFicbSybRsCOXCXCz%2FO3qlIlAXQsiBrIH%2BY6UvQ0CKc9vEaXUmWH8in9uFUftG22V3bgcWni%2BgzgPk6jBzumK7lutaoQxfHLeEJCiOGkpf5pAAGRiBl6PL0npsjq95L6%2FOpixw0P1ynZbZnRXi9XGVt%2BsMCLLwS56ZnSWSEbd9Nj5b%2Bo06ZcJNFRDqbkYVAUL0S2z9vQyu4vst4DK0PjnxUcp%2FGahWKGFIVSRJ5S3hedphnBEc83avRfLmxtVMKShss4GOqUB%2F08t%2FYssS73PIkcnkYP%2FGS3FdelNmjbSwHNfDdN1VPUqHtStL8P0uoYHf38Es%2B0%2BW7G4BmB%2FKO8hPA%2B0tZ6mjrELnJ%2BdC1vtICVWscO%2FI77ze0vDYM2zW3UH9ckToo5XSSfmRxj6KpgQNCzOmoy6siOzzJC9lS3G7T8UIfT5WD7DmdD9CbvZeA5%2BHOBq09YFi65M7isFZCazvBuauR%2FWuI6sksh2&X-Amz-Signature=d611a2a01ee066918a4df43cf2ef76878a3f03748812d33ce3f66e60f75e9a11&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







