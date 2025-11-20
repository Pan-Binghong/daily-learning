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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4RSDSXE%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJIMEYCIQCUx4v4ew4MRFvof5Rgbm5Em6tVICbD0augRlNESoIPFAIhAIpNSeZq2IDoMG8H5qFTlEr%2FpTuo33W7VfprVxCPSriIKogECOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw76wB6Oy3Au9jrlYEq3AOpYFAxlxYCBAsWH%2F%2BLU%2B4caXYCtnGeaCVTilaP5Em2E2K8Bu2PShhB8f0w8LvNzoirxtPr2Id3EQCkSzy2kW3IoJV9HQpyCtgKgTrYdzBrbjARSAPsWtgdxkgeNJ2S75wES%2Fni6hxxo5ClVFVue3tMYN51DYCVlMOIOdBwuNa7D9300valLjzmozbPkNSqlLIyX5eZMrBtuIyEC3sIv%2BjqE7RnjzzDhRkACxh1WijFkQ%2FhXgIDcM5kYVGOl0QGU0tvrOud6kbyGTQ9%2BKopQA%2BbxcdDihcvX%2FO1hZVN1oY3WEKpT5N7%2FijYakzXFz%2B9SjogV2Ve0fW7dVJy3yJQGgzKSbQOO%2Bc6YTM8jbarwPKbu0Fd8gKD%2FC9pLDqGMdZzkj4%2F8iVfpqqye5Gp70T2SGKuRVJ2LKj%2BKanNeTtsUitIwZh9cE%2F5lPYhxUg8TbI%2B8VuUhsIE0UKNPAuCOQWH9ADjzOT%2FfyNQFwpg%2BzoeXBQfZuKAvYKVPoT6dZft53%2BPyvJlB70nj9MYcb36KnJVcXUJgryfUbI%2Bsp1mDwC3DV9kxTCbIBV37OSXIc6QODUl%2FD%2BFFYygyNpSl5NhAl6t43uHdeac7Un00ATXqGizbBwXwsg9CPf7rXWXBMZSizDN6%2FnIBjqkAcMGwG38EBnXUCbNxDyIR4Vd97GRVnG5LZBPSwpgiUfpS4CRE3Hx03bu0akxjfqL3XDQDBvCJQpIzp42ANiONhw%2FKK6u7%2BN7j6WFjR9AcNdLi9AIPbiqexJvGTn2ZiaOjZ3NHZgV%2BprD2V%2FyWRkQWNefBT2qlA7OqamNnXh0mPF1cQ2v6CMfcDbtuh63vXZX%2F0cITeOCk%2Bl5zq57I%2BSGq%2B4VTgS4&X-Amz-Signature=010da802fb8d45704e861d89192c8f344e31d2346a4c9569c64f62484fa37103&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
