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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46653NOT2MA%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDwUCmDaSNDj7xSlGPUuosbHI%2BWZG%2BLi3KgqOFByO4BAwIgNE%2B4m0Iz%2BQFKKghZ1KOzIMCRqdgTiO4Ces2Il0t3nLEq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDBYwWFwx9j9TDFck5ircA8ulymzfhbJrBBdT4%2Fb2OH%2BoQV%2B%2FIRWF2CxBLUpVGD4%2FJQTPp49szSFq4qaIvVhdJ24Y7SOtiCLSezSRSHZUdv0guJQHF%2FAjf3CBA39Q8448JEsa6Czu7%2F5sQUqsyPUFw7s9Zcvwer9JTj8oQh54RIYS%2BukfhrZv8fs9ueXnvlcN2w%2Btf99jVKO2zhm8DxgbrTxqC6%2BzKENXbVAe3FWlHGK6tLz72OxjShW%2FCIYiGNsnY0oxSKPvwRVUJe6uvmZNEAtf9kzmBK4DgajaBFF0al8Xxx%2Fd7l%2BkChbWB8HZ2s5MvM9ZsWMaHxwUyawrAOzaoe6l6H2x7Si%2B%2BcJ%2FfSlC9s07ctr9ReMjqWBcLXGCg44q%2FuzcmXybbmKy9WxhffrAUpN%2F1UQW3jmPfYHo4g%2B%2BMqI5Me8B02y4oh4MQWjGUQjg1VzyqhSE%2BDlM3r%2BAXomQWcEwYEQMf4Pm3Td5F2ABfsTu%2FWsCKhCdeqTEaoyJLzgkDboV3iT3vwdEShtJtWKc0ucDhaLy2L25NMpGfXlez%2Bba5UdtN823%2BtAfJ9hL63myM8SVtM7laUyhK7QUxvwgzoFceFRBAVY9ASRkFtXLiQjV3mxlyN5Lymb6jDyBlRDymoI5dI3HwCv%2F63%2BjMJvpvMoGOqUBYHVUu9R47htzMo9uUZim7hFKrn%2BacnCa545d9WxKzSaeFg1E0lp74T%2BTW0YyEs3g6Zo2gTqFYnbbC%2BH4DQfuNOBggJhIGa9VYDgemO9HNTYa%2Bz3yZdTZesUmUuHKhyt25gVgXdlWuMzak44Kf3JHpI1NBUaiuApnxYdGmYjCa7qJUoqO0NRLUBQ06EVhz%2Fpuy1h%2BbNkKOVhyC54WVl5QgyYHisdw&X-Amz-Signature=75bfb1f37df9d99094e1bb27162e593b4629bd10b7cf6250737ec21940b3dbd7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
