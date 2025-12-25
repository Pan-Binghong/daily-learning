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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TG5NI5IQ%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJGMEQCIF2WAso%2B054ppYrO1LhNRRzKoDkJXbd0kA5KX88hQKKsAiA1Hb9RyLeymshvaJhM01HYaP6uy1pRL0HNB1oVDXrVRSr%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIMTT53ng7i7D4epLwPKtwDR4JNMthyGX%2FtfzNe2nm1lOSjG%2B0KdskkEjaTBWvmdY3bc7UsEvfT60vX55QG%2FD2XlB%2BYlMptrGsyv9xVBkhpjlNwXwofnVishvdNwpsD%2BcZkKhH28uWWplIgLn5HRtG%2F19RjWOPr3RQXfX87IlaAUAMq3z3IIzk5i%2FD2KlMFKrV4YilmMzJra%2Bu16lE8QBM%2BXyI1nonKV9cXwTnRrulRPbWiY0CbxWaFC7AL4ygnUDY8LU3vbjhuSi5iGM8bCHOBOB0K3CR%2B0OHIX%2FfVBe1wXBmsXfceF5%2BkgH9wjbMX1R8Agd3UqpHYdFEnFsRSsOmLljfATumnrItIJ0ZfgVmuR36EvgZxmbw%2FPufuZcdEMe69LER%2BiW8xuczjTw6pN29CL63x%2B9AW8k7w3n1RzMNY2kk4mweQLeTWq80%2F0IHq52L%2FUG0a8eG6m7Ggxp%2FRhc2EycDoOFt7bz%2FxbLLAUTfGsMmE6VgpdfxyQLiRFVEsexq67YJKzgpK%2B233gCaVpMTEeuOEpbLgjIjIKE8h8n28q2gRq4sGkGudAxQoUzfiu7B3CzRzJqiQPeXn2UbwBgoXMK6S7XGQeTLVyWM9ri5VLXoOadxS%2B2hKdk1DGzxb2WFsPi0LB2yNrQLqnvgwhqKyygY6pgFINaGo6pehJZsYYNPqmlY5Fc%2FWDwVVVVopnV140iEztM98AvwbfvNhoHXXWG90EA2qb7sxy71WactzqLmDfPOLlSxvv7GGQ5NqGwgS3DRvCB0obRcHhvp%2FOW6odE8O%2Foc3di%2FCCx41fMuY2RAQwH1xkJOda8NYAFTr86ic3D9gNKNqMyhWSDGPpZXV8lYXcXQNMRpPwfNo5ITUQvEk09nxjvSqK7XJ&X-Amz-Signature=74afe9ea322167a84cd00577438ff16e762942e10063e759be500a495269feb8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
