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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQFDN3ZN%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIQDyKxgHiCdOJbMBq%2BWE56GcRzp3wAeC8LwBszEso8fV2AIgDrYlIaxxCSr7pIys3HmbwFxRP2G0FBhd%2FiXumXnKoZkq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDHJHsg49cft%2BOToAeSrcA8dlFU%2F75YK7uhWsPA969iQWhleI71e75TGOBON%2BxKCAfrL3DRzbsdI4rERXb5EbtQJy1ae%2FeF9x%2Bgv%2FdDw2dGc6Wyj%2F%2FrsDtJMZfhZqcFfapXcZIuZJImQ6FMfLdo7ToxqU%2BBIaa%2Frv%2ByAxUarXfrU2Y6wx%2FpDsY2ewRVESkM1EWtwMIrmud%2Bel31zK3fEJsU6%2Faj4ItQFQuecepVfmjJyvZ7ZLPpft2jzuYaRUd57KqT2c11dACyZMxc4bN7lbuS7NqJwabMt3A2A9LKgcgvvBrFbKqvn5Z8dtGZhhI881lLf%2BPD%2BaaBMJPTNNCPqG40KgX71zI%2Bdd2x7MvOHU4jZQOMBIloVvn%2Bb3uyEQPn8e708CtFfwEQyHEPb9elPATB6vVFgoHESacL0r3xAKdswCSf1fJELf2RZOMa7Lex7RGEo6bKoRzFgR4KlhmOBY05Aft1ucQ41Y1jzG81fMyVZoWgIayCcPTKQtq0rSbZaOczV73mBGW0lZHNdeQuGnOG6pAuqvJUrgFHvwdVU5F9bKJ2A4AO4HMlAoeVKR7zCB0EkSgB3n2%2BokF%2FA1tQeio3bRxlO07%2FwjJ9aL5B2ZjiERRXo8qDlQaUfpbse3IxCHeP05q%2Bxf1U4tjY32MJWexMwGOqUBA8NPhWjB58qV1HWRU8Q5jdPxSwDiScZQEgBHwt%2FrFdUdjeFr8q%2BwckX5P1K%2BG8gmJ4tGeUrb%2BveIoOaJNztTV0tqmdC1Cv7%2B9su7AleSzk0LIasfv25zB98%2B1bHAtchJYS8tQ%2BBDbB%2FKk%2FMGGPKUWxRG6BL85s6JkZa0rCb87mm6urix4MOgO8g%2FLve1y6B%2BXfGpYR3i%2BGUw%2FoTtsm%2B4cSTTT5El&X-Amz-Signature=488cef157293c862ada48e312724e318d8b1bcb965c13db6a2d5f04cf4ccf88f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
