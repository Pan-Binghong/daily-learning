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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665O3U45LY%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T063428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1gf8Ya%2B9mi1l%2B7e415xVODAGGOLQEtwrKp5KaJ78J3wIhAI4kI1svfV0fGEBljM%2BP5TNpIRgNGdFkluHD%2Bn%2FiLn0QKv8DCH8QABoMNjM3NDIzMTgzODA1Igy5wBoZW079eb7djxcq3APp1Fhn9ji%2FKqmy%2F%2Bp1wGxXPCEslSPsPAGhoMvrJ0fyxWZYD4A3bFKaDWgoczBb90vJLOe%2F%2FO5vYjJFx2VJcVTEBCWjuGimspKtdhUcyf%2BYQAvWpEu3wtAbVAk3OBvigfyU5mSgEIGstXjxUa%2F07%2FhqWDauTStOt2qvyfHQymmjTy8IW6XrhaBdZQaZZgQBANC2KwuljCovAeunGQobPPX5pVGNDob6P3%2FH5%2F736ZKCirajJOuT4U0Ss57CMQd6Q3%2BXA6JCQgIUjfbln1c7njqvnfYvMAcAzn9q4fg1SeDLKji0sn7EQAYoGU1Uzm5u4OsNWcrYBbMJuQbyNyd5Ug7h%2FIsy69KDqd5hhvPu9BQtUnS0rjiGFL0DrfV8BEzSloU7SVJLFIRPqGWBaBLRfICagBMzGi75SnnEmbNOs8GkQIGMh%2FNCw9tpdDPYk8PLOrEIG5YFFqqxTFZomIWURGkySWzjSGgDo5cexZpCWUhYbGbatBKNTCka8OeuDLJ3X1ucrIiJrb%2BNoWFRoDUwdPXBvXfvCZfGeZiqlkuNX2EdsZHATlolOlezL2wWIouQvmwdWsd3eUyjDcaOGCuKdjF2%2BodzIgTp7AgUDUMBEG8Pp%2FnD6efMzIvfdeDMOTCirb3OBjqkAeO1lQPboOlcZBDVYthXx%2BP6q8vNMlgrww7RN0Fb9UKKkVjeA6fo2K0TFsXrDQBmyDe8kGVoAc0gHRihcK9rDrhjR0Ik%2FAKPYn7epjihAO6ou6XOnprmBcWqmbMWzTyWzQBsaTNvYlt1ztDuc4BNSMsmkYSoE5Tmt8UY%2FGznp4s1PcWQYd4ycwRQWUnjANY6tZMV7eC6cigcI4GdQ4lxOoSjLcrv&X-Amz-Signature=7dcaa7ee77f598fda9b95cceedc0003cc7feed417b2ee3bd28203a73d68944d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
