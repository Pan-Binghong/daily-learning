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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUC6AXAW%2F20260206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260206T033315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJIMEYCIQCWIE%2B2yFHpUQkPmGYzcITYyqGMBUDpumN2hBKsfm5VEgIhAKgT%2BTenBo5kfvGGxmzIXrBMCiDy5lFVV0jjEPY5GAi5Kv8DCDwQABoMNjM3NDIzMTgzODA1IgxtkXUybLmsPf9Eax0q3ANJ%2FYU0WnR5ld4IWRR%2BiYhGHNInS1nwVwB5s4soVDRJb%2FwipImr1drm3TC9bd5YUrjybKuBbPZLgXI7G5FbMtxSKHAuRWdfcIrSGiXkYOAJycRKMIl4tx%2BnzG5GUPcgNXW9ClFrFvVGFTLkp0rP0ZQaw4S7N29YplsAAVHpUic9x5ULeJV28cEip9b6APankyXWQkGx8MQWQC03sh4Lig3dEHzWouK8EzcbyGmOcA6aF2u5rdrhDQ3iZbQCV1fKDEpaTmJGoziexHOwkJo%2B4W3tYCSY4gQRj96wY9zfJD1g%2FsIf5YrULg3Xy%2FnfVbkAHaAHR3LKRVtMh%2FUIrf9uOLF5XU23MZ5K9h0FlkV3FcTZgRo2BiWQahvlVb925BOxkJV8ZGc2eLX2hvLT8N%2BqnvseOAoUgCkSfZgCnGptUdFXuKV%2FCVCNJBRteAdbRxeEtfiRpprSmsfvopxzF9zGvh2C3Xc2GMFr2SNK7YAm34a0fOBOu9d7vgRWk3XwMYEPPRI07TuRgzfWxb1GKN1%2FEa9OLfQ4whU0D%2FuDIdS%2Bd014c45CDusF7ZQ2Ii3aNd8C%2B6RdqMOSkaSRqoN0ZkIx0qfN3IQ68NwSf4IZyWuRMfByKECLAnDzj2g0%2B9K9aTCzupXMBjqkAewlPbfew%2BVSBsclAtHBCYs91atGVR%2BBXjlmmHrBE8aGG47N4cBLCRvIZ94gfHd8%2B9hqspgsoX7fAL3Ges%2Fr%2B6A2yE4q0EqKQ0uGEDJbLVY0NVlUMvzkZThcbbbKj4yEC1rB10YTqh6rZjyrJdoNdCwxWebi4%2BQKDTX%2BD%2BIO5fyxoxOP2bWhJVxmKOApYj7SKjAJClqze9aD2%2BDINEWYU9MRu36h&X-Amz-Signature=93a02eaf665f004c24f51362101afde7dcf0b06547fde512f362d76aaeefc719&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
