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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJIITXOQ%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCQ%2FozK%2FRhNogwSnIEk3%2FR8e01l9SUiolvaxYa2bk%2B%2FBQIhAKxkbKcN4a%2FdZxcFPDYISBNX3z4Zd32cuZq0lRsYLlxXKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzD3QrSxNL8cZnIODQq3AMSEV7IwdoFtJwcL0zZYJTAliPmq5aWNHkqNKcbit6vznxroZ3ahpFz6o%2FtueuQd7C48ErFA2Br%2FvKNMcpKSxwJqKNTgVi1YLs2Ti7qQV1LBPj2EMme0LKO%2FqzEym7u9rNiABkNMGES4%2Bg1LHbwg5j5qfHDCUphLKWSkct%2BZUMmKmLSIiU3UqREFFEQ5tNQgXenF6JxK3ISOPRRWNvABJwymN4u%2BMbBdHKacDC4dcd58g8tS1%2Fo92k9Aa2i4tQ%2BkMzjGEpfHypHy88vbCcLJq6EjH6i8Rbh2Hudp5lnMgRYvFrzjEBGL7MDnXWg1ydqZAK2bwvkRg4axb5nmFNgEEm3Wg419jDZv7aJwVTq8R%2F25om16OJgYXBlnl%2FmRvJ%2FKUO3Yp1IwLv%2B7ecTpAK5IbXRMhZOFVyMsPn%2BiWPTloAgI9b5IKp1Kx%2F2aiYYrmNam%2FVRboTY9421dHgw7s7C3qIa8ye9jp5K%2BBZt5tExoVw%2BzwYvzj%2BWLTkAtwaQRdXiu6ckAydAouwsAy%2BmPGLai3ItmoiU8LKWcGpM%2FALzSsW58wTyg1Wk70FBgNaR6bhmAceGbyqpbhE5l6E2%2FYs60s1LtMDNeCLC9LnAJdYZwZRtnIrK3UWm0wUAJpvE1TC%2BzOnMBjqkAbrwnqxfxOZiCEyGSQz7ipngSxi2CZFYD4LYhC1PcX4CA5dN36AVgkhUuyoS65P%2F%2BVf1vURNj0awTb1TBvamKVK%2FTpT6XUcCxuo84UvUrJUxVO5ctYW8sUVEyuvNLrT2fBX1XuXmBoHcIXT5A8%2B24EIaKiTZUQ1Szx143vGBwGWzplx5BO8a7YRsUwJaozujOBm13QHNoBTRMikIJ9gdLp2Wi1WG&X-Amz-Signature=5fcd634e8ab97c07e9147aaf35abb9e3f4b49b916bdf6d0ddc77e5513b7bdb71&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
