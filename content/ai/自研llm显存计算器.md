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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYV63EN3%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T082121Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQDilBO9r5Z6OWPRlTV05r%2BTJigbAUtI9eCHrCbF9v3KSgIhAKRQcRCcmya8Ph8QWE3QW%2FRHqg6RUIGIfUOVDZmAkDPBKv8DCAkQABoMNjM3NDIzMTgzODA1IgxvyBe2%2BitnLc0qCNsq3AOjIhIpVPViKDyNgmgcw%2BZFpbELX9CB%2BjEHWDGFnzgkj0eQZvv4s27NFk%2Fybwk%2BuYgiJl7l8VeD6NKUgTNIDVTi9RQtP%2BWiFi8c5ncg9bSvI1tCTRSlzZVDLIZMutLG7AO0%2FZBpCYT%2FktIO6C0GSWSr6jbMfFC1DIugHVd6amjxJlbOO906xAGkvYabC%2FWoEJPwLpr%2Bnpl47rLJjQshf%2Fw%2B%2FluRNms%2FINVnd%2BhE9UsMr1rb7%2Bx%2FxmtVjGp6cHVhmhkGgFt7F1Wh5iGJ5FA%2Fi09S2KfQ07kCCW0HI8gEO30lffyX1RBxps6JGWogcWaQcAYHa9iMQM6uPdXY52Ztyfpwx768CNytkj8mEtDYbZBneSFyhFqKKeccmHhIM010L9zqqqFN6OAt6AtqhjxGK7T9S5XFkzmIVlfwueVq8O8bZYQWyjK%2BBW1kZlyjMe6rgMVbF5UtjjTqweWIGZQ8EIbEOVKXl2D70rQM9eZk9auyZ3txxZOw78MOf4TjgF%2B1GYssQxMg6k0LY9HqAQ7UszF1Yhhs17hEJJE1UyWoYOpX46%2B4mQTH5teWaDgAY74IK4y4NwWlnjX3RGQ9QMq%2BYcneTiCULp79KPmfn2rRAuHuJ5KCsMmR70QtctDCHTDvm8zPBjqkAWZsXechmmv0y7jqvKnQdqKvqfnN5Wd4Ba4jetWLul4CWUGzbB5vvjApgSoIb6bjcnAvyae3xo8GNiftvy57aVJCpndIX8iJd1wK3CIbYUNOWMnbu3O28PIoamKg%2BJjNkhIhR70tXJOTFRgkV0kpLh2k2o42CynI8MPCRod98uN1hHVHQZEKT6ondYP42f7CNQCwWc4wh7cuc6gO4Wx3wl%2BAcr3c&X-Amz-Signature=3a9e4d361c5a8cd9333a6250d728965d14d4e2582220702a4c7adf92b2e50637&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
