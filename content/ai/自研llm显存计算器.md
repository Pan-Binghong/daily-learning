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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V222ZYC5%2F20260321%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260321T032323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQDpOzIC%2BBInTdyteVjVKbCheEo1oyn%2FKN%2F61HkIx57QWAIgQ%2F2CosSBAvp%2FtACCs6vh2XLWKiAH7WJf4lOEZSkwC3Aq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDCwkdS3RqfpTJkrn1SrcA1PJ04ZNeOQZsqieVx2FX%2FwBUmx6cE%2BHIacedVdmLiVWnrDngp6GFU3oJOpJpUqTYMUtavoFOAtQnFJcPWuT8jrvHq96mBMwO1AdO4I5W%2BtNluKfXmc9ILpxdPpXvHIBX7IU63mikIa5xPQrzPiLYI2q5lfzH7xZFYUl%2BU7AYcxUpbmNsB3H%2FT0HI%2FO%2BMHYIw7r4tn7FosyUqdiQFcGF%2FfiIEnQyIDCdb7pX6I1rerI4jYAJnsw96gqrCR6t2J7K71BeOF9Tgcm6%2FLqMicdBhYw%2B6jZULk%2F9gHBiHlDomnwTvGyuELmLIGqBq7%2BQTu6VGxQqH07LetYuzlZ4myH53nGO%2BSsYd7mkdaWgnVQRHXEMnUgXy%2F7tBxK8t9JDA5ZFgPmLA9y9mEepb9aMEVYRHZXLXy4tSJ0mVSpVLQJdiO%2BhWGhJ12ywnqhETIbW5lAQim24Py%2B4d1BXA7WShibu9721Wp6TkaJz9XEMzc8tydhvetL1u2hSg5ilk3aToN4sQ7encnCgfMeYU7Nj4tW0g8rdGdu0iZPcboCft82hZvWnsnZwUdLfSCpmFsij7Oef1mNu1EpelfQEJQrGiewibCyv9S8X2wbr0oOX63Ki6zyqKJHMTgbC8qqKGe1IMNeP%2BM0GOqUB1wH6KpBmX8GCFKhIh5vn8umCL7LvGBSNJcD1sfOumfJGyPBDNFCNv52kGl1SXjFbD0qTws3IlaAVluaV%2FZssmYtcfW8T1NwRQ71zpIgNaFEcG88dCgyIP6YgxggHOveArc1GI3Hl%2BOyC4qn%2BUiEPcZF8OJ%2Bw1j75cUXJDPmrRngyjNp4z5LkeFNH4BiiriuLNsqvWUEPyHcs7Ln3XYb1yFQnBsZx&X-Amz-Signature=32b5668005c99f5e61074497bc49e54e722c36f7872e4897a153d297b1591cad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
