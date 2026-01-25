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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7RORGYD%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T031227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJGMEQCIAH6N2abz6jkwSPSFYuykyFtYAYPYC%2FQiNEGayT2n2%2FVAiBNwxhGcA7%2BkSUQcEamKvB7oNClOWkoOTyg5ncPZc0qYSr%2FAwgcEAAaDDYzNzQyMzE4MzgwNSIMFCkqBvxqDSRNVADXKtwDj9gqAcEmf3w9aFDO3mHhpOBTr2A7rIaNx5ubsRN69Fg2yp%2BqieQ4dP%2F5NrFZogFsXjX%2F3mFmgpIenV5bo29toaLKXNa%2FBPe%2BU%2BiC9nHWfAb9rcmtOpIB%2FIiX2ZId5FzLvnW5qF%2B6iiHKSRkGA%2B4Br5e0w95%2Bw0Iy2QmlNVbl47EfHMMXjP8K9Fb4cP5qOx4G%2FJ2bCwGpj2uZBItx%2BO7ECQ3VEYQsjFaxR%2FLhLtscQkWcccGsUq2oJ%2Bs%2BQZ5QIMU8HueaKwVFHD8uaFr9Mg%2BSOk626PsE%2BfBKatDCOaH9y%2B4bgqEfomUbIq7XyK7DYWAzA2GQ%2FT%2B8VHAKF7afPsDGt%2FgEGaPPYkwEpAnsqCj5XlJ7ZJKyRZ1VoPQcnCyc4BlEt%2FuBd3n%2FGQiqop3MsIID4rj%2F2FuU1hBob%2FYY9YNqkU8eHuSW3QdIMToYKYPVtv2oN5oHwVGUy%2BXiqx8gaozydRNVF8urAVnldDlFfwOF7zzFtG66RP0rBVHkzbmA1DYuxKPYTwvBbBDJ3E7CPoDdcQWv5sLOQymbqekLQf7WaVCoiqwRbp4zN94er7A1QJQx7U5pF3prTqV3F4sM79wq1RAdFUTCMAec32YQBrCT34tR%2B4hT7YdxSbseJhgw8oXWywY6pgFi%2BvHRko3vn3Q4d4ZaynAWpSK3bwlfdT8lFoUDF07h60hqhePCKtV3ZH04FVFMZsNENLl6yZDJ2GgH%2FQzSt%2BAnEXLlm2ekVO4VeO98ad8ky4WFx5mFH3XWN4tSYHBYCwJdQhP4mmwoNZK5FK1ESX8e%2BAD805m96VvYI2fgeB4Ijb6LY1EZS1MASKtrOKUvnp1Jayc9Uc%2FErFDgh3RBkcoyCrCjvIQE&X-Amz-Signature=06119086652d71ec7aff6d7eda75d83e9859c5910217d6847c34665fb5765ba8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
