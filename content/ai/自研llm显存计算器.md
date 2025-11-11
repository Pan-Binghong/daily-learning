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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3Q2SMJG%2F20251111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251111T024429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIQDjwBHYchfpEH%2FnEcJfJY%2Ftz8%2Bf%2F2cT8QPX%2BMQ1jtXDdQIgZWUIiMjT3Q634M0ttEZDXdlELBjGKIp7psoRhxxi5Ogq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDPHGL03Wd4nfxiE33SrcA8F6igGZsy%2F2X2IU8EBTW%2FRH7wjhQ0AoEzQTstDZ42dXGhicSrWZ0%2BgmcQQLgOpJGI88tIJhxvtvyc3%2Bv%2F%2BvF7A%2F1XP%2BTHK9%2Bv3mLxs1%2BZ%2BIkGxCDVl96fw2jGwoJhHPtUssvFVikgS%2B3Gdl%2BF4RA%2FlO6UlCoj6yxm5PPprMLvhx5xybNVGqUU7Pb88vLZVathB79H7mdCcFFy%2F4xshqCvP9RW%2BFw550QmrpGk48HM2Ih7legJ6VUXtoCkHd0l1%2FbWCK5zLCQBDsszAsfEgGxsUNNW01IZSga9Z9xtxk%2BXljuRrDQM1MOUHWgZWN1Xqinlinzbb%2FIFsrDJBT%2BqY%2Fxi%2Foo0ESNWkZOgZRmn5VzJCBL9XEK7bl5kLZWMSlIff0miZHkv1%2F7oAohtGqZ%2BeaVoISQ0zIuRRl%2BlKOdJW56ISRlfLOYnJG9kArkTh77S%2FYOgHsUznAw%2F%2FP1uSPYkamc8bRQCSehpLYFCToAeYLEPN7f2Bc3NveLR7NT0gOnDnj8No8j7H5lTS5Pnp3xcd3sCfvGYNnCpaY54q%2BuB2DLWmNtJBROFFzZ7q4hO%2B6XMQm66trb32AMOTR6xOhs4ExzdHNGroKp41f0cYTTTCRLP69qTfPapnXdiVQuhw0MOi%2BysgGOqUB4Dti%2F9Blecr8dsbvbMfxjgNMrlTCDLEC1p1c8bKhK9ZeSqdEOgR730P1H5myIWNBteTPJp%2FPClV0AjDmajiWT9SVeEvkA0b2hH%2F2rwdr5VVi1ihCI4ns9Zsxac6e8FbkQEPn6dwxByNxc4WOJ9gd0sdNs%2BXHjvGQdWGFz5fP%2F1U3BKAXLDzv%2FkkLI7e6BfWP9xzZqFP0R7ENdyHVpB7V20%2FxfQrY&X-Amz-Signature=ea26a998c64385b8c4ce4a49904d5d666134e4d9530870c853c07d890f94fd7a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
