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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SEF6FNED%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084254Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIA2XndQ0o96TCUtOAfYlap9u8llvpCxDImZGOnyxdh%2FKAiEA88h6Oh9uUoYHfmtYbnXHMTcno7gEWKhw5ht%2FqQMokvwq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDA0yIMTR1%2FKHweDc6ircA%2FXXWuu2WFG5NsjDBNKEZeRGCkm5dM7Erjso8V%2FZYtdOXUJXH0AC1vgZovYW2lZhT4rDMTSaBBHhqfRt6ENoHWijwGoaKQL2Fz34uPz%2FeL6VKWabiDbVw5KDbfsLeB11bKFCL9jhPILsAWcDIyRP2DwQGOWqxiZHCjYUKg%2F8XQBPmYp4gPdT0%2FmNYh3Pm0Uhz5j1REKdG7Rv3PeGIPjDXszvcN07MlOcQtYgTP2%2Bcw7Vjfc6XhsQC3XzIZvGODvUe0PePpTvOYcum3WjD%2FSEM7k2ycGJCY4bUhHXHX890%2Bv9ZyWPG6YONiHf2h8bbzDxUv1RUjxsxSjQhjsJwhYufjNH5ExZypSJn1C%2FlYf74jPU9zB%2BxMpqG4Bn5r3cCFao7q7H8Dmpx4YWAft1bn2GB8e8GhEgON4TFbQYDnLLfbaNGLkCzx8eqmj2pFvLrmgxoSDp6entLCmJz0e45D1US9R%2FIolTV37Vj4vOzPudvcP%2FBigLPRlzXpulukjPSjs2F6%2FEjpbBtJK4%2BY7rDB8Lu8YVWMKV0rswY9WQEt7NrGL0oLl5nYwKVmoFzYnnf%2F9zMjJJvdyMjWZd58OI7kaAvEltVd98vBwYOCWYKZ3PZy7o7pFbBwNvLABTal0XMJqbzM8GOqUBY8j%2FLUSIArwlBQbuAiJNMEWbxdoHduvuPhqC0gfjtbiHZg7fcoKZrx%2Bk%2FD3FMKyXTEsMW4M3g3mz%2BG5sG1Xd4UIU1Ui4kOMIrafFSEdXxi4DPOVmAfWF%2FxnytoXkfIGJ9d3P5o6wGH6McFDGAPFk3bYXivMyb6Jp0cyQJ1FLHpE6zLLXkWcP9dwMD%2F2e35sag0IkgegAhveQiEwEMDq%2BYurXu7Fr&X-Amz-Signature=653e9a508f0c9e8032a71a3e95d8d86a64319ab64f7508c9ec2d25f8d18dfa9b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
