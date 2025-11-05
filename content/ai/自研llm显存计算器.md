---
title: 自研LLM显存计算器
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
标签:
- LLMs
categories:
- AI
---

计算全量训练一个大语言模型时, 所需的算力卡显存.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665UBGMKHJ%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095837Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE2sGmN3q%2F0xtuvhWxov49s%2B%2BCxlXEwyrMXUQgits7zBAiBWxPTqtqbaHE%2FhFq8ilQNndfD5MYtaFxzg1chFxMGlGSqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMH6%2FzitBiHcbPp7FHKtwDjlmGSwx4dcHKv42GzM6Ro9YHfqTfztGP83v7hlOScuhu5lRZBnVfYbsVBywlX6OKTMH39tRLaKXe49tzmSBb8u6ofgWH1M6K1vdt5xCrBNQNdu23slqMkINb87pGB3ipnld1RCPCflI8vcSlvHDAtAuOkz9pC%2Fi%2FgwiTbpoyxBBuBlEbWU7dZEDf6M0fvhx4iIKQJstgS0cs4KnssJsJP6rHnE37tvdnVn2ngdXrOvpK%2BJqoiiZGbWFqhJ%2BC%2FeIi7hiczUXBINkCM6RMI2FJw8sPoxLENAchDkFYXRJoey7MnhRqI2hxzJ0SmCYZSjK3EMk4sPZPwzkhVdOr8ucXPD8BB4BistiY%2FvIL63Lp9YnJDsCeVlmWr%2BJU%2FBHc10H3JnN0KXBmu%2BLjO4pTRZ%2BcLETA%2Fvv%2Br856NnGmlqlGg%2Fj2Xjv4lB4spWtNAUGX82G7NIDOVSUqtqlE2ExPy5QAKqy%2FwxalfH6WilxSYF4wPVckbE9fTLso2J%2F4j8mXx%2FdEVzeTPGz536R4t4L%2FPb6i1dBTVji0A6wpY8%2Bo7VQkaeEyepbp3H9EtqbBaTZg3BCJeqXaQ2sd%2BdkZBXfh0vlJ8DDuW0optbdMXNY8EwOJsBXG0xY55F8J4qIopfcwxZ%2BsyAY6pgGThqVE5Vyj0NDUICFjBrbWMJhtLF7VGaLIw1yvaOAHZZyhmrlhw1OQ%2BhF08H13G4MUyQIXGpIlEGHjtAyjfyIo6WGikG2Phlj%2FLlz6kkeAaj4WjKMZ6g%2BlYSnSClrzrrfqsbONAS063jgGDnJ36icbawRetsDeXMcYyqosoyD1DgS9wnes4rRU4qO881r7rEohwUWm0EneasaA2KZSG5gg8UrMByc0&X-Amz-Signature=75bf74d73ef003732daaf6ab0b828a7af500b69a8c36afa9e2e1bbdc5dffbe5f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
