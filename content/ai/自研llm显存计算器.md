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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QLPTHDA%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBoxYCnR%2B5hzMfK0RkxFNeh353w%2BixsleeSDhbrHMUBbAiEA7V19pWVfrbVp4Bz5LT7prourhldIlMTFcUxQ0B%2F8MVsqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH0t0DIj%2FRZ364AkDCrcA0kJZxCOKcHWJzpo2SaumT%2B%2FuxznRVGhCxOWRU2aa4nNsJONEt1%2FXlQ0zWD361diaDQcTFmN%2BFbE%2BfFYcoKll3SjhzI5ZRdt%2BdNoq8WlAqjLPORGFTjjEH8luIZU8W81rw5qsxBJQqrttONouL9HxhN5zrODFgQcOSt5SQRhTTjtD6L9ZU9bBlG6khDABZV0swXq4CJzfwRfF1%2F1YBnpJKsEEKoby4LmrnTgC%2Fc4Ip9QhfddVgy%2FWRMCXJ8R1rWhTsX2F80uWnwSy%2FmW0x2%2BtKvnAWRjWgx7JdeHot6tFiZuN0sdlTbKkidK4HtP9C1cXAfBnkKcN9526WluWwYDIv67JxAjKJufImbz6VwaAxP7XTEWi%2BB3BGbw%2BFPzV8OMRFydIi72OujEajr2Md2xFVaAGVuaLKbDYMeNd%2BVdAlAPPjrNzMR39F4hXx%2BzcV2Df7qq%2BJg%2Fe%2F%2FCuqsZjtz4B99PWlL6EAmRqMSDRgWMlZyvfj3lG36%2FphRMO3S43AElsz%2BvMy7TfuE2otFuxHoy4haW0kVHooyDcL4PWPNbzvLkpxiIaJltMkZzY%2F3NTZoIjJwVla5d6n8SEUR0%2F%2FQHB2koh3om%2Fbex42ZkD0AAEFyOUUJcNY4HKv%2BvK%2FBxML2ex84GOqUB6tFYWdcYT%2F%2BOGFF%2BALhBgh14hgHtQ%2Bs%2FoKYcr8N4wv0lK7BqWCCVA14ozcTq4kRMPs8C1Pa4rAlPOQntqDxAZaBBQYd2XpgYlbn4IzPavXYsxZXf5W8%2BHrW8e0RGhat2qy52CNPWDa1DzrkxRB7Jd5d%2Bl6HJlAmYdIXJqfSmtktzilzOy74W%2B8KU30EzQFlcDFi8G6eJSk%2FXh9AvFw1J5iJ%2BSmHT&X-Amz-Signature=cecdee47948c76d302abb41179d730d7bbb3c602a59af3db2f3fe0a1ccb529fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
