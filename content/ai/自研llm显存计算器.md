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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666L2Z2PHR%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T025622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJGMEQCIHEGbo2OQA0WXfqc0QeahiomC4Gb3zNYq0APUxbAIbhZAiByypKOcQGt%2BJD8Qd6pWMbsyKVgj9KiI%2Fx6Y%2FRbzVQc8yr%2FAwgEEAAaDDYzNzQyMzE4MzgwNSIMfaWz1F1TteGPyWc8KtwD1%2BAs09QfNeMo1tUYYj8pQoO%2BE0daVLIiPUKsRJ%2BfpM0f4ph6j5o0zdvd6idMtzLS9npkLnFEKCP3SNiKDeKai%2F6gCe%2BLXxk6dsVC2WLNj8yo6XRUgxHJ9PR0L7eMsxZzbBP3UNcwTK9melALbdvN%2BvxHu0nHl70jelHJkagK7TmrZfcT7f4qPCG3WOZ1PsdKKJVZFyR%2BlhDSe0WtOxI4Lu1uEMmV8S57C8faAiA3yL1%2BN3Dmx5ttiVm%2FLXRrYJt1599Ux8Tkv9cleV3uig%2F4TbZZOiUZAiCBt6mTTGLuKhv7uaxCemtqKYzYZ81zgVFdEQkQ5qjJ4kYVqeg7%2BBnnKmMZlov6a2Ftg3%2BJR4ulsqGKyQ2hOdlc28zBGf8EMCqvXKAI9oMNTakGmy2kfbA4kZ%2FA7nSkq2HnIkJMSdL9wnBxgcKWJsmXjws5yNeEIDiVnMONpu%2F5CB3QGtwvyeNc4zHFTa%2B8RwKiiZyX2pDgiLR0nlkSAzR%2BZD8Hw5%2FMp5DE%2Bve4exXBUC24LE2Hfy4fKYwlr0gHX4emCzL7DBCNPC5D5sI%2BaVD%2FXZhYjQWwy0idU%2FZ8ogZJ53DhqLkZt%2F5b%2FxnPIF8JewEhSOdBrlcoXnZE1Rxn2HRsGBi7srUw2fynygY6pgFc%2Fa5kiSXMVETYmi6DMzcd26rU0zUcAYB6h8hudDwHjUM2Mwav1Gi1UYlTmzd%2Bd7xTjJYWr2nfTwvVnKeNJiTRgkGy7DvKV%2B7b%2Fgboj1UOYSrHe2kNfL%2F6vXlFQsJbllcN22BY0Eb07pkTgEqjVip7gvG9DqJgJIJFXtOVrr960Gug4BFmqNE7ghC8vbJyFQa4kUZTidMInYxRs6QCEypoQEAU9RTo&X-Amz-Signature=70ce6aaa2e8892fa2c48c7b217ea0ee32416b4664c1f993089712b7c0385ad34&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
