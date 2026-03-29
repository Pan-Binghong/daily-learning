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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSKNECO6%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQDZTziPRiNWnz7AHrWjMhIbJ65axT9Imohq3oyLle%2FmwgIgYa7WA31IiWq3D%2B8g0oI2KLnfzQW4QQYxBVN8CNGtjSYq%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDIQW5MARFGdOVJGZ7yrcA5nQsoRzmetVw25KsI8ge4Vdr9zVc%2BIiJ4%2FP9k%2FHCCsWhGq4%2FuqvOGSMgxmQbv5h5SHT2h1msfpI0MNaZD%2FjXZSjmWbBH6fyNg%2By5m49tZK8lmi4eLs8roSEWS%2F5Nv7tDs5Tx8Gge%2FugJqyOxPRfOiWeHdAtcbHypcF2coMD%2F%2BgaiGgNmZuAxNU78FOf5UDZWZ%2B%2B%2BrF62A1EORbJG0K0CEd0TnHCpR0rcmflHCYHtnyVf3X1YdWCjzEMG%2FkXPdCU7T3LCgrloBG9feAEBEE1M03Ch3N7%2F%2BXEWE5otsIP%2B8HekSNnWTmeIzFkN2lNv7ITV%2BO4k9tLarhLoiNHf7oSav38%2FUaCmdPDuV%2FLycDCiVGRKQMH9%2Bvpzu310orFE7tvxXH%2FtHEIK7X0qJkRDR0CsY4tzfC8JnO30A9VsOrYmNMthLqNQ6zDksQqZ1OpRwukVixTchFRADzFukRnVRj31uLp1k9LJWRsCbHeLe3NX0TPKAeAdNHCdM%2FTynjfzFSJMPj9mPRn%2FaIDqyJX7%2BpvDMoy%2F%2FVDqRppuoLQ5UyKSsc5XHUu%2BbG3nv%2FroHlKXGZJmgWdsnI4PSiizjwZDjNgXJBeHxVtFQUe6CWNERtBseNXANxfhszQYCwLO1ctMM6%2Bos4GOqUB%2BdLhKKSZhpq6nxSqYu68QZIfdWktrew0x6IIQbf5MzLMmrbJYvCtS3VnnLt9Q8XNGgKvZqGTaChYOlGOTAwICeG1yZr4mwU6UIMsKqw9dL92jt7pnvOLexhFklC%2FqiriUNXj0L%2BS%2BtQ4ZDYWzw17VkbOCgaxmKAT%2Bgfxj5RMGbbHkyILVRNe3BzYbEMPgThcplYfZqsS51aayC4K9iR7Awi3g60W&X-Amz-Signature=7222d021a7d10d42bc332138949cef613e83fc7a8316ad5cdb99343eec2529dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
