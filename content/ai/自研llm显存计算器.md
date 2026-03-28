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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5JCDNPO%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T033831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIQDxte0eWr8nZ%2BugM5VlNwS%2FfXm39bBigOr1R8oa94%2FnKAIgB%2BzRljjntKdSKpZQWN7voAloZYIzCbAtGaFFp%2B10Y48qiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF6IqVN3uclNSbNmoyrcA7NjRxnMUgfWmRqnKf7CVf%2F3iQGN9NI08qjS0OLDedHn8gk7Gx45gH6ZLcfhJsouhnhPw%2Fjx7rVM3EiPVhqSmV11kx8jbj%2BRv%2Bf1ZE8MDo2QANI2FOtMvqEaqfk9ubkWAFMP6CayPDZtSwA2JdbiQiAcIR2PnlnZaJ70pLSMMDRsqz07%2BzEUyyE%2BWAwdd4sKeXR2U3l5DsTjuP%2FhOayufkQm30OJN4vUPZlAc%2FPK%2F3GkuGWGMQAAGs2gQb8ffEkFI4GuOAbgR7ke9g8uAbmYyRdBhLf0F18S%2Fy1ufjPc%2FG4wJ60LBTN1GZRV9lxXwUDCDZoMelqNY%2F7%2BuHOwLf3FqN9hofYEYS6eRdDrnQtgRbjKf6Mv5SMrHk1IP9z9%2FUseJH9Z54tRfxUN1i3i9LD5o%2FOQ32mNCmVR5roKO4H0A1q%2B%2F5odhILmgna4F3hQLiJlUlsOOe1XmWOp9Gr%2Bfer0m6Vwq8aJZiYbL8%2FIegk%2F%2FhmkXooeyuL9IeNdPj1zpzVVe0Iy3OVFuo3aik70vCbLidU4ONkJtFnFGDlHcd9hXFqq7L1UzuaqHb544JyMXC2Ylcu3Aq6Twy5PlnNWbwvyM0d0Ogtl8lgt4TeZZGHEH0tkEZx48CINUIHyYcmAMP7tnM4GOqUBAalhwv4W0yb2B1o%2FocY1SRy9VCeCEYgv99oU3EDW6jkpY4QtH4IQ4k1oqFQ3egrNbE3j9N%2FPKRfV9%2FhVyvkhcXZPvBwsTCFXz4%2FKWbSZLBhBVe0bXQG%2FC6wcZsz%2F1xU2pCxpOlj5QQfBE3u4dkjGk08WtZ5LPd1eqhqh%2FXOcR50LBI3KPZx4hmTND5c3HKbEqFiLs7OOi9wlhc9rGhI6zKUlr4AF&X-Amz-Signature=1432c081867295655d925413ff72407af8df4dff26e3f2f024e3dc4012b6b619&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
