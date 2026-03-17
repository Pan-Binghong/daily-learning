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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667I5XTFSQ%2F20260317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260317T033506Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIDjva0KPoE%2BCfCJ5NlDaQY%2F%2B98Occ4pbav54Gx8ZiR7cAiEAxI7UG0M3kCk4Zbi2KubT%2Fg9C%2FZdOLqmBa8MwOuvYDLkqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHp264EZ8SdLuJe2IircA5T6keIrOYG5C17zTCg6UdM7LWZrHft9KcFP8S4zKZWAsffbfD%2FIE5ZWxnlbeDBhr%2B%2FwCx5F9Jnyu4BuitvSKjlXd3eQmHKD2fUq%2FgRstdtRG%2Bd0PLMPCzw1s8s6itKvCLIdpLznRJ1mXD%2FcQgqeTRuA99Rsa%2BR0X%2FTFvtsxNsOu5y%2B5rlGxmb766ZpAYHtvKBDrYd1%2Bx0%2Fm32nY9F4jbeW8SaYYKgsZIW2%2FQZM94A2%2BIM8IEtDCNx2md0VPwmj%2FPGLu1OxrIBFpNx7iBOF0LimazXdjLBRo%2BANLVpbx5EMjVlsBZsO8KEXNalmEqe5RccLUk47nsUfkmsV5QANaOpdJqUPrNw0Exkc6LtiqtY3k4CCPt0dtShddOpxAvb5N17yd%2F0v552KlhIw%2Fy1%2BRYo7aurdParf5%2BCbc9oXgWMvnUUI26ICTQxCQ3I6ifE%2BheaL8uZP3Kn5WKU2Oa5m2sRqD4k6IIcE3ZfSDpV0EoQ5nAZtV%2FDfAyquFyGpAyNfpqRMvBXzDdhfMDHfoirEndbo6XFpLk9WRYZmmgeD%2BeDhurHpmzCnGxXyffkfziZ3NhH%2FjxC%2FRYOA98pEs9lUKaghKjEVbHGUZEsnmN%2FUtqhDav7gXfOQtNZi3bi8AMMTo4s0GOqUBe%2F5A4tyBFTdKDuGAbdiLytyBD0K29%2BTPe7mPKvweTNV5xwkFT2P5RjaTL69LF%2BLXnteqHh%2BRTvQzX1LNBIssgm0Fvox%2Bdyje1PifzlCQVpRxReBg9RaNo2GYz%2BB9o8DisFdFLdSvZEJwSoPo8F19y7YEH%2FkI0tXJ5bEZ57J0lmoTUTHlnofHq2QsgoK1ge4VklWpKdYY5Ai5leC5WBcUZyfjAPJC&X-Amz-Signature=5f390990fce34aa1952320e72a9a315293cbc51c20503eebc3d9fc8edc636dfd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
