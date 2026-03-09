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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S745X2YK%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIFxc1U0EEHcVnrJQUzUzir%2Fl9uFr09e0BgxWNRhIap1GAiEAwy2HZtwN2Na%2FaWY%2BJ483jxNscoZmD9d9tMy0w2PRhLgq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDHmErzh1h61Slh4A0ircA35sj7C09eHwU9vZ7wiVMyM5Ju0NDVVffMEx5tiLlUrwQNCa0wzP4mKLSqgcwdB6I6ZzbkIOr52dPD2QgR3HvVSe%2B0Ly2nWFCCdFF%2FMpXhtgQ5eZ45HIiZogOzILkifFElG3iQUpQUnoh6zY9I%2B7%2BbzZCED7Kd9wUVreebyRgTsbz5yaO3Zxoobk8KcDE%2FxHBzQBh3pwdWD8Eq%2BhRCa9uWtAvVsMjkIMwwYnYlUuwSzKtzHM6QoHC8cqB0D7L%2BOUxk52Iwd252F1D5%2B5EjsiafqSiOxPM%2B22m%2B%2BAouHI039B0O3fXTyMKIhbSBphmEPW67ve87LgpN0r8aw8ixPb3GvwOcKi4ZEBFhEghz6Qrc3e4M7kPg%2FFyqeAiwU1d19R3K1L5fBsnp8acH6MThzUVLBeU6xb%2BZs8ckGMJgNvn1My4KvPI0vG6Qk%2FMJ06ZzEbP%2F4x2sA8b7rTfNuQRU%2BX22oinzLdxAsDqmfQwDGSeOv2RDAoAdqIxaATWbpDWIdulAYJkzb8O00d%2Bn8uUisMR3oxUyH9chPsXGGsbr8nLnNX3dpmZsC52s2lrMa7pj%2BjZdLTscnH%2Fhjydv40zY0adCpin2zTvYwMHMSovzEfqNOjzOe%2FZazEH1acKalxMKX%2BuM0GOqUBn21SFECU9SGWlt8qabscNKnF4tkNTXzgvrTebxJien0nw0uTNKr5xqcCBt3dIEePvgw1xedsDR4mQ2XVuzUyzd%2FptfvZpZcLYjhPcI2A%2F5MoY64%2FQlG1XLnZMbV47N2sUvxQ0lMnQTWMoWe1%2B4Osw1raJ26AUGx5mmLrBTtXLftbvbYuixA3DTVm9GfFIcpuDSZhTF4CKbS3OgKU%2Bo5O9xF4qV7K&X-Amz-Signature=c372841dffee6d30c626c13c4fe079eaa6770866ac12b74b2adb8970e9f88b52&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
