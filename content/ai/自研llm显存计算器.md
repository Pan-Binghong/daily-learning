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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIDZBRZF%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033106Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIBvVNFbPQM%2BYfBJSM%2FSdBavWCa2oLllXkJ%2Bv7WrmtZ%2FEAiEA6rjE6JBDWj%2B80%2FWPdCTVeC4%2BtBrYFAaiTgpJEBfFOu0q%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDIMJv3gNwwzlworVQCrcA%2BxJb3JW3gxP9%2F%2BRSCGCE%2FIqfFTdqJLMhJU5hYTXw1Ta3Cf55fWfw2rXnSFlT4hybsUfS8T6%2BHxZE%2BvjF2SqfZ2IsfN5XFpJuA7rIFk8nZayvxmTNyWdTEazMw25MJkQr7KBvhTveVc9cQ2tGsdgSUpn5RQqCdqmDndhsK%2BtgkcBaedO8MrlDZpoz3siUIu%2FrxyHI1g3O4w%2BcfoJTqqZiroxOmmpeScEi8cVXU2jatFge2DsRgIwr8UJ5Lxv3eU31VaLoKEYldH6EStH74E%2BU3x4nWPgBP342V1Ewx1To%2B%2FuYesTWsDP5EoLcUpN%2FA9RLMB77kCtRYBB2wOrd023wBAiwdRMC30QTUdvrJZF8bLA1egebQsoXbYxLmmXCxkrAhPdPjV0zd9k13KpR8BRXO%2FR%2ByjHnABoBSXL3yR8RuppznKQ%2FgMyf5vI3AbE8BE80edxNue8OIAq8jU2EXU2G6pN8Q8qvnn%2Bo4qL9COekTGBg%2Bk%2Bg8S2ugRXcD2HPsgURFeTb6H8EWZHlZ8GjJTNrBKFcTtwH6V%2FWZw9K1Brgty5ibpLKbvrmDYr8DLBqBBTwGzSTeu7WUU6mFw3ENfTenr2c5hHbe11La4f52Pp%2Bt5IxODfUKiwSSNsoaNqMPaFhM0GOqUBn28O2c3kZIgChzESKOwn6ArSQMuRgef43zlSeQXwqAptYcaZSO26FQ2AgFrGoV6z2E6IAbijIP2cZmKANNJu6nipXeNPQh1cpZIm5BmMCRV8a8MHdSeifZfXswxCb1nQ6U%2BEduZqwYFkD72WvTGT%2Fk4oI99EGzSMYPuEtZmrZy3QjIfc%2FxPejaUoLIsdTQWPOM%2FMVn5ItDILft38Fj4l8odXQ6ur&X-Amz-Signature=ff46921698cbb401d0e4e1c5d7e21eeaa82b182bd94cd70beb31963b5918be61&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
