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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TUQODXYD%2F20260420%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260420T042126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIQD%2FsRCoi%2BG9TOI2E3ngoO%2FMEUiq9KTlRBOlgeb9IStGGAIgSidp8ttmdQN%2BuaeIqYw%2FXNRs8jWtMElgp4F1B4jKLXUq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDDxGAT9bgvYSVkQuhyrcA405kZ3yWScQNCRTyCUxYJsAxCUT%2BlYzuwR%2B6Wks11i7apmAbSX%2B7%2BoIEiHqj4aCHAuSZtv%2FFOGOkG0bAimSt3idE5iUqbvnGr%2Fg2vjxJMfEbwT4OLsd74R0nuKAavB7pp2g8sR4QJETTShqP5dkiG9P9sKsTJU8vMu2S%2F4w1utj4CVY241w%2FwjhzJbf1tztRo2ICyWPledZoXi3JxT2yV%2FBCo6Jfv9d0nqG5AaCcpXcOHn4JHd4ZKRqV9%2BihnTsX5r%2BGuIkrgWLESn8lK7%2FABvV3OX%2BOmLMROEGRzCdA7qARSRi4%2B1%2BFuEF4qF5xyncPRAv2Y8YBbbDhz7ZAmRWgoSWekQOVotJ2bEx2JZ9wp44zE6HxEk96UnAnjpoM8u06bf%2FLjE1ya5YPJau7%2Bnb7YesIyYln2PEQFdZ%2FrW15lH7zP9FKtOtWCzqiq%2BxOMng%2FAWy8JsLHyY9C4HM5HdO9Kv4nnXRl6dfGCNslM9%2Bb70slijQIqJpAyv1SDmjWjDbLX3VZKmNtSJLTlEnc8pMjrSbko0g93IIlobMPHbG5WGw8nhp%2BKZCP3p7T8%2FRhKhoM%2F9kPaG8%2Fpo%2BWX0pjKqWvNfrIMbK272FZWG8VRIUChPY%2Blvup%2FlTVfZHpuq8MKuXls8GOqUBaIXDMktxeTEmawN5oWtb1ui92MSzY6jFzkleQTO4tr3QRarmRgBmDIo2g1PoOKRDZQDkOVCJrk%2BSxQ6DpedxXl%2B5taFtfeV1zez%2Bq11n6y94I%2FQXc05M1Rli8v8F9LK5GNzQGtgXZlcUmtKRV5PbpvM6xhGpFHYpQj2JKfAjm2g5%2B9qPQ1eUbWJtobrvgQ32f4tPNd8lo7oUpJ3LdzEd7akcW38c&X-Amz-Signature=02b92920319481e5ffe4f6543977dafc23c061a6e5530440d836bcaac3f90bf7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
