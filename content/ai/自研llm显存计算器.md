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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXJHQOPJ%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIDdxHD1KoCPdeuBPIs8t1DZu7MK%2F%2FNEG3XEVjF3uJSjLAiEA%2FyYiKsRCXl%2BdMZ0L4UuqQPxSphPquGq1pCz%2BI2%2Bcyg4q%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDGos5NNa02PTMwxF%2FyrcA6Ndn%2BKm07b3KhuFmuKMQyA8V9NUGzlIeVQs%2Fu20n62SsqCVOFUn8lJmrqlQJIZyVa4%2ByGmaJcufstOFvbuArzINZQcyhVfh3fEncTnn7UyO7c8LRZzIy6CfOfpJHFnHIai2UiE6U6eFiF0sop4ZoZ%2FvAT4oo175JXdSPX2c1WKj5lpRQVQ6jMDlIgfxFIAdvB852iKQSl%2FgxZgcGwbmNHSheZISV2EN%2Bh3iRfZ%2FaasFRMihPewq%2Bc7bv3c9ydv2hVRMjULR%2BA4fOLR%2BH%2FklncVR4ZMsqRXhsJwUQ7IXmCJrxRSVbRDPBJq%2BivtzxhVEVdVHF9pEc9X40uTmxrZy6e1WsvZHT4DwRwIA6tJ2jHEyidN52KzoURo0IypUd0cg85cphY3HrdYzfs577UHbtjo6hJYI63q8JN3%2BIxOQteH4HRLZ8%2BmGKHuUrlc6gzrlDvnVvF%2BnFCbAj6CgiT63cVZsdkVipxLl1z7hQ4lTMcKeivM8U82t7m9jihSs5bIcDkt2Xanfcfke2DWSG9KYTaFilcuKvMnNyhr%2F3FpjIQedImkQ0YCpXX4lSUhvZwrTQSgwMcbjEt2mlQgfJhPtNHN1NkseA5zGxAJ4FD153xe5UuZrZFtrjIviREqSMIqbzM8GOqUBLUkG8g%2FyXtPv9BU1FJKvsPtQNNi3ScBC%2BZd8W0OazfZ9hg6jI5NAwqte4R54Kv31OoAuRN8hvwFAz%2FCpxV4iQJPWNuYkS0T9rRacABJeGOENq2RkgwKQS7MYHkzYjXtitzlxMct57mW1Hw%2FauV82YRtw0kcTq1jRGPWLt0HermBTBreECddqC%2F6Y6DRPAF5VyU%2B4cxbd6RgIucP6cUq%2BCHLrhGkH&X-Amz-Signature=bdbf00e42c5b8fb4ea344eac54de58bd9cc4933649ea20ad342581ed9be1e6bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
