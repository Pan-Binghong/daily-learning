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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QXNTSCV%2F20260422%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260422T040925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIGcrXK3MaaIjM1e6IRoRAfvb9rfqvhvcV5Lk41xys%2B0kAiBIFofXWarTAzTHmrx9insNGYOU%2FH90%2BGv3bXFF9O1pYCr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMNIOeN1ZYZtf4KyPYKtwDQXAquMsMoUYFNzDzjPBlARVWJY%2BUWER3RKtUaD3FtoKscsbkZ53P9ml3uuAMjBDRQ%2BF0iyzTJLSUMks%2FMrF72f5Uc%2B6V%2FpUKUW1wNZq4ZNML7xFjkGAF%2FeyGTpradjRVOj9r%2Fo3hjkwndnEeTW3L%2Bz98Dy9udHFnW94Z28i7HF%2FzKaXijY8GH8MzBfbK0lpqZptsEZqJIeY3TJ4czeH6pQESS36uh635zwrXGn6NJcwUfxtKtDeviF2Z13Qd4WzaNOwYtTk7q4OlZ5JAN8%2FPaam%2BunSEq4GR9hooJgqyBcJjl%2F77%2BJJZlrIIm8ZcdAmT3nZKO8L0%2B008xwXU5Y%2FLHvVvYIc9E%2FHA16%2BdQJ3C5sv5xgXZ4gsuh%2Bd6Pcgt1kBOLP2FTmsfO4OrX3A4CZFsokDIAHDo91KNokGG77Vs85zkii5h8AZTM1txtbw4TTXCfHSoH5uu0DSXsy21uocNPea7nznKnkTrWHhDgmxAGK5UO0d0r%2BBCITIeA3lU5lLAI0962ykI7xJ52JvneYBtfEChCepN7H9kw%2FEWeaIJHN2YQUaxn4bMFw5HxwMKIKb%2B%2FLgD7%2F9GIq0UPFjC7Z%2F2%2FiykDmOLgNgsFLkzHjc3qaU%2F1EN5vS79666GGCQwrPmgzwY6pgG4KxM1CJDMPxotbBGZBsEY2w%2By0GuNflS%2B%2BDREJvwLn38a6tNqeiQz3l4NgeKZ2G7tgJBq4y0i5OXXTvKzIe%2FOk87X7Jqzjxs4e37aI2VETn98UHFv4G5bHNMDihPkXdp14eXX8PBsIbGIuu6t5AEosm8yIOdZWNoHa3dYpzRwvma5IaTYIt30PUN%2BdL8%2Bb2qmr0iYcT3qCWBGMQ3CJcH5Hd6xj3aP&X-Amz-Signature=2fa96ed042a0d0e4461064d48b65a3ac4dc7fc0c91f303e8455759603efe5576&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
