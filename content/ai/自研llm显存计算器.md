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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFVT6BRW%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIE0vfE4%2FF4VZIL5cvaz15pL4Gw1bhhH%2FRsOYaNxLJzYNAiEAn5jJnElcMeKw%2FqyCcnaN590qacFBpQnwWDl5fYppPjUqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJcCYVnwd0SVx%2BehOyrcAzyd1d1WwfHEs%2BCaOHnz1TKu1%2B0hgAkAKErKoOgme%2FCCDA%2F8IfKIV9NzuFK%2BtI%2Fku%2FDAzc%2F6JrUlXO14Xkwgpvqs3tAthuRNV3gohTeXBHBVQG0b%2FVpevbXcawYM1jV%2BqcrduWzEx3qDItPvlO2nKTmrs28l%2BYAWO6CifosH7%2FOSCT24K0%2Fs4Wo1mgiDLfZB2m8IFvrWkiL0bEp7pSLL20YgP4xhHFoyRtLJTG%2FsGrN31RfjfM%2BfcRo0Io4MhfTq79Ps%2BvlKaysyTI7agXvaLHkEKPc7CfLkyZ1WWdrkBxeTnCzOZ4xyn7MiOaJTq1MOTIuuz8Ha%2FOtP951cuDWIXHFJTAAU2RMpwr%2FRfR8PhX7FltRBRtmh9AB8Eh9gsHQg3Q1fN9led2EvrPY1EWVWPsiGBueiIgDXONfGn9hOgOAPjrqDAeCYQFJjjuBA3vPpaONDG7nTq%2Bs3T0A2YvsuIe1oyrrDhthR2ih6ofVguugmH6Rg7hUalj7dKuUnw8Cok0IyftoWX4rzZHwhIv5Yj6xjPESgfDw0CiynMo7qh5%2Fyc%2F39rw9Jbdr%2BVjh6fypQeteNu3%2F%2BlsJUN7qxchzgsex%2BSteBjFN5CN2EMe7m7WbzLu7pttOPbpxDnMHLMMr3kMsGOqUBJTjLEiWQC4ToullKWJ7Z28Xectcj1A%2FfhwdNmVyJxRxE7P8bwTU%2Fq1EEIjo1uMkIMLtqfKoYTM8k1CVKtaw1Ir0lya8VBa8N%2F7VbdZzE3BB%2BFvv4Tb0ggBaHOJkqGJjqs6aVsHgRjcrIiSgiHa1PPTteA2YE98TYHBUbEhZM3oD47%2B%2FWoMuHsuxYaMarMAKCP8%2Fg5TgnGlq0nqiWm62n%2BklyAmGs&X-Amz-Signature=36719d4ba16deaa192ca92f0f6d43c4f9f215638e91dc57ac180904eed976959&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
