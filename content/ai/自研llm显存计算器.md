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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666THZYE5U%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033008Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIErGxiHTdxfFbRbsYwCAa0%2BtebAbwwAGcsLOqeN9MZxIAiEA0SAHY95CVd2iXKsEPO2hzdYXQhdEcaIi6p%2BkKs48bHEqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA1qkc03oDoet2a%2ByircA7AbzugGvM1MzwS0SPaABmEWZjOnOdebeHKplM3lLgcOFe0CGoGxF95A%2B3TLNRlOCTOBKZzctHCmccG80no4Tm3MsaEdSacR4rfGoJA81oozP6cWWoDWOJlUa3LBDgU0Dn576Kov4GOFK3EH3HdniARBb4Vthtvd5dnmqR%2B7OhsGRNFXL9d%2FfZMAPIZ%2BgntA8OIbZKsH78Fn4HT3iC69Fu6khDLavc%2BvAa8Zpzqf7AJ79xr%2Bkuy7PuO4cp4B2SwQQVRvgRamHF8n51E5rDD%2F%2B9rc5FvnemAmDa94kdOKKlTw2KvlcE4afbVncMHKBUVZRbopL9wTOPxR85Fk58pxQQMc98PTxt9Mkc6fAPpy1BpLag%2BM0P0XLPswDIDhEfdLBqNRc%2Bmp6OaXCX4ftbObmr2j5Pbd%2Bu7czuWA3brl6LZz0ekCHZ2kJhTHP4jx6eWU6O6b4JvMYv6tdT4mQGUXq%2BQw%2Fs%2BSglO%2BvSNjaWjzEaQXtKa628ZPrUgWof4aTUrB%2BY0bz6HrULq5a26bMAnh2WLDDiCWeylMj5O3iU%2BHW86J9PKlQtBkUQTTgY4Ga5dOYT5rjGuCIVI0gEh6ghPCPKGnlw2EmpZGKkXLISfZfYdLq7ua%2Fp9UUaQHmRD4MNfgo80GOqUBGGaOutaTlGn89ABTszYok9r1AyyJSWMqF94l94D8d6Sm3cUzJInQaOndhLvs3mBWkRcvrKKuXqdJ5GJGVJPO0l5y7dGU9zbfBcQzCOAEQsxlf3rIxkV9oammMds%2F0BpEZqSFV7ccHCBfLOUFzVqY0lfXNK9yIOHEiKL7c%2BR%2F3aPXN60dGjUs%2BMw5XG5v%2FfPBrRlfoK2mafyvl2PdeN9xNtvvV6w%2F&X-Amz-Signature=24af889744030bdc5b7ff76e00525b780cb52eaca945575c99b97082ddb73fc3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
