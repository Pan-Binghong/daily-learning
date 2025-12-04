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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634BCB7IB%2F20251204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251204T024930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJHMEUCIQDzW5Z7VbJry5vsdK38Ziv4c6Q%2Biv8laLpg6%2F3kC5PFMwIgSyWSL3Ng8XdLdMYHkbUqLdBMtpHrt0mpXBa55xNYFp0q%2FwMIOxAAGgw2Mzc0MjMxODM4MDUiDKLdWPOwRXQ5FMp0CircA3PNT9mGESOatZ569MXurZo6i2LwJJm9kNuT3sAluCw74g0X8urINjFq5kseW58%2BgmbjkQTCEKwCRB6Ue1Sam0jJMi3FKXk4uM5gZgpOv8G5JJKJdSc%2FD6gUWt9qmKMQ9DQanVx5G3D0zGySLW5XpV0MLDM7%2BpRiOHawkQCXOQVktoD5rovFnsTiwjwT7uHL%2BANcWIgnRg6Kga5wo4X8ljBBlj2Fq1m07xGxqUg7HIT596A4fQGFUi4Dqvz88tLa7krqwDOJLuzcFQ5N%2FDT4K4JFUbmyq47vn9Jo5WnZTj7V0npr6c%2BF%2BcIn3rA0W%2Bd1svDJKxRyUhvVYP8CsH6tsOO9qLHL4RbpUmXeQr88X7wRv63IfmW3wIGcyv%2Fpfj29AJIVwmU71BOsJ1NS29lCTvom0mNgGsLigK8mQ%2FZgIAn46k73ViMGFVvkIICqakOrgNLnOGTuLNRUqRsaK9tq1X0OeF1U0t2Z6WttR4OmMarP5YiZZq0x9PMDxn9zf5dHrEDKPSdMXkuBxwM8wYsMS7VwyyOpEnoASgm%2FIDC1GvD0H0x0PAnTwHgq5ZWAF12vU1FAyFZQeg%2FkvUdVRJnTFHqJx0odeO78EaB7AkwLErreBQ4IIANmaWVtCHA5MPHUw8kGOqUBh6h5GeRMLPih9Tg92C4Glea3l7%2BiNTnoTP6X3o%2BadcIcVFNNxp6a6mW53irTfnD6j3NTshkcPNUX6CvpkTY0Khsxho1LL%2F5Ipc1LEZZ2bJCPgOMGBPP67BV%2Bu%2FFzTXiG%2B%2B0kJk42ESocweKoJOZwvzsKrj2rLzWklhFuQkJ9HoXyrpKi0j%2Bg1iOlyu2JY1v2y0a689CNnXe72iFBlycWyHy4X3ey&X-Amz-Signature=edadf25da014f75ceb1cf44d337e03fdcfa52332778419fa673c9235670130ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
