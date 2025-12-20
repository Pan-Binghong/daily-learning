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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYIWRSWR%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD28WJI2NuE4sc2FL6xi5RIycsHPp%2BI2TcCnHGLPUmc8AIgE%2BTU3XbV7fozftE6K6zDW6RoKo6fPd9MYWieOSUNvMMqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHAj8%2FWWrfsm8ulX5SrcA6m1XZSRCubbQTGBVrkZE8x4UowOwATqz3epFEcu5IRWWAFaJbKzilSx7eBlh6mGZvSv8Ir8xGC6oDqlz5EM5WMzXu5aneMEUGyiKjyjSBV8oc5SJD3oND0VcH%2F4zo%2FQPCv%2Bwimdd3DYOD8e5wmcm6R%2BGoxFwVunamyRYFVVHNFE0Ch5HtWjMYefp4muanNIU7pacWVpHqhdRdXrlfLAtikBlCnf3XOHXLXzL4SRfnwRVq2hNfaNQx8yidCzwZferL1vuA8hQZ7TiuHBnC%2BOtEGf8gEOEIivV74f5GnDc3M0nxb%2BT4VpD%2FZN72GWgCA%2BtMutRH7DfgGQC39UGWhem0dTBmBvEcGDFY3u0Pob67f3k1J0aQ6B%2B%2Bceb%2BUYHkkkiaTpU%2F5i6mPDXknaZNZf5curj44YPDDP6pBK%2BPYPyjzRIojMlYtVvX%2F729TX1e5dy3az1GXGxaaYLFnekjajJqYpCFtfIr8VFN1wiGKqhaVA%2FL%2BoG8rhHM%2Fwc%2FyufObbWCLW7yGcsFWeDDuGvrZWrBESsESbrtgV3jZUob7gTeQEKxV1%2BCXGtigNvNXm8v%2FoHzy%2FwtPWe5nKDiiGOk3ujw8uFxGX19n8tA%2BEcA5DY8CN%2BSfZp%2B6XreblZMhVMIiGmMoGOqUB0sZrqYVXnSe4NUDku2Vnbgyh5udscG%2FNgaJbc4W7i0gwxeVNW0eLJW81Og8CdVyYDbnmQrwkGam0EIqz91i5rrnonrpIrZAFMuG8ChbjbQfc3XQp6arqfjWXnEP5SX%2Bzsp9tQIfw32i0tiYZh%2Bs3Z5Fw50RbBZKJh75j%2F29b4Mo%2BzhbdXB5DxZZ2y%2FtIyNH8dRXkznJN1NkURipMjOA%2B%2Bt0b1YpN&X-Amz-Signature=62c3a760b0b10eb66efaa98442cb038c386f53702b46ddad02ecf114834a37e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
