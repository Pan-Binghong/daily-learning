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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPJD47IV%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031614Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJHMEUCIAxk%2FqKL2mxZJ3qvExaUOPnoQJD62%2FjVS3OvzzPdZqyZAiEA5wb%2B%2B9%2Ft1CioGg5pjUH8OwD4%2F%2BRn3TNZV7NtvXNQWssq%2FwMIMBAAGgw2Mzc0MjMxODM4MDUiDLkl4IkBmkYLA6LDlircA5hn124UEg0ruybsQ74nmpZHl4%2BjuaadXdRJp5rziMgt8l3h7WciPqbtXSso2Yj%2BQnF3knj8zwlzO%2BVq%2FzANZA7%2FINK81akhJ2XoCNFJOtwQWBh756%2BjrDepS%2BHusF6Mw6oKvolCrTjOtmAiG7rwhYLYVP2POUV1gvOj2aYNotn0ZYjI9kPV%2Bv2Vt8DyDlJKGeT%2FcQw5wcxnb3gD9yAt4hB%2B2kRErFxVUgNiVY4AVF8%2BMOX3CvwFNWibOg0W39NeZFYPBeOZmjgHoqi9s8VLlByq6ZAdvwBS0yPTpTJcx22tvKBl2qmfsW2TaC86xnN9ec2u5uZkjPmqLc1c5UeRMU2064by6vHCTRn%2BacEDGdPt5O8ziNBeXGUy1pxLl5%2FO4x%2FFTgowviLyoRJspevZS%2F4CWcjrtXx8XlMAB4LOtzUnrI7d4pyr35Sk25%2B6BfJUDHBFs8qJc23icIweyYVcEY6oGcbKh%2F9VSdmEPVoMwZEe5PrdSJcD%2B1YXbj8ekRUZnXQjD30Qyi0ay72RKdmxPICazu3aezIwV%2BhhYWhmmBiTx2xiRA9Z4lwiOgZH3f3lnXlQlkajpW%2FIikIiyTgAV8DvmZBtoCJpGUtpSyUZoY75BzmbpR1142MjkrucMOyy2ssGOqUBh5%2B3Aa3PzEEww8IuGejBOezUly%2BVYkcXcz8uulYpGrX6E1PH6FWUO9kEGFeh4BihRPRRfj4uoix06YdrbpGmvEddF1J3Gm2jZLrP6S5mWxF4oMOy84DlxB5dApF5QNkA%2FMo99AFvnC5p%2BiV2FX7Rn%2F2qQgGfqcPK2Z1WBBUwhnPx%2Be%2BLk4BHGciA4Z%2BUuFSLlkeICziyN7BWFuhrSKOClxAOdi4%2F&X-Amz-Signature=9eb7851e8219571d5ab51e8b918984e543fe8b876e3483b99a787a716072d9f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
