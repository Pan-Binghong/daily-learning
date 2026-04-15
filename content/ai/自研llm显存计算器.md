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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPJFD7S3%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T040937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA7XgfrzaODddc%2BSbRU2tlgZxSK7ngVet5UIN8%2FFtKnHAiEAzTF71xAEaLkpLGwYyKD1ZFU97YcxbqPesoR6rJ2clhYqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFqV8jOBrv5jElEyoyrcAz435JgpN4dDGRUGSf4m0%2ByYlEjE8uzLaKrs%2BiQv330f1fjrAV43ZauIaTplvw4foGOq%2FJyL1ir8XDM302m10%2FNstzl0LRuIVrYUPKWDG49c7xcTQzeJ5OzKYQOWSOohO7IkC1fCEiW5k49KrflZdfCv4heBvr7WGN9hG4TQpf2yqt9Nvh0TV1PC2GE1yiHg77WLDenP3XIapr%2BRGfAGvwSe1sFXQc1uV0inkWe5C9CkDlKPwA6PSwp6CbixwAUL4ygz96g6r306ihWu9c0D%2Fk63hof6W5dtMGbchsD5LopotpF3pOb4kv1pMOXtsAA6xbhk5Y%2Boznz%2BsOS5d5vvJYsM00wqMOoy1tWmm3721uAxOhc%2BpJ%2F62EVQc2m%2F%2F0j3f5sLG%2F%2BNEhT6L%2BNjdvJ2wIVAen%2Bx%2BB4lAimlcm12OKgk2NZWcIbOW3y1UAedUz3QMXzXOmUa33HJS9K1rBvJC6A0lDqX8isJt1A6GXUF12vCCiyTNyJInTAErf33E%2FLyIvySjdUy36lPmrHQZrUWr6PjaZwatjFvxAgIVrPIjbte2q97Ol9W%2BFv7N9W84i2vR49opMy8ADUAK5nrgSHrk16h35mJcJJo2t6W7ZJjgvF6LUoTr88cHIJ4qlE4MMiU%2FM4GOqUBQmLkvYyRQXR9WdhF7zFspciA04wbxWCL0DBhTimn7ocXQdgqQMGsMIOZIEsmcOr0uLEbXWCTss5Umw%2BTKibXCGSkHFa4cWDZcfUjJHLSykDipNOV%2FUCTUfE8hjcExji47lec0r9Un1k6DpfeTJ8KLvWw2XY%2BUdBodJKg6M3QiNwNwyuTSPpJhOs9TXu5WmrX4FGyDG%2BmoFTQAbA0ApPm5ayCszxU&X-Amz-Signature=f52ff2a48b9abe43ed44762d8db5167741f274ad96fcca751361a2023ba074ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
