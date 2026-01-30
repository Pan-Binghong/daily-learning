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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOY7MFI5%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T032841Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCPcLvCmMNSa4SbRUYW0nIs6Kzsu3iHVchE2hBc%2B2BJQgIgUiJQcS1BT6CRo2xq%2FlK2mGcGhyRnt1WRdOMTNMxtVZEqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJnVBsryG1QE2NgPfyrcA1GWbwI0%2FuXMzTdqpIQaGl7lHV6SBTdZhLI7Ao9xPjwczRPlNt7vZFoIUP7wBVT%2Fv8upqZOoIKovC5OTc1pKMuoN5YTzBIVS3m%2F9oIBBua5c2dLkdqxO%2BardUL7jFqzdoSQWlktVaQFkux52rmXZZ34z%2Ba46jWwohBJavXtYaRCosePdWalZJvHTuDVYo9dPA1KBxZxLFgE9N0PNqOG8ncREPmSdyR35vmZvyEGTwwYu713NLJPzpCxUHJiwHngytkQQabahi0rpU77UNlaIiwqzuwk%2BmwnwcnIsOcSBexrjYuZ9K4fi2CysASQAe89PtxxJy3Ef9ipAOoFSFQRCCt%2F8hVEOOxOltAG2RN4BEBD8Yi6JwWEpLeQM8xbka0l8JYfKd%2FVwEKivuXQzNdkUhqZ6eTnWRRDWX7A7chaV3Nnco99PoQsHmCaqrCaq3g5s%2FTR%2BmTHaQwBTjkpPIXYmcR4YzfDDytw0BqrDcdkD6w5pzUjliMcv0lijmJ%2F5wbqDnUAuZXbs2SmgwVadYizGAHdl9wk3RCw6Y3hqPYlUKJW7rDCpkiohzQr%2BJDeM2qiRtzJaoWQXIhc9tP7NyGbVpf7v1Y%2FFbtyp1VPuNFswvf2vDmL63vHWgDat6Pc5MLvI8MsGOqUBDJyELACQ7aq96FjaZ8f2zKLtMUbgXnPKbWxrysbBiMzTu%2Bqdq%2B3CGY%2BrX29AwzwGcqEQ8CqFwVZmFK5kaEueBVOiiGrxFQYjVcH3UvjRtzI4cVzGn7lnPAUVL3B7qkTOWFgF%2FbTnf9NYEr6ObZ6WWDuKI5h9VkaNb1G56Umu88Bck5KxGE%2BacPv%2BQtxPJHto0NWhIjfFnU1L4LJn1KmYMrwJj9c8&X-Amz-Signature=4191337bbe5b58bf6acb2d4fa5a09bec53b47d4c7c5120dec425ddcb82484a4a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
