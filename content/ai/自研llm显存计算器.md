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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXMCSEVK%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHCt%2FcHYNpio8A6oiiWeadPRCBnWcLkQqe%2BMi9C3uD2sAiEA99O4Sppb%2FndSXh2W2JCeIsUXJXQFAlGiEjvwSX%2F01Kkq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDJ%2Bja1j%2BIrrAzMAU1SrcAydo%2FzWrY%2FCgM2DAW1fOk8%2Bz5EuOYA6pWvr3pi0WPUETBubrB2q4VDD6JBb6A09agWMPQsLzKDr77NJvMrEJOaO%2FeooW2CWx5v5lcgxyiYdVr9ap4A%2Bv%2BVGX5B1YO3mG%2FImtwHcPxaWQcjrmghC%2BTucZoL%2FNCc71iw%2FrHq2x7N0ujN0iVtyfsD8l2srUpvA5gxH0N2kPPRlVtiLHoGoici3ztKhk%2FhC2mQJFg41cn9I3Suot%2BD9A45SWrQDxGFXQ5Dgoa8y%2B2o9I7NSMu7Eh%2Fk%2B14eTqCtGoLMPl2THt0ETSiE86MEIqVY0M6BzCQ0ZaUgr66A0sASgV4EWyiqrDg09JKjdH7PQi5WV%2FTw7pc%2B2Zu3N8ENS3uX4KNK4ezYxkS3ajjaB3RlvlVIWz2KJNfrFi3%2FDg9NOXNS%2Bs5eOp0OJzoP9onwoAqGw%2BnQQi2XuXctblZ6Rbh%2BNmvuiOw4z3M%2F%2BAL0jiBl2HpwRb%2FNdKpSkiv%2Bzks%2FPgYlzGE9w5RqacEkcePDfIr01PzlNuw%2Fv1MhTwAjrF5qn1Z2egIUvRw2rILItzXdejqH3aVBQzoltgLuAMPEnvTCidfa4fzQRugZXsXaXGcdy1U6Dk5Uy45%2Bdc2%2B7r0T%2Bv43WzMLq4MKDrvM4GOqUBTXDwVVdlOZorC0Co1TamifvwadYdNoDCBhyehAGVSg%2BUkFxFlkPD43yfZHfSCtOOfkLfVduN7BrcylQ%2FHMqG62anQu6MogOm3HFLuGitJNxZ33nIaCbyXabrfQu4DMmUDWYVsz5fys4KeZqWsfspWtvQx0TeYDGAdb1eQoqdAfC5sYEUXXmzDMvKgW4hgPkJ750gge6PF1d%2BLO94igINtQQG9Xpr&X-Amz-Signature=374111622a6838a54a5260a4b839ff830826ccabc064fadc8916071cae23ad5d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
