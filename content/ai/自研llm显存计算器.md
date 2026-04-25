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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPOSYYGS%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T035311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDyIPWt9Qs6Fw%2FlZrX3fAvX1IDm7kQMnZgV8y4Fc69E6QIgAyo2nHonFcqn6wnzt3OfkODMr3lLisIg9JpwS%2FOBm3wqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP4PwkfYHflMA8hPsSrcA1nXvMtj9w5OFaBUlO0sQNgbeRAiRSJkeItRBLZcAv9gdvmHmPyxWDtMeyjg8UckI8OQ35NzxSuHbQbzbDuu8OlmTLTX1UGE9ZXCQGW7jzSunFELQGRHvpxFz6I7Iq1H242wsLj%2FMY281xLotNVe05Y%2F1CfkkSr5w1Oh%2FQf4XzKcvB5ju17se2RoXLraf0WOiKx%2FW1ViOGsG3hdsLCqwUPUa2ioePtpa0iHAudDEoYqgG0DhfSTDx4g5XwxuXKvCd2N4eIcTcaLJDXatPc3gPRsLLdtjdtOIrPM1Cpc4AUd4hZ3VT3qhcym%2F6ys4xDmK4v1yfnp0OwAwJXg0n%2FLT9oBWadgdke8x6QgOBMRK8ylectJw%2FZI9mahxZL4jTvqKvBIiiQZSlywAYcmCQ0ZbFwLRqOL8HHdS%2FYweZnDiDH4xkJEt9PV8aLahehxt5aA%2BxC%2B%2Fx5cNGgsfVJMZRHNZNgatfJPXwjHkELR58r6JlnXvrlysWRxpfChjoe1k69MfaH9m%2Ff5PmTFBwkXdmri1I2gGB2ILXTDzwtnolDIDrUnPD%2B88IuAo0nhC5LRPvylYv6naQYTdHhwkk%2FC3Vemq9ZPkVZ3vKGnroI5PFLfkMvO49qVLKK4mM69GtR8rMO%2FysM8GOqUBK3oQC7RW5fcCmFo7sFebS%2BZ2LdJK23bo5UtbYf53oCju6shQE48Hxlj0eZc6OqP4nQIi%2B3H6O8Lv7lM9giNXs5Sw25UwyuncL2fQBQfB9WN6ETkLJ9J4%2Bzk%2FVq6e0vIJokCb6k%2BZW2hoKex5o3d03YhM4kHTesb61jkI0n08AdXR%2BLi1b6ZNRlJy9YljtsoPppmsblOy%2BapoVpD894nVoeQfAlJi&X-Amz-Signature=8a93cde0140b8e9af57968ed8cd381b2d2fb3c435d8af8aa86d95d766b355547&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
