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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/037b7e03-6ddd-482d-bf08-6f0aaf7c57da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RMW42RX%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIGuFY25gM32reUnfLSnJ0D2UqtZa1QGfWl2E2EOkEyVoAiA6sP8rz63X%2BITwlhSPiIEhkBrl9B8kk0ndt1YJkFjK7iqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTKa10u5JKT0L5sYnKtwD9vN6rVj4Sq4X0cnSSqfM7vIipC3pVT1L6rKpqA60Pk4iGfrRCPwfgOcAubF6kxzmVyJkIr2HtNXb83qc2vHHVrKbjJzNAmpnnFGWeuO0Hh7vCLQ9TtJYABd5P3ukY8HPstpUfe5V9sSGm8m18CZkt6Z%2BBTB%2F%2FUZALR2A%2FuFdbAYU4VW18WWEErAFvmcalZ8CJa34jbmENIdTw7iCZoG6aYYvAKw5qJTeSKHozhXksYeKQzl4i1%2BoZKR2UWzDNs3v3pS%2BQvr8ihSXVYzX2f6rV7HKv9Vpcq8xpQH0E2Y9m%2FedNtUorQGlaoDnEq%2B0Ljh6KQ2kSYc5ylWTWFJNU53SwuqStaYVLBTjVhX9sE9x0ct%2Fc3P2uO9tCzgDe1kB9HzWUzSFAlWA4AIjDSNYlCM9y7ZlkoHKnV4oc1AQl4vE3WiVNiMC0OTJ0kpcAvT9P0M9OB9f2oypg272YvTtCLc7TCN2in0MbyFI95tqQxutbQlnKT4D5U4l8efGL1W97Qhhj1kGLL56YuL8EX3FLwsXp%2Fk3BkjGpfnxPnWRzsJS28VyZ2ezjfdwUSwcMg%2FzwD3PtVAL3LDwNKu6BjqShmIzuqYzWr0Q0KX7wh1cdmgIi7Ix4U1%2FDPKBoFdxUTMwnNC6yAY6pgHZr0g0U35kmRLPZJ1CScgi00VSqTk7N19RdxYSG19x6N3C6dF3xsLPL9NdCrUIyQZJgJKRen8K2TtHP8UkmYYZGE%2BZRk15vOS49pVwbsP9oCUn83lakir4OVS34sD9fbBKjjSin4nFfQxhZLQ43KDniLS59FNcEKAojsrmxxwpv11%2FJE64Ro1Mha3TqvEq8Z2Epu9z2%2F2SEOxlLCOc%2B8SP0WexWWdQ&X-Amz-Signature=6483209cde1514e70333f1bfdc2221597fccd3868542042170b8f9dd42877cca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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











