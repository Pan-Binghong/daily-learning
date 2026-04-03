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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLWM6SJV%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICAPvsr9368rKet1SZtv0jNqeSGpe7qihIg97QwDCcsHAiAkBmVot84oQYWP8G8oxXxy0wDSOtd4kA9EM907iDpTFSr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMsCZloqCGxa5kY5spKtwDp17RJ%2F1BS5Ssw2XcKBS3yXNQw2e0HtacPbswqB8BCtaSxupTVrhpp6diw%2Bw1sTL69zy%2Bqmt0hnwZOyHqHdk9FIuGrMMHCEpROckdAvg1cMjvwepto6iz6%2FfBqr4ThjiC%2Fv60%2Bo%2Fhri4VDVJbTH13Lr2aFu6mQe0gkjP3JJOnBvqQR0KNDf%2FHb%2BynKyUUOfTrfZt5xP1QpP%2BzcFIIjqLcgR%2BWSn2M4Sm9ikC8ssWBxZTQfkpTZAkGHphJ2%2BC1DVOV0DJ%2Fj3bNDBNXH2wCv6cbYyZMQvel4ktYD9y7q29dEYZSYa3kA%2BjtZPPvLhsIUXJ7%2FCFnAHNVXjndOfVYCbJOK%2BgCE%2FrMkWVcRvEr7ScS97rK3KHMg9IDm26Ff8RV9vRx5IKAQpvbwp9G%2FV9u%2FBMdZPvmQZtDjKXyoVLkkZ34q6Md7eWkJGJjUVFgclG68V4M%2ByGC8II2G4KAhUGfqkXUZquhKdJKfIX49SSe%2BKSP4%2BJ6CgwSuRQF691VmUnkdD2SUfFLUTYc6MSyuIPJHbj0Eug0EoUY9Cblbe862gVKuKIUjkG8EKWzTWOQu0s83zOwJEejKai9b8YiLIn5u2MceteSWTXDD2iEXc1xcT0FP0gESQCWvY1SiXx6Ym4wvq%2B9zgY6pgEhDDf60VmERvwdlAczxyC%2Bsykjqb1o%2FkxPqBmVFIiFWQi9gmkPVnIbrpKnzypSKYaP1VuTJcPM7QyINUC4yChoSJXTOEBWnGqQf0gCd5YaGPQRddPt6a9AKBlr3DbH0mAIGbSyFwVJyJjGdG6qL2ICXvdHGQE3pyAeo3R%2BgMdRwL8FKzcAnbW0akp6JmNfhw2Wmg7v3fq3abSkcm3kzJZruRoYsAto&X-Amz-Signature=6e21c263072de537bb930923b925956756c8666d1bc41946abf7d038b9c3ca3a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
