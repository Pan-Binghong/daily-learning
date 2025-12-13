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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657ZZXVSO%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIQCnFTlkRtLHxto8rYs1zIaFEiEiWF7ufM%2Bz%2BlCloq1fHgIgc6ubWCOCupEHNnTLO3ckO8JoB3DhigKKiSGQwDydzegq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDNdyu1oSesW%2BYljVYyrcAzqSoKvOUutDzNws%2FiERXVQ1E%2Bnj5HWfb2YUOl1b8hqq%2FHSDlptnVo9Zxfhg05ldRgJk906DMRPRZ1FaNWWwZjBKu7b4nxOOFWJ03EAvSLrr10fUyBcyuY%2FBM6CFuZNu4wQI%2B643qDUt5Z7H5O9FkN4BMOffC%2BDoFeiwpFPypfGwLUIiMzd%2FSz2NxwyLLJ7HNzv84E0tWuhWAW8woCdhvNtGeZ66TikR23%2BG%2Ffiol%2F2TMq8rLiKfaB4K1vSS9RjAcG6jB9bNZ8nT9SC0ZqJmyMTjeQ%2B7xIxrFTB4XV8B%2B0Ft8KUrZbWmDuts88Crvpy%2BJjbo%2FskpDugLooET38zRRHOC6ZzqGcPwM4j69BYkU%2BD1TQ3ALvxVQUNtYO1HgXxD2nmAPxd%2Fwg2EYlNeFdRERx4OdKHvwTJfMW1vx6qYnpLhXKmJQpD%2FsLSMR4QB9DdDvkhcAHL2Yo3QI2UL%2F37aZk%2F1pjuJNNt4pUEZ967apYV4ThQWggHFC4V0%2FW7LlOUlaMuWqzXCl1pTnWxX7I5%2B7R62udrD%2FESVZ6%2FtBJ75%2B1Y4ioRcKBDYy3TAJ0zfSa%2FWo8umuJgU8U2t2rtiuNg%2FPabTkK7bd%2BHxjiDPm%2F0q1T2oCZTxxpYUAND4c2NdMLCM88kGOqUB9L6Ci1bvZqRZmxWen%2FBEAl2H170%2F5PKOB5G6k405EWMjKqr9pgM%2FP5V5vXcLjckUtlkcHuOCPDj%2BGIB49cBAgPmkbXWlbPXM4ZmNk7O4UTSh5VcgJhDJlV9lqYpDyT6Xvl0jT0WKkVZ2YEvg6InMTdKmetINRQJicVb9sZ0mwkpHNPMZkmTToVRLdgIM%2FyX5bchZFBuwkOs1pzM8oqwmc2PCZXLm&X-Amz-Signature=ecc48844a540e62e3cb17dcd43a11f52b1b2bee401c92e24345de978cc41e27f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
