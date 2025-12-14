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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGJIUGUB%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T025925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIFyRdIRYqzcIn9Z5V0z9OrErHGBrj7nFyWXVX4u3krV2AiAzaDNnRGpLCtZliK%2Bu0at%2FucYdiM6oc2IpGhIHIgs11Sr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMclT1jo06N3cjm8JVKtwD2ZqnKuMgDpKsYwgHdtz1YOQTrHkQKcqvsf5i8bb4Rl8veqH2cFh%2FTXOaR6D6bsj%2B8kfgmgVXl0rayxvX98P8d8utt6iR%2BWKTeemyCoQwykjJKxKcBmEr%2BeUpeyJRBuQVkF3ppGIeIN%2FFYB1BtYy3DlkV%2BYJ3LRGp0ShMW9YUkv1Yh2CP4AAMi75T1VWLqoH3vdXRRsgUy7d1E%2FvY%2BdC4tBwNB%2F8zFa0brZBxGrSRWasUSyszi2GVIzuNEDjW%2FS1%2FyQNYY2qV1GOvL%2FhJW7I9oyZH08i9JDe6YiZ7jf1MeTwwKauClXct3W7FMR9G9bv99OBL4t%2BYs8ApArcgbsTgUBo6dtfcF%2FV7Im5B%2B3OBN001%2FTA8qyt5u%2F0M%2BtnFjVpV2nH8YQoQI3K5vEEUHSzQZyaNanPti7admn%2Fb1%2FubqjKfu1REM%2BDlk24kQPIJkb8w%2Fw6B0SEjmcYEsgBQEwkJQgr1KhDaHE6ZQZ%2BKg39g32KLsPjLjJMPEH4ftrmDTS5b3SXMGCU9oW4lqjbVDWt5d1bwA%2BDN7vnvBrIV3zLSnKrZoCYL4WoKCTN4F5N2%2BS5WEXPZeeFuC4f%2FI0iTcmT%2BmadrRxbh81NJ0cBoJzx8gc4qvBJ6aVp6QQ90EE4w6a%2F4yQY6pgGct%2Bxfa2XZnyZn5idiBQws7s2aIaw4XRKrxPrTGbG2iQDIXOHlsK%2BiyOSXCH%2B5kr2VJV9DEUz7LNb8LnJcC9cFVoBOEnWWZnx5OYS%2Fx3X2DgfR1AaGCykBBY6DK5eSVoHnIH59fLDUvwnobjvwN6lQuipMZqPrYgHJ0upvtSqH1BEUrf697nKSCqukU%2F4bBhzBNrOcC%2FROl81mzAfMlvO%2F1RrLfLfH&X-Amz-Signature=6ef6eb6b1e032d20af91022fa905a0985598803fab8c2d35bb264cd4d3b084ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
