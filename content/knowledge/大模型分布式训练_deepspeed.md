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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/037b7e03-6ddd-482d-bf08-6f0aaf7c57da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVNHFDO6%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJGMEQCIGQIjKZ8DkLmyacIuHa27UqMF6wCkAnuTYrJ03MHLU%2FCAiB%2FpRM5I933cLcQ2Bw9jRLEJQYKM9GcNk1ah5cPerQetCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiCZmSwGSEl9XGLy2KtwDcp0WB3o34rRkm159KTz3bdBNZBg0pE2IdMfA5aLqlouzzMDYAXfSaGdjpDQmduuMuqcYynQefegKihiZzyTYnGUVOJ7wfIhLKFO9k0KoNq9ikbvRj0H64Jabj1dL3je4F6kYk1ICBbEwcE%2BbWqpp5TcWa2avtvFS49PAawPe9x97bVDGpHcIcibio44pXhpahQo%2B8W1uEx4he6%2B3trbnEHQoolUOAA%2BG3PqPxJ5UiK7xMf6TulnN2JEn4TvQmn%2FLr5ftHGVBBHi%2Fg%2Fod4X3wvfMX%2B8xQRzetG0pOmzo4xswTGbPyiGBI%2FRhb9Orh4b7fl8LQsY6wuJfIt5sNIoCwU9qvJfcJOTas0UPBmt8GvDIGd%2B7zv39X4O4yFKLy%2Fby8MYmhsPSq%2FPZG%2BQCNrJp1u%2BQUGSMJLQni5KxDnBg4G5VQOOsJ9f44cNLW0Tcl7UbWaAj6H511uOCmkTO7g0m54ypZp9BSrM4Zn0iHs%2FaJP6tu4zMu6VYkjfJJTNTAsyl8tIQ2kexuEJHySHneQdiIsXdHt60dXyenHzCwyR2KOpe4BcW9RlV%2F8lgEoxSnWut0eQFw5A3I6QqvR5NVFi%2F0Ae2KrqtwIVIZoBX7Z5aYiFgWCHjxbJMTPqXFmKww2tfFywY6pgE6WYY%2BugQ9E9U7a51fMv%2BSg5YtmrxsM9KZGPpuSnh18dSwz3IP%2FWj2%2B8PV6JmsRDMV%2FP5iC41%2FfRr8jojrcMV3sC8A8Nse7jxXJF7JGdvhzpQIeZU9ma9XfgeOtcOXqlgtV7iYkYsBPDRmbpBJhaKEH15zklKA9OmrkWKnA6SoZWPAYIcJVA%2Bzrv%2BupBNs8mCYR6YDqJ5WvIchLkLnWlcrfQih9Mov&X-Amz-Signature=08bbe8fe9d6fad6dd8d3dc80fd98b502072f2e7cee9ea4a8974b663b3fd8816c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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











