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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RURPE4VU%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJIMEYCIQCqE8EFtf6dcTmiMlVq8X4sPQRWpazx8dSKJXXj4yEw2wIhAKpDHFtM5e0iPPdrQPQZG%2BDTGSpCXVYD4Q%2FCn48nLaDbKogECOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxBwXMgR3qotagOfzwq3AOtDslpOCkW5R5gGeznnzZfui%2Bx7EPNsvq%2Fd%2F6nbCoUCFYbJnHMKuIyUMaeWCdGZ%2BUtq8MUvDhfdxaTnl8fHwas6BxsH7Z41shp05bwVwuK9%2FEiBFcUTSoScbIda36u7j8R%2BsFI%2Flaet6L42%2B7QAeQqvORDpmzNY7qjiixpX%2BwxCMSKcb6wqagGNdyEdxhNgaARQgoyg7F%2FJRGaDy4oNRKoTqRFWtdztYbW6RJQowMeMc06KTVMhVZs9DCAFKp8K0lPXcOt0gjbXhx0IIZzHFfYqsnx8vS45iyGNCme7mfc1hQ36C0CJi6p31oIoV0Z3iE7%2BT5k64PxnxQDefCVtXzSW%2FESsnDA9YrO6dQds9akUvbsCOKes652TmYHBpdW6%2BWcFxAIzUBtpVdyBbJIYvD%2BP03RGD4Fegtn%2BgxxUpm2h9jhJ08uhGo5ELQFzVIGofCUgwy%2FnnDRH0pmVPLj0IaGeX%2FElxPV1Z9iuHYC3K3FepSViz7EbZMNqcK63htlDC5uYF8YVJFVt3E5FNcmKtld6l8WTJHmhtg%2FAyhNrbNjb89FcHwKPgodVP7uGQRss%2FlqxUli5lyyce%2BmqtAIImrI20Ffqegy%2BoZdMn1NXfMrXJVIWNfBN%2BVbKkwXrTCOr8vLBjqkAfgW3C01u3NVFK7lbGcemWxaGvrBPc7%2Fjfdk5nYdu5Stl8MhPsGPfZqKjqt1StpkknZPDhink3vdX58aD14a8ZgZJTucmrOD2ExeSBluBLMatVl%2F3zp6oY2fkZqDAeOCbdY5KrNOOJVsEoPAc8TVPd45EzL%2BvwxEaDsTr0%2F5qn%2FLqQtH7WX%2BZti%2FJOPcfWudQWEHX9xZ7ltmmObsgm7q4E8mbFLz&X-Amz-Signature=d8a05e46254709deb509c4f66cc01c1a50fe25e03f74a1d8ac31a3c530ee974b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
