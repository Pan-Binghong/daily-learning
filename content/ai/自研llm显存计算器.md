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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RWZ3KAZA%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042426Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFThSGIPE7cWtE6aHyeSbuRKIGmUOtuBT4DM2Ztg%2B%2FiHAiBM9aWSQB0EAnp%2Bd%2ByvtdVEfolwaLKTBEnvx3IZ%2FknDmiqIBAil%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRsulzTZjY%2ByhLBCnKtwDyqAv%2FMd5nFDIalAUK6j%2BZkBmiO0rEKZmDKQDoCSlWoSA1pibxTYgEf%2FzIYWJcmaK9yKzAlA9gWD%2FxDvUieRig4IL00QeLiswTXXfRfdjA38jw3vUDxlMJpr2gVR%2F5fdOBfTfL5oDzkF45fP1RW%2BsozWUH1e2avVVfB6Qcqd0wtQ3%2Bz6E8bLo6RopA%2FoUcjfYUAL0%2FvZ0dyQQeYmi%2F5E8yWzjJhvB841zHBSvOmOyw9JKgBgAkX%2Bj144V4ToEfxE8E6c6RPFcE%2BTYm5yPoX%2FEWCynEroAgGg%2BzwnoWMnbCJoX4Co29X6t56a4RzIO9T2ucXMFzki0MGJmU4ZN0uSblC5rvkjEBCBZjBTHx%2BxDgesLQwID%2BouqjPYIfxIAs4DpawOB3u4wD6bYvfO%2FxI9OclhOZ0gFiCO4%2F6Mr6Rslnuy8fin0eQUADucR8NHtcxx9H38ociwiOQ%2F0%2FnJmQHiJ41C250KTGtlcpeBfSiiAzAkZ5u8InvhvoZvk%2FjvAJ374A37b8MXIZESSM3lZ1fxYqFIKfr1BP8F5TmWTvUwx0N%2FfC%2F7eHVwSmn4hz4lP82jsg31TtFioSddZCKX7NPCYmDOchjToII18RLkrGARB2HmsKrGuIqVEuRreFWkw3pG2zwY6pgGEbva5366ACyGTEx5Lbf7lNItg2xJdg6Mq4fmQbxJHaqJ5NO7Nc0zwT7SpAVUk4GDXsuiaxmHPSIFtHp2qiC8hzSm4Y7zfDztPSfFZfu37yfP8g9NpJFwsjA%2FzqXXSFM4qwYEF3tn0rXfgosWyAiuvOpVpDJgN56awKotTBki18%2Fv%2FVy8V%2FerbBivOwKTF0d25o0O52gF8heXnzexJSW5S4kZwlqLm&X-Amz-Signature=73c0033e5cb969caff239e09fc5d46a3980995f6db8d8152b7ab45b224da7f34&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
