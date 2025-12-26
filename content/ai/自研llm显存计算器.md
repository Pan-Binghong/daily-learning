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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665Z4HRSVA%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025456Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCB0ZEbdAlGUFNqKkmoFMvjlhK%2Bbx2ET%2FSeJtbj8Uc09gIhAJZHeC%2Bix38ZiRWkPn1wBAG%2B%2FD6mv7CAGJuMWeK6QYkHKv8DCEsQABoMNjM3NDIzMTgzODA1Igw54redzTYhaOOZ%2BCYq3APazegg9VdKsl6IriEULV%2F%2F4pQ67XYlREs7aB5TahmjSE4M1lAjnvafEUxB1n1aqhu8sssoy0BZgErIgD%2BzSIzSlNK7Kua6D2gQTjsWVocVuOgwX65lSvaR3TqTqlwjDU%2BpiGqOFHIYzs9AAs51wA47G6vFvKmU1T1QXjQ1jH4VSSAw48e%2Blj6hYxj9rbufg2cJTRUWNW3NoCEpfAu3Npk8BIdXWdbF5qJkdUp%2BAISXFWCIhIfWdWq%2FAleCQMs%2FucPTd9mrZE3rnOOdGT42CkGv3LotYXdGSTG4z2O%2FKVetlyZC7zxIRoU1mL4tTqpOL0fHWt7SsVfr7u91SBEDKKu7uEJHFGj%2FDyFfmUdOpUaDYdXwgYv70eFmWLdKv2HLMoO%2F8RS1pRKDiB8L1SCNG8V4UeIXzDt3VnVSyB7KXhxNuiRRgeUeb%2BmwTMWI0AQRC4aoNhnPwZ2Z9dfT9yBK7sO%2BINzSjgHNGCcXyzs6VtzP2abdKveJogo9ZmSD3pRcwvHCvGTA0xOFPTHfQMN2qWU%2B31djuR%2F23j74NxDVuXNQW62NLbmWtK7zECHh%2FXRKINZbOLQEQub10N1WR%2FqDl1dhVoJzTAhqvq8s0yi5iZZ0blwfDxS6S9%2BtxXsgwTDD0bfKBjqkAYbmnWX72F3sMd7IzanAbbEw2l955slAxOlYoDjRrg8KXLKSfmZ%2FkX7cbMzKfkmsXGFRwy0rJj4oGNZaAGI1AMdT2AQc%2F0%2FRt59JLiuZN%2FospLE%2BZ0n3OBMPiuFuAoRxKIn8emn9TyN1k4YySe1I1uedYtzmDHqNELchktCkPjnnJ0g3ER5BrD64egwABYN6x6twmFi7lgenKK%2Blfugo7IlRET%2BH&X-Amz-Signature=2594775eaf82bb658b4f9c3e94fbf3754c9f6ae4ddab28689bfb2c418bff8a28&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
