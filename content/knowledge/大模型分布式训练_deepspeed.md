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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/037b7e03-6ddd-482d-bf08-6f0aaf7c57da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5APKQPX%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T024907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJHMEUCIQC279E6eRkQe3CjlBx2xrHlvrddVLimgnNeas1uHVwczAIgOP3vkCmSKQvUypvL1ASdDdbzzcpPu3JF%2Bu8mwWwfo5cq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDP0vIRdNugOnkCde6yrcA%2Fqwdvybzbh7DzKI0vHWgoUUkS8Df7I2Fgow3HpY%2Fcnp0FMXvQW0F%2FN3f%2Fn6CTc4ZRtiFYqUsWuQIwAsOCxPPOpkN5pQ%2F1rld46TAD1DlExbXV75H1zADxrwClo%2Bj390S%2B1YhSDzDmmGNgeVZXGtpPJl5T0bPdBcQHdCqe%2B138z5ywkX%2FBPf9iYtZ9XgoxgTTn6AXq4dPUYuyOH7vgs4VtaD%2BMsA0Lr4bdplK1G42W6q62wXx1dYboLTXZi2zDWpQ5KgHluBRj6p7I71l30HUScAZb7wFDcpCmDTEG7cCcbTBAu8Dm0rtUx4QNa%2BJrnu8NR7%2BEp2MkyXFBenOs%2BQN72awnPKxYkPxSTIi4QQhFL8Am72XL%2B5SHUpVOtmlR4GLgicloHCffWmZx5kGmPwtTGMEcyoc7bTJJTeHdCwsW2ywCBIDfYCseNspLoCryxHnBqqcT1wVci%2F5vxPW39HenJvCGtey0HhWLzsVMeBYMTAr6Y72fE2eOwKGgZzbodyKR43znT2cdwYQIIdgvBQ49Cf4MjZvkTFFXQKQSYkZ37F0d8gEsCZqihteeu9nHceBaTgiP6FQZuZX57dAb1gpc%2Fo21FMr%2B1j%2BREGb8CioW9Lo0RbW%2FMbWcuSrmxhMNaWvskGOqUBYaSDmd%2BRWdBSO3RkZdF6qoS9w%2BWb%2F2x3aWGkelYUpb9LUa9v7HEAAHJCdo%2BzJaLMXWHENoldqOLYHE9gQmVYhix%2Be%2BbipRs9FYTVtnbR%2Fr7VyVUR0USQeOTYoCezA97Tc7FrcGUyWAzGH8fj%2BUW0B5IoWr4xyzVzesTuT36ORWe9BU9L8DuydS6Y6xmqagQcYZwJHIG5Kq0OcO%2B0EVv6lllZKUHg&X-Amz-Signature=c9b99b9438a229cd0f189f1be6a96cf6b0da60f37bedcf8ca103b88328a0c44f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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











