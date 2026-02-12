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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TY5626XJ%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIBpWZ9XoMoewvExBClVvXZx77PuwmH7Mh6lEofO19SDFAiAK3Yz21Da%2Bnx9j2bKAGsg08VHNZbbpnt9k7peImr0MZCqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCJR0HDQ%2Fo7EVZ%2BNZKtwDSbtRUO0%2B4V%2FuKnQ7AUeyY5L4FbDMtdrPt8TD%2Fs6WuVUBIFDgLqtps9Onv7phUbhXCJHch9MzytTjIHbad3INVLwidC%2FDPuRl8qWakf5d6aju9w%2BWITK6xQYn1d9m%2FfAxtAoyI%2BuKjGjd6Qg1OPSkqJXwv%2BhUobhLUW76KH9kTUMfoi05Hy%2BrijIRQlBJV066HzJ8VjOWkrO2ZnowsXnw3ABcPzGEPfqgqhAIpKcl0tAzvQbraIRutxL1O4G%2F6766LYvMeU1YJmUburrTWjn6AmOhSis3hl4NkN03JTOVpAlx0hlviFVYqemrJv0n29zFRWkBlCVZHwNjI8bOSUGKKW5slMF1aeYfISWFzHD1isM41nkb%2Fucjg%2BnK3B%2Bt1H5r1hMdV%2BRwBrbpzSpl%2F9b2%2Bso45shzirvCFHS8RbFw9Yv77Wrd2CEf6DUGlTsUNA6QGWVeCsp39RwHAg%2BkuxSB8Y4OTpbshBDweZb7sPfgkMGk355%2F4a%2FQ%2BYooXLTPMqxICb9dh4aU8TFJBzlfQyhBRUWVNhU1IOTxXZSXyh4bG3w5HZpGh38XxuXZZm%2B8I%2FlJjLxABVBUZJFP%2BfuODeG%2FSPo%2Bhd50DA3z%2FxCNN5TkrdPh6DeOYoHXzROrumUwyZK1zAY6pgEZoNcC7Ao3PcG2y7tVySTjYyb7qVKfkB8%2BLf6mf7S%2F2i58KNny4ZITccIuYrLoQ%2FJ%2Blr1qkoTofqaxrSjj%2Fm%2FWro93JBtbXb3wVmxD6IcApobkz4xyhpKIdKU4ud%2BdbUw5QlBkzsU3lmMl2%2BZ2D61rk8UCWCYxQ4nstO8Gi4wamwQzQC1zM9udDPTKsOK0ZOWxi2t%2BC0lla%2BlhTVGzbCXqgfmuZpG5&X-Amz-Signature=fa7d2735e41adb4a1abc4094bdcb52d21bbc7b433af4a0bc138f14bdf2639974&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
