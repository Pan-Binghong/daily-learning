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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPPV6GQ5%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEEVySKACmDfxX8KW9q1Q0ZRjkf8oYQveuhV7InNRQxuAiBXBPlWaxfm2xXFWAWtrudkf1aWn%2FVfNI1NyilwGkslrSqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmt4U2XqeJakZc2Q0KtwDLZbsbsmiMJC0qWLreDGl2bhpxkkw1s1TZNIgeLjx8G1xx7DtX9mMv8A7OpyBZG5IbbBXVh0My4Fi1GAfTxQu%2FIaNf%2BQuyoJHeyC2%2BclC3zGTDwm2GkB0SDQ2er6gGf%2FMilXa1MemJAzvqXRF9KAn4KwSGtUmNb%2FXfwULYrQS3PNTFgv%2BIVjbEHmD2v34CxqG6gsM575DHjcg7y7r7hxX8uLIeWCJKDlpBqjayQaNL210qhyzd0zV2OFEItENJgG%2FaBNXaKqWgdVRzN0iloaeai7ZFARuqbU1SwEYgb%2FUNJtGQNYmrRTKqvcaHXVL2LuSZMerWJL9eiwddzVv%2BVnVmj2b3oSJD4HHNNxLJLKrXkLUe84XW90uC1b%2FISF2zcFJUNR5TysMew7TTlcHRDQctJcdwjYSiP0%2FHJYioh0eUVnkIhN2u3UcZGbNbRkOLNKStkg2HwGaAN3hksskD4fDETTesoROg42iADYhIpWkGkYEgGpNgbnkgraiwCDkX5RjknDfFMua0qEGxWwl51XKVQ8p%2F5JSBVeLoLMgOAU5zS7dt55B%2BLv6%2Bw2P1K6bo7GKfJcSgvHYFCA%2B0OcByECQ%2BjE%2FRbrG78VViWq6g7wCSOCNuOzCnLoOIMKK1McwosSqzAY6pgH1OyN0RigvO0%2BFHOtSP7MB4pVHZm2WZKYd9VG0vDgZJR6it58shbgpBuSb1bUl2VjOMUuUPuzNoSVTgU%2F8HK0irAiObWtVp%2BjPWhrH1PCuE2A8fxpaaIMbVoigtVWxtqqec4FOlBJoXWXqoNRii76P2%2FP7Y8VK%2FbuyN3AbjLAJXXXQ03sMh2zZMOxT3wUdGX3wu20q9NWnSrY4gRBOt5Cy%2F4KupZcz&X-Amz-Signature=85dc8a456a12488694d27886132ae637466b719c66c3852d8c29f71032476674&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
