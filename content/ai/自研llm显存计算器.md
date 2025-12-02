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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CUA4P3W%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIDdJpVeiOkU25l5mpwVggnI1wPy3y%2BJ3UKP1%2BSPu0Np4AiEAhyDJXt5zypERcqzD6hrvDCNQNpVMoNFO3d7DIU1tej0q%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDMvoygU6v7IDpl9rkircAx2UUZv9w%2F2RtMOyUmfcyCZNGozL4cWbZLkdiv0bKOwZEUtt6fkq9AwQI4V5J%2FtjPbqSNxlTA4IPCJibYo5FDMvxf1Vm5%2BXOgND60xVoJwYM4tngsqR5ZXBkGvpLWchnIQRCgNUinX303CjLJDXNEWJ7CiQ0DXOXawWX3uVWtGsrGqaLSjh0f7N%2BKIz2cdp0lLzRuCH%2FX9q%2FRqXYMmmtEVKfBCW5ztwh3ZlbdmZudS%2BTNcj8qqE26eA%2FkvPVBvmH78crU%2BpXUFA72sqwubDAitF14qhOiDwwuQrRD42l0AYA1qP5Z8V4LdafO8HPoffKBPebZ5FzCaZtnV5GW66LKbNk0HKjrGRBb%2BuZGMHtH1eDoZ%2BhtKhLu6%2B6jQi%2FU1KZfQ0jEchWgBqUSXCZ3kae01NDE2GpL%2FUPxPbF%2FmZcP%2FiNbm61PPayIOnVUqc9pBdYh%2B4AkVgRzZRYAFDnJ9%2B75pRubpDAE4B1Hgmj1Z9QOp5MJ%2BGbOhAeZXvuX5eJD0dqgEh5NSgZKBcJ5pecbu1hvl0r9uQHXGFuqhpK6uIajZVu2CPhf8KtJikTwryOGQfXzgCSFiTOOX0b3NOwOAsr9%2BI4hP5JtsGhtw1oWkk9yzbs01SIlzTeuW%2BA3aDZMI%2FeuMkGOqUBKhMq8dz7Df0Q%2B3IwcA87FAisaaMMny2l5aGr%2BzIIM2PGYhd5zpDmKNqIkaHwe5t0NqLU6wxUinBZrq2tXGX1BzuCQ90453Yv47C7XI8WnsNLcGHoTnksCAI9FNRa8h%2Bp1snC08m%2FwxGWE805G3KG5KrgwtwJ%2FAPbWet%2B%2F8%2BXWZD81H%2BQr77PUcAVDCt%2FBdSN9FjdPzQHnc3NuoROswOdGAQk56YN&X-Amz-Signature=e76b370f55382b99ac4e87f2afcd0900f94c471da332bbc1be0137dc4176ad67&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
