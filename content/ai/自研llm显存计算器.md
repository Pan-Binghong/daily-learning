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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6U32OOE%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030649Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC0uXlW6riDqjnPxECuZ7E%2FaiTTXdnRYjDMocJe8DdowAiEAuEkQpHhiqNgmxmtafQDL2disx%2FshwYt3LLnpTYHeVhMq%2FwMITBAAGgw2Mzc0MjMxODM4MDUiDCVT4nTTX%2Fq%2BzNWS5SrcA7t8bjuHP4HIf6xJ9U6uu9S4L34%2BT%2B62u%2BnxxW7pi4wEiajgYbUGBkPo%2BkSrLeG%2BWN0xme%2B4ek767A9UAHMT18A%2FeapDXFrKMOCscH%2BSL%2B%2FM6%2B2%2Fo%2B53hraORll7bjnT73HVJFWZgmxZSajM31cewTE0tDc8oEmaQ6UVOGUS%2BK4kasrB5zzNo9ALhbodSyj5WnchCZ%2B%2FOrz366C3kSBaQpC7gcZkHr6KddhCD7u%2B3%2FrcxVDYKfgoXNAw8bNSOK8RiKeT5XOKWXi4lMn0EclDClM1p%2B1493JthRh2dLRfOKY9%2FPOOTb0tIhaOqS70Z%2Bd8i8MOV0zvfdb6OkDwUc%2B40Ao2p7m1ljK81Xq45vxq%2FaboYVwaUhs%2FpFBiENXvUt4M0vzHRd1CKEcRKsME5LIjFJh1OEX1c6iSSdnhvTZ5vLpuLC49tjJQbx%2FWyanWzsYkgGLdi42EXqTdyPUmmI4nCprFD5PWH3sxy%2B2Vp1ACv6AGU1cbAufbUUYtgVeRH55piz3eqHeHzqKd32ZcFlXlG1wSN8KVz9StQphye84HeeCOE8MAOUekHmquQJVzhH3%2F6b2rk4O1ZQLzqZf2SvNsL5vSKMGBzKig4i1YW0pJkxng36vC9b4xgXVFbtZuMLLS4MsGOqUBW5gn9QxRdH4sATVUx93y4tQWofCuiIMYSyw%2FNmUqT7xf%2FOmj6RHYFJqNn81efXnNcLiJyoB%2BXSZTZ%2FLV0DqfCVQI8%2FB6AFNd213rwvxZCwSlc%2BixwiEeSPizY0w75Etg3RlbnZomul4IEs7poHKfSfi3G85K%2FUXGRKfbAdf8oJ6mJn1Hl5ESW1ytc3Ma%2FlafHS%2FP3%2FoLrTHtWh5iEH5awYEhjoUv&X-Amz-Signature=1428a0fe8659918544730c46b7c80501ffc86e72d1fa525bb47cc2fd22930987&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
