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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EUMN7JL%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T025951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCc9BKGPSsBrMv8srnQFUPTvxFM4FxMF7DngnH4sB%2FWGgIhAK1HaMPx6leAzEQVjsk0iwcpRc0%2FHrD3LrVHf5rqabk2KogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzobjPRSWO3dQwkauAq3AOdDGMNYw1klYWxxp%2F5koTHNKEpOQmu19kY6dvIo3D9E9tJfd67R3ILDqGvjGmBGi5PKYY%2F953rRC4KkfAsBX%2F3Xi6ts1jEjLVCgPY7bhfapDzWW8swJiLGecYhW4R8TqBzNT2i6r%2FmrErNnMM8EiAAC7DmyYk%2BNXVkj886Enusx4ZG1t5RbvcWme6L9QgeF5KQc%2BqDBkRb3K4o5vpRsfWHeueuC4S99CUPQWUsv9VmhEhOk%2Bioyfew%2FbyiMeQgJJNF8vv5W%2BMk6ftg4HmerSzHBT%2F8qOVVkS9QeeqUxlFxegcb76VpnpNOGTk8Mfg9bmYhhI5y4vxsAe%2BKUfWBI%2F2%2BjYRya4680ZJ1TWM7cLcgOvEP2S79PyLHHbch4vBblchlJDZ9RJqBmB8aMSOVsjUI3CChMpmBCppYJWq19j4y0HCnIvL4564JFvy0CjP0m5sYIOmux9dytWpr7n36HDH3zKgbatLJUIi2nl%2BLSO%2FtSvsVKWkYvCl7ahKxZOnp7yq4DUVg7CPNhgDHhrEbRESEXea0rtrzafKl8fA0OsVIIDBnFKdwUkq6aYHDSp3bxfsTpq3ar640o%2BdgRXqE35Al4Ot%2BcZWvdfve0tJu3XwtGuA0PXZ6S95pzFIcdDDBxIHLBjqkAUd%2BwvegjA3esEqKBvEOiEvG8q3YJVHkZuig70ST5snRIex4aU%2BuOg8KwCBSq7OJP4kRJPE%2BZ5gXZ4sQdR9h09EL%2BAJsoFhBzm1diCAwJbr9CloBY6N2rKeIH8iTmaanxRr%2FpY4qDBc5%2BJyyULmeb3m7372hlg9QOtihUbDJzzOHe%2FVceZCGjX%2BszHblttSiLUMCjDlQdFCUP4RDBBdYbMQEaLQY&X-Amz-Signature=55d68e3c4c25032383f29d0c99af1c697c6095b76da1d25df93130f6e553d286&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
