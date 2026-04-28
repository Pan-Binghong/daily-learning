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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666S5YZGJU%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T043523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQCA1sDk8Gxzn1VFSt94kns0H9Jlk%2F%2FJpl9lwgkPWmYZ%2BQIgLQkJEbfrTQQotPSLbYH4p0WLKZeYIGjIozOxxN25aJEqiAQI1f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAuSNquvl4EhDvAsLyrcA6%2BjZMjkzAiF%2BfiF1Tdn6G36fkmfG6OHKeFKwzciInjtrhEihghzkHW9gPJd%2FniL1rieDVd1DCymh25u%2BLgHp61rToDNuxwXBbX8RiYk%2B9IEKWEYNilSWkV77qWzwVUWSX4g9Nt6mzwzl%2Bh0kqDz%2Fx3%2F2SQ%2FO8gCJANtxfpfElrkgp7v4SC%2BIDas8HobXbA%2FZ9JQwRRO70UKzaB9%2BHp9yQgYvfHvO5FCKCo95VPMbM9ZKng1u1rVQYn7JXsZfWbx9zmqBQ57IS7Cy5Sb7CHSHQ3OBbWPeq2HXZZz6sQZhk6Fl9GAFc581LaeBBzbX5c7tCTnr1wtSVtHP0fjfg5z6cmNY2RMHhquN%2BdE%2BRPkuD%2FA%2FG9%2BR2pLTg5EUR%2BuP%2B7Weu%2BVVxYqtbHsL7Ivpa07y5wmtRgOQS%2Fz2Qk1lVytImQnsNFcWX0FKnkcNm8%2BbNOzLyoTo6mhuGsKPyaYzlJJv8MDwXQA4jdsBY1yU3wuB7KLWaYkC6C81DvA3neHRiKvK%2FeReGD9mer9%2BFhzDF3ZQWxihPWHMFTg9h7T9h4dmsvbhs%2Bk99POmLAHePbW%2BYsa8VRyceAeM4%2B8XTi63AKCAXDijiuaLXHCDDC26VfwdHJlJkRgeanI74IQvdo5MJPswM8GOqUBO8Q5iaufYCHJYgNSVF2OEt7e%2BbkKvFhhhbIF65r42V1HMpef6BRry4aHvp2hyubrqooTui7o2t8%2F9n1%2FoAnydcHUVmyOs%2BGq2Y6YJZHIQLEBpBG9JVMDQXBeiUYj6i%2FqDWnAOKlCC00bm%2FXzqxu5Ei%2BcThtTU%2FV%2FZDyCDN2iCVwsS2GMsd1m6SL35r73x29EFtTs%2FajKJzNlK9tlGFPGOpoqbLZp&X-Amz-Signature=a5d02cad088354d6733c2b6bc954ec0cda7b6a57b7cb59e3222a12a42c3c7f9c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
