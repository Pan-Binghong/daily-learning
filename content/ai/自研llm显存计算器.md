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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666K3WDIKM%2F20251221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251221T025940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJIMEYCIQCEy7M58yzKurarXd%2FCLLX4J%2F4qVw%2BzVW0bzFF%2B5AiLYAIhALXlm9MydOHRfnuQxMOcB0xpLF3GPslR%2F4R6Q4YmJMBpKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy5nyvod5%2BWGlaKGOwq3AONsqaccoAzHKOMNSu0dHMkr4OGxk9KNaluRaIWgSMoMZp%2FUOUOkGZS3dy%2Bw462mAwwiV2XacTGKJiDOmtAZDiX05UctrusJzd3EhxlfPZUtERQKLNsd%2BlnHEyye2YM7D3iJ9i6UEl5k5CLqYNYVFC8yK3bxqS0xmDmEYDlodsgb4RlU6v1xPS0y7KqLVLHadnunEN4dzhcrQIcemRiDifnzRTsJW9tth6Si3EYUTQJPBKStc%2BGHKEAO46Z3vGan7Hwrx31IowmRlUmFxJqESZyfQN01ySLnCQ5c1wWEeBxsXCVARSqZqfnkRMUiXYN4pORSsDbUeVuC1RQy%2Fp7MoqfQOIpsLroOHqopPV7tW8%2FWL4WF9iiekDBBOkf5I52yI64ljqr%2BQdtqUSzSm0Y%2FrWTOokMFOKG8wLifMidPnFdW4NKi6va7uO0jxmrRzqD6nRm58fYNtRkdEeJ1R53AtyWSf8o6nO9fAQMREY4BYqwx%2FKh45c7Eru0k1PEnqSSMQ5T4TxuF14Ha9yGD%2BbeTADFvxW6Kt66PN%2Bd77sVTwOonuInXgCGczZLsbFl%2FTABnEcJVij%2FkUgqzPEZuJ%2BfYq%2BTZoMw3P1SiRU4eVorjP%2B3Fo%2FKkXzkxUGoLItRXDCT%2BJzKBjqkAcQbOTsEZeYHcw443Gs7yEJbpyIXaeSsaQL3%2FcDrC5%2FM%2B5ivzMBOybN098bH0cFd2CYOFGowE0Y1VwswjPihj0CBupANELNt1wcDrJAV9hpkwEKl8X2oOiwRbLxlb0ySuzPyYNT7Q8PmS%2Bos1JWxCnqzDHE7wHpQNGpavHsA3QZ%2BdOIAKTws4IO%2BF1i%2BQ%2FNeqeF9ctiCKcgWD%2FbjP4TIE6Q8h%2FeD&X-Amz-Signature=e0f613308b8bcd7ed82e20342c5b5ffc019d950e2a24733b9f797ebd10a3bc78&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
