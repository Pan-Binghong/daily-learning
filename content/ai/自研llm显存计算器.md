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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ULWZWNB2%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T024931Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJIMEYCIQCTAgx3QHL6Ds5XMSu%2B8fEazvToU1%2Bci%2BaXg3lYBUdjJgIhAJ7K1VH%2FamnuEyzW%2BCYKakzBFG3HARbx5CHOndwhkCL1KogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzA46ZqheyIiFZEIH8q3ANJKVkY%2BJ%2BQbMw3wwgSilzoOhlnmlrlC1bOs9unlHFt7zqdHOr8xElG%2Fa9LmK%2FtrTyjRJ6ZiMzoh3VYE4f9ayrJRHxiF85KxT4aWsqBnXCSIUYdm1EAekfini878i1%2FooYotCi3R6HFyjDVbgVeU3gXcbXQyMMMLJFcpcjaML0TUtEavkjwNvts7V4NrlAL0z55cl%2BdBZmAZg4p%2BlWmUwCxknQJ0OimRrtRbDeT2azrgONTYt%2FXIn9aZXB2GLFp3nXl7RS%2ByGqp87AE62gBermk9Gem5J%2BFHPvm%2Bn9uOCsShTy64eu2GyaNIEOs%2FOTGLpiGeDFnyfTZsySkdM9pGW%2Fzwgrau7Zdyvsi3Z95o50O1gmjLp6zt7a87FltbVjYt0vkrEONhqDEKlNVQPBO4sONghFNSuVQaTxtjJJPO3Vpz2q006g8hrbO5EUn88FwoV9WA8gb2fXzu3QL6Ru%2FJunL%2BcQL0CYnHDRYwguSwPGTUGLIN%2Fnt4R5oRNIYHHsoHBq7crLVLqQRjyMS7kqTgnmoXUGXSSsh7%2FEx4dJjw51Nc0CABoPshP8j3pGpPRAUmyzv89oZnYAmLsx3lTuEX4BX2poNOkNgC1PV2wh2m8YGMny3fbvsO0vCoIgnWTDrssTIBjqkAb5Exd%2B3UhMYFBFNJ%2FIQXjE3W30u5AG0Lx%2BSr8YMSPOPmAegg9pVGcoEJlETYkUSIAWRgP%2FnTVSUshd%2FV2IEd1ZPU%2BkXqXZ464ap0BqoR23AL7B58CKREtnbZ45oCs2aW4hoIozJRH0j59iMIxx6o7LyB9YbtwKjUHRRU8XGpojIblI8GoN2rrdCH8djT88CegE9J%2F2IATv%2B1vPysnGCsDRoB%2BPe&X-Amz-Signature=a0d97de5b69a66ecd13f2a8b040e5e9a0a7364aff2fa03aa45119aaeaf477795&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
