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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRL7ZED7%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJGMEQCIBpTTJRCMx6NAN8YkpAr%2BKchV9hTb9zjfWbBRkEo6OoeAiB30TMJryINwIw0ShERe6ciGWb8a%2FK%2Fv0Jbw9QhoJU8SCr%2FAwgEEAAaDDYzNzQyMzE4MzgwNSIMMloTdTxZuuPe9qhCKtwDWdolbkhCQzsRBWQAA3XrsNqhZ%2FU0o6AwSb0JgMYtWU4YmUaKrSKfFU2i10YucL8Ydew%2FrZWCc6IgAV3U8wDDSztZZJBw3dPcni2Kjuv4e%2BAirF7rEjdd%2BG3mCSazs38pellkccgck8sd7YKOsGW3%2Fx%2BV8OopPMFYWi2vDrg1AqS%2BAFmG3idMTLNITQPSMFDcMjfuKSvGR4qkn4OMRQE5GEtlU521E%2BONISmnzcNBnIK%2FER2SAOFpIXZY6y%2FSGTeSA%2FKU8kTteKNJgIcI%2BvMuc5U4GiaP66wkFoOJYi9LHL3VDC21o61K1jQDM6fPbUz7QwQ5mhYC5oBRYagItbozxtnNNy2lAd2Qn1l%2BjgHOa6TxLekRzj21W%2BilhVe%2B3NxBoZn2Dh%2F4Fd4QJneDkQj4PgHdO7BOSCffqtov5v6WSkCqsJZk5OabwStZcxzPD0uW2GAKR%2Bw1sdtnYA42ApICg1hJ8XxGM%2Bc9vQgHzbcgCh9S1niNAW0PVYxK%2BEU46c0AosZRoUhezwLf2yWUhAkbb7LAfMSheLM4TCY2ipXEsmiRLzt1PjgTCqaDyxzts3KqgPfa%2FLbWCPEKiSOtoJnjQ7Uj5DKufudXMDWDYIPpCEY%2FD5hmmmgW9GZH53Uwgp7%2FyAY6pgEAe%2FuA2lSJTcjtjOItjnLEw8mNuw0TRheC%2FdAohMRd4Z3%2FDFIa8a1FgFOnhBwJx3VtX9vRcbe2ElqZYR8ez7Y7xD%2Blof6h0ty549eTuFlex0Er99TcmMVPZqeuJpbIs89Z7Aote3sbTu42vNmtcK5DIm0O7azR1%2FtVIQiETInWV5uq2Rk4I%2F27QIxAw9WLiQUv5d8H%2BxUnGJwUB9eVFrIVilMoTWMc&X-Amz-Signature=c7299612a11bb49638fcf76887facd60c906e022ebb57004df18f279b2b1e259&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
