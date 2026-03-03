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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYZQHKAQ%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033506Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDI4%2BVieszN9kVnN3auXYRrsl%2FEejkurHbB%2B9dPeSkfXAIgGAWwnWs6RxhxeXYmLkj7m4XMFY6kd6Zstl5qthzP2fkqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMEyXxsb8UVjgPJ7myrcAzaef3d0x4RwZ7k1T4krVL1K4kHtpWTyWN2wd%2B06m6o1xL%2FKefZXvVS9Pifv384XFCGMV2f8Y2N39wpvM7PcONCQXCMmydEI7X03gbsxjwLAQWDoReC9NJUEANvYna0V08Oc5g%2FV65SyNz4baLNFekhlpul%2BvBY0lxDH4rS2uioMyR7gRwC9KsAljFSrsB83WOt2uwtIq7QTTlqh%2BXWHSyb6XIIIfTxu0oQ%2FlOCaA7Srs1PKGW%2BkfMdeiHzlovaTqXcESbrLHBbCA9oTjQV6cYyTnfR6Phc715UW%2BRs2AwGMS2gF7h4NnFVL%2FU1U%2FNCi8IJeMZ7XxbuyepupivWGA%2FGtQ0o1tvuJRO9aX8NyIHjQkgxfsEcDdq6iDHp3CN0ffxfooyhgG8IcZteCcFloRTLzgjl7eHaSyAlBqxFizG9tA8TL21VT8OLrefj9RBQ9hyxGzFavVMXNh%2BGeIX6Mhfa%2F3sfaqArgqXdJ5TxBswRHcbAtNwvpihbtB8sRzR09XlvVYydjfIgP8zvyiI2x%2FJX2XlcNDOhSkR8V%2Bh%2BJz03qYMXVeFmElLUsbbGADVAWbW47PERMzGVPrdSqKX1ht2UXQGcT41LxVwZjcquyyTStOJmeL9DN2uZxYiswMPK1mM0GOqUBWgxL4%2FDCA%2FA8rA4zfogZBGWg%2BSMP7AhmOta80GgTdCSoVipX0lToiNnCa1nNwM999JyU1OkKRbqAhW3L%2FckYgb53s70YEyXD%2Be3NV02txyRakIaS9T0mYdytghR31gJqzFFsmwWnEvXiGkyUIg0QYj7i5aNipwUFonqq4%2BlZycYivzIpQWQvw%2F05WkL4WKLhk9%2B05Q8PVY%2BAeZFj2uMjqQN64z9E&X-Amz-Signature=7faab06b22ec41f2ea30a2c13bc317355a9716cf93fe93c86312121608d67dbf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
