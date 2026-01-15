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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WACYBEPC%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T025949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCICrHuqRkDyEIkPngBI4FS%2B1DO1ohYsHFY5ODkAMJB1KmAiEApbq9BzAyvIjQOtyn8CybNHG6WshCrrR5tl%2F8edzCabwq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDE1ntmbp1PoMmgrHiyrcA1B%2BJCUrXAmZjHiJ7Ac0%2F4Lk5%2FCfnPDFjzzIeKyV%2FBr2vkfc0EXNwNFhq8o9hRILNcmJzguIq9kh4Qx798yA%2BE4Ac6Z7QKr8SsKeWRbkl%2FH0fUEE5eBsTIy69ohcCCGg%2F5AH0WpBfeQ0%2FgrL9upvaQGor2eg%2F4jr4bnRTPDwLB%2FhqgGehGvVp1toBlC%2ByczQq6anusJrV%2Bk%2FfgxTHJuL93Dje7NjmWskBG9yhUSmX1qMF1h6SZRqnuBbQcrr54iMhsYTfFY0vejJqsifjgC9j5VGKyDnTPC6xPgaGC9L0oAl5%2FZsMEz4YxfNMMlUyy5TGfHT65WtZvZUj4WH476dG2wdlQv3sEKf2SdmWJFSE3bD6NhzlZSDvZntL8%2BsYmiucy18YFaVXCC2WpGXkGlnGphH%2FilOmJ2un6gx%2B80WQ13NfkMDt4DYvko1mbg%2FzBif9H7cvQfn1WOOCyTnbngbIebnW5YoDd9LCgqGsRH0gJY0hV7PtmOkwJYwr%2Fao0UPbVVpe9iJI%2FjgmNXkq8dfmd4XD5ASZ9emvyLKv%2BwmoKdI6sKE0CNUmgqf2Pd59t8gDLC41uYH2%2Fau3YP0CesFY6%2FJE6zjlh8vKTvpjLAb1lKgETgfMUwcjOVI%2FKXAsMKGcocsGOqUBrjA5fXUApkeySXKjZkUuvCTw%2Bolm7W9Fu%2FQSr6UGC5HtFHc%2B5Bb%2Fz4fURpqX141db9n7BhjYXhlkCJKZ%2FQcX7%2FtgSbLOPDkWmZ7yt0m61LO%2BMJ1kuNxXQXcckuUiyvRv5vjBca0WiQMkCs5n3%2BVen4EXyvMk6DYIheIsuuho59Xy%2BMenuh0FOg2lAQl1BKB4lkIrKsWW7eQlqSELwAIRK2o55C3f&X-Amz-Signature=4a3b3b9c0f90e18a6f89167325def3f882c7d100df52f4e1748c3eae9e6cbd8b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
