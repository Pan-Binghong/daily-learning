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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VMKGKCH%2F20260312%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260312T033328Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDICB9Ot8jJhTu6tEQ62E7hb6OqNBbd%2FuBTsiEbGH%2FL5wIgBnBF65Vxo3KhHuSo4ZJfj8HYYkZt3jOfNmAv0qBHdEcq%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDKMh5PYqPvVy%2FbaZhSrcA%2FNmjG057Mnn6dOLHNX90Phy5RCdOIcoeBmJMFBz2jJp0Rm4vmre9WI%2FYgpypI9vzvveKVNGphqEe19Olr%2B03D9upZB4dK7Chhp%2BK163x0d1ijWYGSOhsEcHsk%2BNOKlgB%2FqJtFCp6m6vlwXkExvWURS3%2Fojxyf7d6oLbnoIKDztLNBfVqlhZrjddijMxo%2BI46n1KcO6lL85XxtuQbrOC69cMtpPVqHnS1kgNOghWq7e97dGEGslV7P6jn8SjWD4ZK4PAGbWBAtQPgNQS6wAiM6cI1MUAJ%2FI8pEIioPlyRg62zFA4HPVbOEcd82DdRE5t61Odsv4N%2FLWPk7%2BVZJaK8LfJbphHbv0wPGaZcRIcUH6St1%2FXyo%2FmAw0S3FyI%2BRde8H5q3OkP12GgtveUoZmVKQ4Qetzd1zm8hytazmUgWNTyTWReTh8J2dflvwlAajJ0inoK8G6cSfcqJD%2BPL6wECzzMyz0Dgr551ClgfBiEq7RNT0YiC7a25uVM9b3f4tM5CznqtOQTY11bW%2B3eC9TePhxoIF9rE3SMZyN%2BAMTJ3KyPM4ZOKQ0ILh2zIJB5Y65HGe1gTBknPZa2utL8tCO%2BV35PS3EvavzeVJv9k8iQgdclhqDrA7mxoJHluqqSMJuzyM0GOqUBDRE4MKd1yaWzkzLXgl30XsIhM9ZEp6h7s%2F4WHxd1GiEuNPgE2NgNla1KnUx3pxZn2SbPkucb0T%2BRR9DQFAdr5URunXYW2zD4vTti9lRkFEKeCmFA9yAwGQadS5AkV8ly41xAl%2Fvh90MDIsHADUY%2BItEzyz499SZ6yMbbBgNhplb2U%2FPh51VwIQDLnf56QOoNPG2H8rAXcZxWr0jVPXuvCVejlbfu&X-Amz-Signature=dc0f051f480a5f310a4b657adedf98bdba9c92ecab6caa09fccd7ca57d8b841c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
