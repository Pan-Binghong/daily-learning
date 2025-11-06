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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GXXRJUP%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG8mBKjsJYE69VmH8XSl68iNqqTdbDfkpovJXPMMX1dRAiEAoNQXc0%2BOW6oGYgTE2ogxoZT1TngTeNJekysjxLiFg7QqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJjIXEDHTJb5JCzheSrcA%2F3TY8t61l8qcvEqPEw9L5%2FyNsZj7RzFx97OWOJ6ktsHW%2B4upMg%2FQB4HeWDmxZmiTnFz876j90b8qnXaPJNS3xGnb29nQ4KtmgBM7h9RNUYCmLePvJ12bp506ainwzQ2N18viSeKAoOlRAt5n7ybpoUP%2F9bU%2Faz4x%2F3QA9ET%2BSyVR3N43fv7BcKEdYQjKCgjd2xyyopQJbbK5cJbdZ3EnkV3VQvJP5GQ0Zj8ZS8MXzx%2Fx0Y7XEGPuPfW%2F1VrNANCZwBJx8tbiqEhfKUxEdDlV9ZSj3WL5sncOioZ1b7uN9%2FEVoP4Milqm3xB9fatz%2BBVXQgr%2B5EMTtU3dtn%2FpJ5lgdDBd%2BOM8Ji2HDY6Rq56Btq%2BMGJoiSY15plubBSyDCDGzJMllYIyl4d1el4vxqsFCjDQIS1JKZZRE3FY8mMRaJdjp6YKSGfsyYsqVUcn4abJNsTATBIEo7Tk%2Beq1GeKqmeVp9iKwUBScJJwuTgOxsWCeHtRJ86qyisWT4Pk4mwkEq0L%2BwN3jR0Bwmn9N1RyKLTZeSjqeqQNfqu1BaklnmsRIfLOODl339vOnseMYqkNesQum9goM%2BnxXWywEn7Q78Pnqx1G3TVuBMFLtHHD3tZYsmIyHkqySHssoLlLpMPHxr8gGOqUBDHqEHb5IdTjirAjAwFvqgn1afJGRpZeSEi%2BtrPr2QEoWsNTXGDsEgrRA5iOK0%2B%2BVbFyaZfnvBAoZ1cpRF0NUUHl5L22gfS0ghOMemgT7qMimkGCSXMSC53FVXfdVyKq6gyFgPqQnAPxJ5%2FhuaGNDgLB32R4ryRO2UVRBholFTUNIqIUrVf9PTcq%2FBw29q%2F7q4MXe9zFGHFo60KcBkXaVkgGoiGfU&X-Amz-Signature=3e54a7caf044071ac784af7d06cc31689954915b80bcc41b131bfe99a00017dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
