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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZUAM63W%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033122Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIFN5Eiljo2YxZbnkfXYrJlrZT%2BKP0OcU5U9yeHCi1202AiAU3FQJfkjnJ5jKkl9dGvz9adt02b7%2BQM7fIDvT8CaXsyr%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMyeBLyDQiRJUZdBYyKtwDoCmu%2Fs8bB2Y%2BDsLbuupEHboMITcAgCSxLlhLx3N72gXaGHm6Q47PoE3RZqnzx%2Bpor7jevIpqxui%2FvSPZWQZ1Zn4CQIYjgl1l3hS%2FsPega3g0KSAjrH1thljUHcbHNw1s2e%2F0sm9%2FATrWrrgWJyiubwKq9QP24ERuw9Po7hBruto%2FuhhHAWqLKqwqGTtOF6wRGjqFQ9hVHlBENAdC5ZIqzXcCFNuw%2FtqUw3mUniin8BNCiGYU6yuqa9SIoJh5PVKoKbqkZO9W%2Btyz2NyGqD%2F94Giry7DgJyJJQ9QP12o0GyJ%2Bd1j2hccEQOQt23Fti89unJcXpWy4qY8Us6S98Wk08ZM%2B1nOpo7cNn9mqZuj79DBq8tasHF0EwYK4RsPnUoKkaXYtqErdoEOcjFOAEsOZBl9WuAaGoL2AQv%2BudeFKGBOu6yn9TxrvMQXy5b3LEcrczXaP8CXMKGf9T9vDMdZ36kna4rEkxWHfotw2foJczy8OJbFab5ScIYesRWPcGj7UIO0E52R2zPSa2Vzr3l%2BAQgHF84gEA%2BhfcYW5PLAc9gl1yLakpRcFDiEBRO%2B2gy%2BcrBnV7%2FIcY62znQkBO8BpNHK8h0OnVAW6g0e62cRcX65%2FgzYoaupbFD3xQjkwwIWEzQY6pgH5FnirPzaaWpRLr4V9PkQtxF6s%2BZ1Iomh4u2pcbbi9uN6rNnCYeNrI5VougY9VxXQ5mlqnGIZKPk4QBqQnaPrcFYGWy33%2FYFPSpVzaUxyh%2FtkBDl0u%2FsZeWyZtf3%2FW0XoNnZKZcbfjwy%2FYRA1htmHLlrv3YlT8AYDr%2Buy414nZ2TQcaccfhvGfMwZKuqco2ZSCayk8ouUV9FRE982de3iqGpn9hZWa&X-Amz-Signature=70f9e08c5ad002cb0a7601159fc9e266e08c7b41afd9e52663865476540e6525&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZUAM63W%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033122Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIFN5Eiljo2YxZbnkfXYrJlrZT%2BKP0OcU5U9yeHCi1202AiAU3FQJfkjnJ5jKkl9dGvz9adt02b7%2BQM7fIDvT8CaXsyr%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMyeBLyDQiRJUZdBYyKtwDoCmu%2Fs8bB2Y%2BDsLbuupEHboMITcAgCSxLlhLx3N72gXaGHm6Q47PoE3RZqnzx%2Bpor7jevIpqxui%2FvSPZWQZ1Zn4CQIYjgl1l3hS%2FsPega3g0KSAjrH1thljUHcbHNw1s2e%2F0sm9%2FATrWrrgWJyiubwKq9QP24ERuw9Po7hBruto%2FuhhHAWqLKqwqGTtOF6wRGjqFQ9hVHlBENAdC5ZIqzXcCFNuw%2FtqUw3mUniin8BNCiGYU6yuqa9SIoJh5PVKoKbqkZO9W%2Btyz2NyGqD%2F94Giry7DgJyJJQ9QP12o0GyJ%2Bd1j2hccEQOQt23Fti89unJcXpWy4qY8Us6S98Wk08ZM%2B1nOpo7cNn9mqZuj79DBq8tasHF0EwYK4RsPnUoKkaXYtqErdoEOcjFOAEsOZBl9WuAaGoL2AQv%2BudeFKGBOu6yn9TxrvMQXy5b3LEcrczXaP8CXMKGf9T9vDMdZ36kna4rEkxWHfotw2foJczy8OJbFab5ScIYesRWPcGj7UIO0E52R2zPSa2Vzr3l%2BAQgHF84gEA%2BhfcYW5PLAc9gl1yLakpRcFDiEBRO%2B2gy%2BcrBnV7%2FIcY62znQkBO8BpNHK8h0OnVAW6g0e62cRcX65%2FgzYoaupbFD3xQjkwwIWEzQY6pgH5FnirPzaaWpRLr4V9PkQtxF6s%2BZ1Iomh4u2pcbbi9uN6rNnCYeNrI5VougY9VxXQ5mlqnGIZKPk4QBqQnaPrcFYGWy33%2FYFPSpVzaUxyh%2FtkBDl0u%2FsZeWyZtf3%2FW0XoNnZKZcbfjwy%2FYRA1htmHLlrv3YlT8AYDr%2Buy414nZ2TQcaccfhvGfMwZKuqco2ZSCayk8ouUV9FRE982de3iqGpn9hZWa&X-Amz-Signature=f15aaecb99aa2e128b7a928e25da2fa88053c532b2462c27db9e1c45cc55153d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







