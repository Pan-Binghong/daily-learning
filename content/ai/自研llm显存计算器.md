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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677GRODME%2F20251216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251216T025433Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCdsivGsehpIiRk6DdcFMjcS6eVNsOaaxSTxALRKs42jwIgXB2euxZmb5PJBB53I9XuACIon5a7sXtIdkIUNK9byrYq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDASNIfq4pFfzgNE53ircA%2F5cAEH4Ze3zuOOGksH2ZAuusb1Q7fueaCL4M8cHGfFLlQrFQEl%2FbJ2PU2MnYA2VNpM2FbAkR1Szq6WJnZPvpnAq8Akp8H%2F%2FpSz5Jgm%2ByrHdxUpiEO1i6qiEayZtFeDicAQeXYE9KA1UdgNpu1db99XV2vt77kiQnnoqLY3Buk%2F8dkKYUhKDN3EKexeeIUiY7BdRDSTIw0gcsfNnyx7zLNy885p1BB9ROpccCdruRisNfn%2Bo0A73r%2FwO8Fz7SGbN9rsnpKJoeGy1oZs2xPMM7F%2FG5bCS6Y9vLFAKiDSQF2Otx5D23MlmnSWHzL%2BJXwKgo2N6AsQiPF3KUDIgQoHh4Q41zdOaU5aWUR9Rr2oaXCMd09G0uOID7m%2FCJoLPSHxuenwIV8Rq1XCCUcKXAiV3skDgJkPTLvyhuy6uFmD4s7NioBdWZK9036rGzYxDs19T1%2BVU8YgB9onhBGbLGOn2wolMfFu8gJZQ7T3wlOOwzt8S6mqt08gwVOa6SD6Dl0z%2Btrd1Tu38bbdCQbwAGlogzmVMmoFbYn6Xc8x4GOH3xf%2F5qNsxVWsaiwQnqVGbkk%2BXSbIfq%2FRm%2FpuUeXP2myazDOPeBk2NhQwEpGGntxvpUd0iXufkew8v7bs4TcEpMNCNg8oGOqUBldcWBoJax2xjR80X25ubDRnHSLUrfi7525a2OANNQnr4%2FGgg6qENgIdKS87HnO47p5UibfS%2FV26s3QOULR8u0uU7yEpgU9UCuzd4DFW9mr2fXu2%2F4RM1AVVLyKXSotjPd20kMH5kU5%2BbIpfzYOzblJVQMckDNhNJRMWQbyXWC9bope16tKgYvueHGAv66pgsyzpFwrGhcDyA7BxIUL3gjbE25Olu&X-Amz-Signature=3b30a998b3644c6e6b5ac853154be0e120fba66837114384884214904d48cb2d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
