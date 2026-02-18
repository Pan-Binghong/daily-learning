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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YKV2XAH%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T033953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCRuSGO1PwGw7QYi5g0b5BZ8UVzlnyVLXGvS6hWtQ%2BTKAIhAM%2ByqWs7YkdJmLmCXDJPRK6w9hoMkPchzTdFWZgsoas9Kv8DCFoQABoMNjM3NDIzMTgzODA1Igw%2FTQ1GjZE6cmEt59Eq3ANUP8FVHULogcttpdooG6ZgO6SkqT74m%2BufqQsNjA%2FwtuqknuEw7c0O0FJQKTVSbR1t27bfnsQi9oDsIFPX0SCbzh9Zehm45cqwC3j7YGKrVMPDzteWVQL2jsvwxSzEBj9kBvnlYbR17bvoIihyVT8qLFoGtTUuM%2F1qhpPOZT1lgZ1a8DNUCKhuLZtxYkTN9VEiwnpg0hyJtOcPIezBmZuwtBfTcpXqR98yzi2uTsAhNg08eFoicQrbGkmxxVAC5Maox%2BqVvFNPp9gOFYBCSu%2F4ORQyMcPUQbksYLjiZwuAut%2FdsRD8APpNNUqISr4du2ZBq0rQcpbqNY7zlnopmXyEVaiCRgL4R%2BQY6Muk04CmAl4rmGa0mfiYDAiIZJq6cLjK0ZiGW37lyjmH6kmFjDC236iKx6kr5cMuH7URKdtrSUl4SMZeDAYnMgRaATmuODcb1ZKZ53M%2BHFYtzRJHZ2tveSgvchdnY9bAqeYtrBxgu%2Fvi%2FD%2BMB5EmHRD0Gjy6wCErIpbSDEZ8Zyab%2B5RfZfyHQZ2bs0hSCMJHWB4BjC9YhCGuod58eog4fNeK%2BZM8NrLrUZkpOWpDZOIpFaNokpDhQQ4kYEeIZ6Wmb%2FxSgSQkBq493rsmFB6htgaAjjCyn9TMBjqkAU3ZMgJ6IkYl91r77OiTGsuDvqS3UJ9DCZI3k16JR%2Bqq0pITLHO%2BVbr%2B45CkjUTrJSIc5MGQ1a4q2oKsGwsEVVvecC%2FWkJTE1SMZqVLNoVg%2FgJAqJPS6tfdnWuwSehrwEH6j2gCJ5s4MSaVryz6SqsgFVBvIQNFmG2IWOYuVOtwnuHWiK0%2B9p6zEc6%2BLYzD3fhFjKP13finqEoYo8oIhEDLFMvNk&X-Amz-Signature=33562237299a9dfbd542763c8f2ff315902d72b4e86d6a7d0144c181ac40705a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YKV2XAH%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T033953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCRuSGO1PwGw7QYi5g0b5BZ8UVzlnyVLXGvS6hWtQ%2BTKAIhAM%2ByqWs7YkdJmLmCXDJPRK6w9hoMkPchzTdFWZgsoas9Kv8DCFoQABoMNjM3NDIzMTgzODA1Igw%2FTQ1GjZE6cmEt59Eq3ANUP8FVHULogcttpdooG6ZgO6SkqT74m%2BufqQsNjA%2FwtuqknuEw7c0O0FJQKTVSbR1t27bfnsQi9oDsIFPX0SCbzh9Zehm45cqwC3j7YGKrVMPDzteWVQL2jsvwxSzEBj9kBvnlYbR17bvoIihyVT8qLFoGtTUuM%2F1qhpPOZT1lgZ1a8DNUCKhuLZtxYkTN9VEiwnpg0hyJtOcPIezBmZuwtBfTcpXqR98yzi2uTsAhNg08eFoicQrbGkmxxVAC5Maox%2BqVvFNPp9gOFYBCSu%2F4ORQyMcPUQbksYLjiZwuAut%2FdsRD8APpNNUqISr4du2ZBq0rQcpbqNY7zlnopmXyEVaiCRgL4R%2BQY6Muk04CmAl4rmGa0mfiYDAiIZJq6cLjK0ZiGW37lyjmH6kmFjDC236iKx6kr5cMuH7URKdtrSUl4SMZeDAYnMgRaATmuODcb1ZKZ53M%2BHFYtzRJHZ2tveSgvchdnY9bAqeYtrBxgu%2Fvi%2FD%2BMB5EmHRD0Gjy6wCErIpbSDEZ8Zyab%2B5RfZfyHQZ2bs0hSCMJHWB4BjC9YhCGuod58eog4fNeK%2BZM8NrLrUZkpOWpDZOIpFaNokpDhQQ4kYEeIZ6Wmb%2FxSgSQkBq493rsmFB6htgaAjjCyn9TMBjqkAU3ZMgJ6IkYl91r77OiTGsuDvqS3UJ9DCZI3k16JR%2Bqq0pITLHO%2BVbr%2B45CkjUTrJSIc5MGQ1a4q2oKsGwsEVVvecC%2FWkJTE1SMZqVLNoVg%2FgJAqJPS6tfdnWuwSehrwEH6j2gCJ5s4MSaVryz6SqsgFVBvIQNFmG2IWOYuVOtwnuHWiK0%2B9p6zEc6%2BLYzD3fhFjKP13finqEoYo8oIhEDLFMvNk&X-Amz-Signature=84e3b825a0cedd6c60a9e398e4dc7c75cae1b5fb611904aebfed6f5409aa2948&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







