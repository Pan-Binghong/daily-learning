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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DF7HZTX%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T033722Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJHMEUCIQCemWVYkx%2BCuPVluSg%2FFkb9y95AdSpZs0uhYhobqqlkcQIgVACv7HDTy3MzffoEo1dC37mKbxscXAJUjdV2rigVhgcq%2FwMIRRAAGgw2Mzc0MjMxODM4MDUiDJPoRDUYtn4IVI4owircAz6ssuVkmRh3GATN2ROTVea9xaLDgou7qb0YQxRrC7EKZPXOzBzIsDX6j%2BBTvM6JlqD5%2F39HU1Q64USn2oIa30ZgX49HHrUhDYVIpXJIEZi545IAjPiYkVNU8fAcihlT2Kc0shWdhdpCzmf2pSDNAa6%2BJ6m4wU0B%2BNlJl%2B9nW%2BNSrrTPaC6mUqLSTlZpISDRXra5isMEzwXy%2FfkqjMlEX0vVhetxj4tf1rpbBpa1jqgtOfwHYR5dMOz9Y4Js6hyIbiHzFPMLNuOVwN9IWDFHvvHYlwLY8wJ8Nu%2BKjI016ssV1qR13lXmkIjvJWcDlvEMpmMpX%2BEve4cJEnK%2B1k1%2F2Dia55aS0rqqEtIWviXtZbyjQwUCKracG1yXa0EAMc%2BdX0p14P%2B4k8q7natIxeSQfIlDv8IyxzQ3rRhje8r09ls7vYs7zL1Zo4XvNAVBgcRDfPT3BScpjMygAa72MPWWsRqZ2wWfFgd3EBIGkmMh%2BI9h0g054cBile2GwNXewiNrwCvbhf24uysCwyLkEgquy7DQNe0YIbi6enfFTpmsuekmx8L%2BXMfQiFUBkAb0CcR2e%2Fep3OPDx6i6blSi2j2SaKd88A92N7jC1IrEMuU%2BYzY7Qzom4xSYBTBWfL6WMMi%2Fz8wGOqUBp%2FXyr7ERjPm%2BI4v3h9ZufLNm7I%2FcAQkeZc6LxyI77R0q3iWVfoPqROY6oHJKX09paYtg8xCu9LLHls5SHbGB9Q8wTktuaBCkA2stLP4%2B2YlDJZeP2WwMG%2BDNE6VSx2C2RgRvS2mQzCgpWwNFAIqlxaoSVpLjeIBbeoUirRLrImrOpIBWiP8682b55iXxalwTEuxH6ReKB8lKiP%2BSLDByugZ%2FOcwY&X-Amz-Signature=86b191fc8a60fda9875c9635e56af5721f1c6020502a573298d03102e85f69cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
