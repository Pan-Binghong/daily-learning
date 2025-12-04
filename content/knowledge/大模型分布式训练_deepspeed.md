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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/037b7e03-6ddd-482d-bf08-6f0aaf7c57da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMD4ZRGW%2F20251204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251204T025022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJHMEUCIBt54GnRmP%2FwN8KF1P0Ap8TNUoFRO92grca3866AeAlgAiEA5QwoCKAAXpotlV%2BMDe9w%2FVn9OveeR3AY7zsZVV7T5tAq%2FwMIOxAAGgw2Mzc0MjMxODM4MDUiDFc8SB1KPKcsB0AFWCrcA%2BKT0Qdpx1A%2BVhgKiZsVyegBJdoKhGA1Hbj6fIpaC4fcwTpJKbWi%2BOS75FdiGaaHtUY1PForQo5TjMx3IY37rIINKabS2Ic947Cb%2BVg6u1I949VnJ3e%2BHxhKAMdrV4YBhkj4zfqeHWWsa1ZtEnXDXa1vaGgw1baO%2FMYSZYt0jlMO1wTKBpcafTpXAWLpyk9pLH11z7xBLsyfzB8j7oX67e6Kj2Fui9uItwGIe1b0vRGgz5EtCrtYL20Ng0wIf0lmyJuqSVTwgouUGOwSQqCJS8ZgBiZoor8iDRzfqcB82qrOedztfR5QB7%2FE6ujSL0Vju1Ch7xJxel3I4rQfBD%2FbpzXoOgg7piTCIgXLQJoPVhT4b%2FgHq86gBcwZ3TAgDJwtwQf2x%2FYEn2Pu1JXwkAODBuq6aia%2FC5OWhL3mg9Uy2X3w28aJo9ULeMNJyXt1dXbdb96ZPaDMvTBrroUA1eezXihU9SC5V3x6WbQFTh7yehPLbAd2XcJBdpOS9rNaiqz2qoVVbmgGTlCTlzJGwxknWTVyVu0xRbFDz9qXt4jcnDFBn5PaiKoygDRvgK3IprOfydJe8B0dvS9arLGzAoxk4CTQ6Xbfn5pHFtzvxjqCU5Ioj69zbgSu22%2Bu1TatMIfVw8kGOqUBKWTinVEUuW1hb%2BR0cHZ%2BD5ILXzO41ovQd1lTLmOQI%2BAg3PwXUwXGuyNKl1jjaiugatezfTkIpzTSm%2BkoKjmiXFTlOlwGvy1diRD8XU8mvb4LM6tJMUt4y65UkQQEj4alU5dW4HfZN20l0XGJkzgbiA0tz4gT2SemN1QQ%2Bi83Cqfzu68RhuoE1P%2BM%2FnxLpdRTKhY%2F8k%2FmCt38QVq%2FgkcbCksUeBz9&X-Amz-Signature=440d3d4fba2f54190bbed682086c3e1e0c88ce1dabfa5ea6451dfd84be4fec4a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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











