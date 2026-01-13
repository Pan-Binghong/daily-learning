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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CILJ5ZY%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T025754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJIMEYCIQDiAChzW%2FgWN8qX7ebrDgqRANX9L0ObO7meZ9L3Nj5yRwIhAP3eK8QDmAt1VXh2RJEoj5g8%2B%2FsZ%2B7yF%2BJXqTnNBEMW8KogECPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxc8%2B3wWuue8ZcaeSgq3ANnaU%2FzplLTlLOT9YbbDy8R3DQVr1teXpQAZhQ2Yq0mBRKhtf616wsDdmJQ%2Bjx8sQQ9%2BeIyr73C35amw8FT3JX6%2BydJbju67Bv4xgKYNpw9KVLqQ0JwK%2F2UUpIYR1ae%2Ftu72aQTSrf21GzitDRWLSiHHpOcte0tbebIT7P83dkesE9OQsfhaq22p01fI1WVchdGVl8ErA3JvP5Ql0mfmuFWXsunz0PwWVSrZMrkal8DhbJ6vLb%2BmeEzS9zjQme94pHOoIcUCaZPBD2F%2BEQFAcoOEZ4fdjx9wOCCFmp1tStezhaTm50pcu3ReC3XSZXf3AXnJCySlZxnZvDMFVohmlAYzIwRvguvBMMqJJk63rZAfYvgSkPF%2FANMD6b9tkZ%2FbZ5USmPzO2QI4so3qP8DkE8PIwMmmwtD%2BZb3NSDcg6%2BVQPQR5cpECJBKRqNGo%2BPc0pwA51HcAIwIJmNSel1PmsNbS5xkfv7DE8IyRKD%2FCb6zgriOIE5paT0JSWyVgQjcOaDWJlcNAj1d6SNxNLtHYxHLodnhrJqyEtWxLruX6eN9gAVPomU5IMpjSzbEd41YXf5RiTaOikPmlggD8cqmKX9gKEf4rmKvE3rr5OKVmx9qrsPv6t%2BVmqhfnv5WojD15pbLBjqkARfuGMFxsdDDyMKPTS4df5gZ9nkei2YAk6AkVNv5%2FSdfxwBRqUTru0Hk1FwN2jve0jrkKC4z3Z%2BpJ%2FSesUUtnjgrCW%2F7nno8NNEOEaBeTUsINBNEri2nSV7Ru%2FLqfoJuAFLFjE1R8MSG2ZCLm3KU2eiOkFEkF24emFVv%2BzHCqcFoDLzhQPST0I1QeTrlsI2pgqX6Uf1e6XnrKfc5SA3MlfL7Q1h%2B&X-Amz-Signature=ba54e59bc79e8048f3677824e2a6d48cb5436e2728f5ac2e98a5e901fec85f12&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
