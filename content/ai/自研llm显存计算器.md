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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBAM7GUG%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T034916Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCateqeMo2zuztI2emz196Bd%2BEDPEtrD6Gls%2FRB4fGKoQIgcbantUlUUkf54gwvboB9EfEh45Z594RiveCrLTzgyBMqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGrRhekqswETWQiU9yrcA4JJWkhPZnOcZdR4f7q3r7F54vxZIGVamr7I4kchapKIc0yBdxFw7%2F15qo%2BO%2BLIeFk%2BS68oM8FrYvxBrZqa9TQXPha2MhM%2FQUJLuAVIaFxLjeZTx2WNjrgaqVEFFJFkH3jQJS1sqTGfeFRb70AKXPGjJjUrg4G%2BoSgwy88ZewynGVo44%2BdKLWOmNMAm4IAsvNfnynAwZH1JoKiIla5POY2SLcl1uEqGi%2B6eRHHMm3tQljftOnBR5y7Q9mohIGEONgtggVCroPltvMbgWE6katL9EjGE9Yfd47tPOFCRxbiDseiRk1UMAA35Kp%2BPGatkPvb20T5CkuR8kbjh%2BcRMC18YX38pVLHIDRR9wwQ5VZQ5KUrvrKlR8LJ8wYWDJwIoAaXu0uGnDVEMMJCQSdnUM5sL3jYAA0KDVCUuMeJoUBpS83vPOf72uyf5uFIXXxvgKP9cp5MpFRCLE77RgDvvTMydpVd5uzG3K2cT16TEOBxxUExt01I4CnOhp8xl5ubOSJCNx7aPbEM9ImycxF%2Fm7%2FMGT8Z7MZvvxR7S3HKHlNGL4AkCAIt7ehPDzKSACyvKCI6zjLpBcSgRs3SB9s2GScdBFoFXGcH%2Fpxm64D4dNYK0YUn1KDkYDDWiXKCEeMMHKks4GOqUBN8SBZAh3k27EMALuNEadgu2jPolhKTMafHYyHO0%2FTYYPHIETfjrfrfmb9owxeX%2BDOU5Z9RvvQRYgFuhwr9gYrNtjW3T1YjoFQJ5qnNi7j3%2Fe2oK3LQP2ZADwjVu2aRcWLL6czvB%2BygTi2VnzxY1IFh6dbm6jEBj7%2FQ5nxwlhqliknA8Vq3%2B%2FGRi%2B5uRwER67UfO7bNzwY%2F8UUX1ZQ3OoeMNeTkkD&X-Amz-Signature=c6cc3cd1bcf81202fc1337e7a30cd535c10b655b6f21184e42ac6234558132ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
