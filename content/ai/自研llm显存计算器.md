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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632Z2KIYN%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T040909Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJIMEYCIQCcP2p%2FJNCYmsCJWPj33%2FNu7BlBblFsZg4NzFURsHUirwIhAN1ahL7JOp%2FVGMgiSqFvlmjHhTv7EwA8T9%2BtoJ6%2BhXH6Kv8DCCQQABoMNjM3NDIzMTgzODA1Igzs2Toab%2BSmwycmQvkq3AOtXsI9H%2FKY%2FlqJrThxaPh6SQhnP12zjRFj479dCHZBkVED2DGRIFwqi9yWtb0CLJJq%2BiEm7wCeD7W%2BLlVt77uiQRZokP7bf4feqzaBRFjWS6JHBdR1CcOk0WbGCMWZkXy9ra9YRZvu4dmPa7LhhFt%2FV6j7F2DwXCIy6QdTE6kbYTzDymc2LqSJrcFHV54eVhQWrr9uc0ftWuiYvphGbRIVAhAGDWpEnpzIYNrbRXDudN25NhJgE8ta3KCFZXgCxY4MiRm1g6fEEyGkz5eVTHFG3akYK4slgT6BmQDMZJIHH9G2lqtMF6gm1cstMg27OCw8vuzYYfuuuP6ARNQkPjJiZxeVtYXoyT%2BxLVdEFrPFfzyfkHz1JiXVWXvDwyyycGzB%2BfBF9co%2BaTtDVvOgHupbOYuIHGIsXN0W%2FMI0ZDR9uR2Oag63a8sAlXlh3OV0Fuashihc%2FWw03%2FIb6LqBZENKwqa%2Bl3VQcAJ%2BDX1TLcXbBbD4aB2Dc%2BPMqE6el4VMD9DA4Ot%2FEo6mc0hSxXX1dfdHRC0oMa%2BCEyxvmXW3pRSxshsjAdasfLPSO%2Bqawo4n3MNJeX%2FldyLI7VyuIViybIP9n9qgDo8G6jNHADp6a1os1RE5R7TIySgD4Bw7dDCqxOHOBjqkATOXV40rvBcsJ9xE5Lw%2Bx8i%2BGXHsRgzmJpNcCCCqVnCpmuGIYaiG4lQQYRu4auRvvTRWmrVGQjEu%2BSJxiIpSI5VnO2HQsCZ9mMut%2BqZFKUJNYYWZzZsBQjIlFXDqZ53lzBA2bv0m4ehjNr%2FTZpdERQic6wiiWgay0vdNkO4xy56fKLGfCKlJ9DeGTLZDUHFY4CwjA26H7DWmIBHR9yqw5mqpI%2BYQ&X-Amz-Signature=7295a044104130dc2c56e2a6de3e6ec6373c1bc0247168d19bff71fa8b29d545&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
