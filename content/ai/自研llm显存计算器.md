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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YARIGE3U%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T030725Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1MPqsoRrIPAm35xvbg%2FjMpM8zO74EIxxTFvY%2F7pH6oAIgOViMWLrguOnEuTWcO95Po%2B85hYzOopa1UXNrpZhqO0kqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL05Sc1YdhRh7WwCryrcAz0XT2HrxlkW5pllRQtiQOYp6oZK2TGlbXuQI%2Fci%2BcOmME6glL3ZyhF86Gar%2BcBsSD56OBT9hh67g9aYTorjYvqUL48%2B0aCr8bGWWGSjvQulvPWLIrjRa40x1v9w%2Fm21RANeBzNBroYErGxcwAUzNOz0rPYGqSvc59bdCXv%2BBIGszb94rKDHTE20wGq6LB1iAHuUUZD48CQjPnvBKIq7UzYMA%2FC0pW3eYuu%2FC96987vZ%2BvaqfmSfUc71HaXjvTeFXySbwENRXBM0%2Fa0tzRsoEnb335zZYSW7SnGogpBH6xyfzOepuWPGgLW7zYA5FJPIxv2D5pn1hJbIwv0HqSJ%2FYrcZsnPa0H86DNSZJz3LR5Ila9yM0gZatK4xPhWhTRuVR%2FuXR3xOQkM6WZ63XhMXdckBNMZjjVyj5JIVkFwNpWktQa%2FVOEAoIThkt%2FWp2KkNDbrHWcZJYBk7v6oD6JbOTrB2IM%2FZirgRdRdcQl4K4fISyn7CjwYU%2BsdlYxIVAP2i4hbeTq%2BBk9IjMnyM%2FONRPrBXk%2B1f45Z%2F7ZRSVVZpwjCfWBsU7zLx%2F9yCBx3iSfbTr%2BngnF57RCjribXgFtSKK1GUwMkjjv4RaLfUravawZ0VaU5tzvoHiwAZaaDcMK6cx8oGOqUBc91L%2FVTUR7NxRJfy%2FSzKN02PsmsmZoVAbcnp7pjlHJYY%2BepjH26eQGuelOh6qxFrpkqFuVmvydzDhG9QG6qGHJjZ0HdQeqP3dvcJAa6B879qZmDidnffVJC6FWVzgxmurQKpIINGRzzcfNW70JA0GTvcr59IL7xnyOM5UDHXK4MJHaKYzeQGtXOD7LEsZK6acNqjSUd7LBOOI7KoYNprKYcrpIN%2F&X-Amz-Signature=30ca29b690f7814ae8d35daac3f2dc9be251fa7c4a90c9225d3a5556a7308dfe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
