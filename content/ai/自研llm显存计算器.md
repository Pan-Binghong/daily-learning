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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNGEAPRW%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHP6%2Bee%2B%2F%2BacgdX956My2GuUUw8S7sUSWJNUbUhFcxb9AiEAoCZIEdqxhqUiySCWh%2FMY2CaTSCBJQeYzXW82qcavpjoqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIRxbyiyZwAeqDM5gircA3E8IAKmc9HCGpR8r6oIpenGdmFT637mABL9vZV6W48cgxEbM6N9l7A%2FyKGz17KYkSenMcCbwWHSFZJcjvtC4sW1N6lVh7xqXKaZxX0TqA1oSduhZwPm4bEEFAM3rbQ9YKfzQEJykeR7RltyNqe%2FbuY5eKvEK%2BVY7GD4VptJ3fAPAE4%2B1IacTTEUBkDbUQor7kBkKMjT52qxPA5e6jI2TPclMqa%2BcGY0bdvSZyFjzBHU8adlgJgV8nghbk2rQ7QPwr9BqVH%2FU7QH8Sn%2B3MrDNBT1Ms8XMx0MLin10ziA1Fw00fs2A7%2BSkUTaqGaIjuc3owAbPIg3GU9OBrg%2BEUtPDkKl%2FI%2FVJdkrILNkc4F%2FwNOA0U%2FmQq4Ino9%2FtkarEu%2FtK5DiZMIrkWajZM4x2zaBQ288v7rBSVvvaeMoe%2BKQLw%2F9TwygJcaFAZxGnUvNV7IuLFrOP6nQiMaxLkIj1JcovoxJv5lRe3nRKyAU1KfewTazzL90OOm1JZ7A4O%2FdZwuPVRVYbtWZX%2B79Kvnr%2F26WoH0movFwmDZEYwFM8XWznZavA02Epid1qRxzrvTA%2BfV66qLfBpUkCwV8Q%2Fc8or12hCHyQZTyzEblnwoGyD7fU5Vb%2FFlrshtDcmx6lNMOMP6UsMgGOqUBh4qt5lvLH0pH0YwI3VGnW6%2F7Qbtk7qo1coat80R1BN%2FaXujtXTF7LxWOPNe7HukbAMqfsX%2F6gvuJC0aCy%2FLWoqms41Q%2BMnSOs9zrFzwcm1ukj7WNJ2DhX%2BwIZpEIyCMXEz2XhaQahx6eIaOtdMGoCRiRXNEdg58mOlYUA1jWVD1r4sVqSAECr%2Bzxf9TX79JgM%2FX1HlbdX8xHbBUhsVeV8FcV4C7H&X-Amz-Signature=5845b32f2a92db58330d8603fcb604080360abc606e4abc30a9f98bd54a8cf64&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
