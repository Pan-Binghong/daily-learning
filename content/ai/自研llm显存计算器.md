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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FHNUVSC%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIArWB8qnl79RXzYUKABfCpHvqfC0tfWl51cnz%2B0ugC2%2FAiA5JaQC4k%2FhGKaCwELHEVfng%2FSQDSlLB2lvZ2BqYU9OaCr%2FAwhNEAAaDDYzNzQyMzE4MzgwNSIM%2FKrvd%2B6BfnoAl3UzKtwDHqcb2e%2FMxxlbmPU%2BJCkKXR4uCmeGny6cuKG8HD9A%2BmNEqWpwn0sPsLAU7a6yZA%2Bxrn9tGjVHLrmTmeMLlRtINrZ6MS66zR5JzbPgKkTBtc3F3j%2FBXDDSJjLbjrdRWYp%2FanIyE3jiFqSpl80ciG6Vyedr3xAzfjAzcJG0zW9HUbgLjan0BtXcnWTBJmNA8Bpwq6BZh7y9Tc4d5J7QQmuR2A7w7cMnH06juPxakg7aCg%2BQjE%2BQr2%2FxkSj%2BAFUM2ln3PQgXwZ0oonwPAjz7W9XsffdikFwrxBObZ79zAh1PWU6ucNXLmfvbqH3itTV2hDV0fdur%2FcfjAhI43whEsVB6MRLn4CqKM%2Bx2bnpufk5uiZcbuHW6i4G%2F6c%2FMNRjqs2TssJQjVeLImERe1D3OgptCI54PdAALEjiRWW2NxvU4ow8k1bdArjLCxbhdLnQJITs9gwVVQnsNWHIJtGGffQHo%2Bcp9HfOqd3s64pif0xm7WklZT2HdhO2kF%2B%2B1BBkpzxaRqb9BGqnaqtg1w9a1OyC51jCbSwLxcGmIloughILfzf%2FbUvhbLyuxmpg0QA49kqvEAk6TTVygAwBL28jGsLShwvrBhgDmC8xen%2BWfF0pAoACe4BNV1m9ecoO90ksw0aGyzgY6pgGcUH0mr8tFDrklJfAxEoXXYXEhmToRT1xm63KgZ8xNkomJZy01RbKb6R%2FZmU%2BNx0tZlHgycD03SF%2FrjACV5KkclWfd2dg%2BBxMkxh93i2%2BAn4ttqipgW3H1jYLtpUt7PWUMD8UzVt0tHPQyBPvjfkOSN3iV2YYFz2YC%2FibTS0siBt%2Bw%2Bo%2Fi1H9qyjWTT%2FYcjHPIIy7%2FNPQeieIn0oDK%2BgaLsVdZwPPy&X-Amz-Signature=8d5771b33772e29285e8363491779e7973194e5f8c98f1fb08d0c958caa3565f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
