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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FQ65HSZ%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033142Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQDI8Qve4whzveiwdHO3gHwRb3jMle3Gmk8V6PHVdugelgIgeAtEUGspGnm2mQV71YuoK6CzUU2ylYc4xY6HAxUUIhMq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDHd8IROYpRBD9I%2B%2BGSrcA3F4lhdfikYgxSMX2TDrr3ZMxWw9ctjTMHecARdn9VFB%2FP%2BO6DEGZL2TKvwcSg%2FjkKx48rf4ks3ovqzekzhsCbxCF5u6xXOufASx4XzcmCgjqiKYaca7DEIlp4ONwWJySeTQ5OfMnKa2okYeD4qrid0DtReVk38uOi1ZOJGb5LisD7ddW%2FXdo890UIQwHX9HAoskVxRpx4ts1EWoqQl%2Bb5PXfB%2BkXBG%2BIk8TehZea8%2BzjZboQI7CfZcQiz2uYyb7SOyCMh1NksQF%2B9r%2B02HjIN4XxCKdJr5a6BlimrX0dR1%2BDuPFDJ9hYWkZuVQAodArmVFlUduOE8fjlhBPSSpJSgINB3ATLvssuIsNYKVx9sq7drXRh11G8naMlmhzf4V32NmnE1n8HeZe%2FKAcNVf%2BeGczjUT7P8ZfgjO%2BuY6RWZv0cbFyT78f4M2hmOu2RjXz8jfpGIQGPNgdot%2FFCnlHqFWPXXyMjkQ0%2Fr2Oi%2FCBqbYUQ1igwNB5cDR2%2Fthvn%2BNf87JPTEw4NmXtZ9Atkw80Q1Pfl3GYglpHDOqEnchRUNgJts4tnXqVR3cOag68ESY9n6UODr9GxM4qUjMEHCs3PTKhBK32GHfrptp3bZOY35Hvi55n%2Bj8et5wOrLf%2BMJ7Cs80GOqUB8BGXPhAk%2BeZ%2BDZ3TCQf6gztlaySguDOSahuZfzMAIA9zYd76gBwRH%2F2gxmxOdQDXGxBgLRFdP3GxZLO4Ea9viDzpW%2FiWiMFeRALKSj3CHChEaGHLFWUrEaWTE1Ba1M9aGIAAugm2uHUqcZHF1gJYFn6mmfqcFO5qfTp5j149YOQ9SaYmf5f%2BUr2rheiOP%2FdqgcXSuLqbwKvLmQfJKep%2BbeTBMozQ&X-Amz-Signature=84831aa923e9d113cc96b1d0582edb5f4fc3c365925827bdea2388f9dc53f818&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
