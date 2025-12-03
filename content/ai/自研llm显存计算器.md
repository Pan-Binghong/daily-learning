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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXUZXJTY%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T024815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJHMEUCICssT3OsBAc1umdIJfSdSZ7M9CjWuQgQ8uRofdai4iLaAiEA6DwOP108F6pmejg1ZV5mUrz%2B93eezCsK4%2BwGbVHKouYq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDAAgnlqtu%2BxqoRiDwSrcAwS0QaSlsTdsiTWAVScKkSJ1CJ%2BAxBHA4dI6u8orJbowgXe48UVltzZwT7LBGGIEvBISdd48P0%2F0iWn72TbPXSmKy9CHrRXjZHSMmrGRNqVBI33P9dJzsY2jwRlAfP0LpskVpPcFOrhTcYyXQYQFJy3K75%2FsJbXq%2Bg5ncrep8HldfktsLUgbWmhsUwBC%2BVQ2zHM0wGKkW5YYbtEE1OR%2FUK4svHZg5d9npPXniqTA6fJBXt3m%2BolHN8ctPn9OVEDtjKvMw%2BqzznvqNLYlviIL77GW5P4wuJl%2Fc5QM9brjREcSdKyUH%2B5nliNeUk%2FyJ5DXFVaeYUW%2BoTy7Gj%2BE331vUZ3uHfR%2BOm9xXeOyRxiP8bPzoymPaDkDrqeOuiNXxEKQF9B4iedm2mSoOxMnPxV7wUsdnBr10crtVFYyDE6lkifVV1RZ6ycqeuYay3uhqwOi0U8YZ%2B6fgnDoz6pQ%2BWMom%2B2%2B5DTOt3vJBWZxERlDRXU4BXm18Gi52LvVwcDCTHGkPgpzGQYjGrdtr3FrJqPtIXjQoEmAGlhOhJLLBlU5UwyQiRmWdRXy2AoQXpIW4wTQyu6IXKsKbNBAEjLHASVuhs7zSMEEUOEVJPjAG0gS3nWI6s0SLEsbmW%2Fntyy2MNeWvskGOqUBjGTFaWPE3ucBcLRV1s4dVduRn0ha2IABW2YH1OSiS7eTxkxQfXM7wPQ4JphL58DoloUPwR3bqxCMxdFj64K0gVygXIw69xHrypvMdaLVh%2FlWXfSGDNQzNflp%2FaOMQkm7SvH%2BzDyPfmvdQsW7rN6yykns39%2FYtvnuKQ3Z4vtT38RvE1HhA%2BdC83cWU1GIf0%2FdurqB3x2HN0sJ7lofMng478fQ7OtE&X-Amz-Signature=8bd2316f4c048c0ffba6d09f5cfd89d3b81a543e3410204c81ad50ff2bb3ba1c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
