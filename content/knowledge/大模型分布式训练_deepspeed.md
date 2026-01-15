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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/037b7e03-6ddd-482d-bf08-6f0aaf7c57da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WI2R6LEY%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030106Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQDuAa4F%2F5u78n1MCT7fdHhBkrMSg9Zd1d7ySl1eOvkOogIga15SWmHT791TpDsZJNtQR3oD%2F3KN%2B5js6qk64NxEaFAq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDB6Skn5iGGVUEr6HiyrcAwp%2BEgjBTl2ZTA1uGLRVI2qJAEx6DhA5ECZqYKktundqqgmGPVqoWhxC8SbdcJlr%2FbrfW7R2CLrwVgoNl3uWScEqCbRKMzsWP0GQ7E34uEFbV5Y%2FB3PvGBX0qDjYAM2UCGcaMT1ZL4eHpok8sW3nYzBe11ewv0HfHppt4T%2F6sgMaGoke4acC18AoANHLkdfz%2FKoi7KZ3%2FqL74hHJOfA%2BYmTW4Hf87zbmueSBNamcKIouPaOnp4DghgBEjfpsE0KwTXjEN5WzfnHd0ZGDFOhBJyeFHqe3zOJhCZbVH%2BlumCz0yHyFDro2JVRk818Fnv0rekufBocXhpv47ESpYG3xAj17Mp823gdJKO5kZX8zUn7MTS1xDYcXI8pXl%2FJog%2F0R79dXeiPA9FHPduguz0zatdybfDnsyCJ9ht1Ya%2FwAMkjZgU5Rfx1%2F39KvKL0Xc2cjcCLUMQ0lSF47hphSn73PA2KTiX7auuRXhiVfaK3DoF1meUB18YMlSOJzVxRkH4mh6WIUJ7eXflSRHDvOeuTfGxaX4i6Xl68McfspmnW0o2gmsUWM494cyeEUuvX4Y9CrjlTfm2wd80e2Avi%2FHKff5NllPam8SNXrV45i4si%2F6pY6VAE0QNpW1OWWbly4MIybocsGOqUBvZRJWOI6PpaQBVc5SP55GC4JXhC4%2BinTCED6rU7R7meqsL9PJI%2FrVMX0FRKsC4K8NpdTfimjQQazOiVn9dbmKW4HtJU8xw5%2Bvdcsw4TQJPLyygoWjNg5UKt24%2Bv4X2csPX0tD5mDfqOeAADOvZnp9%2B5UIRHAHHZxgeq6TmJ%2FsBmNNnJcuyeOuFaQ4lEXmnSxCIXZBOHvn3RMhiaPfLytudz4MUtV&X-Amz-Signature=69d794993f6b02ced3926c447021c84f3d2727f257a578a3c9f3a9bdba886564&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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











