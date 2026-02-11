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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOADJHHJ%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T034904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBZvpqmy4F0EplODzdRkRhT%2FkLUUbFH3NrktGeEwPyCcAiEA826cJWExqRyhWWPs3HF5uT17w1cEArAY6V%2ByMcq8SNgqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMFrpStShk8N2kSz2yrcA%2FTAUL7lkzHIgpT0rdkgu1FbI64MzUnPwVQzU33KfZii928lqyk2Y4pJwbeOSvC5muiwOKVIBSz4PrxDkehGiSvyVeyNM%2FT5InCLE%2BwQiXIJxhKMtgWepds98cyBPJGBIlpqTAoo208TVyvhd9YnqxBZYAdkayAfUshBcQ4csk%2Fj56X6guoBdqt9NRBFnxYc2rqDcYukEJ2JNQPWk2xjhQwVEMsH69gWQ6kvXFS7jqzKdWOKQNQoT%2Bf9asyAFR318iH7hrucdDUUboQbeFrjeFdAoy8%2BYW0hRu%2FKiwdyl63vttfLwQ14MmXUKjxtVM48x%2BrtkNwwpI%2BtrQwJFkeG4UdDpyJw%2BwHJFBgb6HsDToDbQDOzEDGmOQlw01SRXLLOLrmoUeGROC4gYZo18lWhXW2jrTukqTHb2e49t0dmqe2aIyx%2BPnjWWdpgoK8K4uan9QtioIu%2Bmz%2F5OzjJnpjOtEBYQBLM3lQgPgCR0kDYTslIXJsAu56nm5X460neT7h9qm7kSNy3w0idDE1yjppPFoTrLWm6XhmAN%2BykHOEa9SBVA6N5t9jh0mwjlGEPwMkwH33SD970GSHd%2FGcYveGdAXxZC8XqxiditZeSnlDN6i1nEYQaDSF8AmsC4o5yMJ3Lr8wGOqUBothmXWLYvsaODdYimL00Z6Pu0nsfM0AR0w7Gk9CvtnEWnBGeag6%2FIzvBweX0BQExz1gRYUuPXQejLzzd0g%2FipcybziZ36FkFa4poXuGIpspv0hByB%2B%2BK%2FCaGuwo%2FSpq6xGPAw3uFKyvvtHGKhlewIW3kxqCuJzdUExpTPlhx3ULJ%2BGsVFCKcqokYV7Hz09Tw7NfLQ%2BEPWteWeEvfZwKEZ32yHoFn&X-Amz-Signature=6ad55f0a3cf495eabbe480aaf57f9273ac055db0e34fcc03ef48173bd4fe2aeb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
