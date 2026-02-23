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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QUNSSVO%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034202Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJIMEYCIQDFGv%2F2fXF3IbbJrFixtXvM4JxFHk0e4H9SuNjjX8A05wIhANUL1B1HiloZiUMjHtwbsZqRol%2FDcEXSZwpILVhh2HdpKogECNX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzcJuPm9Zyq8XK4SP0q3ANSvAZHJwz3KbhRoiqhLfclEK7ZVUft2P8rYBUXXCnd5UumSodMZFHsDN5f2C5MZ3dkCuRs5C8Za1FR6i1V2ckXjT%2BqRwDuLrim7xbrchPWWspO81TXQn78jXop601HklpcFFdkyKsSwjvjhLug1NHWiAiF%2BV8XKse%2FC0sJXpzCHS5NqY1lPYr75B8mO9CJIHd4MX6jQqSKrzW2cMSXcchKSfR1wz%2BtOc8AskVt0Ka%2BpsrE%2FSolC%2FNB0%2FbTS6yz%2BrbCWIQLowqjN2tbK6rmC%2BW843z74osZoLCoKBs6JAb9yxNxmBHaEGnqRQDeL6V%2FAjpnST6lCkopikO4gy6HZoXFM7zXCKQSj47n7Xnb9pUptwNWu77xjxQV4U6TKL6xuT1MIdMD1KH%2FbJZf4vk6CqVnQaNjzR4gkCgej6AeW3BPFUbQwWfEOUs4AD3uoMvQfCjohJQAqW%2BScj4D%2F5md5PiWdF4EWRhu%2BLJ6DIoyiHsSAwDmDoVzIGSinMEjcUkY5bLzmHHo9cas7f0MsguqZs%2B4zk8nmT3DknnuLGM13Css%2BbRFXas4GiVsx7%2FBddSnDnT4AZ7GJcDCWd2ja3fc3a9V1ls6d4qTCMQOwypY%2FJErykMCYLzNBVpULv0JHDCnlO%2FMBjqkAYGI6Yi7xOdA9OLJV3p5rXGcPbQhk4yAajF1bqRcOf4C%2FMMyWgVGYSutSUYCQwa6Rq1MpjqvsBX%2FhRp3IemHmnn8Pcmefn7M1iASHocre%2FUbTs%2Ft2nvWWSmsWx4TQFukYv6opxD1RIEdSrDCPsJ%2BV1TTCvOnOsv50NvjTSHvnIMtltvCU8XKA93kOmlM%2BqTJqIsJYuOIDIepMCAzvFO8RE0nkNyk&X-Amz-Signature=84d84b2c28fd636779c94b259722ef562eb9c3a752161d1523d4f85b48970fc8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
