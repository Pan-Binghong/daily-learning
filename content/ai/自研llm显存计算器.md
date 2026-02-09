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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAPFCQAH%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCKTdr1%2BQTTnnqQssSsMpApntMdUB3wJ9%2B3giaSI0T4sAIhAKkM4Z%2Fr0WwyfacPqITjiOxGCk4vsEyJ0MHsAOzXAyLNKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxM%2FEcEE6cZi4PvMqAq3AOwjBGm%2FwZYqO7k3khunaWdT6ZWjVUH%2F%2BHTcbk8QXGbN6hMjHd59nr%2Brj2roRHq%2FupukbXg48YCAIn5ow8CT0HqXXBML%2B63NX%2FGu7WfA8Md4lIgVD%2BUXwxrnhI9CTdk0jM7xzzEAgG4%2Biha0EPvP7Yqbv%2FvddrZcwmzovsqX56%2B%2FERvBzD3LmhNzirrI5iTuMfg9v4wS0GjJ%2FfNa%2FjYwanh89KnAkiuhLPz%2BuqIyN3yaWNEJbOkTFS2y1DGECEBFcZHvMCNLewcAIyX2BckS21VRtHX9M3n%2F3BG6taWW4mf7OmSlItV9A8hpVvPgC8sUSWl63qFCnvzNU1D5%2BljwfianuZbSTKxTJpHP8qn4SdpSHmy8IiA7Hd9DNh8kc%2FCrVu49uCdvQlPyDN9VmHr1AFR92koB%2FbcJWsIToYm9SVNmWij0ZSSesjPhQ3DUrn7sZaPHI%2FI10iMIeS5B9PRDhVud3%2F0LAv6wMAfhfR2Ijb%2B3i9gMkBSFfmzsKgYZj9cAjaA%2F4RnUFu6Wpmo2TpjrT7SoXlWFMIespO5dQt0XhkQ9GaIU0Wj3NQub%2B4VfIpHC3AfD4y68MCzkkIR5epT3Tidd3LaeWJ%2BqR35ucHqVTcikkm1lPTBXpIzJuigNTDfl6XMBjqkAeJ6QrlPhMij3OcxkJz7MzJsTxD%2F5rI9EYrlBcGA07bm1QDm1buHUcXq4swtRYBnZM96hupiJF363az0GxcF31%2B29w0oBgjrJKObW2qnU6X3QKAtTAr5XCMhsIRv8wKMKg5cUqQJ2KZDTAUNxBJKcj1zURsXA1jx2wcKtQLaSWakYbnZABNusNTlA34T0%2Fs4U85xP4eaflWlkAGvsoxbPRH8m8Kq&X-Amz-Signature=b458dd34bc1ff160618b943c31a830ec2ce6c1acd0d8bbf197a5c9120bc10b64&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
