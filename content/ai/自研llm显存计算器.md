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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ISBSCUD%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCMgySGyhS9xotbzMb3GyzJhkYq2khdj5N2gXQYiNZBAgIhAJXUE9STcx6pYR1ZcbR55RpmT0msme0CLdrUZddXd7HOKv8DCHwQABoMNjM3NDIzMTgzODA1IgzIgA9zn5sM2yMlzKUq3AMMYr6pA7xtsCBgmNQ4loRLgoGFyPAlhOTSZrWSjuZmvmNZBM8SdJ%2B483udzcc3RzyKooMZWotSwL9mNhhdJ5IJS6k0hIWC4p%2FqnE5cnbKoFB5tT7lWFRyb69%2FjXguA86Pq2zD57fzqJdPSBDNqgEReTxkW3G8AaEGlWso6koQ6V%2F2Ppp0Fkg0bi9j9V4BtgUVWIMFdYdPKnwHZyklpTsLC8jjnRWIOe%2FXFyg4Xybttph5ip4U3NE%2Ff4Xjk4mOkvf9V6I5%2B40Mkcq%2BbXiWSv7G1XOL3%2BjpCp%2FOKa3njZpSgkppIoEGDqz4flQ0E1op8tFek6hJwnB4RiqlUN8lJa%2F2nmeobLuFjA3oyQJI%2FbLNwB32q5kvHcfnlb2a84XCM%2B9jtEjy4H8b8%2Br250HB1OPul6ZAxznO64x0V%2FWRM4LwlBUb1OZouXvlmXOZMSB9sZIzb2dnBYMBceEWZU5Vdd4YZva%2FUx02jBpkwJpYx%2FHNY81G1c1v80O4uQ2Mou%2B%2BrWmgES%2FJll5lBg6edVVytFKCDYyQKC4xrBzNvOOGGkJPQazpYy8SqMLTolrF4rGgNaNjvIq6LCV3xtA9mMEiiXaDS9aTFbYhcutlZJK%2FuqVRrPXXceF5aIFBavFiVlzCnouvLBjqkAdrzQjK5JctX4klRKys4v%2FgyOd%2FRLWoC%2BtP%2FTEOp5KYuvsE3xnLt8tYCqWIEDPBHfJjFng10toPYhVqemWLIHf7AYRqna6%2BxF9Z8a7eGNVGVUkZlUgGplYdWpP6GAcSKXZ8CjoGvt9PsBMGwyTkEjptKoe73U6YubUmeYfMW3d9nTViOxe0Ipa4PEy%2Fa1nog04nO8Vh1qoozam7mFX5aairFnwg0&X-Amz-Signature=45fc831c85dca3abc7d77af11d7d600411113aa58fd47ac55ba98ce54c3f41ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
