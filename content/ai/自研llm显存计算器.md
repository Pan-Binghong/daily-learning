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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSJ6GCID%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCID3Lg0izzU3dNIJagx3sMOHmI16uQXDBguh%2FTZTNa4aDAiEA3%2FW4ANQXTh7YeGnhzhjwI1fBow%2F4mBFovO1MvmGoY5Iq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDNwBU6JXc9fEcWTnxCrcA5ejl89noNgZZWWAYW7uz3Udai2Cx7KDXIZ4d%2BwkKHWrUG0d3DxFSh%2FcMUEmiRlbnafKOoswUO4FWgG88S7PlWCugsnP0%2Fh6dNol0gE6vqBJB7%2FVp%2FY7Gm3Uu%2BA%2FQlvUBRt5iQnwQs5ICvSQ%2B6ijekgSSQRaRjjfM4vfP2s29RsL4SELSBDmTb8nd6%2Fcvax8JJgNwgpI%2FSxmlYc%2FKxsd6OmNa8yzuF7gyptOZV1YeurdXs5dA3MV0Z62betsz8PZnqMDP4Fp8shplQwu3n%2BL4IhUGDaqCtDZond%2FUd%2FhIWj1phMFOSmRJygFRlXOymqQ4hkrsBBsDu7BnS0MbIYwtspezuNuJNhWtDmw15kjYYmKHFzXf3EXH0jTScwsGamIfrMoPuqf%2FyOAy1Badf8PbJTDNN3F%2F1NYj4etihFHD9eUky1zV0bamJgcnWxkdGUE1S%2BxwS%2F5e5LG7BrkVrxLh1LHYyHxzLJAVWyN01iMe5Lz%2FDuL%2Fzk6dT8oFaID7rvt7PxJykHn%2FASR2u%2FJE97yCED8nNa5ytiFtnHQzN2do9wg3ftmCB7KS6AVdwINhGRiBWyqrEdBJql7zUxpkxLP3NuNphYEZEGoUJDZEspVa4GKO6TlJgh79E%2FhG8sfMMfVm88GOqUBmyQG4CrUYo5dHyDDgvzw7XYBMik0qjcTpmb7%2FM99Efj4E2aApAtd%2B5Bx8Z8%2BXZHHEzsHCI7IrXNKwCtS2M8Q%2FUl8otfinpnLc7gaiSq%2BqdF67TR%2BIDUCKckvBbd4Rx3CR9KcfGfoQ5SUgkqsIopi%2BvlTPDAkF2pegqCfaAf%2FjvK7aIAS3rud7llveMlqbUNIa3dVxFxFkWOZ%2FO6SpfUZACdyq%2Fph&X-Amz-Signature=18957dd395ac388ea3ca717d851f7f812b083155de0839241339476c61617030&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
