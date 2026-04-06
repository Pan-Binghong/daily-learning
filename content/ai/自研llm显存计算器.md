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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y4SBAKXW%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T040836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1yHECtw6tSIAQfDQyNEGRx3cQAlgUTzSwLhIHtBvTqgIgDs01aOEldXmuZS%2BD%2FB7QIfl4xgO5a5Ga8i5f7cHBSNIqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL4BemmQvO16Z4MksircAzHzssKB95n8RElFmGFpn4PrEW8LvBQSL20%2Fkp6UDFwUE9aa5cYX78JULXcSIaXIWECxzTfCOM1i3ivIr%2BXJkzkeCLrTAQz4ll1PryS%2FHp80J2Clak2H3yKMwl608A%2FJid2dg6w%2BtLXBj3hwm657e1I6YAigBTY70jTd8nxEaQjJhiQrUT23DjpgKH9k69S02BgDXj9WoCmPgGJgnpfgXqdZdc7khwSgYuIBLSeLSnnl1k3xR0b5jazjZCB5iewbzQ6EfPOhacDmCF%2FpwKA8k2EO7GxDHAdyHJNvtQhpVS1OcV3bQp2gFfPAK9l7%2F8LUTCpdWS5z3JUQ9lNubFOwDwR8bW3RQ2ln0P6CyQo2gTBi93I1KMBQQL2DwNN3c4ox0UgwC9MQCum2tnSUwFafWd%2Fh%2BUlt717wjhziHHTjGdg%2FsheTNwSr6GdPLTEncfSW4Mit%2BuPvpb8JXwbqX6Fnr5%2Fzuy7slftGoMVHCDWBvNADrpwrnzpvceqHBLUqbNRzcpLv1S1qkB6MCk3AztL9ufvD%2BjI68ci008ktG5nUNu3qSHNAblAma2wfvKU8F0g%2BSu%2FjWrKlhRxZY6ZYknDy1wWx3COmskardA503ZKdnSTBE7UANqSVZcvoXOCxMOuxzM4GOqUBXStEJDlYV5VdzPf5%2B5pYvM6ovpfTe9ASw9sRk3fD7vqcW0DldKQQntkgnApWBKlURt5bVutPA4eYe7A48uorkKICHhYTJqd%2FYv6kpvTwfnYaZhZ2LswrTR367sgTERMbwSshTYaZBBnQNSpSpJsDaXESTorNIOOMSeUNC5miuivdkMCWXg02Bx25jypqmivS%2By3YMiPXDXTX0e4XdQz29SYw%2BJ0y&X-Amz-Signature=3ad3221b98a3d97d1541b720e9977ac9a769d6095bd6542631478875352b5ea6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
