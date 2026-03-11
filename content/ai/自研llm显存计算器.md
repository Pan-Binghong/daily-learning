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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623XIRFQS%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCcOwrrFc3zGUNg6t5cBBbzSPgClLwcauUq%2Bj0LYLnIZAIgSKChTJAJSqhS8FEzvSduCIzCvSBOvLT1TwSdJpBnJyMq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDMjkbI1ZtKqhi3BLGircA3zlud0RB8kFui5%2B%2FoSiUvCWH5kVVRpa%2FiYlsTYtoTytkTNqnYBZ%2FN8GqLGY6xFkE1tGywUxB8Pg4VE4oc9%2F%2BXK8V1fpXUU0JGv%2FsboInfXccYNle2rdixobOpCqemKxxDFSzW%2BbfLt7uPx9f%2Ff4Jho635mMAxIJqeda2a0wPSLA4i61xANrM6LKvB4HKSMJDMFQzSbzpC9oIx5%2BAwGWIyO4H2nzgoyQearMQZDkTcyyJ0HN1WmqwpUfgcc%2FIYqV052tANHqRpLbQb4vgiiorDLypONQPxd3asw2NW6Vp4VmnDkc7H0vtVLvY1RNRhNL4%2FF1HGZTs60QyXgSEzJ5BRjb2l0kMFEHCsvAeCarShQSpRoA%2Br88GHSf6WgK8O%2FVtByz9NCL4Z0LJ8oYKnySGwNaWDwoQBzGgoNp7coRmnNar0w1iRD%2BE5R3k8%2F4%2B4IKpbfsXZtx9ePsaKTBLQXEXypkiyAaiBf38xjtoehFtbBJiEvD7NGLQ5yrD0knKm5uetibd8ySDV3RJwnAyTl282ynsM0kyPRt6QTqhvAuI58tHKoOfe0s%2Bn6u2gNNsCGw5EwWqu3i8%2BIb6Q5moDLVoe8vsmb7x2sx%2FP2vXCFThcQAFIjiG2qNVJhtaYdnMPnyws0GOqUBAnss253sU%2FPDHToIv2sWEcxA4SY%2FcXqURuY5yUH13%2Fg0DJrB7v7pTqYJ66Hl%2By6CYLOIGH1kMDJSADRfrj01aKpCtiqo0XIPtMasDJ4tk1auiVv2Zwe%2Bc7b6g2uOdMOqK1DDjsICP8%2BIYP8ZjhaOOqLZvEE6PXw389p6wf8Cr%2FsbkZfSC%2Bv8JyRHUbxhxdgGCyYak%2FjugdtSDi6J%2Bs76j30DnXlZ&X-Amz-Signature=a039e4748e1c06a905db1b57341b6e80b6b44a154b79d12a0cb41aabca3de348&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
