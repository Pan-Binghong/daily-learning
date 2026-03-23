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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKQ6QNJQ%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC7sIXK%2B5GjlbsdKXUcwXjka37M21K0F7GAwG0wesVTqwIhAJVcRgxWYtFPHTxKjnzcn4OOYIuXJFoBg0nIb3tjy5cAKv8DCHUQABoMNjM3NDIzMTgzODA1Igwx1BTyNt5nDQXNvokq3AO10nGWB04l4qMWuMJsKJIZpwxmH8DO%2F4lvnuvG%2FN8fQFv%2BHhrQum5bi7Qg1p1MPSNTk2tubqOw1CCqLwLPHOnngkaddviXyxiXMpTJhGMeDrCEjwLkOun8WQHQbSamtVvHvoq85bJjNxckvZj2FY%2FNREfPRQIqCus3CGpNIxu%2B1fRJY300ozy6Mb1B3lqoeSGpqvLQY95%2Fo%2BViNjpR84%2BL574auKcW5LB9wAVGaeubIXAW5bFvdR13a6sIqsxXv%2BAq1G6De2pNwH4MkUj0JRXi9%2FW8H9DGIkX6ed4PPFrRq52f2x27B9rHCYLDs8i3kUQ4k3Xf16O69ZIbqSl1wqmspRPa5GUVvGSd%2BSfBAqUWzUfbhuCkVMrcZlBm%2BbzhErYppuW%2FTJZuJRrNXTN9SA%2BlZBdbZCce%2FBJhWbRG3ajul05ypEsUK2yL%2BwsTn4uWuNSwZ5v23eBMIggmy%2Fa3jXT5%2FtiLof%2Fpvn5I%2FyluqYGMKvLPKR33iJcRm3hQpoy3fZBf37XDaAuCuuPwyGHqD4NOs5w2U%2BiV0eK2KLcWi79LsjgQxCVJWfAKowTjEyKqmZAQADWg8437%2FQ9G%2FxDMy0dNaQtsxlQ3OO1Tdqm2stCmVCOcHUydtKXG6ratrzDY5ILOBjqkARQVROKQ6RSc3bGZS4PgBe%2BmN5YB%2BL8tIcQ4c%2FRwjG05tzjbQazI9ik8YuTpPEQ%2FZd6W4f0GD%2FvH05bq5vCSD55%2Bz0pZHAbMoAFKde0bXh67IWeVPIWsLpVWisNPGG9%2BEXLwh6E1Um6cTzCzdHt8kAVaOyR7HfiBXPVU5PCPoOOKDDigY8fSJ8n3d%2BvwiACzaP8lFqUSY0wobwXh%2F8%2Fi4No07I%2BP&X-Amz-Signature=e4260af80c595b7ccc3ebb7831ae334a3d5c6f621ff2ca4fe57dfc1b4d7dc330&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
