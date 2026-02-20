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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJA53KXZ%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDlD0n7pxIaNk%2FG8oLRVb00loeEowFrB5g9xEIsqJAkqAIhANwVoLXiW0X2liDZ%2ByyqOFHwJD7YmVAQPNXaDmOKGEoxKogECIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxx2SHmdYzWPjBZn%2Bcq3ANDeNLnL9VAq%2B4pQq2gm6waDkSRNuSRG435u1EwRORyHadvl%2FYY2cjiKzm6OqK%2BcdxXDph3gCynhJtPGghFSgYYcudLNRlDwcHxswbcjbC1wS8pNwt2U73kGXD6wvX7wQeEnTYB2YA0WVQnkPGKTLadCjtK2bIPQerKFxn0umojWaYjCi%2FB6J%2FyUbEL3R1vmBkSyvYFe7nfmmIF9VJBesT911Wh6zlzMnDqgUW49HQ2KKNqnfHQx4Gp2hQsA%2FzCR%2FF%2BN0L39ZFPbAuaZWvzS0iAVBgsYStqzOGyaEMvEBzN%2BwuyZeS9tke3tzw0eUvWwz8svrGvmnBc93YjVy4%2FVVh21IG%2FmoOYzflucdjdxWtZj4xfpCs%2ByAU9VJXcOd%2FOQlAZmR9KwwhjMKPc%2FDRhP871p5UHb7ai0adG7f8eaAdLkByclDL8%2Fsm84mTBBx6kAm2kLYMQDvTEwJSD%2FbYIPZu1%2FredbTJpWBBBsKYAnivEOgLsjiy8ptJpbKvlb6sJj8zImAIMyDy63JdrLh%2BtgN9wM1rPCvrVWoaD2G2kcNys7Yz6QLrSjDsKHXEoSsQsFsmJt1KxBq56NIpM2y%2BrOmifL%2BDxu4ZSFMabS3gCGcmXRIsJVhmZCyvWfsZDCTDKkd%2FMBjqkAYF%2FujOdaHbADAxPJbxHoJTim6kxNfR5qzNtY1L%2FiiY9jpJw%2FYyFoxVvGuuoTcxhKKuiUwjtC84ZXCOqZ7HP1D5j7jVpbCHa%2BraRhem7BBkEsG8djrG8HW%2FhFZbc9Jrh0dhVfkajm%2BjIPM%2FqfVcfF5U7rOHHTwjT1nD3wRKmcIgr%2FYI%2BtcBD9LsuWIYJZN7R6KVgdjsjQ7k7w4F48SXE73u0CnX9&X-Amz-Signature=ae04936146d60ee21b83341f308a561ce57754d5e7303e44a6cf6932654cc2ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
