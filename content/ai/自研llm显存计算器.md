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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MAGD4AF%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025202Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDh60ORsV26MDEWJJ4vTuBwVz4vwoFqokPOxaU9oDLNJQIhAMycccTg4uX0y8jIBFYr8wJz1i0DPq8GIAnO7yQo%2FyUXKv8DCFsQABoMNjM3NDIzMTgzODA1IgyyyxPq11WyJYmTFIgq3AOKa9Gu8abQVNju1jRHzW5pQkBAtMSvoGWxDaGcVT8QaRRu8J2nSlMG8q4jfuCkQYzSCa42rASW6%2Ft2lx1MJscRs%2FWY4VGSC6y%2FF8APUNNYDJnQxLYSMZH0j9PWkTMIPrqvcHlkI49qgOJpr3BEVLZQKtFpNYYlZv66s57ILE0b8haFYMtKtmhM8LxxSyNIDLU8pyWSUyoEe%2BF79%2BXGFaFLwNG7ljj1OK1IphDskYIb33mS5tlXMRedl3NvMQvYm6%2FXEoJSYnNP1Rw%2FsDgSDNiyFvXQprEo3MQChsmZc2AJY3zne9kmY0iZO2X8BAods3cgEiG3loJf4XqaR1GNALtkIor4nuw2JgwJFXCe1CQzHVrOE3Nyg5tEPcs33vYbpFUmZdPuJBiBy%2FN528esj7azWeldLb3QbhHL6GjW58NivgxmANYpSq5h5QrCMSojWh9123h8KxFCVlj5aHTwpyMmbhMnKy51ffuhwfx85pVjjedjbXgvkIXYTCpLogtFqZY0sflIl9nehFzUQpR1todkz8794T%2Fq34dutjynZMR%2FHB4U4hVDW9KNGGkzSZcjbfwL8PiQoHVsH4iQ5cSYredgej2sjN5sRppysaN%2F27csdKz8y2hs0Yqm0OwS%2FDD30avLBjqkAU%2FnZorExyIsavSgj959WAKsM0zmy60GUKvgzf%2BTwFAwqHV8tArvIxzfd1s1EqZOMXLJ7tmO4fqWn8ws8qToMRG%2BXirbo1WEcdqmPJr3nlQyOSzaFwHxDw4hv%2Bbb2gtb8IVeJoF8AHPI2zpEKzby%2Bg0BDLJNeDtlSba4%2BMZZgFEseHkN1Mk9i3ekGsxYqQjB8HJ6f0bQidhfYD2SVNd5KQ%2FTwB3b&X-Amz-Signature=a5e8ef6ee413e291b8360fcf40069304f4d64e98f006d24f69c85856f60875e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
