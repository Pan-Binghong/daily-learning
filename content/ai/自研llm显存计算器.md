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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UZU55UT%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033911Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJwNVa%2Bu13VRGRIUk11S5S93R3iZdv6FDAQvMwMByEkgIhAPJhS9evahrmCgr3zKRK6kYXeMJ2xCt0XRC5dF4HmlZCKv8DCHQQABoMNjM3NDIzMTgzODA1IgxUwiuNR39ie6B%2B5hMq3AO47G5H1Q1xj2ax9ZikMmXV9CkfjT4ZQeSXiCvouqgZ38FsXZgcx3pWqJYN5IdccMYHRwNcilVovT%2BffGOGyxxQNA6PsLTWJPpqnpCoTBJJHdxNpI2dGH7L%2FnT8WGv6385c0FRMRju9hHwDbHByi4VDfWDXgzMkYPq5qs5SgR%2F2DRe6tlniDEq2wfJNODITCCWjCZY3ZU4CUH8vF4anS7TePXkpf9I0yiqlyYju5Y%2F7FV%2BX1NJWOQdR6wSPymNgwV1L0hI%2BOUBKLULQaBAVDBWVfFI%2B0n1GlUraDj0ECs2BhtAo%2BHvjdg3Q5VL3E8t6pkDfNpwS7dp1gI6n83NyltvyIhJcfnrsb0YGcC%2BTJBpmDsNy6gELQcmcIFmJRiXbIFwnXdzwgkraS9sv%2BqBHrQwq9%2FHDqJZLjsdq%2BTAZpBHxTfNhCR47ocXj0HjIn9G5GQOhMSqPjr4VOYtQDjPvVbGnr9GZRnTSopC5jEe2%2B5Ttn7TApjR%2Fn297HNriZNLbXLePgHKZeQl9raOk61qrtnyiOhbnBxjpstdrGqQ4uqke3xiNNNJfiZjjtvPgyP7c6jq3qLyYognA%2B6FENzSJBU%2FP2Dc%2BrRdTLUv2W1iZRqvbA3cxzqB9lw3msN49qzCf8tnMBjqkAdcTyaCBHYd75MrKPJVtO4Izc71ckm7d%2FnWJLOblksf3kf2nwUu9bYQoktjEUbsXgVyBf5%2BfuUHSuB9eQuU8HRXKeyRYkO49PaXOthRsMKZFfom5NegmYv1ot9E9strPDkmO3hjhefIaCmkqIgkggkks7qHOAEkZTgsQOZ5kwiZim9JHS6s%2BihzkZkYHtD0iU%2BCSdEZsZk1ws%2BhJ8fXJSzWEQalz&X-Amz-Signature=1b7ab0dad0769bd134370ba1f4a11cbff0fa81c4679f12cbfe02a1c0e69d7284&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
