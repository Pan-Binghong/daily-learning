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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642BVT26B%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025709Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJAvWWnSEOoBWwvBlkCYJ%2B0Tfaim7E7scSZhd2WbYImQIgPIMoGocL%2F%2B5p0MZd4geSWJQT%2FGKxYR5jKaz8nGEf4KQqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC4GGF0q%2F2OF6uH0ESrcA9%2Ffn0XJL0fXkAG3U5KjU5blOVlKVuHhHsnS4GIcsGmANwnEpx5BIph%2BsVhv1zsk6Hf6Jj7BNPEJYtiQ5Yu%2BBcO4oTfT59GiRvZClO567r0XSHehCttc9qxYDIEHMw4H83XJuClis4x%2BUYk9C6I6M1lJ9qjNM7aBy2S5ktDh4xnQRnnCyMI3x6WoPhmiTGLmc7zvK3S2ggfeZq71VAOpGH%2BOI%2F8dHGmmNAl2G8A7bXncOzxSPo7Zl2yvn38QxKLR7xMknV8XrKik3VMhlTRqyd10NG4kLx5WpGhNORRGYf6Upyoyi2hiKDdCe5Z9fLaeoz2lP2TDn9aaOB4RZLRpwl5qskJbKbht4lt8teOZg1EFmL2WqGurUiISff7medY0yKYgC7HnWdvUTp0C4JHArdy5Pm0MnWBgxLVxOUPgKW2v7SggwXjXgjFRKe84oOk86Vo58c36d71StDQjzSvaHsrMYf%2Bb9D06QH3Ih44d0gsSVTd6VPZdEGlbCqOaVzvOb9ojdQeg4joRUDHmPQ7lqtwk42wjPz2yYYljw8gaD083OOWEfa1uvbKzDsG67kmOfiKudv4jrDvygLoLm4S5WtZOzSMz%2BI2Wdf%2Fn4fR7rAHJpI0B2GigXgmhaiVmML%2FczMoGOqUBi619ofna10RUjqjIVFbLiNmRLNodaHyxt3hkmevNl2kKidzGBlwEZ1wODoQg6cPUBnOFCbYMysf7nFCTIxJU%2FvB0tFmUtaeQrpwb5gVfzXpyos15aL8wiDRgmm9q3TCEwyFzNviMQLkVSXzQSBN0n3S%2B7954ajZi2milAIyTggsqjNM%2BeSjguQfVdbqitDdvDhPsoYfNNdgsu9fpKJ2foXr%2Bfszn&X-Amz-Signature=919744c75277ff269437f687d111d9c0eef71c2f4e4f545be87348c29601f396&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
