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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XLZ3HLY%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG3qbGTOfgtK4OTCpqrNERJBFJMkWoiUi1KOhYnj5qalAiArHG2dHAzmexPe4NYpFrfY8gRG%2Bbs9xxRQd48ok7zxoyr%2FAwhkEAAaDDYzNzQyMzE4MzgwNSIM4RgyWIrWYtj%2BtQC8KtwDBS6sqbWP5%2BqsjRgRLxaYQr72ff21YUtlTpnF%2B%2BFxS%2F6ZNGOQ%2BPOZpXVv9%2BkKm0%2Bq3JWq39FFguuH0RhhwEa7lhvijWxaOSjnxsi9mCLFakW7HxgePlFJ4DpKC15wQKN8ydNrvHx9Ikcoxwx%2FAR%2Fc35v8P1JP%2BalT4D2uDaM9mS7mLfkbctkVroP%2BDQTjzCf7TGkwjvhYimd4j03Fr4bMWAEALRVKVaYQjeemUcdG7zP6jwDiQkC2hZjoW7hTxITNhR5gLRx4hBE%2FdAwIY49FxCp%2BBJUxCVrMQaqhCCtASdzA4tmqR1jTNnibh9%2FojGz%2F82lfuD3ej1enmx03U7rG4oC3tvW8ffp%2B87t1wKRDjw0ujxooQJKi2R8Ef1NvLsfvpLnkfd6zYmtynJM3MAb2w7fawgIIhPRz%2Fzk5MSFPYPuBXvjiXIy868oTOimZ8DYte9unqc9gG85mCT4a881UQ038sMM1ni8t29fL3xrQk3fo%2BvxE%2BLcuhkaY9oEDVextZqjvxEz7f2C8yfdOc9PtE9iuQkQF3jqn%2BTCR1wWY82JHn%2FdjnmcEHm4bKEgY%2B%2FG6o4n75lZP%2FCCpRphQTB1YYep0AUPkJB68yvgHpjy1lPUIgTKAhW7%2BbRJ%2F89UwsK6UyQY6pgGfBiZYySYqxHs6Zl%2FfY4vAKm9cSJ%2BjXrIg8M%2FDNRLdUwMpnhJeHlFie39F36AJFvyh8V%2B%2BFKSJKp80pvKQevbwofdCimQuWxWw351k7DKorF%2FEULfq9wNbC%2Bpm8LBFXi0karXu3C9%2Fuxhu0ekTovRtmwNNMoaBMEILfqTTExEj%2BmHwKL831%2B%2FKu4NlDuRqTiQC8LXEGOPu%2BC9Ml9VWM6en40xDAVOH&X-Amz-Signature=5c40496fc44799b9f7c59613424b07327ae868ec3544ec856ec4e7c531bb3629&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
