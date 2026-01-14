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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QMEWEXDS%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJGMEQCIBrEGPOHh6HCU65%2FDd23a%2FE7ALY6RolMi3zSfvgyVIODAiBQocPksqU9b70LqpBKytwxzoy4z2d8qI8P9HcsZzaXWyr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMH23Z8lBqsyFnEl%2FyKtwDHe1XWTCmbtfqTAb7Vc2OFGH7J14qxh0%2BQVkm61agkNgSZwzqVbHmTUGHHkSllzWQqvtHPzHvGQBlFKuyH6b7xL%2FM8yPKWFur%2FiDU9pK2HTDMQ2laLDF9nskqW6Lz4YIz7%2F9LoHVaiwZqJtJibIHx8dZXdpvHHb6FG8lkBmYqzCF4I1L5hLv5twZ1HXd1h39rXErIbdR4EUjgsCcGYhCbk5eJqaMotbRe%2B%2BbjYjGY4WCVx%2Bf6kAQFeOpZ7vFTzCG60YA7SaCZq6nZarF0o8QInCVrSOwTH2Cf1bu%2Bmg0nZ8gq4IbdNsFoZCRRkQas3qJ1UxU3fHMlWWg6nSd%2FLFAqfjt3aH0k3U3eIAR9sO9LMBBH66IRAsj7WtfCsnPPAcjEgpJXVbHpB724WcINhba1EVhuqdq8uWBHKoiD%2Fhoy163wzHmjF6p%2B6Owv%2BLr%2BeLMQrHXYZ6fXFf%2FRpDTy3l%2FwBsczhI31Ac4uafupZSgt6hHjmW0srfpX26bnscU3dQ9truW0Xx36kiawIZ2wpd%2Bb7Etc4DlBtzFyRwXQTsLoPKveXVloKoeo09gyDfFnLMVOGS2lH7r3DWTIUt%2B%2FPjVmI%2F2gSoPdndKSyRD6wZqM%2Bg2sgpP%2F%2Be2mG4CFlYcwkO%2BbywY6pgHEgsWO0Oc1D4kf%2BDmz8Jb8mOSdqaU2xYsQhbR6J56Jkd48NLe4ViFP6zEIvalL9bHr07qR9TmHMv4qb9dICqUS9TvtCIjdcMov76s%2BSE9oomCo7jfaDIEkrd31KYm5uYmt%2F0udwXqrkBp2nWx3vxy91WIPy%2FL9rH8y3TwGT5ylAID1hD2Ea4Z%2BRffgZ9agAMRu%2BEqMM%2BRuHFlVT0AdEa2Y6CXc5tAf&X-Amz-Signature=e52895484d9149a943dedf70a1db1c7abcbd67bfb46f333aa7c4f2654659ca10&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
