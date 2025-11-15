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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJITNA7J%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T023846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCvK9Z%2F5S6gbc%2FIZTx%2BvQ%2B8OcW8c0H6aTTV%2BVy1twHBvgIhAJ71HYJp7d%2FrhkStYKOwFEvhZcgswg%2FmIBm1zObTtqesKv8DCHMQABoMNjM3NDIzMTgzODA1Igxse%2B4cFt8vdiAv1c8q3AMLxpiZzI68K9BuPja1F%2Bq2xt%2BoE2f2kScQ6%2Bv3TJmbRNECD%2FEiuMP4IuGGwMfznYrkneYwlxtV8GnkzxLUeaNZG1%2FqoeXGwcJVsvgTW4eheB94fHOhkQGKiom2mGAdP8k0G%2BkrDlghx%2FV5SMxpc3gUObWQ%2B1JHTdDgH7bkdfBlKZxhsJXY%2B9u5Zf7o%2Betee3qLWXgQdcTNijfvzo5aib%2BaeR%2FIojhP8x1vfnlDl1vUJ2FH8%2BfXmAZKko14s5FKYiRBJsFG%2B59tQ2p6UmlvT3q4wqUS1EBFVgCC1QrzgvylL4VRc42Cm806Z5pDFtq7XGPA4AUXYJAL3uus3D%2BCW3IXwogH3mhVPxgvHpANJJpJgiGnpWXf88cOBCIIWrtmud0IEKww1kRvn9%2Be1tQ5NZWygsOOLacitV%2FGCGPRifCRzRv9UFtIGNBmKrtEsiew9MW1C%2B80W5aPuvv7MZJYyILNUK84zOkVqtFfagbovPgaCUqX0rsP%2F6pPTPhSjEKo0FR5KWa1WstsFbSSq8Fgop%2BxAfANeNmp2LQ2bVyz8QmrCxq54DrhgCxDlO8vBS5pVo7Ex2nZWc3Ol9iAfjbsRHbQ%2BgaCR2jMeDSw0DURlUZO0c%2BEFs6JbQHGKEhPpTCcwN%2FIBjqkAZP0JdVd4FhHHFZXbOZfCuEsHDZ9zsfcjorjjkNKqdP1zUKwJFaK07SrQihTgDQQ8xNhwnGLKKhQs1Mb%2BwwMUVVIuKE9oAuJJGlX3oAqOGNXIvBXMW5zEqb0aMaK14aiejsnkUORwqJJvsMGkmI0G3bTeQWqua%2Br%2FszkbXfRTlW2b%2FlVm%2FZbjqeGlBT1rxYfolshBEq33qzQvxde9QZn%2FncYGF6k&X-Amz-Signature=1093eb552a924d0cbb04baa8c08de7860e9b97ec6497264e09715b02f941739f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
