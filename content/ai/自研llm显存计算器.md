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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676MJJDCD%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIEhGkT4s2nEM2xVda61WI%2BsxEJpZs7LUM4GWHtv%2F8CbKAiBH%2BH4ZkKTaVSbmyyKGJ7mmTRAPhjzLyrG7DTMufMGtayqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAVrkQElpNmPKyA1IKtwD3ZhG65%2BRDCtvT69O3rJJ3DfsjMPfNmSPZfhaSTLItFUiIyrFHw1VYqbTXyYFP6AY3EGFKn6jQ6%2Bw9wt4A3PgMF1ts89iDIyYfKax%2FPXPuVSslNdS18nbw69w9%2BjYUflkTRJOsl8m1R3zdTgnaMT%2BySWExnFzVMpPmFaG%2BQ%2BgVEf%2BcGFjccQ2%2F9nUGSP4mdHU%2B8baDtzqNO76ecVz%2FIJH%2BFuXZm6VszB6L%2FUSz2Zg0rnGTvVqzz5VKmxjs6tKkwRhWFQghGVnuliuDx24KdcuH7Bv%2BDhcs09yRIjdOjORryTa2Uf%2FobZgm0Hn%2FvHWGg0BY%2BqJPy4aVrglFAkwmCkXBIvG%2FkoKmWAto4DhcmXz2FvrosJIHxyTwQZs9iaN1t97peGd%2FIEFyVp60S4nf6JWRK%2Bw7%2FDzdDpStQ4utC6l6MK6tamZE0V0odyWl2BQdwG0hkqShOZz%2BoDA0n10AdAm6%2BpN%2FvkxoNoUJwyc1wGcIX7jI8elvC7TJGAB1PB0nre5qFRt7iujF0ZWAzCNJzpPEqDs1rlGbuzcoM4qZHyOjeZFimeo4mV6xiJOlcH0CVQv8cZuqt2%2BxGgT7OFu1PB4eBo6Mifga5hRg8koB2NEDEQAOGotfeYberr7NSwwore%2FyAY6pgGaBVcX8cl3Nj9YoO4fQyPp2bD%2BZ%2Flq%2FwktyuIClSS9BaSu16ir0FeduRYO1TZEZ5UyVvD%2Fd0AqjB2InGcneLpJnkfBqnb2keox0mhPdW9MO6no3CYM4tcWbGOcL8sc6kbWd9Ay6BJ%2BIah8EVEWyiihjLomJq0EJeISJ10vmvzOhsskBixu0aH3WzxgEw1gpIPEaWHyfZb%2BzCwHwHdltcVNYFpzlIxC&X-Amz-Signature=b91cea9b92d9f43d405c1febbc6c6c9c19f808625786cca03d76b16671629653&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
