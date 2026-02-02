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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HBVTZKU%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIHPNQ9c9ngXyZ7BfIU73OVSkILAo1z2ffytM3iyjv00FAiBztkA5x1mJzMPA8qw7XUq3tnLaS2dl%2FpQ2RqoslU%2FanCqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcK4%2FLKbKbZc%2FSIcFKtwDksR4Md47SaBYKClIZtXeS7ZlE2WC2na72rVXEPosTfE5XwBhHSJ7oMqwEbL4PrC%2Fu04cg%2FpH1ApuuTzfZ7i%2BR%2BnxynD9QhTmqAFFtlbovuZ30SDU1EuenYPvbFC1M6kfci7Tsw2xMdQlwjHqeGbn67P5MylPIjt8li5DtFX13S%2FwGsxuwjkZCQClPIFyS%2Fa%2FYD8ufgkD%2FqfG0UJLN4XQgbfGCf5jBPbwGHOBtDjbvBSc6193fNBF0CJhVUaX5SNzizidtMq8kvI4wSwR39BioM9KQYQ%2BV0e0FFnY%2BiMC4atLvhPRosH35eMFFS3evASFe1o%2FDGwme6SNmRwlqmkRldrBQqNvx8yAOsx74pJxGuXRlx1mLEFTr0Fc3OZQr%2BhCzZqoyIh5Audy9XD%2FgJ9Udm4pu2T5VVMy9Y9miJlGvH8iKoddntegek0E38JNxLjPTx2paTCdaq5fzp2%2FTT0qbdjwwzJgkM7CL5BSosT1oyyZMEbL4EN9PwVWURqCCqQwmNfNXLQWrIo9IH3S%2FbhQqMGBfnLYU5yjdKdGmPOpGgFF%2FgUKU8JlavttAi%2Fs7dZlUFdDkwlMKMxG4G8tu1aqfcl0dbkf%2Fi%2BW%2Bp0CgtzwE%2BpBjgFazZdWNNlG8%2Bkw3YeAzAY6pgHGdb3eeUsfrTPwkb1xHP7II6RVWD6uOPw7H51jZbdwMiY7z%2FYyMvmagv4MBlb18w3l8HqXgZhgevq4xBVolPKKOcjQXjLse5Jii%2BcQMoZBdm6dfAggKLJKP3weFpRU8NXYkh2yCw5dN9C5qcvLIgHjljiXKI1BUlbZ2mXJQfIuZTIy1YdV9B00LXQ58Q5%2BCq5fv3%2B6ZBtzB9yGcS249z%2BJd%2BdNisq6&X-Amz-Signature=42ba670369780d6e1c2468694593e8e55fe7ec58c757306014d2e889714ff598&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HBVTZKU%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIHPNQ9c9ngXyZ7BfIU73OVSkILAo1z2ffytM3iyjv00FAiBztkA5x1mJzMPA8qw7XUq3tnLaS2dl%2FpQ2RqoslU%2FanCqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcK4%2FLKbKbZc%2FSIcFKtwDksR4Md47SaBYKClIZtXeS7ZlE2WC2na72rVXEPosTfE5XwBhHSJ7oMqwEbL4PrC%2Fu04cg%2FpH1ApuuTzfZ7i%2BR%2BnxynD9QhTmqAFFtlbovuZ30SDU1EuenYPvbFC1M6kfci7Tsw2xMdQlwjHqeGbn67P5MylPIjt8li5DtFX13S%2FwGsxuwjkZCQClPIFyS%2Fa%2FYD8ufgkD%2FqfG0UJLN4XQgbfGCf5jBPbwGHOBtDjbvBSc6193fNBF0CJhVUaX5SNzizidtMq8kvI4wSwR39BioM9KQYQ%2BV0e0FFnY%2BiMC4atLvhPRosH35eMFFS3evASFe1o%2FDGwme6SNmRwlqmkRldrBQqNvx8yAOsx74pJxGuXRlx1mLEFTr0Fc3OZQr%2BhCzZqoyIh5Audy9XD%2FgJ9Udm4pu2T5VVMy9Y9miJlGvH8iKoddntegek0E38JNxLjPTx2paTCdaq5fzp2%2FTT0qbdjwwzJgkM7CL5BSosT1oyyZMEbL4EN9PwVWURqCCqQwmNfNXLQWrIo9IH3S%2FbhQqMGBfnLYU5yjdKdGmPOpGgFF%2FgUKU8JlavttAi%2Fs7dZlUFdDkwlMKMxG4G8tu1aqfcl0dbkf%2Fi%2BW%2Bp0CgtzwE%2BpBjgFazZdWNNlG8%2Bkw3YeAzAY6pgHGdb3eeUsfrTPwkb1xHP7II6RVWD6uOPw7H51jZbdwMiY7z%2FYyMvmagv4MBlb18w3l8HqXgZhgevq4xBVolPKKOcjQXjLse5Jii%2BcQMoZBdm6dfAggKLJKP3weFpRU8NXYkh2yCw5dN9C5qcvLIgHjljiXKI1BUlbZ2mXJQfIuZTIy1YdV9B00LXQ58Q5%2BCq5fv3%2B6ZBtzB9yGcS249z%2BJd%2BdNisq6&X-Amz-Signature=beac51cd7ed3457f8dae1ae1e2439cad2d3d12be701ca333b0bb0a92e2ee5ef9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







