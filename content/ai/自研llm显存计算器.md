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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UE3PFC22%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDyFXF3QqdT%2BpSxm3J0gLgYtw7u%2Bz2DujPKlt%2FnqwwLHwIgf6rPjDpf6Dj9Ogza2mOt2BzHI0SHOJhn4tNd%2B0%2BViGkq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDOQ08hou6WA81Ef7iircA%2BoFs2aTFSnJ7zIDv5rlvVxD2V677H%2BOPgnfoWPvDuVk7EBY8khxBqAxc%2F2wVnKvd8SuKcS0eqJ775iBnAlxAcEegwxxsOx0kZLZ2Ggk7rJUhKl5s6jG9nXma5I1g%2B9ShZcsPzj1VTMHnHhII7TH7O0v5w%2FJ3%2BSG1EULJCn75P1NkgZrkTTsihqrPT2yQqgg36MQG42tS4OYFm8Ti0su2vr4Iwwgro2X8WBqXf6ftzj%2FE8gRtHRJb%2BsvHX8sb9LSRnkiNrgqdmtm7t4poMNF5C8Haw4UK89wchdGf8PWu7IEnwaoi7mIi2tT8IYvL8t0wB4fyn7pUmij6qUUUCsPwlNlRUjxuHPgAMOZh4OakwKJhuy4b903bST7%2B4KWGN5IOjCCkTDdsdJsWQT7foDol2b7Yr98UNBvc4CQ7W0oGUphXhhxxK4y8%2Fdcp5mcP7XaBrpp5qq0v6IncHWf5rFaRSa4vGv0PvUH9LBYMSVdQ9oB0i1cfY%2F5qufR5SbpsQ4JA7pOTD1E4lCw4aPvNT7GstKkw2EZTPUii%2BfkStJiaLOXB0ABfB8IYKT9wV7H6x5ea02p450tG7hZu2JqK3gQ6p%2F%2FZqdWaLqE1iQZj7SZshi06gy%2F1krjHBtFnn9dMMOxiMoGOqUBASsJfjMu6Sua8XO61iqmX7DqAS2XVmb2t6lr9pkHxe5956NHIM6p0qpPOjOv%2FP5eZnIbWyX9cV6QHpinHOLDIHC22K%2FraeRPlFI5cEseWkBmHk4YWEH5NuN0q7sOlFaT3fF0tLFaTYYRdYXiqob774w9JDQOgLJr8eMwd4x5brNQxccMLzmcjqz0lNxG71Jqi%2F4LcY8WgfwOSMxD80TRC6BajPGS&X-Amz-Signature=59d83c76de93fdf54f10f7ef30a3da2f8195e509bc9e3b48f302695442825655&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
