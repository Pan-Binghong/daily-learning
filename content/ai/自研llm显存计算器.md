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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YLMNGOE%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T040922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQD%2BQLriyKieML1g6Hrit2lL9TSS%2BSzLSV%2BQLCKBAjBHfwIgS91%2B2%2BCHG1cvN3PXzbA5ORINBugqZsR9XGGWjbAY3%2BUq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDOZMyUHXtpxcaAtDpSrcA8ecDF6Afb16iwiPTEZLKJwY0weK1bj400lXfg9hXCwbMAtoHh410K%2BKHNEaLNpm%2BhDhbIafzOoNL8vka1AkRiqe4X7wiBZTuL%2FDT9nF8RHKF1Hj5TnXDFG%2BB%2BYG0whyZh9iaCJuWzScb0LCn9tCvOcHHShuHFjBSST6zO2j7fjk70Ljhmj%2Fx34GGvRrlylTyCER4YL%2BhSU3L1wp7JmNNNobDZE2inXpsPUg2O6ZLDN%2FmxKuXVTRt7R4q6C6WiS6rtdZ8N2%2Fi85c7Zu6MZIS1xygJDD59ZlAXt7pX175%2Bn9LIILFFyMP9%2F1ESMeoeg04qK3TZQnH2nqr%2F7mMkKLh3ZMLmzqtOVJC%2B%2FlpVuuq9ZRck9%2FG%2FkVDvyzheMIG0QyG1TsA6ONKKhVv3mGUrSSIkjh%2FzFzhfrOO4thGs1So%2BejDdjeoC6HJQADS4GT9oKaGH5VVSuTbpy8CaQu67tOmK2Tn5w7UN7F7YtbIHrFsy0QUiF5KMvC%2BkOHiOAtpWHaDc4g%2FIHwqVIKPxF%2B4YtsZ%2Bv8rGfOJ8j956Zg19NPQJTIM0NH9zmGpF%2Bl10DTj03Jtc7MPssgl44xl7IIDrcBRkxaPwRpI6mmFstBVknUZyvQGWTLDz3o7cud86YmLMMLIp84GOqUBHxtr9ITkFR24vvhJ0DaeZSQRhn6v8niy8PClFo68UD4bjDVLfMDuyAr4uufDbBBcx1M5SmQlUHuyacoW%2F2msyatodIg5fFa1C2xXF033%2FR3zWyb89inwMqMpfoXeiWTYiAdtBOZnnnq983VXzvkdRM9c4mZ2dpFZZja53uPKDJa3GPtaEomlzh83WVlZhGvQXM1eqRZHu6%2B4D0IjvrfU7V0OoRDu&X-Amz-Signature=0cbc737bef58fe498d825591b03bbfb0b7efba9c267f0edf4b89c00bbec8f400&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
