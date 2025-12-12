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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4W3UDCT%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIHFaEm8gsTrOFf0S%2BQwVqkyT9d66SkkoExs6WjxaGhwFAiA5GfIW8CuKYZ0ZzsdcFQaWJr2fXfFjCtZjb3iB5%2BPe8iqIBAj6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVIQIb17opQ3eLYoyKtwD4b02giMSJ1QjKFSiVdXF9KUC2uPlfVUpPDrJjsTI614G8aVZtEOb6GdKfD6WOX8Djv8pQunHPZbUykv8I03O0zt0p0Yq2NkwpWNKO%2FBN3qgI0loQUND5oExyDAcQd%2Bsmo1RuekBRyBxNaHhd4SdrbS34IyQiUKFsC%2BscQuR8ekP9aGnFIbf5qPXExu00IArKG4GLHNSdZP2eWnALSQBbFRwLmdiR8SVon9YkPSn5Tz0Md4AxcTe23ilEN1Fp6JubFZhf%2Fd7pIFaxwNvFGy82YjIRKxfEA9fYtiSbwENqwMD0frdfocHh%2FGCCFRZirwzsdE91dzjWp67qc2sLLG%2BSDHMRUH%2FTduPpgYvDaNJkfRPo5%2F2YoxmbXrD%2F7cCQPRIA4MekS0ycNxVWvg3KkJ0M%2BWzUIYDsf%2Botp6XhjoB4k5OGovcvcqZi0fRvdyjykqcvi%2FGL5ZVfNZXG9mWAzQ%2FcDSTIdP4aEKPs7KFHWDmA1tVVzYtqI%2FOksMncycD2ZZqvn9oXOVEX%2BiqUjVa3qObaPMQHxMvnvRvaPwTvLdPKo%2FunIO%2FErmFzSFDXK%2F8Y%2FHc4auPihWwh5BmmZQxg2BNPq9rux6dSbFKOMrcedNsVMeJnXlfb2J%2BRIqDaHeYwzNTtyQY6pgFXg0QXSwVH6It%2FWkMaw0x8smEi10u%2F7JkImXqQ34%2B1M9Y9gcpIVZjOjXpzVdWdN4LNHbqn%2F%2BCrcC35S1ZbAnUMOfYLCTDI0NDz171RtSDtDgGaIs%2FvOZ4u8MI9mt0t%2Bdw3NOX2sY1humGSJ%2FHronbI62%2FV%2FEK33jNxsOfKLFWqcBMlXn3BHkmHCNN6CNhKPJHn7u9Tyd%2BnzuM%2BNCsegvFeez89DCBo&X-Amz-Signature=dc258446352aff3eaeb8f3c95f366e04af70dafbb1657d8885fed2b663735e7c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
