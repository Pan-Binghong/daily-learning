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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664STKUDMF%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T024923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCfgLyTPKY4f3VpAvnG3QlMqXuQPhkmJqalZKLpABQY4gIhAL%2BZ7icHkaPBJGaJ0luBnCaTqjOGl%2FFrWqBh0Rq2I3%2BRKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwds88r2o0z3ex%2B0I4q3AOeK7fv2sJMSrRhI9x9%2FP2HGQi7UgzDsSj3SNUCTkSWIYpHVnrwqpmoMR%2BLPkcaktHXFmlMJhg5DNgsDzY%2FxB3wQmVGYx5I6M8y0gBekXJviOkcv4Eqfy8PO4bFUdCDwsOtQbc64E0t5%2FV%2FPF6QZzVKuf4auYaQ%2FqfLCXsittJrnP2RxpOfsYxXetgvMxfI61guLPzvZJmwcHlmfaFyVcuZXtMH89mfEUAYXix87qrggMj6W41MYAYVro%2BxhiCdKRBRNqvEgFiv16jW4k71DiJuFXUx2kA7n2Gd5hSOeYW29XLsnjdce5T0Jb53LaJ9SE8oqlpG02cHFWOmPdk%2FRaV4qO%2Bm60IusXWJAMrZtXDeekS%2BXGU2IDbCFaP63Ahg93pK%2FjIudlpAudT9H%2FfiILqaqFF173wA0%2FsmIOQ6h2dOE65SGvq4HJ8hT3maSxcfAD%2Bhz5zEckS%2B5vcxEDn0z4nQ0zqW3UnYInZyGv65HAhioL0Y3AlCWZRBsEkmnNzgJxr4V06IU6Q5y67iTGp3bTNMVizEw4v9v6%2BnVFPqNtUX9R4fhUctzrdNiWUZOUKmdGTrAWqmD2QjFLr14T7E9l%2BWb1mNceCZ6e8z%2BUCv2mOLTXC609t2vtUpQe1PSjCEj97JBjqkAdwTRsjz6VtlJPpVSXhkyTo3AqKmUbZyEWx8KYGVTZ3jwtRRt5mCtFnQLMyB0pBN2ChJpFssd%2FYHE%2F%2B864r610XYjoQ3H03BYWEZt4uDVvK4hkAAM3FXzCW6v5IkCgz5gYfXl338SX1V5Gphi9sS7YZEqrKlhcwBzc8MsGt0cR%2B80hNv17CzRGKRUef0L23Z3kx6vYX87UGe65TaAkoHXmjClI0j&X-Amz-Signature=5a4c73e7dec3cb4e8fcb782c7d7017582b8e2e514dd742f4c020978683df295f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
