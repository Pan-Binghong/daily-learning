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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/15cc9226-959a-4153-8d9b-50983b9a392a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMGPLXPU%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T030939Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIF1kCxaSzMAZeSq6OgWg4rdUjjrN%2B6kUh%2BY02SCU3C5OAiADNC5tVBss%2BrJ%2F9jMFiQUcg1Z6T2JuQ7JHfUiA%2FEQxSSqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYNybiDKJGRVQB7YbKtwDNbFanVslYHrF8fyuMAmIxksUExzf9jRfVIB%2B5ODO2uqlQHVvTJtru8gAydfBeh3JJJGR%2F%2Bh2jD7a%2B3G6EFBD0OjpXJF79MzpmCTaXDh%2BlgPiVRiIG49ksaDarisitYseGyk3TD%2BVRnDZABq5CRD1GDrG%2BqefG2hNKjBZNe5dZeRzMeFL78jq1bRpk8EPoGPCuE8Jtho6RPt%2FNCZu26TC%2FfkQWDserOAzOiiL7OfSSVSKVM94EO6X7J0nxSm09baGVXctzVS%2FqdjUUfBKubIq8mo4Ry3Jyzyt2cqb0JUudfO5e71Ql%2FUL0Va4hs94zrb0AjifqGP1C1GJXEK7P2wpwXXBJ8fa0ex7z7pL%2FAnnGXME%2BXpSqlVKFQgnZujJulYTO8bA8ExT1rme8nmDuZfH1dF5DFkN43qJomNgJBOi%2FIbhEv8023xjOM8a%2Bt2KoSpkj%2Bk3ViVgXJe%2FY9TGffNYnGFidkP%2BmHxyFLTn1bBeQhf%2BntOWUrRLw39XOEHERcRmFF55HXu%2Fkm2PL0KqosCVleQV9A%2BS42UKlIh1Sq5ZVcgzmMzfAGalW7%2Bm5pxXjPGj6UtPXtF3CTw%2Bmn5tCkM%2BxphDQmLFXIWfT8M1EtJAtMJyqvVawYaRGs4ru5gwu%2F2LywY6pgFJSDcHu03rC1bLuur7xH1N6ZiECMxOhL3CvWIaTTTJyh01qgfL8Ei7%2F5Bix%2BzuGiy0i0NrmwIh%2F6DXU38z2YivgtTG8tUrEQPj7xMA%2B4S%2FiQJbxBbMnhhNnZ8wTgsTP7pnM4ebqPdhNVONwsxoBViDwvgqXlH9P%2B0jdMLJKz0IHqrGYu9DI08dI7vXQAU6gRkLk4o2gBE56JwO3Ie2%2F%2BalSsXGLI2F&X-Amz-Signature=cffaa7da2a7bbd3fbf87b41d81ed12047fcf4f1b229215424a4d5c1e39ce7812&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
