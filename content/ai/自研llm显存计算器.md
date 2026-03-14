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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOLQE7RE%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T032816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAViPo5JXGDBG%2F9eGpF%2B1IKd0Cd%2B7tZr6DbuX2zxLfEfAiArliWG2TKOz%2ByH6tlakrny81d9JurcWYNn4KocTvLTeCqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2B36ZH3uxKewoy34UKtwDOR6VGVy0W4qXv7yueE4pewsqmse6nsy8O%2BfqDaiODCjDPaGHzquGGOwzP8VQ0ISYw0LzN2xW53oJqfK1elvmWIRNZ3NhChq6tknUVTZ9jse1e%2B%2FZ8clXjNpkMRwJ0fVX2lZV0fgMSz4xFTV0WL04NoZJA3PiI1qDKtEvg9daBs26C4gE%2Bb5A5xPDAyBKnh7jrNSFR3VCCmBK%2BbiAihGbnpCE6tmzjj%2BobpgYbTTIkaAHb29tApSzQEnPbwHkitmfA6pt9FtU66KsBPo%2FbvqT8h5zzs96udufJ5%2BgeQS3dac%2FL2Q%2FtDhKu7jhkKWXBQGEFdvzKkt1IG4mi8stBA3zfmk3sLCOQu6nuzevrPplh%2BAioP0Wt%2FSIW8vP5Bbee4DRQIbqNtvPOq3AW0%2B2%2F%2Ba375wFjctNTHJmVXmyGpJkFs2XlDqsSM3%2FbfPNgrDAMl6WDj%2FNzCLiU7GrpnUIT3l4%2FR25lU3pKGA5eMTddOU01SqIkexdwyx1dx56Ib8YgTnUgho6SBB5vahv3NmoeGcthM2ATXJDb%2BNgE8jZvzjRCXfKzp0ygGQM%2F1ydAvHhpUb%2BzOJws8cy9NEm6xwwU%2B9DsZCicVdak76oEZtKuK9if1N6CNy9quzOAwH49GYwkYLTzQY6pgHo0WGTf8FlYoUGen0YTNSHqtO24iGvyKAndaqbGrj9kQTywWvKt1uQSP8BtRg%2BVZ1Yd1Wm4Q3JvASPUi%2FwAU9t8oRKA%2F2CSsPnJ%2FjNOeA30FAebXdrH%2FJdN4ZdEgDydl2pNV0Lu9Xhn%2B9jVK32zpgg%2F25l8xwqITSTl7IBnC0x3kgOD1BXP92QR5hrPHxq9Nvh8DNvIr9eAHWT5LkIMjMdmYH0CAuM&X-Amz-Signature=2a6327a7db86abee699996b34474f71b279a8f26e092e84d32bfe449a8ed74fe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
