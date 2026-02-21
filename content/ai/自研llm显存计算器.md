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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YE4R3FMX%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHAbG7U5lj9pFg7o%2BlsNClT6QNeNcD%2BN%2BKsW%2BYjNnpKUAiEAh2AHIq%2BxcZmqk2ybzXKQ9yvn6UJXrX0uS4wxYtxh%2BKkqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMNbQ9JY9NAgE1OzkCrcAy%2BfkuedRpgyrFVsxVxA2LPtrp1h42CCJFfeY%2BSGlir8KmMhY%2B7x6%2Bm8GaprAJeDgoTeGzO3qRJLcujLxT5%2FjR0RPKAL9NHYNYtxudA3NKWwE4H2Gte4JPt3wR86WXpcxLvdIuprM0dRLR6AOUg9NzDGCI8MmxTu4y73BV1wL6HHfh6MuE9QSwtjdxRkhF4WfV7ZpKv8oY1kQtwhCDGTcGBmcKl%2B%2Ff6mB9IzgfySMkbNE5YDcLzIEqn77UfdjCJogYxkf24O6%2BU5UEj1s%2FPU82EqqzhGbLnNMMcp9Vk2HPZ4kcUqz9v9lhNpG91LbrPSZ1NZpEhUvKO6GKcKpaDmDZ%2B4e65epg2jKQ6TyqxE9e%2FRjEcmYP1P%2BVn7Isias1AjZHpfj3Lw%2F6q8I832YZPsCZaD141rCuOqKK0nMSo0LKnBis9d8jzuYtnV5JvVMRHnxfbyiyObLtbNPf4VwY2SCGX1R6Ev%2FCYbKOinNxobQvDcYp8X3s9u8PVA21Azy5Lgn6K7wt8TlV20cnErS29xURtbHZaQMk%2BtG4qXVtjREhZUQvRdWYGvJxG1B%2BEIHccuyecp%2BTvWD%2Fujq%2FeD7pU7jpzX%2FNPy%2Fsg9bewvMpyDgsXIt6ezD3gUJ5%2F63UhNMLe85MwGOqUBcvohSOLf2tfV8eAQkaqd1o%2FOXwhqrJ3YcA3r3zq7as1CVwNznkNtv1X0fkneehbFGpBe5cGEo8TMmvbedat1NDtTAk4yTokMTSkQlX0QF3GhBFhbwcxCd%2Bb6LQ1ELFvIR%2FPYlLmfuc1qZyfwabsJA8S6ANwHejM5%2Bn8ChTtGk25T01H%2FhnvxXpwi5mKb6BDaE9WxjjFI1L1M6akE1TagtXN5PG9K&X-Amz-Signature=94e1e3b552fdac97942ef1e343456e1267b8408059bd3dd1ce556b9e6a8fd0a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
