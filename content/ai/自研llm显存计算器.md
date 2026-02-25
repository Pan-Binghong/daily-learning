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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2EVWJAM%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T033804Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIQC4nPCRudz4rQ4C2xstYf8iQ5f7YSK1qXXw1a2LvjSSOgIgcsYQVoxW0F0aBJ3idcN1WNhmLTkAxNVPcSULDm%2FETfIq%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDH2Fs%2BzJNpmW5G40jyrcAxZ5EO3%2BjJ6KCw7CZQ9PztB4SiHCDW93EMduTP42y7hlft72rbTI0HRRuf0r69HIIBG3hxZ0RyDnaKdjneb62i%2B00dvirkRDfqAXcXdHd7eYf%2BtHUX7nG%2FyPNQU34cQweZ8FmNUEZL7b%2B8IJNgdPtVYNJxNjhUaE5DSEG%2BfCSmGcOLdylMQ4jqCgFUccEtfHpfE2j8F3AOIxXXEm2ctQlpf90K2beqLbJoVT1IwFZIE7%2FaB42DbqHAOqjMnZvFW79SiAr%2FTB7XtNzT0f8FBsE9RcpPlxjFjJd%2Fvx4oByvuV3ox6gmPuIcUkwRSOohHVvG2YYPY%2FWmCU12oAFDdQzlimN%2FE0J4HNOA5pFLC%2BZ6yTG5OPVcl2FfRMQfvItfBzlgwAJB0HvVz%2F1xaUcCQxFapmuvLNjSnMFYeTq7Y3V0ZV4bjknY0JVGK25v%2BTaWY9BuB7UHcV%2FB7a5taED4hrjzHL8RvRKOHDxyYbAk0KRIPtGEda8txhvqs%2FC2R2cYgwZn%2FHrKyM9n6rFa%2BYvmNHQR8OtdinQe4KZyOL3I8KmXARtux%2BNDjv5H0TIXA%2B2VJutEFqY2zYZzlmihMPLWKKD%2Bk%2FHFBY%2BxcUFnmB6eCQg9BYUGLq4HEoUZuKqylI9MI3O%2BcwGOqUBeuJ1A%2F9oFR96R1QVSUY%2BVUCnYeK%2Bm3tHFQun0xCkBL4dDshbkuvl4ibqjDMv01LCTerAtuDF%2BkHqxAe8SPh2yhI6FtCMH9xfTQJsPvvVgg5IrEPnHp%2BXZYKks6nq70A54Ag6tQzEDOCY5WMT9J%2BITdV1siEGyF7WbP3LgoEIZxVmPv8yO7G32DrBespW4ShehDFJA83Bg2X9AE6Wa%2B7FVn%2BwuNiP&X-Amz-Signature=403134db3dc2829499a71e580fed70d74ff7437d6475ed692b70f9fd2b9ae57a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
