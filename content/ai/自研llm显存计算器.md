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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SX5HPMZE%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T035147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGse%2BDPNGwg%2Fd0zr7js93QvHjUkzBioEIz2scvb%2BecJwAiA720JahfFHJrT7l8ocHsxvhk7fMSEPL7uxItWnHYolsiqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGoBJ8AxaR5YZckLUKtwDJk5Ak34nQv0iLmss%2BN%2BeS2oW4W%2Fwxg3v26seBa83Zelcvd3G%2FjQCTY2dSLWvpV%2F2GFC3xY1%2B9t1rTr9ef0OritVsWOjwGdeQim3Il897YfDj4awWcxd8zyGda9Ke4XYcRCSy1QEPiHi4p%2BKSEHVj86MUSxQLdw9k8n%2F7T7Nv3suAT7dSHr5g4EIOhMTZXMCAv0bPFB9U1Y0ZtIJbQR64DQ3GFQxpj4AmJVC2Js41tAIaGqqDxdxsvBWwExgD3rf02axxw9cfTn9sDFDB%2BiGRNtcndozshX2ltvYKYt%2FV%2BuwS0ta1LZNacZliOMsnGgl8ErB%2FISKRDCUH1zJTkh8kanpF3IHr6DC9jcUEljhyiRNFHk%2FlaBDBTR%2BjZcFTHXEFAA5CotkILwzVmSE6erwda%2FrP2g5xqLTkPhUb0ijD4hc04n99EtFKeDfiTyfk2KV1RDMcvuuQlaNvEfvEZMuam1WhNX89On6qM0Byv9T8xYfIIcscqoX2eD9uhAqwVvxfzUb3vehlCeGeF5ZAbszqvyi2GGugNlb8VZk5E8MfiyL9568VpSySFwPQ9CRTY2ACi6nDaQ4sghcpTh%2BPQoEoBVdUMtIWXDnn2Rs0VTRuh8fcRMs4saiBBI7Gn0wwmJHYzQY6pgHrgnbBq4oNe7xjFDtjsTcxYaOpg6ByT1vyOevSWDN9L%2BwZqbPDuEyZwQ53QO4CmavfSMWHi34J9GFl6t2IXS6jLhhYO91ohCfybNw%2FYxkzcmCC%2FzSeQrMc0vOeu5mI4UwjTl4Ezee3mGdMxw3A7f6MAzzP%2F1IrzSq4zTD9rLSm1MLkkSFpCl9uBoqpkf7t0mvFoZ%2BpVMfdRjFupjvdKkh7%2B4dVtyT2&X-Amz-Signature=7b0f4c29923843d0cbdfd2964bb4d50462ed9bfa4d22e923cc5fa3499dee6508&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
