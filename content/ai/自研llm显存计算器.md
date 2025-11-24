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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAN6AHAC%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICAVR64Ru1jg8DN0okbCk547p75ClCR9ELVNgahKScOsAiBJZtD0t23T70m%2BXeLL7JnVZTrb%2BBBB09JcfU75ONyIxyr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMHL40pa075lcHKMKBKtwDvNRA4Fk%2FP2L944xqw%2BMHEKTh9Z3KIXneT2tWye3uNFDOrBtB%2Bq0FZbMvUHoEFCrR8EkkjB0oqBtYIQK77EBSvjAN1mN36%2BHkcJCVF3Dj%2BLeetdG0HPvf9W5JfrPTXIKDlPvTilW2XSvBl1Axxb9vHoHSs%2F25Xr45PgSyzn49X0Ho7SyBijcsfZuLLLp9lcyAhf9vjMxv7fObGSV%2B90S74D1khdjoOGaQvAqMbCSan4RjihhYxSbsy2YaP9p%2F8rpqQjb2J%2BpyRcPwWgqxTLxMu6KroXQQvPjiZBB3cWN1VdY0Nfz7FSG4pBJfbcJqx7MZwAbXRWf43JgFZzys0y93Az52gQrphA4ezcLUez1KT3n0JTsK2ABkvjGtOMbgXWKZ2jJ6Pd1Tmye5q9kuOGXHvBeUHnXZ4h8F8r2H1tY6XqfrjUBzjm012trcc1sz9oD67Od84%2BveLokMGYFf54X0WOGq9leV8GWBust3xJ9Y5BRIsirauhGYssXes2p3RJfwYNXNHYkLOPnlPrs4NcKHkNdyrkO23x30ScX4zd2TTA6%2F6F%2BWqgpOhlzgVKnf6Cra92TRH1gyCjeEAR5f6qV6Os0KkIOdJthprxB578S4mb%2F1UR3lKaFvEOsOdmgw99yOyQY6pgFhkT93arK7JfD3SFVlsvrO3huXbuXNyJ827jDnS2a%2FeAfZiIGAaZrPxhUu8RuPbB92PaERRkIR3a8fdy%2FYuH5fSl3EfwpO3NQaoYlDUJsE2LEFz%2BF3s2anYqvpZMeGlrf5f1HQdOISaJCvDOcjkVD6Lx9MZ%2FeqbTgjlsFBtpYV4TrATCisF4AmMcnUh1q7fmfJ0gUA75uOgMEMXossPM7Ob3S%2B0awD&X-Amz-Signature=56a0dfc7e1018aef98bb8ebddd3e2d088bd83914bd9dad2b38e24b1f2f0b3507&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
