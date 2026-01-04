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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQHU2FO6%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T030952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIFRLRdTcKzJI4vWgYO%2Bp%2FwDSjgXbd9IiEaytAGXcWmn9AiEAkhWvesKxWjqnI5Vpb8Ntkr0%2B19sRxruGJ%2BORTDWgGhoq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDLMOThZdnAVt9kR29ircA%2FCFraqjM7rbmuJvinncKwTzwJ1IGa7180AuhgByLYhOYJma5EbidtnYW5Nqq0F%2BhFq46L1%2FEHHDT0fM7yw0buGtOsmFTqPl50Tt6zAriOy3qKXRHepvwkr4zQufQJj2yFXg7gmSDmTXpL75sL9esTts8WIFtg0stEKshK5p3xtnBAoS5xzJT6kGXmpy%2Br9KBkWDgjpDp9Gx4bYY%2B88izw6h0afv5N9qXsojOEN7VUEnoNDLPwHOP6xKV%2BiaPyGrMoUr3ZZ%2FttrgzVqWMBUrOBkDQwgnmZTUqCc%2FeqstN5XGIazuucdHe5mkxIVLxFaUeyI6AzaU3utoT%2FG8J02F6yPoPXS9Oz6rszkvVbsNTd0yrhFQA3bJRJUrqj0hxjAe4FDGa61rrh64SC4JC25fM29zZyWaP4%2BsdHDrHhK3prJKW9zJNJlZ%2FYBNJI%2FY0cuOispycYa7oy94brPfgN7bC2hLOWQi2Nj0uU%2B0keRR7r%2FWZ0Cea8WtMs9fThvS4Ls4D7TkgUj%2FvZ7XbvMrLbUK01NhPbIe%2BX13v%2FsN9nCpAhQyPnBzPKOrdTHhJpLsd%2BaytGqflmpyp%2BB9edqwLTKDJ6CfphnKV0F8FAu6oNqxcOzTU8JxA87FncJqWG3TMPaY5soGOqUB%2FemxeSdyYyGI%2FZaJieiNBUHzi6vnuD9yP6ORg4CDHDfWSveOgm2VIal%2B3PCxBwbnu9JuIo7vWw2LkbptmjuZJtrLYXIW8exAp1OV5PBT6w5CqCNbJN%2BiiL9Fr6f8vzsiTzYWk%2FnnJOB0Rc6cDPbNwdhu7T7UG9egDHUpC7%2F%2BW4uRS1hdxu6SU8TrEq5295j2Y40w%2Fy1%2BF69M1ikr2tNAJw3So2FY&X-Amz-Signature=53dff6078cee19d8934582796ff2b4ab1d1d616e8824ae2b0787707ef3241698&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
