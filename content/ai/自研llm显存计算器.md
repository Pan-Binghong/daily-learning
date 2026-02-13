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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SAUFWV3X%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIQDPJb8jKjDNQX1Q2vlW1FQpQ5oOjP1gInczwMslGlUz8wIgO%2FTtxUr6BKphucStwXav7OrFBGhQqS7kHsFqaEzbCz4qiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMqVw6YWvDyMxSYnjCrcA3qluPg4pfI60JQhYGw%2BrgiwNtXCnd%2BV1g7%2FBnkMFxT3KgUy6NX7nhRai8Orgu0M8yCkPne0iD0vBWVkrfUaxLH7fa%2FUHiBYjMR5fRO3yfgq5xUeOoBXcwNnLq07F8csp1emW4Z%2BT5FMXUpJdqljnJYE1SlPuYKS8KV8szu4PbY5Xp4dyvJD2uoReW1ScVjH0E5HjzG1swhK391PXkj9WdT84qYuEMskO4%2FpQdIoFytTQ0Zstpxgh7hQ3RvRtLpNI2nludJ5qokl8ZasxJ1CcloGY2P12z50kq8Sr9y8RODc0ZFZHty0mI94U23AOeyJdp0HGfsDXlginmwvxyewI6%2Fx3LqFcZyZQQd4ivD22HRZsA9ZxbNIjG9jco3F9Lfp2Uf%2BhzEzYerdo8JHKR6JMfX6CJKMuy5ppdMT4e4EYkZIpuaaBru2Oo1GRhcEolEkWzzG3G4BxlQyWcIgIcX9oJ5CXbMZc9JgmDR7pNw332PIfc%2BJ7UGB5PBNPv9NzQ1sbEBfX0jFw%2FHuXjLcjdeAy%2BQYVWF6ZMKEE6iKSN6y2WgRnNUMcDURpUmPbEoJlo1H9%2BS59kox1GuX%2Fmp0n1hzQXxFjbsjpd%2BnA9cqwXHwau1Blrg7eIGPKO2Cn5iKMKWTuswGOqUBI6KqYqufKPEOEzV2kImrP99jtbBKR5pNgIYz2QB31HjxS7riLnEvSQ%2BGNv1FLxXEtfNnhPA3KJaz92hQaC5S9NOcfLgwklBGccKLLazXXmDT%2FCOdBiK%2FynIoeX51eLsl5G9t4YZMMc9LzDnJ56FbT%2F84xwkwl9VCeSV5G9BT074wDGLFFZN0%2BycObfgAmyMl36rJpS9MH61n39k9X0whcQsfLvyd&X-Amz-Signature=b5bbdb72f452a1e7cb73262b175d712caf770080d2a876f9ea4403b4061eb400&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
