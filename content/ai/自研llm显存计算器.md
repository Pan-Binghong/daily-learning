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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAZ54B2J%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIG66VNGginHYmc0WLWNJgcNHIZIU%2Bbl1rxmdylj6r2MKAiAL6fa%2B7voJ4RElHmVHTudWbYVm5jgoxGiSR6SQ7hImxyqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMw5PM5bjIRaRgb53MKtwD1Qh1HHUX1XThbu%2FkDXNC797X%2BtHrPOwvT2T%2B%2BwuyeaA4w2Z9tbMERuZy5QWeM%2B7Bka6S42bQ2qBxL5NG0FmCCdEDNF3p%2BKut3lFObOoFv14lYd2EuIUSjiYFd0HK2hrtib26%2FNhaxFoKOyjM%2BRZkKFddfmusUGcO3UO2s%2FZXFY5sGZ%2Fs%2BPGgzB6JATt4zod0BMin%2B6WAqS6evAYTr9GXGJj2pKL9oTtlWVlpGogrcPerMojotvnKYAMfRC0a7T04WDtHucv2YhCFnsplcal99v0GSKwp3dc6Lb67vZ%2BGAxebWapZ5HOlXAZmo%2Bw3cOYsIAGiqOpSE7x%2BNTxVXbETrTYTUzkxwTD0qPz071L87c81A4oPDPB9%2Blesye21xS7veXCrG1uuT8nSDZI3X3JpT%2Bt%2FChA1SAzlTWQmHe5YtCRucLHVP01gohpxH%2FpYBLYsI9kR9TOnSzRFUiPvFdtAXKO86%2Bl1Zt3QdlzrLbcm1kfCRbkIXlbJpVtJbzSBsGbCzJXxgAE08NsgoBv1BXb3XOiAhu%2FZEHShiC0118Y%2FLQ6ZW%2FoH2FBs0nX25i1a3TMvV%2Fk0KtjuAKpCuBSwhyQNPkw7FQjEbV6%2BF6Ko%2B4dDsQwhVMeUl%2B0Kwiijk3cw4IeAzAY6pgGwhsw1yVm%2F%2BGCnKrrjglNGnHDpgvM2EJbsHYaY0vg9k0C8wDR5TqoqpkYrXc5MuZ%2Feb1toaD8pWNtWA6I8mIW8lrpyZFuGG1JaT8HUUl78hypXsBSIEMCbYI0AJyyHVwQyxS8soOUVl2h%2FnoOifu66hKoi1NFAXsRPeyY3zJualCi%2BAAMQHOWzg3Tmn%2FbLTxn9BHKr5vMEE0YfYTpQPom7M5fg%2FvQd&X-Amz-Signature=c689280542a4ace7c322a90ac8b694a503dfdd4e3014478706fd845b19e8dbce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
