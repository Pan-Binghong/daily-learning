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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XAIXHR2%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDPA7Bj1ZG%2FOAJE20KgwLr7%2F%2B4hSP%2FGL0qjbvkxwK2%2BdQIhAKVLcs%2BbaAz2Zzml%2FITzJcNhG%2FZRUcEjbKGdYCjuOVViKv8DCGQQABoMNjM3NDIzMTgzODA1IgyPW3Ca8HjOO5wNbwoq3AMfL%2Fk9Qz57vT7DhnYx10OLMRMi059DzXi0Cm3iSO2Zy7kl7i990cVahMYlhXU%2BL09eIn%2FL%2FF109zMWZl8sdWyIVYZ5VmEuKqKKsntJau5F2m9%2B%2FEeWVFflJDMetn9isZqXeTXUF%2Bi7WFLn9aFSp9AP7upcD0lTwqTQ1KaqY4IQnW%2FquOVu2v7HBdIt5OV9G4tZmGhMHzijgJP%2Ffmq6txeknk9i8CRYjLRymtW9BueevP0%2FBiLMo9hGbVyofjkHqJc4HhK%2F9pYy%2BGOrJHPlvB9lFmF00xlym5bjj87qOcqu9gBiSKT4OJac4%2BP1tayki1sb%2BfAQJomFcm4FrguDSkf6FKzMt%2FxwimolJOqjgwFVL3fhJb4faB8ACsqf%2FZeqX7TYDA2scMpeVYxNc11yd5%2FUZ0iHo4sEnNLeFry7E1OI8L%2BROUrelCDNTKpFVomF85BUzokotLeSadkIQFgWTTV9YZ8Nu8BQm2%2Bw9tDApacOCU2yMpIsyJlPdr0FxS%2FAcKQq2U%2BkGrtowH%2F3VSVIimO31sXnstWHOTZ32vBBsurw4qBRKp9saNV6aDQ%2F2pQ1RjsEx9JBg0g2jln3eaB7AbAZtLk4yfxMYYqauRVvOkNCITdm0SG4lCnoczBspjDkr7fOBjqkAYsYkM7tTierjU6RFYeoOaDTVhb7Va4JKl4ftMLo8X0EYfEhX4bKlANjN6m1VbztdwQGi3%2FO4LpzI0kIQoUE5mEti0wwDslzlEWOmub%2BKaRnxZhFdrQgfCfxDQklHwq3MnNofqISgA1qkaAZc8v2aQxtsvpyK9sU5pUKXOzW1809hSoj%2Bdd%2B4gbv7Rhr6fNzCjlC1Xol56rD1zhr8t3RpOOL2dRS&X-Amz-Signature=6b15ca8a4a1423ca97f4ed438e84ecad650c8f28f87022ccb171dd639ffc1b8a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
