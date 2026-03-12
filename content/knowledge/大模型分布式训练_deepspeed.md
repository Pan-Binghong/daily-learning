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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/037b7e03-6ddd-482d-bf08-6f0aaf7c57da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2JD7SHJ%2F20260312%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260312T033441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEU%2FHa%2BUS2Rz37WSUvGabsAb0Gagxo%2BxWyghKYdCaPxdAiEA55DzKBBJoqehd88Her6rJdXQtNm76U8Zv3IQRKK5vvUq%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDFj8XhtaDRW2SwCnGSrcA%2BZAuv9Qzri7Q4NglS3gI9K0wIUNWVS%2Bzupe%2BwQr4%2BsWLPJwq8plyCGGQEG9Q5RhqGDUisZ1Koqhv7E9sDQ9NQv5nK4HOmSR2%2B46jHk7SJp6IqEmLnNtBeC%2FWHuX9HYFH0wbAUxPSsfjlA0t24pI2zPWJ6QOemEeb6WMTNx1vG7DsMfO4dNrdjbGwYFQ0kTDZowsPrIkg9h3gAX9JwB%2BsJ4FCjEfZjij2voPKjbIIZEOw4rYZE%2F0YSIFlJbS7N7G%2B7A%2FOtBGf%2B4EfuQ%2FFw%2BJhrDdqBuFTiHYETLhprOTC4C09xjBFbKpgao7sW3lKtePRNhQhirN2rKjFZzZ2%2Bn7BWkTiLaEj3D0goAjv%2B07EnO5h7LoaUzz2Ide7xD4sMexYaAs3GQ87Wr1Ce2zmUU5udu6VZ7EG7clqap5r9zwWxzB7%2FFwGWDwWfbTYfHkd9HLIxnvKoWYkk%2Fkwrso1CbjTbTSR7ROvofBOF422vA6s2%2FXrhG1EEmnCN9%2FMvWuUghrOdcZip71M5AlaHpeDoNoZQs6qBZLQPa2ZL9qT0bynmiqvJDa9BXDx0xjgEFG4qPX9B%2BTmOiQB80KKVCtggGMs1gcAaTxoydRxZIvlY%2FOoYRzXKmhisitD3Bjwzk5MPmyyM0GOqUBOTgDtHrL5VlXc2EMzPdJq1R371Kh0kOnPr9lMdq43lDAf9fthsCOo9uiywXFNAH9nPjJiG6vzxLDZsrR4hc9fH3DZ7KLv0VZolOgh8JE4hdDCW6g3HFj2SDOelDzBnqg%2B5KR%2Bccef7ZLw1F%2B7ql9QTCG37o4EkU37HiQE%2BUugRAIwhbOCs6VWjNb%2BygBwshBiai81zjDx4KGcFV%2FOwuk%2BLU3vZJT&X-Amz-Signature=e8202e0fd5d7c422c65acf1dd0c0b3c6f2c889d41bc5ce87309eee37ba56d868&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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











