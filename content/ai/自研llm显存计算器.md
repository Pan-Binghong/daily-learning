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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIOQQTA5%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDnWtmsCPz%2BJ9qL67yB6CrBVDMkiLLJ%2BkqKv9jYwJJXKQIhAMXqqFSwK1O0m05NjOjyLgEi4utSxN0omdRkGaKvh17FKogECML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwlhKWLa3Xfh%2Be2OYgq3AOoOEoZoP0oXmogtuM%2BP6eTZvdXuU5yREY6AoEEkq%2Fn0nsFvBA88u3ortUu8RtEd7iHd7tJFg%2BK9Z%2BdMpoYjhp%2B2Iem36ae4B4eWnf6XWe%2B2AWbUbCVloLPxWC464I%2BlN%2F7eurgy1yot0GNa%2FDTmm8QaJyLqjzdQ9OqTFlzgYKCzWc9cT2CLLBLshFISidoS4MnKBBs5uAgdq3CMdHfHQIX93%2Frp%2Bu6%2BlZnSJi46zyDEcRL9imI5UVXezjvsRFqDAX%2BoZs%2BdqOynt8bwFl9T75YYKAX928umT71r6a1%2F%2FJAV9%2FFNtOBI9Qrk4TQbexqg8Q1L2Cefghzp72jWBp6Eo0ZyJPxCGuXkGhhOac2VFA%2FhWBqRchvuceF0uy8QmiX1z3TVys6FCAhTRvKN6SLaVuGH5Y12N87qq8RniCTGpkec8NDWGC65m1Ek1EyM%2FiEEp385f0vFALU3Mal2RiaKEwLmw7Z4A6ohu9gWocsFknGbuvr%2Fn9LqA%2Bf5Bqna%2BLQkI5BsjH0V9xvvctUFJrKbYRXqkqrlq03MJ57ed3wmDQugUr4yxhcUBfL%2F%2FnNJ%2BDBbV45ZkaVUfxAAGzfb8ILfp%2FFUvT%2BfsQUrk6vcrS4DHYA4MSbSg%2FsRT7crkrg4zCe8dHKBjqkARU62h8t1Hf9uJYKvNJKDZ0aGxXnTQDFNOV9fTYhulc1hAJDYS0DsnOpiuhx%2FAwMcYPZ6t5MS56iVLsXIhQeWirYPnLfno02mEuKmzec4Geo%2BFHHa%2Flc%2Fnd0MV1l8UXg9Yu339cy1HKRfVHrsK8NBD2U%2FZ8CwFOWyp%2BFxGKe31WvMCx14bHco1K4kwZ4rYFSrC72yGqG4N76QIl9xRNYhxL341S%2F&X-Amz-Signature=17c864751476f8b0f3afbcfc2027338b1c5491c8cccfca64d102e8348fe8de24&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
