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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666Q54QOYU%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T025847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCmQS9LrAvzqjluIAMYtLpFtxfZwajpSS9NWhjEP1gPYwIgFBFC7S0Y02w9NcCFTWAz1uxCrUSyd0AveY19GXgUtUEq%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDHku4HweW4GSVsYiBSrcA%2BHd%2FS4UlLx9GJ5FOx%2B6SkqhcSbaliMpE%2FzADCg2wzmSpJo%2F%2FLSSVAO6w8HEFCFMfnneDkovm3CgV01GoHba9fViGOr55ye%2BXXR6kT8BBhD2YPKG5%2FDAkDKVKFhnzuWkZjRJAKPoo0%2FUcNWDQJNx8%2B%2Fd3cF0ILo9wh%2BD4taQ8PX8onVlUjTfRgCwHRJvqlRNiK%2BoW983UNDwuTxNORgWdXCgO7%2FJSHqEKJh3UgA4xD0Si6Yi6DEOUvSnAb8c%2FoBKOmqT4bNDUT52KH8xmP9pAs%2FNdf%2FDn8otQfc4o5fDfcZICPoSSYjmVuLKi0T5EdIeSH0PCvkjZgbIvgMxZKo%2B%2FUvTSNpp3PRjOs9V1F%2FcwbRhZJbgVV7SkIiBiGhBv9j5cnZUQzipT0wamSy1DwQNUwUZRynXpbF553LeXTGS6%2FU4X8hz7bfbYnxuNG%2FB4Jqo%2Fwnz19VDBRse1akzo9EkQO5ByG1H6p3SjSrdS2vUq653DE3FWZj1qSJEw0yvaMglFtnrT9OCfkqcwQP%2BjmlqOUd%2BweXW2vY2PvrlZqiqAds%2BfVC3dZ3%2FK1OL2O1Ra93INqqrLWALrMJ%2FtPvFcrfdTIegSezPdeF%2BKpMSVQ9WEzLMOQsK5OdXqetDq4eaMMXl8coGOqUBOp5UIdbZSV6RDGh4w2hv1UAwnE8XUujsrM%2FezpTNBIHIlxjKrZJ6F0oc3M%2BgJcdNzS4P%2FykI1SLB5KI7XJVj6WerpxubkozdtGFs6%2B66Kera74wq8B%2F1hxXnXJXLwiuucDzVOzMPpeSox24jTXYZtHnEl6%2BUbUQDV%2FPF0kHpdhc4S%2FrO2FE2mFfsPCCrbp4Wpzic5LZB3ZeZySk0fKV4DdUUhe3W&X-Amz-Signature=c69711be197a9bb90659ebe62cb8de1ce35e0900c8db5f0f3ef3dda5194e4cd7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
