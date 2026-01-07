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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664G6CVBUO%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T025910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBe5TFSq4bScIOlKVCxu3B4ti0PPhhZAqtBroflwsKiVAiEAw%2F14LYC9akVgLY6JBlN3MPFgj6rS0w4mOy3sCu%2FFdrkq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDNqhr7vVwwVGKxnB9ircA5aRigvumRDhxn94IhuL%2Fn0%2B3f2Sf9iAMNv7lpSyrFImf1gzm4Ft%2BFMAPNEqXychShzHaggqFT3JbcQjJ4Y6b%2BgVVzT0Ks%2FDw3zUaoDDz8Q6TdnI%2FxsGQREId9%2BAq6dihyAPaaT%2BRu%2FJlG51qFmPUttJ1z6uE6cU%2Fw%2FsrZGoRn7eH9n9MGaOFZ7xiq%2FB7ZAquFlaahfH%2BHXOXrHZrSJj0EyyT6AOLY%2FuwXihD3opiuKrTi%2BRJfj2wE9nWlyQCH1S3tVkRA30hwUJ9kx43X8W4ZHfE%2BIfmixOqsrWqzkmlSDZcXia9b3I4L0%2FrWQHEpmvjNbLd%2FD7%2BnP3vbqEQueiHEMyV9N%2F%2B8Y%2Fo7mLyh%2FhLNFLcr7SLO4uWpaiIvkYytzFf5%2Bj6nK%2FILOljRJkNJ77tsVNvONc8%2F8cEBS2FSLKLAtnEWLpdPLBu0oDRDuvKiXgTXQPGwdp50c8xu2qYfY5OocK0KhvZjO4qC5nLimdO7d2X53GhnIRBpW%2FAFlIMpGDIoufTm88gmbKWqbH7CJ4FcGlbF0QYOsJNdDa0Y5KcJqKhsP8AicvvafEUbJSJdyINsMNTB2k35fdPaaJa6tmpDGhEBu4A%2F6HMjIae5I%2FFQ7oNfKVYpzILRzNOsOuMNqO98oGOqUB%2BVwp3QQP6JU44yoc2Q64az9Dt49vN33bmtmx3zeRtzjBFH0FUWU78kZTGOr4GW%2B0x%2Bv8RMvVoaoM2b6e081R6bisFtSEXvN3tMvTwpB4YmG2ZajP8w0i9zNzcTZ57AfQfUQyc%2B4hua%2B4NoXrbgMC9bW6nDnpdAcLAO5wzGU7UPlNjetQLlJ4%2BYsCBPoCOUprHHrSte%2F7wCKIn9b%2BAHV0c3zdWphT&X-Amz-Signature=a95a18c495cddf8d5ff0fa615458f22bed0beb7785f7856001528678d74aa12b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
