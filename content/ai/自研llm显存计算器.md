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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RD6RZ366%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025238Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIG%2F6uSv4IxbQFav4MtpYgy5t3%2BXz6bWEuq8Hnqh2VMHAAiA1Km%2FSxK%2FVycP0Jh1VLrzbFPCnvs7ITJhuWZyZRARb8SqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMj4l6MBVAN1nR5LrYKtwDDRI3s%2BKl2%2B%2BZGd1sMNwt503ve7N96aOdDn%2FrcHEiAxdVzvrQWVJaBhGvfzZUGneTP2Dmg6uWtF9vYLzDOLrFXczDzXNRanxEmT8PLkhqFhZG3yZm8WpHOjCSw57tFmJ%2FaaYMh2UwSRvcZkVdK1ykUJrwkp8Gkfp7rylmbyebf1gwQg6sqO7rc3SegDz2cWcR2XVnjdhHp%2BW7Y7XJBg4%2BI1qoGgMl5UvJt%2B%2BXlwEVc%2F5yAXAq%2BJflPqsRdrfZpQM7wBe3G%2BnKk%2Fo1Bmu4hVzTfzD8xWyGQHcjyBjWGoeb6NXV6NFGKWUsGEr37mMHiH%2FfGkWQMFzezlyRSwzRfLUbA3hP7e7aXOC9Ss2Rr%2BDbGlfMPLXMn2pW01NqJkm0rX63jTBdmfBLQen2emoVLYdXXbAuSuM%2BvRJ9zaKFwHMHJfSGWx9EM80dOqrN2t5ZllmmYswXATG9r7r%2Bpp43umSPxiLeHhu8DXfWkpJh6dqBirFR2t%2BlMksO7zsef%2FYue%2FBRwRbMSa%2Bhqwv1ZupF4zPMEmZaSAUBzj40h6qPER7tm62cQyhRoe2V2hoqhxhvEEvYglNLacBSj1CheTv1lpQoJB8mTrcY2YCEMdfp4HtDodoVTHx7%2FXOtKAbsvdow%2Fr7jyQY6pgH68XAmSLPyItMIgBTXk8%2FzF1YvNB0YwSTEmtEkDSx%2FnKec1kJhUGofOKpamQPx2E1DzVLzrVQsGDykmQxLBnfnIDuY0ZRikAsuWtll9q8lYuDg0s0GOVIZ2Ikrzn7e%2FgNW7XeibtTdBSdD3VCCOVctAhZMpQpKnlReTENVV8WuZdf36SsthFlCft1ibTM%2FMfiHcOvIPAjYpu6TyvsyAzYybpjJwGb%2F&X-Amz-Signature=ed3ef4bc0d072af949f82e6eb0f261f9dd2b07e1665f3e6730bb8dbb0be7cef2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
