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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664D7HL2FP%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDcgR4vAYc69AqWKJUPBPg2gHAYslF%2B8InHsgDgn2M1lAIgE4gwcqk4uMQRM9AyahG03pB5zjRcI8fiBJ3Gq3bzoNgq%2FwMIWxAAGgw2Mzc0MjMxODM4MDUiDA78YYT2XXz2GuHMgSrcA4n4Cq3qQ8i%2BDspFtmH4lEsBQWJVJORqk8DV7kwfZY6zy%2B9kg%2FRgMvXUEmqr30w4qO0HYJQX5SUuS3q8CzDWRR6wHKCFs5OVwwg2hGgiP8yF6Gb8Xak1L1z0bEXoFucO%2FtR8Q%2FB5qfCzWq%2Bacza3s1aaXiHfcXBJNZOZFpTCW23%2BO0iYFsy%2Bwgr%2B6gdgXDsmPtR%2FUVsdgUObTpc6Iz%2BNTNwgonB9Btd8w59Xq0y5NcrxeUjKsPmXDW3QG5TZG3M%2BghoQcfKbN73nxXFRjrV7CjwfFMJI3N4laPdz%2BsnBXfCYiCyAhvitFI0rkVWjb6xPuQ%2Bds7FNye9jCnOmLIt1p%2BeZF4OIoKF1VC9duF9U%2B5xz%2BnHwzedo%2F0kn%2BnFWEjh6pRHrpckgfx4cGRQif1qMOgQ6kWdUPIh5qvPEH1YqXUNsTZYfHZ3JbbrmAsoNVrl6Lj3u72%2B26li3QghpTJbcxqHPHjK4nwEgR96fEZnRe4BusXnQMUYC8UfvcoSKWEZx4HnzY%2BAXE%2FIkJo5Hb0hdx0lNB6els5R%2FPozSkNiBqEVOfG5yLuvP%2FKtY9tEsb8SQY%2FphenEGMbbJO4tEqsQLGHfJfZbt178%2FKAfvVHdHIa2LbSY2Hd8EjrDv5X9gMNiK2sgGOqUB1ZI5%2F36qipoAcblcKStt0EZCKt%2B7ipx7b%2FeG5tSfgEIILzmelC7FjEta%2FFwwEkJauUYbde1WRoWjvUBxvzhaQo63oEU2b4QQORb8GtpqdlL9YLGgzqHB82%2FVtQHj0qY%2FtYxEoBZ%2BZMGA5EJEnfhUcltoxCOY4Kd4ccrHl%2F3zB927%2Bo571bbG8G6UDUs5Mwj1EDf3AuhCGCXVszFEVc9aicTI29Am&X-Amz-Signature=fa5d3871724edcc560a9b0354ad50201f86975c9e39729596c5ab29fc2108b09&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
