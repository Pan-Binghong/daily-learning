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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFAYMGJK%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJGMEQCIA3qH5Q%2FS0R7XJr%2FoZkoxndqmPki9yRDU0d7gBipzCQfAiA%2BTlnV%2BFhiRCSHSCerL%2F9y35mDhBt%2B8xoB%2Fwl2u7ZCCCr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMrYAJa%2BFoxvH0i7BGKtwDGg7cTLWSGVkAGXXM6VtPtlfUIcPxXrW3YBnoAxzEzvVa9YwlwSnx46iG%2BM%2FV4SbXbCWAuL17toW0e2V4syELN1EIANmc0G8KPrcJJkobQFGV2A04o%2BmeG52r%2BA1GMqic3IqAuRDi3i62N%2Fja46hgEurT9rU8QlqQqJzWOoiWnWcq%2FlYUqfS2EcsGbDyUhQKmcbPHWtqOFwtDlzf14EPcfcl1PYO6Dk16uSbzCc39CS%2FiHTZkzbcXQkyusXhGsZpZ%2BxLEoajrbS5TpUsxOSTJ44qlXuCoe%2FNC905Yz1tQsv%2BM4K%2FUSwWb7LApciXrQztWOf0lZZrGQx60Z4LNr%2FtM0gVp7UTa9uOzVeoUNQSYVjqmosGX%2FUYHHD768foI0n4k3mE9BBQ9GRTz6wzQcoX7rd6QkelfWxA0S9Y4IZ4hEZZCPvNUFuE01DmFE08yF3nBbstVFNo5Xy3iZ7z7NA5WP%2FPb%2ByXWdPda54FqacIQfS5OwFyu%2BQiF2atxa4P5rQ6WUCcStCy4ulyWkikebR7zv2IUQZ8eiL7OZCqgVXpv1oL1KnAsl7lB%2BW2mS4Q%2F9P4p3IF%2FI%2BN6dNW%2FXhJTFaLleQn2uaPUw5orORt0Ertpc5eELYyeKsBzplMrlS0wz5OQzAY6pgF0zFwdX3vUHsGYoarBGsMpWwOGRsh%2F0CMQPk5R2wlK2X%2BJAdvW0iGiNEiJxQ2RUTSsvXlvq65Ro1qnyoHamF1DX6ze2NgnpPycO1DnB%2B2TaL1L9oDQxkyVLq7jwk7PbpfDTTKCEbsSz9UUBQPEi6uGof2fBSr2ME71vJTPfUmB4EPy%2Bfqv4lVovc2EerZh7yBVmP3%2FdLMYBmqj57VDs%2BC8x%2F2hBIMb&X-Amz-Signature=247513ff89c0d685cfbe7d8b7e9255181efaf93c6062841210117f497e79ccf5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
