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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJNXEUFV%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070625Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDwVdyZSaICtECZwjp22uCySD7vBvcoRRJYnMTIC97GMAiAmWybKH%2BW639bICHfm4nri%2BzrdTXsyIBiAORnKtbpt6ir%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMQXDrm2i2ppNCFsLfKtwDhUdvYVjoQeEYd1OqtwuqnEayEAQWB5WJ9NzJ0poXkwhs6bra4On0WNaag3EgL2PrPIGtVu56TPFTBtGFYRQAN5hdOE9BWLhQ%2F1T38TOETJAqErlc584lxZ1CK5Hgba2nyP8iJGKmFs126ymrTTp7iHx9E9GNicX4LalCXVzKMzzcyiqtGNAN5FtZD1ySM3s4dEiddjUBWv%2FO3CA8BxFO7niKLIYnd4Cw8T7aezfC5%2BofwI4QbEQjWvvOCwx3VmGMcoNmya2FtcMzyh1msIi7cqOA16prx7jfa6Ps4rpkqFsw781bgfmoy7LbO%2ByH0a6JJBqeVCNIHLcNG3i58CTi1WhIWc3OeyPehGH%2FtT5ulwFtQ6sGFMiq%2Byt6%2FKYhE113qasdiJcd7TXk4pRg2PvE5WOr2ekjPKw%2B7RgWsyf7bDcsn%2FQGMOa2w2ferStazlbOP7rnFRgKa%2F8pzhRXWx719hYbhsqiP1v3GlvCx%2BKAZP17WEx6oZEGmim3LG0wSyEdw3s03R0WMZ6BXP4vcGsLtMiMf6BVRgeddqk3j68II8LdNzabElkDQrF%2FeyGhdd8KYCvlGzCM%2BmE556X72dKyyJHcBFhCEu7y%2FZYQteZvBgjKf6%2BA6csqObqzIqsw56y9zgY6pgG5lfJgmuTd7ef12ihe7RavESHKsfxHV1dmvDn%2Fi77qm4PPQCo%2F5LroVEiX5DAJY6oIVfUoOwcs9qAdPqYuFSSrgqVWnlnRSbbzHDokb1ugHQahr%2B80DI4xDFt9LUYu2Bd7s3qVOV2zor6pnRYDPdLDtZL34Umbq%2FlFODVe9kkWSER87tt5odSRAxN6O0EEX8GCOE8JjYbR9kU4RjX2fkUSdFkFltV7&X-Amz-Signature=06dda72bea2761502ad44c67a65ac176942640036e6e804dfc1961b5b54bd6e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
