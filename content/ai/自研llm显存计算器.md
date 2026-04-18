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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664V4ITUT5%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T034912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQCFZ7KKfgyG1zokkOKLS%2FBDFKC%2FmmUKB38zdhONRJdvKgIgOO4Kf%2Bp8wyD52qhYdKoBy0upVNe0n02buMQ2XvKuHv4qiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJsN%2FMsD%2F6gO1s24wCrcAyHCjQ1kgM48yMeyIpIU7NqsGUghyJaFnJ3ycS8Ey25fibboTxu0fAcCMujLxLPpkM6FEHi%2BiFyvUtIfQqRu9zOZTMAI55%2F1F%2BiIIY9vyILE5EcyUHDgN1bC0dIsbZGp4CxJ3qAzGtiPNzVmyc7JR1bEJ7cib5ksioinr4MLU87STtZKwDGewfJsp56ZN%2Ft9NDYybF%2BgQMzlXcm6m%2Bm66dGnNpk0OLH2PMznHHKAGWRJBzOY8EcLUFwMwxEQHWYlhG%2FPLP8OOCmRQWGGjEPlKsg0ittIcNMQDFHh7nYP7mY04Vul7PjKBtAXayiZCY99W6HUZnDjX0MzBIbKluRQpJyKEMxWkzLS6jHezmEPwkycNIqOEwdyZ6fyJ%2FLH8Li8k1x5ktZgqt%2B97PeZrPOvmEtLAYu%2BhK5wCOfrLkGmXVx%2BIChcdk9Qb7hNj7PHBbYFK%2FRdqXMQ5R3iXrYqTAwHyXsg2AI7bGLPOlo2DTvtwj83F1ExDem1SkHokf3kKCIjGZ3BQf7grUYh%2FFvz5OsSH85MmVSW5j58rewNWgLRmQCNCY4207tswbeFK%2F552WXqmfPd98E5H6tzWIs92VH%2B9Kc1RH5x6hlyZN3RvOl0UxpSlMOki9xPPavzlU6sMI%2Bui88GOqUBb5TlU6eWYVamfNzR06UWZmIoDMDdMTLRM3cpY37hI6wOXc0%2F3erA856ZlnOJAXzcvwog8T9KELyvXJh3jm5MIg2hv7ft%2FOPh9QleQ27mJEjGjE3E43k1fnHi1tuDkAeNKALW8AkB2%2B9QfBoR6TUG6SSZ6rk0rjvedrOtXs5fVGm59bLVTazIwIW8OLfvDh4%2Fi0ZJ7NgHGp99lguCuH3qqCjgdv50&X-Amz-Signature=f5b7a1cf8f88629af1a90c176e0a30b8ddb4c89ca94f3a941d3741cc38a562f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
