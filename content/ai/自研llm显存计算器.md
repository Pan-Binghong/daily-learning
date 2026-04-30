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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WT7SZ5QI%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T043402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCICGD8HX%2B8HFrw1GMuajGWCL78AQ7eI3V0rqVXYq0UemNAiEArCMd48UVDLrmFQ6i94ClJHcsqc3%2B05%2FS6FAEunm5xS0q%2FwMIBhAAGgw2Mzc0MjMxODM4MDUiDDnIKRNcDGYxjvBXiircA1i17BDNDNMkizEzmphxtYM%2BNOHqMDWGRA3nnRVvaVp%2BaPVzuULLR3sb%2FTMHwqBgsJnePAEyoU%2FFZZadkPbylsuf%2BaiiOu2BDOkbgOKucpKqQTOzocCKpKvh%2Bcx4j8Gh8GQwodLAXz5G4ft%2FgK6sd5NMVLe%2BHbho3tEigHVRh6hOg3b2YW4l4lj7LML25j0KKKw47fWUSLPsgg67ZtgljnQe5ORbnH%2FcdEYUyhs8Xt%2BiMMG5SOkvCSag67qFOtprHKNrYi627CmGmiBpkya%2B0nTg0ITGxlyz4eTD7Q8VlqNIfKBy5X6zEMoyNIwwra%2Ftad1aULK6IYk5yZ%2F8HiKoXwDNxFkM6hCTWXG26k3LJsNsZUvtRNWN3exmdPSLj3cQb13JV5KFJE99iBpUoJpxlX1JzSyGg4%2Fb8W9eoY9U6Cu92gMjuykjL62th6L9SXdg%2BlzNMuINj5yFfMWBavPtLZ%2B4AWqxm0KrO5FcCMHB13NOhFNz1fe2OdoC8ajrcoDoq%2FSiekshjrCVqpQmNhwNUnPNwzVXADANMpTUmnmx%2B9hiny1JLW6Z%2BjgtgfMPwsTo0kPkryBrZpk5nqzYF%2Bq5PW4LeL7X2QxTUAUzIsWVl6IC8EBgjRuriMNpw%2Fy2MOyzy88GOqUBRRfyba74FLz7tufGfCtCeP%2F9fEdMfaFwrx8NYY27%2BF7poE1gX91RcDHpFY6jEeFFUarUMeiATagDxrpGdOWE%2BNWsVjTsT5vdmEwfyS0f7XDNJfJ0OCoSM5UQJ%2F2UoxB7Os%2F7wSyyJJdIqXkZc%2BgtYCxBmEooovKY3GXdZNQFKzKzMuZE0Kn3HMx2Jv3FB1%2BZEPmesUEeqOa9bBmaCeI8O2HlEnzZ&X-Amz-Signature=61496aacb8b089f1b4d807cc5944f7dd27761f6265170a352e4938d4b4d92b96&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
