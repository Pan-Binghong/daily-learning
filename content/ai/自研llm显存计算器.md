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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQATPVEJ%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T034943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHKay5%2FQVT6l82lNSSv7pY5pcBNmA4j8ZStgGv1abL6hAiEAmx5TYY6OU9oqhPjCE3O8xIBTLzCLqPRHZXV6%2BAmHwdwqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBlmj4R7v2haNsc0iyrcAwT%2FU%2BR2FeA0Bp6awVVhlMLQMBJqFrZ8o5W8ykurs5TGAxXrnKdosC%2FJLi%2FtCurX6pzToEV8nc38de3oRex%2BnZyi5cZI%2B0le%2BOHulDCCd2cW8mlDypw0oKXjxqE8Gm7pHs14%2BFovF0kGyj%2BYGAE5psn3BlYZ5q%2F1Y6R6vm2jWLBv3011xq85RR2f%2FLtmtZc%2B2T7pCwA40bLdTlvZWVVGV4Q3cKIlYkH4V9ZDBBfLIYGWooKnbmG%2Fr%2FIekzQUIb5gSbOxD9Cn0m4NhMOq35y6yX6K0%2BjO2KL7eNzdc1nsaA8Vcl9CBf924JoLPPOMTQl7y2o5kv%2BWNKMSXvwe8o4uotq70NjODEFO%2B0lK6%2Fu6C7OM3qg33vxFMK5eA8zFlZzkqh8cqr1jzA6FxMWlhB0LjFCRuidPsuyjX3eRfcqCk55a1y7l5n68lWLvdINM%2FGHPUgMnbQFbsJ4qtjJZgxOxQVUHVKvNrqgStIBU9Z30usLoAveo%2FLailpcbEho5T8%2BWjGhvXBpCZUrCg5kABAkK98wPKLeAm9TUo2uM6sC1aVfLN1qRy0MfU3d2h4RPpnuODoKvZC6YsUqsUs6bp9Nn%2FmU%2BxRFUGAJJqemGyj9Lg97JkE44YMAEVGBZZ%2BPAMJ6S%2B8sGOqUBnko%2BeAph%2FIbuXZie9duOnMnlFUjdCAX3fd6bM%2F6gmV%2BXxSGcjfaFENkviREFdJxdVJItttPQ3529M0m1Dp%2Bw0XJB6OjWN54uvQpBOcRdRV4zHSChFuHM4XYNIvU3eLgabFMmCQeGx79UU9MsmrF0DRjgl84D2c%2BBR21E2u%2FCnLpyDtGG9WNF3Or8%2BAE%2BSDoovJxqyNm13HWY%2BBigSXJdbDyvfsPM&X-Amz-Signature=a9c52178c6552efe53f77a52e5af3c0d35562a22573ab18c871f67e1ea1727a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
