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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TXKNCFWZ%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID8OMwQRw1NsHxpVLO%2FGlzing2ptmsgHFnZal7Cr4NMWAiEA8SSnDXzh6a38wEX4A6WDIpL6Ll3IDEtW8vP2h8IlLxsqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGYrBu%2BafrmTA1t2pyrcA3vZsus9HMOp8Kh%2F07hI0xC29NgFf4zJwABPzkcSsrCE4thSMnzqHyMfJvnPnnRlqePDr%2FvGaxM4ln3GshEK0lPO0Kr5Wq%2FgfE%2BpL0KVhSebn6aBWr5eCog%2BzmLDnA0l4UwLQ%2B0TPw3snzvLemqoEOOj8u5Z6HEQvd%2BwCHVW2dUidW2vmEYBivsUPoVUg%2B2fz5mNABv2J7H5vDqlwSCa7EElhd6aj0U2ldCHSsb0B3m0%2FR547syB0q2NrDtYzAfX7QmIWsiGBCkSY8gG%2BQTykVXf0muDDMxv8b6heZHw3VEgvHcw1TrJV4g0ItQkgYDkVc2PM4gT4VVhvDFR9j3SuuR1FsXRWu1tj%2B6jEHmUtuXuJ4mkgGhFy8%2FH%2FNIkAvXsJrxFk11XXIW0Kx0%2BtVKLjjqkBiRuQreieV2PQO4IxDyn9NRmWQ%2Br9de4QjtUCxc0cRx7gHs4pBohHQwkdP%2BlApAeNNUSuCcWg6KkYOZTMI%2Bxjq3G3YF3%2FnJ9AAeUxTi2f1ufjOi5Ut8qHs9kBhbluY4EiAhb5qg642gK8uZlNz3XrE2ciwGbLRDybrJZ7HanHpTOpkCuPc6Z8m8ADItfPqt8znd3eM%2Bk8W40qsU9QPBpCywO5LkLb%2FaDGB11MObhnskGOqUBrNpUyxiyZAWE0ejieA97RacVGEai2Eia%2FNq1oFhF1bzx6cR0fka0tIWovf6d9LTQWNFcC7WMDDobO5hUQ%2BIp511yuDHSjE1ZrDyzyqDAMFlni8EACAMj%2BtHR1MxSBxMmmtb2robTOreyDzJe6%2FcIdlQ%2Bh4Fz6RRWBU7cBWIFogTst%2B%2BcwK2Xd8NwJL60cJLlYOI5Z6KishhxhUO3fKbok2w%2Fdcms&X-Amz-Signature=bb7ca0f72ec4b2612cc324e0d837b6d66a3eb3caf8f66e6930d59ee2f29e9f09&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
