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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MP4G7TQ%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDCDTBJUkVduZ4wUazhIMjqSHLCIJkZVaEuQf4NafsGTwIgDLmFLW1LB3%2F5yF1GMh7eiMoZf382yWHMpTybjXt9PGgqiAQIoP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIZa%2B6mMUSnNEUhiTircAxR6EQgOJgv4PKA7DBLGahn7RWW4hcrYrswYi1yLthhIum4H1tLa8NgTY902LEAIOcdNNUiOKKmXvv5QIbjWISJfPei%2F5bI%2Buy%2Fc29b7ZXa%2BseZna%2Fvvqi1BG12dd%2BS2GXLZreqUH%2FS2ZiXyWzynoNtm5d01pNDWdr6ez4O3nXqVoiNWXN74I4C6c6uXlYimEsD0yBSketmokjfLfVE9nfusZsZlAcGZerfBoR3dBeJXk8cO1ZRDmNj6kdc6EodH%2FFrkX0g9ku2LWbL7zRhaZM4VDr%2BdJA0Gz6YXgH7SJcAGGeSku0KnB16sjZkHbQsmFXQ%2B7jqYrToFBbR689hIIJUGEDAFle1FlZlU56LotlRT5XHMzxlmbtWrdAVTIlux5sXvKexn3jsJ3HSMajj38LobQE6%2FQgpOm4dtbqUu31GIsxgb6VMg%2BoEdTbxJdQ%2BNRfeu0T8YiCKlx2XCtV%2BF742uAz9GlLerN%2BLsPsZxPOy93eeJdWsiAN4opy%2BGzVnUi0tbRBpAJv6Jlm2imG45AnbBHOR%2BJKHkabKDBr%2FP670EuUphBhdOJ0PrRfv4bSO9zU%2F4%2Bi8ruWZXr%2B8JMRz8kJnY9e7EPLVFI88TMNS0NG7pIuFg9s%2Ff2ABFMGZPMOH0ussGOqUBTHPHownniEbrIzm%2FN0jZSO73bfpXG1Q00YJDyPXl1YVSgspdUnFyjqfAZFCXnZQwtiHoqm1tvsS%2BM1lkOPZ5L5Q9SrdYPKCj3vkTV7Xq5%2FRrwHhvfzXILf%2FQ0xzVPuAtSWmx%2FNvHLeC5XE1MxcyqFeqg8ld%2FaI7UkhicbBNt5V5ZVmLjjKYqs81zqUhGUKMnu5WkXdG7fzokfg%2Bn5d%2B0qRSoa6PS&X-Amz-Signature=d3d10583de89ecf836d6e9db67e9d993e1c75a9dab1b78245046bb903829a440&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
