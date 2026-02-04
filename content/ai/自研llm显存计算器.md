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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RAGOXT65%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJGMEQCIBnZPyukVl9m5PvO3SDkjLC1VgarX%2FSlbCLM9Lm97OmgAiAcx9uGuQNLySsWAWJp6Xsl6pNMACipJ8TcU9pb3V9XaCr%2FAwgMEAAaDDYzNzQyMzE4MzgwNSIM5bT%2FUQ3gu1Q2l2AHKtwDsljW3zUBZ1vGOAq1y3XItUYfr9CVCN1%2Be1x4t0BZiBe9zgSnOJfOoL4IJLzDEQ8ujZu6wS0RQFEteagnhLtAcSGm2EZY%2F7%2FLIaGkmGgCSQjP7hf3W45QRF4pXW09zdaJfbiQdGWEWn8qBDXBOLPg9tr8GeEhQBO%2FAzkl2NIF02qpegf1l6XJrz9SH%2F0GQqspGRBekt%2Be5fk2HKNXThlqR8f9eNVw5twQUQ3cDhQ9shNSfSB2Qs2Uw1dAeoJMAWF5p%2FvmwUKrRV9kB0yqcI24ii1Xgd055d%2BXPQ111WuaZWWbkS%2BCcKAnhYiKWn2zS%2F8hTXsUGtRmx%2BdJueyP9pxHPN5OpEjucHOu%2BRtSn3jRpROtiimFggXgsxHctxZGre%2BdNtJKBahb8qFvjHHPXmmBEZ8Ajt1oiMGbQJ2xkxqXvLWXu7tqJ8zP0T2mhuTnkd4zjPhN%2FKSRVP6IA7wuKF3OALL1Y9cFyEb3TCxJTXel6gQ46cU2ZEBua5z8RAeYPFsTAqzLyStc3yeddNyyihJhdJmS7DF5G5iU68TI0%2FwsqI4f1axpvDO0rsgW%2FT3xQeudAYTWd3274SaRpUqE3svZjPpG2fHND2ztEY1QCgEcy30KiSQ%2F1hB3NWKcZ9kwguiKzAY6pgHbiGNT3HDo%2FiMdNu%2FbTMdpfhDI6plihfrMcvVI1dgsnMKHQYrmAmpV7uerjoqZfrEQvAou0s3PzxETzjY57dfFBMZL%2BcBJ%2F2lrepfTwzoF8g4eAEqntxjdYxpqbEoqWE84eZLN00JsSPu84RhQb0acme1p8FmCwpCeotDN7dI%2FgSl%2BovaCxb2zzcX0KeMfx566bQ2MUX7bwpsYDQj98VoPTzqKDnVf&X-Amz-Signature=e92595c69e1b3bca3075b1d1ac9ca4c3ba17d414c26f5697bf3b9a0820a400fe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
