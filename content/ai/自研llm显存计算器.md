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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HEOWZPP%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024238Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChzRKAVS5duLZets8MaytTL0jZ8wSmHx17dMqHWqXBEgIhAPaMUM%2F1kM61XO4FQ5zaoDuwE3KA1lrAmXPSvy4UlZIjKogECKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxqJO20%2FDiwcNuEWwgq3AOvfIE92BIzMIfmCgR7z6uy2evKZPBN9WpsbTg0xpoM4FOeoRnJFfJyk51ItNjwz%2FSSGWWBmnlu400IyV8mQ2TfVpYbdIOLv0U4izglBEyGVsKT1Adx9g6tIa%2BFbB3s5XN6j5iGCFBXOkzy%2FOEn0zgY%2FUnE%2FcTdN7C3pheNUdPDj3LgTwNnat7WxHNpp4jL7AwEP8ehBXinmT6L7Hir5n90FxAbgiMES7qxSxiveQboLzUwJnA4%2BSNIbVTSmtNlDGbPN%2ByLwn2FlCX0WVpHKInAUOLB3emcRJUxe6PpP2yJbywbSp9r%2B7JBWQm1vsVy1WrXXfzf3xC%2BtJ87VOHnIRP90sVCqb0VC0mYRWLoKR6nSs1jRe5TTP3ieajI5IqvBYLU45DKBpCs72oKBeOJOkDZFvnQpAHOnpA73UALk9n95EL5xHI45R%2B%2BjKq3ImB19jjukTu4zC8B3BzF%2F%2Fvymx0ji0JZdyYOK3Ds8YCc3PPYAtY7a5ec7sqc%2BpuYS%2FUEzU5u%2BapCh%2FRnv%2FXrcpL0TIQccIrmIlHgp7LztuSCAXrtBNrDwQ5ufeA4SumnQ%2FrZ3YrzbErZYXIwEjY9VgBzskZ4nJnwmzF1R2mD24FieqsZf0EGgh2%2Bzj1XJxHtbDC676PJBjqkAfC%2BOVfsPlMWyQdimF78Zx8GYy8%2B4pcOnCZFXpiwxAv%2F9Op4ukmvKBips2NOMBbpafQ4A20JGUYCI%2BS28jNUSfXIBxaUzQ2U1AfeSN7asCNFL6gTr%2FFpL%2BD%2BN3Muv7vqLiZ%2B74EEJ8kRXK70fdfO%2FIwncgdqrirhUGXBp5kYOtdA%2FNH3pjkHt6rtUs%2F6yTJsVE2zD8FlTdViJK%2BpOfU9PIIgr1Cn&X-Amz-Signature=541fa1b7f0f9849424349841b88bfb991aa63d0a6ca6d6e0b86150664ceec1e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
