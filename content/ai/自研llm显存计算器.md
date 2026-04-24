---
title: 自研LLM显存计算器
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
tags:
- LLMs
categories:
- AI
---

计算全量训练一个大语言模型时, 所需的算力卡显存.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662N5NXEI%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAKreBsUoQ01ZCSv2d3Te15Gun2I5d64d2gkNSzW9qi%2BAiBOMIqpvfCeA6kuwShbVI01VHMXFKjTqN3UKEo5kpJSiSr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMvV2%2FWV%2FeYvSYQnJKKtwDAewiPquHbMzjxUNl%2FPuHqAeaLWADaTBONuZLhV5t7pWfdllM%2B7boRInjdWYe4kxsZmTrCbUlHg7vUFZV6Ly5Lc2ghdt%2BgEDcR%2B58Wk0NIJMgC1V8nq3gSJPdai6ui4uGR%2BRFX427lLx59WJjMONaus6%2FIxmG5tURRAQyoytDUh6pdqtiOjjKUUDKk7nUtVwA8UL8sS7ijEelMzM%2F2rSaFd3hpskXt4bjE1G9%2FqGcN9woK9RSY%2F5h2hSiu0h1axuiR4tzBL61z8durEqAzykV6J0qnoLg08e2EFgSC09OoPLm0fQ9Nh9hUVNnvqmpbpQ0nquplfxn11Q2p6KOS1XAf9DkwibQ4qH8s3e%2FgLLgz7v0g1Ypg3Nf9m%2BBrC8Fz6sRNf5qmdAtYr6PXVZa2VbpzfOxDo%2ByW0CMg8zQu893KN1ezL%2BsSEmndAIJy3y82c7MUT6Kg9JSyxtc1xGqjd2E1Ugq2FTLxqaD1DviepvMFJPd%2FmBjdOku%2FUL%2BcFNABp0PvjhboZEzf%2FPQ3gZzC3nowi54X9ugjtmrKkR%2FlXZMq9CU4DYGuLghp%2FvEYK4a%2ByYtHTDdgB%2FMq9FxSl0YRJwrYnGJN5W4pqnpcpPEPrTI7unwrkvkyeWM6SaKvKww262rzwY6pgEJuV8ouxEJ64gFODCdtbmPO1NsarEnsWDJmdJ%2FKiWxyLjrzeW%2BoNo4vUfHSQeQXJRuEhblA3WGl%2BmP8ye%2Bj4tdcqLxplvI34RAv7EfJNB42hojKn5LGabRwNwfSy5%2FRvUYkPxUivCiDhBvhRldfJS9%2BCvTJW0S0jo%2B%2Bq23vqZW5QFPh1xP%2F14SPzLHdS15rraKTfw%2Be7GxBgFvv9yLE3jLZgAE5Dw%2B&X-Amz-Signature=6d47440af5e5a2e756be6e2680bfb88e69ed11e0a286a67caed2211216d543e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```plain text
RuntimeError: CUDA out of memory.
```

![](https://pic4.zhimg.com/v2-5e80264a8fe8ffaf312d08a50ce103eb_r.jpg)

图解：不同数据类型的浮点表示

该图显示了四种不同数据类型的浮点表示：FP32、TF32、FP16 和 BFLOAT16。浮点表示是一种用于表示实数的数据格式。它由三个部分组成：

- 符号位：指示数字是正数还是负数。
- 指数：指示有效数字的范围。
- 尾数：指示有效数字的精确度。
FP32

FP32 是最常用的浮点格式。它具有 32 位，其中：

- 1 位符号位
- 8 位指数
- 23 位尾数
FP32 可以表示范围为 -2^127 到 2^127 的数字，精度为 7 个小数点。

TF32

TF32 是一种用于 TensorFlow 的特殊浮点格式。它具有 32 位，其中：

- 1 位符号位
- 8 位指数
- 10 位尾数
TF32 可以表示范围为 -2^127 到 2^127 的数字，精度为 3 个小数点。

FP16

FP16 是一种半精度浮点格式。它具有 16 位，其中：

- 1 位符号位
- 5 位指数
- 10 位尾数
FP16 可以表示范围为 -2^14 到 2^14 的数字，精度为 3 个小数点。

BFLOAT16

BFLOAT16 是一种 Brain Floating Point 格式。它具有 16 位，其中：

- 1 位符号位
- 8 位指数
- 7 位尾数
BFLOAT16 可以表示范围为 -2^127 到 2^127 的数字，精度为 2 个小数点。

比较

选择数据类型

选择哪种数据类型取决于您的具体需求。如果您需要最大的精度，请使用 FP32。如果您需要节省内存或带宽，则可以使用 FP16 或 BFLOAT16。但是，请注意，FP16 和 BFLOAT16 的精度较低，可能会导致舍入误差。

总结

浮点表示是一种用于表示实数的数据格式。它由三个部分组成：符号位、指数和尾数。有四种常见的数据类型：FP32、TF32、FP16 和 BFLOAT16。选择哪种数据类型取决于您的具体需求。

## 大模型参数计算公式

1. 大模型参数计算公式
## 显存占用量计算公式

1. 显存占用量计算公式
- 模型参数存储
- 优化器状态
- 激活值
- 额外显存开销
### 相关知识链接

- 大模型训练策略
- 人工智能大语言模型微调技术
- LLM结构对比
- Sequence Parallel
- 大模型显存计算公式与优化
- 理解Transformer，注意力机制(Attention)
- NVIDA GPU卡SXM和PCIe之间的差异性
- LLM Memory Requirements
