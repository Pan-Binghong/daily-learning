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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRFCXXJK%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD814SattVSFfe8kiw92nAbEXa3CGo1%2FCzD2gOqkidJKwIgUcwPh69iiq4O3pbaVmKhRfNgbXz8Hab9QMhq8x86cTEqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGBtD7c2VNAEjw1vHSrcA7mcr0GUdi2c687AQAs0BV9pqafLInn8%2FHPqTc1krt4cn06QfrrbDocnGvO05e4cGgqDBBsDiCXOeXiLxZuFVJYtKpw7wfFtX0%2BQXFWHcy7PwN5hWMQiuylEl6WwBa%2FPpaSkTmjoBvvOUliIIO5p%2Bqq26uyjmF2zNGIpproh3vmAJ%2BixmzMvMHD6XXKHIWaa7KRk12pSJsMqF8p7CFz%2F%2Ff3MFg6r6NM5nJ5UvxojaI57VJNGKT2t4YRbiEhrcpbxrLMVfvQXkzU4IY6kTc%2BkDS1G3CQRYKvgV87XWh0H0OhfrNVrcw9uqaIyVmYQxmEQGU%2B9z44Q1%2BlNQyrop7vd%2FFQRu%2B37MvJ%2BiWrsKD3Xt2FvhPRJCcyTUUuXneVCcklL2Y9b%2FK6PTlWa2IvKVjuwt1tYWyjmJDEEBZE6V1M8lwKunCetlaAKbkmfC74B4F%2FyGhcVaWkqGhSMVHib%2BQ4wmwb7IIAbMAkX4A2DmtQ3Z7SAd481RJvYSgpF25TZHbHFLfk3tyYJJJOFp2IfratduYXyji6xv%2BywJw%2BFbbYQEKKPrNzeMmKmgHhqynfSEGoi7U%2FRi0vH%2BuGReJykvRxy40M4hw0prXWybaoZRgl80xhgJ5sio40b6je2pex5MLqY78gGOqUBQXI7JFWw3WiV3VDg5RM237Ljn0c5sjTf6HPLvOh29HYaN59fpcafHT8igO%2Bt87q6TW7GT1tgrut%2FgZiawgtk4F%2BvSGdSy3e26iTKGShn4dqaRBy4JihQ2cTXJOMAa7Us6V6%2BH79J3GXFSjqg6UCVlyD3NqMlLsLIo7cxF4KfLBKKQfeF38OaCw%2BN9JKP2T2zHrNN9k%2FAtxjChU9KUwlUVl2i40xe&X-Amz-Signature=7ea911b2273d26b80b8cf1c5d67418027bb8f3e38a65e8778aedf7d503adbc9e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
