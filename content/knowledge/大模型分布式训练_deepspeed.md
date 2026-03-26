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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/037b7e03-6ddd-482d-bf08-6f0aaf7c57da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2ORJJ6C%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T035049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWBjl4Ztcvr8lPj%2FBr0Kewet6EHx%2FwRv7APd8ZCFm5OAIhAMbqPwQK5Ymulo8U5lrAr%2BmNowOCKhCb5A93PI%2FYi4BqKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyPOfGIB7yYBBiYYGUq3ANV%2BidOdCH4FZuRK3l4VZcfIwiSRxs1lxQFA7cD1un%2BIx0hoqR44RYK4BP6OlpA2zjZRvd1lYhn5XFpK27k2r3y1E2OZ7k16zI21NX4Zmmn8ipeI1TgJbWhKKxyVLhDkBupWB6KESoPqV%2FcaRsWFiNArgYD9thMFnVkf9uLmMK6KLxlOXmuLOdaDr00042GIzEEsg9plTPYycqI893fLxMjyZvbKdv3aZ1ZmiMm%2Bi1%2BncjQ2bMbR89lR9teZLroOfIpmq%2BSA53nbG0I9HoAs4d86SP6GENGqNEprOyLCX7Ql0Pm1ndU2Tj%2Fi9%2BrrXOfC08XHOBHKckMB7sV9mrL3aPVHoTN64Z10HU6Dt%2FNBipFC2NmvcKG81kAiuPFfwrIQqXu3QBzG6fAA8hQ%2FEXMd7eL8ToEWC0yWBKRMk3ZwmGQ3vDz2q7u2RNZ5Qdx2sjDU0KI%2FEy7TpkzAZKjQcREDHLUD5FwcUEvTs%2Fjc25N%2BRg%2BnojNc1jSB7UIA%2BxdrXBYkjRhD3XYgnWrP%2BfIRtYtyFtcTm3IVyjxcC9fxvCaw95Bet29RjCYcJ0zljmugOHTcK3xnMER5%2Bn36XcxA0vf3Ee0aRTydnVHYwaaERGxyDHjdpFYYmAOHc%2BP%2FUIUYjC0yZLOBjqkAf5y%2By8tNOelgxcEiobFallCJuVbioTWmsRjhnwFb3kKGVjoaNFUm8k1Nh9dDgw19BaOLqVa1aCFcIxjcQoXqJD%2B7Unibd73ZJ%2FJVsQG0ZeVKxGcBvnDBARPkTHZ2bIIeR0iH25Wa7sE6viCza%2FSIHIhl0i0ApHDtn%2BCRLjKthV3EPJJr5g%2BFjMUwcucIh6GROI%2Ffo6h3NSXEUmf6%2Bx6piS9F5sp&X-Amz-Signature=8fbf36d1bff6751a7151718beed0c483e1a20fc79d3e3b4827743a112351dc0e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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











