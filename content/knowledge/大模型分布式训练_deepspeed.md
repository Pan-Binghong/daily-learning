---
title: 大模型分布式训练_DeepSpeed
date: '2025-01-07T01:29:00.000Z'
lastmod: '2025-04-28T07:10:00.000Z'
draft: false
tags:
- Knowledge
categories:
- 知识
---

> 💡 记录学习DeepSpeed全过程。含原理，代码。

## 简介|Summary 

DeepSpeed是Microsoft(微软)开发的开源深度学习优化库, 皆在提高大规模模型训练的效率和可拓展性。通过多种方式加速模型训练, 方法有: 模型并行化、梯度累加、动态精度缩放、本地模型混合精度等。

DeepSpeed作为大模型训练加速库, 位于模型训练框架和模型之间, 用来提升训练、推理等。

---

## 核心技术|Technology

### ZeRO(零冗余优化器)

> ZeRO可以认为是数据并行, 但是用到了模型并行的思想。

ZeRO是一种用于大规模分布式深度学习的新型内存优化技术。主要提高训练时的显存效率和计算效率。ZeRO通过在数据并行进程之间划分模型状态参数、梯度和优化器状态来消除数据并行进程中的内存冗余, 并不是复制它们。在训练期间使用动态通信调度来在分布式设备之间共享必要的状态, 以保持数据并行的计算粒度和通信量。

### ZeRO的三个阶段以及对应功能

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/037b7e03-6ddd-482d-bf08-6f0aaf7c57da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXOLPDCW%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDh%2F6mR5a0bnGx86XDyNPUtN9TeVKSS0r6JFkfgjDVDoAiBJXCq6uTdMXgoL7EwJSMcSYeJ6vf9Z2%2BdtadSo%2Fm0L7yr%2FAwhzEAAaDDYzNzQyMzE4MzgwNSIMD2N7LBmlF8xrAS34KtwDaoZscn%2FoF1EJrHAiQE452n6230C%2F8%2FATT%2FvJAGfb45hSqIRI2obl61%2B68QmfXERMBt0pKN1xYd3S72X5Fa6R3SrVQo8IF4h7fufqzVgDwWaVBC%2FLW7zyq2FRQkVdjgOTKQ75rr%2FiUvkzfV3I6b60jnCNrWRiLKJgbfGh8tLBxMLt2zsRI9Tv59364vkOBUoReRmC2MQAobFS3WDj7CwVvilt8XaiOh3tBbqFYnAbaJscLXz%2B3sVTVYjA9V%2BzR933X7PpoFaQUAqMQNSAIh2n5Uqj8o2Z12okcRF%2BVamKqQdDKw7gUN%2FXTz6Z0Hbo1SYciU6vEKjew0nITdrwR0bS%2B3GeOmOSImrjjIrGH9tYTNnfMHK7EVyRttKSxqSEnXun3VjyiJFpCYeW%2FSe5152o9cfkF9s4DfPd4DHBE%2F%2BfSJVEGlPyVSiSQRYbRgQ7CyLuuhnEVpxq51KzeFQS0HwX23HqRY1jBwrbRkp3cE51x4RkNqiUi%2FhgN7%2BJo8HLJZxTWn8M7W%2BsTBBEp%2FJwNLPTwN76h7Tbau2IzGT6nyx8%2FrQP6k46G8X6DseL01OlEijoCxefOqeupoaD0lG509zKgTBznm45KNeBYTm3Ch%2BynnijS6bhsYHEY24G1mQwusDfyAY6pgG1m%2Bqw8HL6nxoc6I%2FF83DuSh6b2cM4ekkSksjiit1B%2FRYEoaBW1axczmovVIMZQRVBvBkVuc0aLDJmN6GLsuNut1BV%2BPja0OMWoI%2F1T9KLkm1XhDVRBzX%2BYgp7bk2uld7yuD8Un9zExd%2FM%2Fim%2FaVh%2BlY6AI2O1r7Gpp8FKGd0RNZI1OW01FxhwDSAaCVXHuoApVBAj6th8989AMbkt%2BBp2iFrT%2F5SD&X-Amz-Signature=c203672523806156726604810922f73abe0901e80dfb2b96d60dae5043083665&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

1. 优化器状态分区(Pos): 显存消耗减少4倍, 通信量与数据并行相同。
1. 新增梯度分区(Pos+g): 显存消耗减少8倍, 通信量与数据并行相同。
1. 新增模型参数分区(Pos+g+p): 模型占用的显存被平均分配到每个GPU中,  显存消耗量与数据并行的并行度成线性反比关系, 但通信量会有些许增加。例如，在64个GPU（Nd=64）之间进行拆分将产生64倍的内存缩减。通信量有50%的适度增长。| 训练速度会下降
> 💡 个人总结

### ZeRO-Offload

核心思想: 显存不足，内存来补。将部分GPU的计算和存储下放到CPU和内存，必然涉及CPU和GPU之间的通信增加，不能让通信成为瓶颈，此外GPU的计算效率相比于CPU也是数量级上的优势，也不能让CPU参与过多计算，避免成为系统瓶颈，只有前两条满足的前提下，再考虑最小化显存的占用。

### ZeRO-Infinity

ZeRO-Offload更侧重单卡场景，而ZeRO-Infinity则是典型的工业界风格，奔着极大规模训练去了。

---

## DeepSpeed安装

```bash
pip install deepspeed
```

- 安装后输入ds_report验证安装是否成功
---

## DeepSpeed使用

DeepSpeed 功能可以通过指定为 args.deepspeed_config 的配置 JSON 文件启用、禁用或配置。下面展示了示例配置文件。

---

## Example

### 代码对比传统与DeepSpeed的主要区别

1. DeepSpeed 初始化：
1. ZeRO-2 配置：
1. 训练循环：
1. 设备管理：
---

> Reference











