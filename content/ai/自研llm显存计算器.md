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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZSPNWSQ4%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEO8OU68elEqkYcijxZGloEw3A54npvwBw%2BqA9o9lt3wIhAL29Xv4RauZzg2CzCJppWnxXNc1KKZ8SwcXTC%2FuydjPbKogECLX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx43nrOsEmrzjBTGqMq3APNj%2F0fXm01UQ1qi2Q5ypSIvj%2BEvQfhTytTKP2gn2vGt9P8YqPDuTw6LzBy7ycU7QMuju4jzXPYk6qIT3Fqz4x0nb5rYTBjt0yBZiHptZ7sHcKIr8BBUE2QxqYhJJdYR5wDaYl9RBHmcl7D%2F317W5k2z5n37qSZHg4Thfzfu35rvz2DpW2WSqQr0oRPErmfGf6IcGLWxG%2BiB9Wkn5oNbMtsTu%2FLuKvlEffCtahV0faSGUciQOkLf43Jy2%2BCp363zKhCKlH1ZFZ5GjZHB%2FB5eTpBytIFk%2Bz8Ac36sZHspSjLLH4REKqnFEnfqnTLc05eWcaL7QB6P0KYZd9rxv02L4%2F024oYYv9P%2BmnTeSoDyD9DJBPi4vWALGvRnDrfVgBg8ABjU7Hzog5fK7GEuswdwXEJd87pXo%2BTSdTYIbqqVvRY0lZGHQEeWGx6UtATEavu%2BcYXqmpTrV5ht6vxaDakNzNEk%2BkGQj0ZxKzqonuzCT7bTjNbT%2Fc7YwwlP8Ps5OUggWmLdK8UCD%2BmmckqHN0waFx0PtsIJhzY2xh1kg6zsAyTL0%2FAu4osL4pjLbCd96MauOjNdGDKjLATgraY5%2Fd9O97yeDkjne8vuyRVQhElO2DDnNdQG1EnkCFCNaK0hjCQtYHPBjqkAaQIzcigLCdx8gBra%2B4zxCHJ9O6OOxYvM2UM5LI88X3wnPFjrVqM%2B3aZQ%2FNVv9IzGwMCzPUMmhRETjd%2BdAqXlxMIpcUB3jwbdwZ9QaigdOkh2ljtLYscVKddN1v%2B3FhvALXedJJdBDHdDSVbCKzWCsz1o55J%2B4B9qLPjjfUkN2q65t96AThNgDdcViHFaq7FnpLVUWq0607whjtbAS6bjjT5zfUS&X-Amz-Signature=49deb272d2a496ae58c387cbe85e2b5fd6864721dbd491ad8be7111c5509ff79&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
