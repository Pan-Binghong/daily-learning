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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/037b7e03-6ddd-482d-bf08-6f0aaf7c57da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZY6UJ2IY%2F20251216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251216T025547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFbhHh45NeFq92RzDZ6lqCWpoPavV1zj0ABs2oixn8%2FGAiBqA%2FE3l2%2Bk4%2B%2FvapzVqqsjG02EepHwwLo8ERZ2z2UAyyr%2FAwhcEAAaDDYzNzQyMzE4MzgwNSIMp%2F0DjvPd6E%2FyPGCtKtwDhVnSbtOyK1VFYG75nuDvpi5uih4FVdYhwOADJoYAGcShjlq8WIs3K1ix5QagBw5%2BhE32uNIpOIL1B%2BIvN3e8AL7JbWJ4odLs9Ysg7YMeuxY3BlBpo4IhrIv%2FEAKCnhP%2BnsMrx1ovBahueh%2FDbAtXsCJhBse23siziJ23LVHgDLSOYuKkGlMzLFsKZCR8VY1NKPXf5AzkUI32fm%2Fk4bci0Ef1TGqBZLOm%2BzMWiU3fmY7IGCdw9hdRqp9PHkbWFOF05AmxtO0oL9YLBLhlUwdB6%2B6iAPyk74Mo37kocXHw33qeNtjxT3%2FEgPusvCHDK7Zh48qHqQlHIBSGzLg4pGjMCN480J63rc31CGAUPhWZjukZxClLMXVleQmbOriJVbcjQGAiHOCuBBqcskLZw45NIOXWWbnfK31LVY%2Bgb1XN39IBxhlT2PJ0h7aahTQlzg5LNcd63WI%2FjB9og9I7XFLfNI4x7yE7uZwUDLGexoEewYSoq%2FY8%2B50DfyarQl8Q1u7qjJaorp%2Ba6NoUGvkU%2FzxSIQwa7OBFB4kMZXMtWH%2B8y9cYvUltWsQVKz7bcZLNw5OIp2f6IDEKHPfPyyF%2BuJCyIj0r9gkmy9bfCplhHUKQlOhXbcYFtZzBtIWPI4Iwn42DygY6pgF%2F6qjHSl%2BB5el%2BvpZzss9IvnfVLXNa1gAtd%2BjXmzEf52nUHuJYoBrL%2FicyUScAsQPrJuvG9GTTljdJq1tN9xBayRiIPqP22dHatm21K%2F4ASCYRCtAg6BiR4r%2BniledRbbbbvZezozZoO%2FK%2BG%2FaLxqySU5iVD43VSyzcl27UnrKRQ32Esjid3WrnC0%2FiMMiQNSWHVebddvOfgcI0jWPamIhFJ3AGoPf&X-Amz-Signature=3a3a4d33906d99cc650e5fbebf90a1938b9abfd29b71fc3081654869626d5059&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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











