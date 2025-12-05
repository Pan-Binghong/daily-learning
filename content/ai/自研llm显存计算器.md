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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ULSOYHH%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T024943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2BpIFh5LWjgytaJB7mah6ggV5OSgnghBbNXjfH60xkHgIgbVvwIOhFyHgeFi9N6hI3QI9B5fNFg7MnUQlh%2FeEIs9Qq%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDAwfgXdvkjPAKdClPyrcA67pAF7ZeeXt7xmHMaH9S6Y1Xk3UqSmbXBlMaPeKbYnnW5YYY7NK%2Bzmns5n7Hb9Inn5%2BeWcPTG4psHFj1WkLI17%2FygkR2SUJjO7cK11sm6orL4bUady5cb9QT11EO6w3Ml2dIw5lekSpfoVmlw6glM9EN9nDYfm44rbvpdbdFVxU62KJEp3SrlgVY3mAReW9qtdJKbO6hkd9yrTiq6L0fnFzASjDdDjmwrhLc49KVc2ksmWzGwvk%2ByxqDqjaJuR9djI1vQDzaYV1LncNZgQ15zj7lTvLd93CDVphrNimVLjTT%2F0vOgX5Kb5nArGDYhDtJZjoyXbNr5Povc3i1PAcMata35xZJUU9339oUPpdXIfZBUuuVlTGiv0JgQ0HVi5rUqpl7AvuBHOTFz8hJuRxGlIQtKAr8X1DcE0w4R7v6B12FLE7pAbpvwe53Se8nSb0z8T%2BkqYGyeYzCzR0%2FqHXbWqaZkXUkzfNxOe%2F3FRx0gTNkA6w81F%2BePElTBPP8VCSdhs1mQwLBeTIxwZARQr9sVQThKwVRZ74e55JYgh66x1lFBPF01e5C6v4Wc3PEUOQfdO4d5OPRrvcHn2f9IXyomZ9X8fg%2Bozokrjwo8qd7DN3esoCBaEWFB3eGwTnMISMyMkGOqUBv%2FkrrLsuJ0WXYDHjVALOkGqfUe9M5NBhWszQ3H8JAAEvR%2BFtJayaBuRbmmsRKMwOMtBF%2BaXOctzZzGKIsV69lN0Dml%2FV0v9Kwdt5Bv%2FKqUBa7OInashmX3ni%2FRZlLzgcH2WqrA6oIFITKSktBWmKH5tL%2FL%2BMw6GqEL3F%2F7PJbiLZNNps4o00GmwhUs4iuNroopK50lWFd4IntSNpSacDSo%2F6lMvY&X-Amz-Signature=dba44dca58d7370bf0f73b1c1602245059d104f6a1a8602d43d44c7dcffa732c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
