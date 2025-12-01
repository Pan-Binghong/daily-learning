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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KPVX45R%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T030856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJGMEQCIFJqDNuDvTD2o9N3zPliZGOOpEF3tR6RLImioQZjGvIaAiAaw0PWXO6HurNeipJVG7kPmFUQm6XWASJXzq1T%2Fk31yiqIBAjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMq6E%2BArssu%2BMfpsjbKtwDlPyT02%2FusDjCBPEMEJe5qvC%2BL8d9KWAjqqk0xIv4R1zqEBA%2Byj13FZxkL7zY8e%2Foqw55C93mXwtlMLpzlFXawZ7ZH3aM%2B8Aoa16Foqn2d7Npcr28OS3slO8upZoJjqg7%2FKh6y8jwI9Ihc6VTgM6tJKfHdrykyrtupcQUyXbZuyCuNgiuvD2URmX2u9Os52lyf0VfpyrCD%2FAjKnKHgOIoNMW9pYmhLKS8ECUh9Hk7B1RgEqgzSdT9PGTa8BsGVK%2BFAF4GzgqQTH3%2BFxdnZ8K7NXXvySxJ2EjylF3myoKAtWy9I7%2F%2FYqqusuVv5UZ6d9gQdmnAuxrR460btL0nzggKf9I9ur45PrIKyUpxfBXqFLqs31JtbNEhKZdw5epiyMR5Lo0L3R8ln2t%2Bk3jH9I39SzQo3oLa3Aixpuhu6DMk7glsmQurxPPz2dVyxh6Wv%2BN%2BZfYNcNRm%2FstsAdAywxDKVh99e8tikKMXm5fcPZ1y7gmbf6w1NiaiB6yjuQmCTGYnIZwagIfQFXLcHLF888q2gPdOJW2%2FQaSxxQ0qeJkK6C%2FcHIyRoENEgJTxbXLoErWPMYMa5zbziuW9bqYE%2FTWC2gfuQXontM2%2FlxN0hFh%2F9e8q7Pv6c6MnR9rSs0Mw0%2FayyQY6pgGvy7zfZ1f2Gd6%2FxE6uHuL6MYjxOVQxCQBq3ykpttQsk37p9L0Qz69mfqof37v6pqg%2BDSin5g0adQ3Wp5W6gJWIhdNDZGnQnXAvcYi4%2BcSK6bB90F4QWH7U4nQaaCWN3oqW5cVnqJQLnAnjKXTvdcZWkbt9%2FrOWU2yH4dbJnWGouKWaTWh6LJbauE73MoxYz5ut2Jf0UdYveP2BtuXbqwWb3ZDlQGSs&X-Amz-Signature=76bb6bb8947e7342d67f960f3a77fd872aca64024b384f812e95b28ffc900c37&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
