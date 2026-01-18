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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XBNKJXX%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDVzTmfzJZ%2BsA3BMms2ogl9aRlmsIbRZnBOWbAFZzbrfQIhAP5yD7YZKhE7lqHI4b87xzt%2FmnZud8SjOQFZvcpHc%2FztKv8DCHMQABoMNjM3NDIzMTgzODA1IgyPq1X8%2FHg6POyeOrQq3ANARDt0gKy95yu5xnRgnfP%2FMftQvu1OrwMJiZ3ktP5LmP%2BrZGg%2Fh6P4DOfQq69gyzGHVtSnjCJh8J7B6cjVTPcgNrlufmWni2VK%2BzMk7iupXVa1oemuO40LYrLQcFUk%2FOOCnfYtEB8cLvKfrb2Hs0Zv%2Fkt5EpRSGTnqmwb6fQUm%2BuPDWSSvO5V7vwA1%2B9zca%2B9weCZZgh2aNK%2BGT3KrjbzJI4M8BHJ7j4xjs9bvB006ZijIFj6IHQqGqLCI3ABTXy8aQa%2Bklf62wwjlO0SsQbMDXERqk9O7O8xNmcx%2BasnAN6aKmHAHHlnTgXRFHPtqVjdSJA43FJQc8ROi5VQYlpTtxnX4cARxB%2FRc0WUKQ7r2jr9TKGKoSETwIDInX%2Fg%2FshqJA7yeRRWf62iQhikhvtLZgRLRaYh8jLaE77ENbc%2B33Jv4KcB1jPZGL2OL5lUbuo%2BmdXMhG9RX%2FCkgVplLuKz3ogaEsl3RYihk1dpJytIRo9Q63ZajXMtzm58ZgwrJvo3lsa%2BODsTAzF%2FzVQAwn%2FpTg0Lv1ZnvSOCfGmVJWkRWU37kDBbR2ZQMjodyZcEmejSdwyRGJm%2Be6GW%2BKCOTCZ4mDV6%2BmkkV%2FVWa1gQeY3cj%2BaI7m5N4fWFE%2BxiwmjDxgbHLBjqkAdkGq6qoDTdBPQvahAr61XYCECRj2vdxufENEmR5FIEeRDlCOrfyHJtJMhE7jCoi8wLvYpeB7zx3oKAjC3t8C5I%2BBKJnW2un6txEkYfTiktI%2BzLWD7TDQJcxKU7WcIyFtpyuRtLNL0g0X0FxuroRWBp%2BMhJc1S4Npz5F2Rp8AAFM1gqnvGdDeFAmL8xOwIgsdGylw5aauWebKKu5iqt1ZKtLZuWU&X-Amz-Signature=ad15645d14dc62ac65d4a20a4c4f543e365021473871b035cb3edc222c9efae8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
