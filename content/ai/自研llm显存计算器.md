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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624IP23B5%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJIMEYCIQCZL3qGdmjsH9W81OS44mWrrVzAL3jEAnM%2BdCCVlb1%2FfgIhAOm0MQrU3eUMv5Q%2Fl1UKz5K6BHTKCtzbxDg4fk41QjOuKv8DCCwQABoMNjM3NDIzMTgzODA1Igx6q%2F%2FacwYTi3CGYfQq3AP8yAQZUPo23OV17MGa3b3OcwQt9ldgOh26cqvrMwNXk%2Bsfj4139WQyb5XArqqE4qOZyF%2FL4QPUVSeQIdZs0qxM7TzCUlVhR8VNj3WqyVLW%2F2pukBTb5F2gl3%2BazYLF6ZKHP7VXnZ%2B5n2GRrNCIJBmXhZIK4WHKx%2FYAnc%2F%2FycLbJ1Ff1Zog47YXrEVRt6eqj6PR3uDxl14isCyHBE%2BPVyVWgCBzQPM4cIGWmuW%2BM%2B61bvLCKRXcgMXsx0qfWPkt8euJjNR5ALJnxtjz7a1NvPiLRb7%2BhZpGOI3Z012HQHOO5SoVloYBZE1JdIS2VdkHMMFyB8g4KJ1VaFL6V1K%2FnIphO%2B4ZcfVv1K2ZSgwTxdtyLIzzCIgl%2FzdRb5MvyUZLFr%2FNza87kwL%2FvaFrF1bZ4vuClYhptX1Cb%2FaRlDyQNuwhZu8RDeCfD7J29UUKSLUp%2BYt5xssEkiaidzbdqn%2FxigzBqyUGdqE1TmeGWv1aXViu5jBfQgF4Pzm%2FoRHGLFzMxg6%2FKvlCp6kJPBWUVaWoRf%2BlUzc9aBo4wBJlKErpAB6TNPGCG2StN5CJkkINSm%2B2eJd8EZMHZAa%2BMeMXLwVPv3do5qZ1L1ckBXWpB%2BfCB1zD69Rwk4ZKCOv%2BvWQK1DDh48%2FIBjqkAcOKwXj6kTxtN6xC9xItJtFA4ndcS9sG93%2FS5%2FHCLGJfJxnYmL1Uzr%2F6dOfS4dNflCETpL%2BYHkOx0X9N7E69DMhA1NrjH5IUN5H2Zqy49SUWUZJYNbaCOt3ck5sxQrnGSk0BR1ZY7rXnuBETaPzRKnjQVW3xCwD%2F1coUK8%2F0Zwf9VAUsZc39ys7u4q%2F%2FlixnOiC3qUjoimyqiGl6zVEg7rfYV7MY&X-Amz-Signature=59b65c0f4b76c4b8a889289daf5c7b2d395fb1b0a10c0d11f39358efc1ea7f9d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
