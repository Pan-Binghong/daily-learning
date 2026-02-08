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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7SXBOJS%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035451Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCpVrBLPL5N16p4mnctoQbP1mRScK7EeoW1bZIaHwUgJAIgB5gsPs7VWjoty%2FXj6NsE5o78S2mAgwoaI3nGnBpkt2wq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDLEgW%2FvC3rpYwZrOkircA%2BNzYy0wmIi88ryr2CJWG%2BFOKQ07rc8KpiV0H%2BlpZBhBtYQ29%2Bac82%2FtJqlSHR3J%2BPM72upvhhhXcY0oRRRSMBG8rgDFIXrBatliWRsyqw7oAhICtRLGECICMD%2F%2FdyUif4inABbzNpp1s2xgb0NJpAkWdP7jGjMroaMCX0hcymvAK97BGWOweL64exSwDgcsXmL7BIy%2BzMCQLDzwgx1Ij787jK3nif0E2ER12z%2FGBKElimYU4VWwJpkubbKPiySbbD9crtrrJ77yoFYZGYVERc7dVofU9yguexwaArWGNxI%2BveYC%2BEBYSaVAI37wb%2BrLMFR5HrQEnHTGlopraaQ5NGXnBr5w8Y%2Bthv3voZCzTh5JoYxCLEC%2B%2FUjDCyS%2F7bxbrE5a7mQdcYusDKEJ%2FSOYuO9qVbeeRC328CAbuaV%2BtFPEqUhQpT8YgPV2q3WoHoX9LmklqiKfh9gptTtO0kubzdubxxqGB0RGtxXx%2BdsQlzYisHEpB3D9b55ioJlAYNu9wCAGxnwr1qlziV61tGU1OwGNMIs2gEN%2B1mRE%2BGyCXuYqX5TJrXYpXNzkBm8tDy3BUS7OOfiRllwOXRhso2JNIUklge3gXbLUnx2D%2B%2FjzAFIHvlGjnqHNM80jMv4MMIOMoMwGOqUBzntBrYVr4Sifj4ZfOafbwHL6yjhUrkXI4sVb3e1eAzOx2pMjyIAEu8hbexClhAmRM3xtrPU7QjissaVLTZhF9kVVAmWM8XuFRxyvyt%2FtBhnpiEmmmAF1tWTRpVu5Qw4CBxe7JPZwNaPd2Z8rhwCqyjs82DmPc7tbVOzkwplk7IkpSWTU0%2FiHLD0cIWyeTQs7pGzblLlMFwvPTqQqZGmUAXFWST69&X-Amz-Signature=f851a785913299f2fa99b03498ac1c59eadb83ee4920673932d6cb932ab4cc78&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
