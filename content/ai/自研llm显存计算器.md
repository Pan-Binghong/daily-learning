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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UYFCZPC%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQC4SVzJVG%2B4QdofUieozBAUDZolrcveRegMNX0RZ31RuAIhANuCFyGUaqQuV46%2FmAEhz34YtyKRqlzp3oK1KdI20iIAKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxQIOdHOR%2BbbckmDN8q3AOCDaj010P7n4EwGcZ9Te22Cr25kvs6KYIIfu7hf3wAKilzso%2BatoqBeJZh4yzJLv0dIN6yDGcYIQq%2FNVahrkhk4FAXioE4%2FRwWCrSfppQ3SAwxaO1EdrZYCmT8t407pWwst%2FASqJ5JLl9atWLKvlqw9Xl%2B7UExJueC%2FtZlOssiXsZ7Ablh0%2F4J%2BLbwxW2qEpaQybAiN27mvwmqUwBUmtTeec7IGCo9gHXapw9hQ%2BW265r22sXzlXBZFfu1VELRfQ8GIXsWm%2F1h%2FWH7GLWrHyzKtEzpn65RyZ5Hv6NZeYKWrw%2BvgFC%2FxLcsKgRJQIrv3wmCIdCL8EnxiyIWDkXHaGn8%2F5DlPqM216ZGs%2B%2FTcPOBwlh1%2BPBfJ0Nv8yC7roe9StV1j3cq7nSYOsj9dzF%2F57PPKmSfOHKPgjhQRyDWHMMO53gU%2BZgWzGp6M4LZBLn3GDpHc5J21vqPyz3Fa%2FDPNeIMmd0s8RgFzs0CY%2B1Mc05htm%2Bl5Exe0sz0fCBym8ELuGVX0nzuszWScR6c9Tw94%2BSyXSH9svDQCjvJyOhJQijjUNCybqCIy9Xv89xUbdEmOc7Ekuts0v3YLEVqP1kQZEU7xaZCEtNKb86XIUOCpw3sdrVwdW5y547ppMhy8jDnuobPBjqkASqa8TsYy8yqGkXp0pkz%2BdeXfGF8Hk%2BgQLj%2BxeksVW9avySBxcCJVaSL3lijfWY5Ayv7Ns%2BeRPmVs2dcB3wVRLb%2B4N0g5FXU3OEgOKPi%2B1mh2JdkSpzAgKeKqOEKJxLZYP%2FncIqrWulMj2quj2gWirCvCnZRnaLqRtRaC2VXjbPVZ66Sph1krtbytLYkkeQ2FQjeiCRt24oS2yHfWirLDrISidS%2F&X-Amz-Signature=171f607e3eb140d552d580ae88917fd0ccdadebfdaff6f46fd6aaface76406e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
