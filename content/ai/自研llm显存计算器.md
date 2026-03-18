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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMVYRVR3%2F20260318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260318T034207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJGMEQCIH0lxBb%2FnvfEuzD2K3A3LW4b6eYA8fTx%2FgYW20dBOvr5AiB6hSK1WEoX3JNMXRAYa2JUw7g%2BtBdrQ62%2F%2FuATKLRjXiqIBAj8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMA4RqxWUPqAUs8T%2FPKtwDB4OWd1GCiG2qIcLfdsaMKv%2B0QaNwgVaZuWUaJCqJaJgS9JNwcNFFgr1ozVVN1vaFDzZYZtx6J4rJluHslR6ZO9PIwYFZIY8MDR3atvqzGJe%2FQaKrb3TU1IClWQVHZngKuBMdgJdGgkZbuNcge8h4heujhVgnu0DZkPFKP3klNbDA%2B8pbRgoAQOf58Gp%2B3QY%2BeQmkVYaOfSJbVA0OfUwWfGkU06QaFiCo25HN%2FIiaiFFSB5myxCYNnPk9RwvpxmpHOdiDcUsATwhwnoeKtt01w5bKKoHRRzHtGX1gc%2B3zjeF9gmR1w%2F7jtzhZY%2BzIkqaRHVtoJPdl5URjhv%2Fb417U99XMyT1jtVhz3Kta7UteE9LcZbRf16rDYApYxk2s6qxWp4PNNftkOBm8ztlcd4wW2Nj3YUPr%2FjXr5XowrFCWi8poKwTbKQzy6eA4vy42TG0qqLWq07TdSZKW5YXV9xeL3JPyBNIa7E8LZd6oLcqpsnrORqhPzkx0Y8zw%2FwDl3KMs%2B9HcGVyGPgC2zVstRuD5j2tlLexDNLSiss8OvNozw%2BnKSel85q9f4Y1oIBckDZ4vGHqs5BYfR28btAGcch8PnzGi%2FXshbsRPXDds6dejOpI82dYC5PfIDw21fdQwi6fozQY6pgGBBkSHdAUvYO5bAVChkkYSbJMJS5HtE2Sx1wFVOfPEg4rWvW3rvmNb5NJs9TKll4H7oE2DvyTtzrmNSaCGJuYjS792AqE%2BiDbXH1yRPvMFFxeGpCuIKl8ufO%2FQ6e8U3epp2xD8zTbXkWRSnDX0Y%2BZ2jjttl0oVeng%2BkItr%2FLJbe0eQXdzjugxFfMx%2BxCiR4AYPjTcCRFXQ4TorPo96aC%2BwU7qQ0Yns&X-Amz-Signature=3518fdfae407c4d32da1e90a61e6c0be6552239b43b3d1c19a393f6d491025bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
