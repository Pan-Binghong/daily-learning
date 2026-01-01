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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAFEM57Q%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T030912Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIDEbgroNJlKmg52nZxxLnHq7p0Q0Rjxq10Aojceey63dAiAR0%2BuborCAkw0lAxM8gXKhzIMRDYXd9qpQVpNqI6lKmCqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2Frg04TxbEc8aDAAeKtwDq%2FG2p%2BU9z3I5thBswdqjvUJKFok8r7DrFvQwtvYr4YQziAw1h1LjAYS96I91DTIUUs4iaf0QHf1UpVzLbf%2ByfZ%2FaqYKgXiuy604p5DW0y9kZcRIDhM4Tp6oehnumVxNG14%2FeZMeTOXXt%2FoWBxG5apdeksz8Jq0LDrM5r87t4W0%2BLb2kRIG1fmQNk9YlzKPIapkYbdLl35ODPjnzLHSMkOSqcBrCq3FZrnR5Ff1tJSIWk%2BoZyTHeFkstDg%2F9XMLRvA1q70cggLRIjjBky11iL900GspqzgqfCecN1k%2BdfxRwOEhyx6pDC7IN1OPy9fJyeo0pWdGcNMw08BCigJMwfp1ZIB4AfYklm%2F1FOSPP%2FNJHEIvalK6oIgVlxpqkKIH8vtumRROhIPO2uySIdoezS7HarvZn4%2FuAW8n4NH9eCBh9uF7%2Bn3qhNQwUSKpE2nYervKdI5%2Fm2hlj8zLkWZwkiFlWwhiyc9lQrFwLOQpR6s68fa9RhRtAnHWwNfLIKZaC1YfSDZo%2Fu%2BsqoPVUwJdaJ6mI25H5uYyU6MB21XeiPqQ%2BhN99bxAmux2dp3Bqf9yWQxmn%2BpRnt1oz4xKHzUxE9aJ1E%2BWXBMq08sZxqjmejX1ybCUfd36ECBZWKxzowtqLXygY6pgEQCcm4S2a8urJ%2B4WQ%2F%2FqM25Rva89HO3OuhIVdBFS%2FBzrfbRidI3qb8Zr0PZvnBh82HXMP8X3oo5mOAWk3mgRh4oaeKysV2UsR%2FP%2BSxN5vHikN7NNc5%2FYhcfT%2F0FLBHDmFqoNe7wqssorY8Mk87528errsbA1IryQn9deYsh%2Bj17piH55mn7naB6pL%2BGRYtY0%2BB%2FRaQZiKwNgJegNdIUYGgfjVMN4J7&X-Amz-Signature=8876f568450bb520f29cf75dcfa091e9947f0135117a4f49310b4e5a8f450081&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
