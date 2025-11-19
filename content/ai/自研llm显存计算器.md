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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YU3HEMY6%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCIAnT2uhFwSj4quZiFPjK63Q29nvDqc5jGTiH2bJBKjEkAiAC7EUVWF%2Bz9QkAuSSWzBkclKxMjgQZd6tmkfL1AvEg0iqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoRO786fTpGe6DknjKtwDDcDz%2FiC9dl4AhLCH4LAJHNPcqSLQJ1tB0iZfYRUzhVz6x7PJJ6bbWRYVzkCqtiDKuV%2Bg7cfeyJW9cxoPL3zatEPIst9jpN%2FDKmvnMHVOlnvQilU%2BW7O1Wsi4wMML9bLB0fdnoSdVLqTL3BrkcMv6J%2FgUZNIN6%2FVN3Rcvb56duIpKIGmGLBQkCZ26dTyIEB%2F2BYTBcfgnzAg%2BPZC%2FFgQlmmA%2FCULr5U0PoSrybzrRGAm%2F48IpzEv%2FSdZ3KX5O%2BMMYMUwh9L85MmIE7ufi3O15gJ7YIUMzyLJHxKE1uC%2BEiqvrU%2BAkki4wcgIBshPfEuMYMVFsLdAsy10ns2xd7No3mttECmyJiKc6IuxmQRVQRFw3De%2BkKX7h2IZJE7Dou80tVcI0iyd75e7bPAOTdMGOvdEVsQQvzLnUXU4wV1kuE6OaeyygmHgg4tVWh2KPBP6%2FyZiV1hYQxzD5pexJEzdfLAeuZxeqqhKp6fJAms5hlpXiHwkRrziER%2F%2BRQT8%2F15tZdi1GC8bP%2BJfjpOHe9gybCqDYCfrvnDgGk3jYPPjJLJTkM0uqdTTAMAMwNqJBUgnjaxRNHBYGmY4TOmAy1XgOdRjJRTdkPkhdl2CMtDcQ9MsUD6jmVbR9JadBjWcw6sn0yAY6pgEY1q8lQBKYmj58OYa6PtBN2jyPl8VrcuYHQYM7g6xuC7qseuI9FrwYwGReUxCO7Gud%2Fwu7%2BvklkBIujUEBBJxUu0TiJ%2F7o2y0fd%2Fm%2BgQHmlC7GpHDXR5EQ7UbuqAljE2IshvME8NukPhVQ5jPOD4RQx3OdgluVkTuA9TxjvStpZVKMbknXlVtsvvYUeTIBAy9BbZX6ofVuZjMDRXnutLs2CZ4QGXFt&X-Amz-Signature=373d8d4d9b574c5335320946eb0b070e38a40e576ab3f722bdd78c949f1f8bab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
