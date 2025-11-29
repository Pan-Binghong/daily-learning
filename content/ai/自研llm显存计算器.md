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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKYMJNAD%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024158Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDWlrZsxUtBnas6LNlFzD3te1UDG3%2BQK40CfkPJvGYobgIgRkNeJSBKJhfjLu6SxwtRCnR%2B14m%2FNckMRR3cVavI6OkqiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP9E9A9W1wUQOjlTxSrcA8miv5O31t1Zz1VztRCwFNxxxIKuUrULNdkaVv%2B8jLDn7FKIdsVVTG%2BbPb1%2FTzRLJNzRIAeK8n7TkXFJrqES0cgJIM%2Bt30C7fZZgRIb2RkVSFRMC%2FaTitWddLzSJBbizvCq3Nuklh72lT%2BNOiX2qPe%2BmF940jLl3he5a%2ByeMm3XRWVg4TKyvn%2FMHvKlMAq2lOILaioDaWaFK4vjeFg5r6zu7sXmSD7ErWuATlUzjTpr5WyXKaN1y1iCdRmilVzjcCQZ3iZECp1qsolr43eS9kg6N1VqDUL5a7fVj7M74jnWvqnW8FTeImistjegD4BvKkzMjmcF7PB2Pg%2BJFitUwcEjv3m12A10IgGnBiZwGRB%2FJv1Um0aQTppn730x8SlYZ6wjXqMr%2BunfpLV7c2Tv9%2FjFxTLqM0A5U%2F30d28Bnotjpw056mcINDOX4Bit9QvClyCJTQoVCEkHNCfuFo0whnR19%2BIl4hZZdPvqhHXXIl4lj%2BbOpaD3Wqzi1ZUu5AJFuJzYZAxHNOOsiUza1%2B7Iave5yTmTRtWP676mIj2NtfVFRbzgZ3ctqvPeTyeQxlyvwh0kqwmurOkhm%2F8%2FVlmXFxwvAm5x8sX4uTUOU7mAzAV7sk6VI0KJNrXkcpeFcMKyUqckGOqUBlc74Dwex9%2FjXVa6vRGcChBwip%2FXwco8bP9%2FM3%2BaXkB5ez5i9jGrz%2FXZUw6Vi%2FSsGao%2BPhU0MWixHprb9Z7zhE0C3t1%2FJ9rVxGeM3oFPpq0l6vc%2FptIajP1HB%2Fx4Ir0z1iNg77WsCxExkYs3jyIL6latU7liejWRQTgxHuBF2MwUHA3Xh8J9QeFU%2BGUQqGRDximUrw11Jdv81Jd%2Fe%2BAdBgFu7k92u&X-Amz-Signature=0d022561f11171ad43fa25d513f5ee4499cdf969f4f9ff69b6d28eebd1919ffd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
