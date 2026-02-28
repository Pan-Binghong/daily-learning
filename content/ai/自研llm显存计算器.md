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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7MHDVC2%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmYkTzhMvAq9Mz4GRPLUgFzfJjvsSzzWh3tacu%2B2MHgAIhAIEonNsRU2XNSzddQK6Vn4bEoIwSA0orSrSmxdgA90VUKv8DCEsQABoMNjM3NDIzMTgzODA1IgwDRm%2FMr%2FS53xPKjdwq3AO6VJoqMY%2BNni3tmg4DiixWoLbdrM4FsEFXgdg7KEXchoajyLtEsJaammxnaihecCTySq9U%2FED625St0tkMMBJ04s%2Bsx1yF4%2FvgEv5eTfZchJAlfLmW%2F5UdOMYVLsrzC0IJ%2FJ%2BNXlIXbid2oR2tQ0ierAMLusMNDx5fa8QngldVAgqWVaWSUTKNFB5zD9oXkFkS%2F9xCZmAt7AnU9en7Mi4PZz%2BTaliai7dkOEAcvt7vH4uHbsKU1flC5v2BwVupNBgn3KrBCYx3z4sHIzzA%2FDKdGD81gNptIXVds837zngNKjcrraN2ofg1r%2FCVp0NhZZdOne3fzC6vAGxx3R3g%2BLEc3xQeuBOjGOVL1GVmdlvX4Do67ZjWJmPe7MI8YpvhelmlRDAfNm4CaKINmfyp9szMdcTA5bfW1MGbyYcGlmskYcOd4MHgps2QyMqkaMd80XaKEPjU%2F7uaYAlY%2BhpP1WVPnqtTlY0NP2R8ohjzz9xfisdP4WnFJ0gB%2Byym0v3AP4%2B7BidKvMxncUBz1VWKdEHGNL1%2F8mBiRtk4IVywBMw0OwPp1%2BiB824MLf0QWRW344a8fk32Cy4AbqQWbV6zbX9oEY1Zua7hDo9yMYx%2BMOdWewArTGtJSOR1%2FAlqtDDPlYnNBjqkAU9J9c%2FGko8zx1dMt0u%2Fg2VSIy5R%2BZA%2FrP%2BfzjfIDdE3OK6ZU%2FbFA%2Fat6GPCuCkwI0wHPKYYi0HRAFPHZNNRZWGmI6dI0Cc5lOpBBjs8QUSWC%2BELdoCruUxh2yWM6mRNNyCR%2F965epk5gzvlNayh7m5V5NAlkJWIUXRM6nXCALJXdOJFLAylTiPjE2bSAkx%2BoaHrEG%2FEia4i6Z72UdkGwYxQjMlP&X-Amz-Signature=82aca9d63530c0115d82b29a9fa9a033a3718e82bfa4b2fee20065eae2d5fce3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
