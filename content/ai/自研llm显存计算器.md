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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTQ55DOA%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T025942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQCxB7183ipj1f7ifW%2F3pujCb2UwfyWtIr9PUjwTua7SbAIgEVQeGXwSxSngv0xvQYdUtf7a31%2BaG0ymo3WqXwylLwcq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDLC9e%2FwZNQf8BcrPDyrcA5u%2B%2FOVZkZvLW639arvQKTuLHlRPouvN0QU0mKFuqTFXJK3Cn9YEEZiTtRSu1E9oktIOaVxi5TQ03l8PgOFWewuD2G%2Fp62eB1mZBaH5bzCqVI9m2WmfN%2BUImRcdEeElYpMtjY15IFPcSV1dh312Di8HpOTW%2FoZ%2F3mK5lhlQ8Tfcta9rAUnEo7uu5u7I4F72T6feMZGNDUXIFtXWcA5o1FwnyXfgobzMi0G4cW0YxSgcSaVahgDRoZLAIMBLsf67hzMfs2DyJ4usuKCQ4udQ4uxOoImjkcjjOIpVtOVun0AWy1XusV0ICEmNNcfq0bEjdA59wly0USQx7nbwaeAeTCCi8tEYW2elmNv954UyZu2yPnCvi%2FTstopmB%2FGodjhWfFUXfSo4hoI9yZONxCA3GXpJt%2FeY%2BcmnDuXuNEeHqhMOL%2B9Qg3cyGGUBsuTCsclDiELnVGHNKIXDj6BldytxRZ12m1P52kCN09134SipQNe6hQJ5ilxq%2Bk1pV6Nqa6QBQA%2B1u672V5BZKegFKXIp2IPzUyiW2GnXx2J04wYV0qEx4NsjqimeU5m3%2BKVlPX%2FPeo7vuT%2BUhVoEKzL9DUZH8MCyAZ92gylMy8HV8fTN3LomKFww9PqIDDJQB9elrMKba%2FMkGOqUB2%2FegqYiMfjyCWBMZXwVJSYsy3Uvi%2BuhYUj64SdNyB%2FVXwxEtGsti18Do0TBZs2FJsKzghc85hJOurkZ44He29OLwVnVaA6bh3PgAn%2FqUo%2Fh%2BQcfQ4rJoCYrP1oV1trnB9PkO%2FNG5ePPX8eT2AbiXaQf2KRnYioKuu8JfWhbKty5ZYFrm0BbVP%2F3RWcYthn0nHbQ8CkxWqAB%2Bf0qilqmRAJRNo%2FSd&X-Amz-Signature=1ef0c0325209f5469454ae89adb1578f30aeca5673bd5f5edcbff8c2ba487875&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
