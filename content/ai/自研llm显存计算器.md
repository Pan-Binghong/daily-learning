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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SAPN623Y%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQDnMArj090kWzOnRM%2BUj9HynfDzVDs%2FGZLz5D9W6%2BIhZwIhALgDi%2BW6DHavzdgea1%2F2gl6ZvKfCxNeHCdPOOMJWeUEVKogECOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwGYk8Kseqr2jW3Tykq3ANO4ZN%2BpXnj%2Fgkujwh0dMihcqvKZDj7wbtnYpzM1lJ9PUnXqt6c5U1O0wSN58hvVtmMTAyR2534426UTMt9qzkSwktDP%2FF6jBXC8ZhxJjFBxywvgcB8kHkbINBRYZy6HXJVrDfUeJA%2FmcVvxTMDmG2PThv6Qvo293uns2TOjYVsG1leICA8zD3mLqNJfXciNBz6QvrnRZvVzUoUV5WXGc3az%2F8XX%2FeA0Hk2YjE1ejeMmlQhzP6i%2F7L1ZlgXEilMwup5itprr%2BPVRk0rZ%2F8OGruyaBz8f8e0F5jkYESNh6MRAEX0X8f%2B6JBHXu7DmoZU%2BcFyK0fdfFhsg2bdvkDRTcbBVWFHgEMWTzaV1Pyrd86E3NPuC7qBxwCf5cxCt44DGTVds58N5t7dktJQh%2BkF2heCOAK7QubYpFMoYT6Qr3619DNwoJ5VnszEb8DnUTYxDPP6AO1snJI6WvHIji7pgDiIpY7oME3E6SgM4M7aAUwEKbXBLjLFMVWCd4HxMnqnOpcJok4zKWP2K8PSMc7kprAdgdV8kztuxwHFlbKQ2MSa6T4MuenZFaZHw%2F5t55YggvlkKlPlPsv%2BT4hQSZCr59gWtbW8gbPVIZNiP25L3vlEO2%2BxBj5V04VDiS3qZDCBtejJBjqkAVpPFZzswpJbmgYz3S4W1q8rK3rKB2ZoaUCHA1Of0xGOHMV8Li0Kw%2Fw%2FX6aILufRV7r5LxGZ81a17TZl0BEVEcie3ixntxRafCluCMxTH4NfeVDPu09Hm0qFtIPkIsYxATM6jGs7kDXN58muwjstRPnFcExt3V6r9VtgnqBcG8PtiEFB9OiKl33JqHqxoQuTVD7DmclIQ3ErOU%2FuAOtLnKwKEXlc&X-Amz-Signature=71cb534d613207150a2f006b1cd324d0ea93bd393e064d0efd09b3c0fa0afd35&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
