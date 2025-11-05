---
title: 自研LLM显存计算器
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
标签:
- LLMs
categories:
- AI
---

计算全量训练一个大语言模型时, 所需的算力卡显存.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667U2JNY65%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIQCweO58VIQV7nR54P63CETBZTD5eaSNPVGDEP1WrniCNQIfHnZDQi8Ap6K4uQxAahVWNZpaEZpbDNwAXz8IYqH0wSqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrElMcIIeZmAFnnxAKtwDEG%2Fy2pqYWMtgJc1LpzuqZLS2xsar%2B0GZwbVlU1aIGtxitDM1JxZ9dOnPaLOC1xqRpbm9gtjljuF3WFWjxa%2FezDVuwppVwN1J2sHVRGlgX37r9hXm%2F5dHFabfbjUgJjeRdEArLAPudUOFNIhxMVzjup66Uams63kN%2Fh7%2FhjvR7pSujybjPdpW%2BBGWCCfVf20Dl3CvhBlTLVo6k0tpM%2B6n%2BnrpgS5EY1fCM2RJFaDBu45zdiC5fihkwin9N0UVJwbpghkoWL1kJdSW7B%2Bjz8R9DIYd9Z2KmkxWGpwbDGfbjWCS5QgOKc1lORNitADPqMNn7%2BSEj3STGfw%2FpudCIjhyu6Xo0UvanXDYC3gWWKRCyJJJWDg3kPYcKjdGB2ri1YZFeo%2B4FP3OfwG6m8A8Kt9Mz0u8eZVh%2BWK4RveC%2BtqShBCgbPJ%2B8F%2Bl2Cnt4fs66z8DqFg1Jfz1IhPEaReoQoQHGHNO2cwmlmDUs9hdVGVSfvs1MEDwJJ1WPJa2XsQKV9o2CjrCaS%2BuTzdb%2B1VxrzrPsSJUeYH7nTRztoN1A0JqgDRyOetq3kE%2FBnPyzsUGPevZKhj%2Bqo8xPrNLazwxyGoPZB4YvVWx8QyPV5Sv61cZO3vjBWs3dTQUlXa9JA8wuqOsyAY6pgEzG6wJmQEWWYjpVnJ8S7K24rD6QqEsT78JwNfLaLSkiWmV88TVlKpE4LzvvGbh6FRRpBQfNNFc%2BmJPUDwvVrPJfKZALUzmmLp4EmpiuwK8o7u2z166XYZ%2FBM1gnBMFSaATxKKKUt%2BB8ZfkbHH7z2ze8MPl%2BZI8Ctcp8qUw3PjEEPOH1WJ0hL8AK3Mz58hhGEG1R6JPBpxd6iny3CmwBQ78UK2gf1lW&X-Amz-Signature=d4c0777cb6285f3798826b7409a7a1011382563235d80d2169dbf1866551b5f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
