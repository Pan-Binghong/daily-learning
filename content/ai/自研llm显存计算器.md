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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663W2RA3IM%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDOtVjss12wPq0BFZT%2B3EXHThPp5tH5l%2FI3okK9MDSNowIgEMePEBX%2BN0gQHXOT3OzLfugQHnBJ00SPGWrZbcRxeWAqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNXq1meG1A7MUIaLOCrcA1SglfegeiwsMVOeE771b0vtiItmcESgPF%2FLgeac%2Be94xgQ2oxdeY3oLXTcqLAOwOnucmadJsni1xKdfjCbafmnR26IV49VOFwxIIHp5y6Et4OdqtdYPQX88oUsMjrdo%2BZCp5Q0FrQjNnlLH5%2FoTX9Pb1FPaI%2BcBDL7vy0Eq96nQNJrW7tFL0PCYT%2BO7QWrOKYpJeBDrg2Ziqn3CoWiDLpP%2BQ59vkY7%2F3PgaKkf1r8842asW0eaLb8lYuIwOtrIz7XQ5pmv%2FucHn%2FggbFBnIyXS%2FXIM9xW19WzGOPtvGZe9tTmepSQJ56XNh6bSWjq%2FxgSadwc%2FMx4tVKowMIxabov6Uoc1GFpt2pqJzvISMLmRJiVPeVs%2BJ%2BrZMTJT5iYaz%2Bc7oFCAXU8OE1%2BvtSC1CmxuHTdBva6i3qgDKiza8MWly5EWwgBYZ9NOtxv32nx8z3asttlWnyH8AkoyFZdD9kiim%2Fn6TYYlto8xmZipzCNuDsiK0i1mkoZXcBxocGqR0p96Nxfkd2QdLjjrugrGdGPMaMmbaJ3SEtJdF0%2F25ZHqOvVjWAmnJJoU3aWFOAL6jd%2F4rX5mucWiqWoQ%2Fo7J2qkyBff%2FAnFmtFHUK1GXcOe1la%2FrDvt57mLey06%2BPMJLdtcsGOqUBUvB%2FjoHekPrdbDzdW5rOGh6Pi8wxqZH81jz1lVfCng7TeoajcTWjhMnfwJFyk0norgHfL7KXOOdQqLo94OW1MBYeAy8CxcnkA0bmizcY%2FXA6M4S3zJVg0sjhEU9PE1kCglBLWd59tadExx8dKbUKhWHqX1KioOLxdwPsSSXNXugFpLSlZeS554c1Eejxx01JnJ6CO%2F7dsbGlzeRYNpWZVzoRevJ2&X-Amz-Signature=13010e42e6f31bb7389af8ec479cdd2d56d2f67175b1f998de9b407a874a1a93&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
