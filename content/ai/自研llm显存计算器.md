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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663AGVLFZY%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJIMEYCIQDeERczKjD5xuhdShvEd0H2TcfSxUq9wzSaXqkq5k64KAIhAKNV2A43CvYefmtQ93bW%2Bn4ZwJhL4jM1dw3hIzG9Rh9UKv8DCDgQABoMNjM3NDIzMTgzODA1Igxqm5b4%2FYXfOVkVWFQq3AORrmEHdALfqeY352KNNyIR0kACrTCrHkZYnxGep4olomIAVVbGcYVZdBib3xquI8SbpsjgOT6sCaZImOoisUF8NemEPMYD3hFIhAbyT2O79ddLwVQIzv5PZsy9kRNYxDl51ATkYG54P2HsUdbOiSgd9cxQHFwSPrTPabLtxP5BHDQUQzhXcCEsF7lCtVTyf6D5P4odbPPaTMED771mUA8%2FLwaxcMEHUijS4Q%2FPFlvg60dFnPQZlxkAKqDRvVvZNM2%2F0n4hAUs8NSB3zXAOLiON7c5upn7nHW%2Fu4jfHUiUVhr1Azssn2iyZhlIf6FCt0JcNVjW23I%2FUcDmjpfrZHXXTnBRkLKjLdOZ%2FWpqQUNRHFcbuR62zITYHb1mB2bDOSDLj7LuGB2SATZebjXaMfCccKJfWJIQJWBinRMgAxu9WALcQ0T3ou4sskqjE7ThiCVO931%2FNpy5bRTcelQQW1v%2Bs4oEG24OA%2B%2B6VbRlA63k5IjbkEFPGFjI0OLtM8Xx2kv9u24jwGJpqy4mvhJy8uiaeG%2FyigmdSIfn6eQoDIiEJPFbqQKl24SPwrZQDu4YfmQEwaksaDs4gfox3N7v254BvvV%2FIywnPGA%2BNrhTJwCt64fNNyMRTSCZ1NLaL7zCh0%2BvKBjqkAeEP0AejgZxwCdFEXNl8saSmiQCr90WsfuRMZFtVHt8c9xQdbOiwVtA5Chb01aVSRju1Tsv8G1aqiJJ%2B%2Bxano6Z58xkkwZ0cKRqa9JqJjBTHuau6eLuesPpiIX6KI3EGDE0wMovAa2jYIS%2FcLDUmc%2FrWVCIpRCj5GLvFl%2F5KmdnlTWLf9rAMt%2BKnQ6Y7G7X4n%2BGdfbBmF5%2BtDnE27rU8yA1ogETS&X-Amz-Signature=0e2a5e9c57b20d087067f0babd5103612fe7c80b32640430715a786198fe3c0e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
