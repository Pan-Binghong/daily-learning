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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFHA6AM2%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041226Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqWrAIqd%2FrviDad6xov0XlDWUjSSz7md8q637wKcLJCwIhAI9pceV2PHHFhIhsbpBqLQpKkW8pBUaoziWHHDjiAiSIKv8DCFQQABoMNjM3NDIzMTgzODA1IgwDDk11pYpjcvinKfwq3APYasigZioA4GIYpQ9UIVSdojk0YMx7lmpjlcTwTBtfyA3gN%2Fvszo%2BAnH0sn6rJoPB7NKxDvSPy1l9sko8C2Te2F8Mcclyo5Zz%2FrsGJOGpzBW0fjthJSK3aDZCb0TTu0VJzHdqeY3TaGRL%2F39ZKqRXvt9L5HRjenAzRqGzPQszh%2FmwxLU1Xkc%2BlE6KhbSmg7gl33u5IxsuI9dksPuHEHIjE9zPF5pfLeAD%2BvKHEkl1Ebc5OZ6mP%2B%2B%2FJNUQ%2FGC2yZSS1LtjRi7an%2BlIFBdhvrtl9RlAW3Un2iYRS%2BpYVTy7PH12YcIghPGfBO9Fpvu%2FDL%2B3uHrkpwayD8AcnGj9DjkDn1LtjjBMm9UJ8JDzRk0rxYkBMmkzYCcyWoXXN7OPpl9vuoGG8lACd2Lha6x5eHp17gG5nancPyRKS3RiVwXiRty%2BLZhk7%2BZQ0JRWbyBA%2FFeqI5uExXUuqUEBPTuH1%2FDtNz7Lc5WMWRxEIMHsIiGqom5EG%2FDWm3xJxM9mPr%2FDaOQt%2BqX1W48QY%2BMpwz4uee3zLvx6y0ilDLspfSwaUAYDTVIlYAw6CW4W6IE7t7oQbg6Zfg7j4%2BgZ5Io%2FY0%2FnDAq8gdlPMohiRMoGR171XQ%2BtMEvVjQlCE4huUb0naVzCch%2BzOBjqkAS8aN6tYoeKXMMulsf%2B%2Fs%2FhSsD%2FPFp9znSuibTsuE%2B7UiV2dMolSzLk9Oe2zmN1kYny2NjkB%2F6D1U4wBxLGQO48QxzPu77lhzH8Us1QSnBoWAWuuj%2Bwd%2FBZ1DEJ3dm7QRw4KHM%2BfVseEU85jj6ITvFnG16HfGUfNDRYrInk0J1fXWoHjwnc7WjUnjCn9gxK7gnziSFZByd%2B99bTPBPlkZIlE67W8&X-Amz-Signature=2c9ba076d9b1d44d5d1aa56b1ede4741cc92533ec00ef7d1d5dabde8dadcbeb2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFHA6AM2%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041226Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCqWrAIqd%2FrviDad6xov0XlDWUjSSz7md8q637wKcLJCwIhAI9pceV2PHHFhIhsbpBqLQpKkW8pBUaoziWHHDjiAiSIKv8DCFQQABoMNjM3NDIzMTgzODA1IgwDDk11pYpjcvinKfwq3APYasigZioA4GIYpQ9UIVSdojk0YMx7lmpjlcTwTBtfyA3gN%2Fvszo%2BAnH0sn6rJoPB7NKxDvSPy1l9sko8C2Te2F8Mcclyo5Zz%2FrsGJOGpzBW0fjthJSK3aDZCb0TTu0VJzHdqeY3TaGRL%2F39ZKqRXvt9L5HRjenAzRqGzPQszh%2FmwxLU1Xkc%2BlE6KhbSmg7gl33u5IxsuI9dksPuHEHIjE9zPF5pfLeAD%2BvKHEkl1Ebc5OZ6mP%2B%2B%2FJNUQ%2FGC2yZSS1LtjRi7an%2BlIFBdhvrtl9RlAW3Un2iYRS%2BpYVTy7PH12YcIghPGfBO9Fpvu%2FDL%2B3uHrkpwayD8AcnGj9DjkDn1LtjjBMm9UJ8JDzRk0rxYkBMmkzYCcyWoXXN7OPpl9vuoGG8lACd2Lha6x5eHp17gG5nancPyRKS3RiVwXiRty%2BLZhk7%2BZQ0JRWbyBA%2FFeqI5uExXUuqUEBPTuH1%2FDtNz7Lc5WMWRxEIMHsIiGqom5EG%2FDWm3xJxM9mPr%2FDaOQt%2BqX1W48QY%2BMpwz4uee3zLvx6y0ilDLspfSwaUAYDTVIlYAw6CW4W6IE7t7oQbg6Zfg7j4%2BgZ5Io%2FY0%2FnDAq8gdlPMohiRMoGR171XQ%2BtMEvVjQlCE4huUb0naVzCch%2BzOBjqkAS8aN6tYoeKXMMulsf%2B%2Fs%2FhSsD%2FPFp9znSuibTsuE%2B7UiV2dMolSzLk9Oe2zmN1kYny2NjkB%2F6D1U4wBxLGQO48QxzPu77lhzH8Us1QSnBoWAWuuj%2Bwd%2FBZ1DEJ3dm7QRw4KHM%2BfVseEU85jj6ITvFnG16HfGUfNDRYrInk0J1fXWoHjwnc7WjUnjCn9gxK7gnziSFZByd%2B99bTPBPlkZIlE67W8&X-Amz-Signature=688ec7840b3be9366be880e43ec2a4e40a8aba102dcb6521e3d432d1ad233c9a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







