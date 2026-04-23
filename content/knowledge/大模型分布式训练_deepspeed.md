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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/037b7e03-6ddd-482d-bf08-6f0aaf7c57da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665L3S2YBQ%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsgrGbt6RO66mPLFgzG7dMOmXxaMnM8aud3CRL5ood4QIhAPSKzgRHAl9fmeP2v0N39FIZsKihmLrOBDeVfearNCqnKv8DCFwQABoMNjM3NDIzMTgzODA1IgwdFbbXPqjhZIx36mkq3ANPKhZPRVJUoaPLgS%2FV3i9UjmqmMmcmT6amSfZzHwEW1xKa%2BVKg7%2FUB%2FN3UZ0p2IGVXaR92ezNxLnN2er%2BAAKRN7YkyCO4Jd4s7jNCa05rp%2F%2FGKupl6WDXE5GiEisjrmV1Ru%2Fag8sZeb9b7OvpYyja72y7HavuZE2cIRRBfNPYSeR6DJltTR4U1QoXpI7AsAQD3Q5eUXv8gbVbZ%2B5YWEueA7NHhvEBwUFpGeyX2UnS9CmknYo%2BIa7sopXk78Qu9ZUClN99Ymsdm0uJ89aXwjf%2BFZSBtVW3yP9%2BiZ8vG2PQCxu8eXr18igyqDMohUV7HoTElDBhszfEKBl6mlim7iLTsaAsIXfjRI7xyld41Trequ%2F83QQnZGXUt%2FIZm6GqNI12fb0Bo5Elipg67Bp7Aa5n0jSZpWOapgAdeW7Z%2FmMkIiN%2F7wX34eEARm7WpN21LgpsURpAb%2FCzWodQWqVdeSwE4EJKVuvrivZ5Av%2Byy7LaZ6J3CM5jCBkFDOxm7y%2ByRJxINbAvBKf8J2X3qs28DtGFcxbXK3A4FWZ%2F1pnVBChEphIxGG63JafzDrhtGnyS%2Bdho%2F55j2BDa35L5SbR3qflR%2B6wp58h6dqgTvHICR7Bd3bBYoGXUU1PYpnrV5NjDYoKbPBjqkAXRcjlYDlDJSdWLcmZLPQrPty%2FHVQ6FnZb3aalBN%2B4IMAvbxyHu0xLUeK06i7lrLBk3VL09ohOpM2LYKSA4lf15SK8a1o9I2TZ27ZgAhIeJV0jcoKPPYNGPVB7qRytSSOMNprVj%2B9gh16ZaiIvuHltRdwtyvtMOHMGP3udFN5uXn1R5tDxZXH8EZLlSztDOmV5cpTWI5yFUI2Wcoir5hnjPsS1yD&X-Amz-Signature=1e3adf59ac2f8e7d7f8091e3ff15c837f3a70e6d2f75eb1778e1c7d61a92445f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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











