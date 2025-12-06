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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HXMU2VO%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024106Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhq16zylLjl%2B3TJNMtEuMUElTNF5NWKFxACQkxj8PlMAiEA%2BKPlbLUi4ZI9XjEriT7jjyvvGoZYmY7I46OqcNlqF3Qq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDKieGYrCYuF5zPUGwSrcA3lJxYh7K%2BRQSJzQS3pzAI9zsnnJ9FnCa0NpsyFvMtHLAX9KlH6aP9EsrpM%2FpH6rquG%2BFSZKY7VrT%2BokvVdYWQIEGMFXJMiPvXXGx9i6mKKCEDvGFI1RtSu%2FOIqkB5l%2FCuzaU2Pu%2BfkTB7dbDCMzMfR1xY%2F9Qyka2UkxvflUGMxd2U0slvIDzAA8vZeBpbaSDJzygbyKPGzERORUBNqrfQrTYI7LMeCRItN%2BKZmk4E%2Fom5GIo1xOSUR8pY4e1ybYII8YU9A70Q6hexETU9%2FeE9LNItytWFXD03m0Sq%2Bu4uMqcGHkhke%2BwSvPKCYx2Hdcj7VzHzAtGbscChjqESLIcv75c615QdmHW1m36uayg2hCjvl%2BnkEnZ0iuooCqY4Zb6oewUV6G8D8qmnQFgGtwJ7uIocwJKNHrEyFsrsHdebJdiGByQmTtnwsICX4YvU5IlQ%2F6CJrGib5AKvTfHC6Jrk9%2BbjpTIoxE1POvbD3XGuBXU7B8BkxPMMSolDLc3Rh8m58FFeUuVkarqqN7Tkn2jyg8kwekmN9nluxRx%2Bj%2BVmU%2FkR%2FIBj1cCFzek8URmcJ2AruP3Nhj3tpz9oGRgmyn83G%2F7N%2FZ8kR4IYwIoPUBGTXCBW%2FkEQppSD%2BhbT8jMPynzskGOqUBwSMbaKtZxUuWDQ5wVoeKdPQKyvguPtCwTYcca4eJXdYDfTmT0F2pWZqHhg403PcKTaVuq0gwawXFrB9mFV8A1NTNsouchX5b15WVL3c1KDNsEiWWutfGC%2FebeuLtnJqHmYj8G7O6QNr9Z%2BPP0ed%2BMSlQsc48SDIfTTK%2Bxhjoc6J70p0GL0byfBJcpD3NLxhqbmFxLp1D8neqTRAcKtWQzZQfZoDi&X-Amz-Signature=6be289e9f8ccb3b20e043a93e2c0b10d1401a2460ee50c11ad37616231165ffc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
