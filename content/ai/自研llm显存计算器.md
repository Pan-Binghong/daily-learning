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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TR6MRBWK%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAEzLaG0Xs6zYtl3GMBbPTO8HT2JmBal0L2x1IhVH%2BjqAiEA53I5oxrmW0JodbmxJKIZ1e03LrZ41%2B5MQYgk%2B29LBHwq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDECGkJbMxwdEynGE9yrcA9eaUvtIIckbqGFf43AUSTuJl3cuES7%2FHSCJyNcx5svhSPEwiQLi2GdP4%2F0atDfRhXmzCr2NKk5HBgCR7KZRvmC7ZlE465w5oo0RRLGVDIhm1VEgVwjdjDOUBIJOeXJsBe7F%2FIECcp%2BCNNDBoimg73e6%2BDDdPIU%2F3i%2BxsUEz1UNM3VRvgnzAXCTlA%2FWCCqH7zr7zOOw6ofKE8FVxDk86h4v7aTlv%2BGczg%2FowpW3t4O7N%2BoD0MgJw9vkPFo4Eo%2FOZA9QzfZLvOtWVnaiREAq1Q6RyyxaL%2FWyHUlOvrv74WK%2Fu1swkYJrYn4aIKmZBWuYAWis40nDf1bG0%2BD6ZLlajScdBn7FtL%2FiWhrnpdMTYT7MMwFv%2BXKqOTiZybXJkuerSxUHDB5rfcYS2I6ujAuA%2BwLHqFVsfifX5HR6Fq6%2ByZEgQshBTakWETBQ84qrPRqfxYPkxFJMJ3AWJEwXIJjUN7eLZ4Nswc8wCgcCIZEU60FBW6pBQUax5iUG0cvd%2BtqF7gP7G6g8KhA3%2B2h6AAgwSRWG%2FRBKs8TdE5cmQS9pIaz%2FkHAOWDvKmKXR5WyddjIv246wKQcvFHIcTWAnUC%2Fa044NYu9fzxgtcTYomu8NzXKIH2fvQqpIVT0j9eLDVMNyYps8GOqUBosRVKY7Fm9qhXYcA8JbLDwGwwZNbsjPI7wQ69GNkNa5OJDv1K4d4oWpgRDqoVj6eCk96O2zTD%2B9tEZ4uEfs4dtVQHPJ0rR6cAm%2FfdpncvwdVlgQlAnDDR%2FH5Fou8vuTBY%2BufUq4nvSTwxxfdoh1o1a9ymbV3f0VN0FNU0ygaV4RmGfU54utDls5F0PPBSzmsOJoV4DBm6oTHGbDjZ%2FHh9K6mURIQ&X-Amz-Signature=bce35a30450bb13bfaa941c429e9c0abc0c2f66530833e723b7477f5af5d159b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
