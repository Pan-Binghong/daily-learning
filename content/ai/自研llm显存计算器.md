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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRLARN5G%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD40oqU6iCPuH%2BCq%2FiWTKa6mlmz6PoBX5flvjSjYSNl1QIgEAVGeTdZyG7ftgd7H7P8XY7KWQdQz8mRk%2F6yIDD9MJgq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDHjANnjucstawxMejircA%2Fk96IxyQb%2F8qhoh%2FvlzpI0UIJEC%2FU6KhG3aqaztVLy6qMP9CV4VzsIpdPblTBLXLUq56D03Eli6Y0tMBsu8wksz6mQXx2k3C%2BGR1No31vYvQj3GQHSUdsHjVAxFKy5hyYe3K2pAYjivhNzw%2FkN6XA2g3J7rDh1GAcdNw%2BHsIW8lxv%2BCafMdfH7ooDcz7dZB2BYAZg5TlZCRA3%2BYM0VTF4ekgZxqLWL%2FWdjhiuUZ%2FR%2BHPPJ53Md2OjezxOjxEkVWMhNAajMtaYbvsLq7HetpzMLoOhsLuW4biLDnvnxlItgvjFKHmyK%2FXkX6gfEEG9IVDyzCAk7wJALLqQxGfJuW4O536DDY3u3u61c29qacrzdZNkjoZTzvQ1mnSzXdEbtNbv1V8%2F9XFTc2c4PNz0%2FsnV2Au%2FA8d3wZCrL%2BJ6I2CCZoPFEoVAAs15yXD8qlXDb5BrjwcAPJzgfLjBnz9R88nDwjCJV0JrBG0CyfOBmm9Kw6ziQ%2B%2Fe9zMdoQMofdgi1YR03AyInAOjx6SoV8%2BpHGwdV%2FsXXuJK8gKLVGB1rEvog5UDhQMWvc5JudmS7AbSkrYLQ0oY7WXumUROws3jbY0x7ktAlLJuGb5SigS%2BRA6%2FEf%2B6KW8tB8Fgb5DuFQMKmuvc4GOqUBn0zwQKj7YOJq3Y7%2FUUcsYB5m5hCMs2JA8IyUYrrV6Z1mR0eGt9cnmYxbU2n7g1t%2FAPxr87N%2Bc2gD3jw12t%2FgMBxfCpfD%2F%2F53C7BkOyUkOmSGNCI0tOeZvc0igLu8Jag3lkTZ0UiSWHj0hdhI%2BH7S17T32G3NIvoR%2FnL0lmj1uYXJzhpC%2BobjKlick2PT7XTKHO4sjGV%2F1Fa4Ie%2BW0YpNfPoI7l0F&X-Amz-Signature=8a9b6af41a2d2a5743e041280ebe3dc715d60379455925069a86d063a37d3098&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
