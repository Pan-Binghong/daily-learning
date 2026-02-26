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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAFLTLA7%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQD2KgAYAXcTFK0cuCERt5Mi2zyLv8KLAaAzJo66KgEtOAIgPc0e93%2BbC4x0UzwI%2Fk6gPGHRadwfq41C5AjLMhrH%2FD0q%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDCRLOYwn9mguIww3aSrcA24Fg3bK7xc1%2Bz30j33Pu0CwasCixZ6WYQ6UhfCpTAUcBE%2BBbkjHkzKfjAc8gFVEsLjqAOSwZWKvmo6QTeP%2BUwZrfEWCIsngKklI34eJXE%2Bni0YYjwqVCI4GSD79H%2B0kCUvE6Tv0MW%2Bpi3pij8fKms%2FdHN0RxG5qQ7aqK4SA%2BTwPuiWbFj%2Bb0Ke9eIx4WvVHc%2FpU0IWkMccGKzTbPN5Ox35dSUoNbKa%2BCzR0Da%2FbZbO6M6ahyBt06OXkFjsFg3nK8dwj0o472HQS1vMCF6YeNyiGmyd5FmDVuayJ40NJpYsVL4e7E2hzdqV8Nh14RkZ39UDDWXfSrpG4GlEEajgfO6U9sriSTDLEIbepOMxN0I7ADH9WKZ8mHlJNxHtVgbRSpXdE0PvSBAWsMx0D86Ihn9Xm8brx0q8e60ZWJdaQ0xAavnEMOwin5shJj0s%2FFvUQH3U3739kVpUYbrykxHNABQt44GhULTCrH7m2mw%2BLBdSpqFr15Kl7l7fnYVXw3%2FpQG80f%2F48%2F7SC4fp9yXBcP7ZDh5ZrDRad0QwtAayYwe4J3qGoVN4XCfNbunx3aA6RZEn2dQjbhM3oVpKZreijvdoHhbIdjMqkjzA7eFKKeLyIisfQyYTjk8b0uL%2FlmMMD1%2FswGOqUBcrbuYItwv5RfGpKahJNFzbSD7xK9bKZKFMDwLQ6%2BqSOhOd9aqwwLNJzVndgamw4nMDKosOJrrHVq7LQ7accRf7zESdQd%2BGGFCXesFPgFWSjMUYmsV%2FY2uA57WoaGkH4z2quvieddo5kU3Cp6IXtmwDNDz2OmUANcZCjGIygqnRN2N1Blw5G%2Bxt4%2Br7r3CS3bTcxIyVvGwyCirlLdyy7S06ME7Vtt&X-Amz-Signature=dd3fc9ce40273e747cd6c3b6e37b86e4163f8fe33e0b3b14997546913e5efa2b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
