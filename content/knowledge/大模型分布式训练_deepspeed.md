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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/037b7e03-6ddd-482d-bf08-6f0aaf7c57da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4NPA3IR%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDkwo%2BUflYDT5NVq%2BBOzeilfJDfSQi4n2Hd5eeBXCXazwIgCddZkEN7gVCUkPNXFpfhYbOGzwCMiNI2KlsXyQoJx6QqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBWoSbx66QDNLnh1YSrcAzgRU9sTeny%2B4UnEP9DKvo0fRnoizVQfxoIFQVVWqDZluk3At2eda6E%2Fh54wfFNZOrowBPNGz4ChsNFtBXRzYbWX%2FOm9b2nnCfletoaHDiNDx0ibGoDLMByGk4a5oDl6c5UsZkKsmhvn66vvZ%2FNRQ8CaVI2VapqTv5Jn0janljxgguo4yI45fidrnXiKosBcMntYluLOcfe89ErtJE1bbpCDXJAvYOiaQ7ldl8%2FnbI73MIRFGKPUhyECOEUzJolWCp7ZXWzXIjG%2Bsn085%2FxDxkwAJvH%2FPwtV0%2Fl4UuifYhNIx8SLHBqsKVQhKge9cgC2isjTQ6UUoAQ6i9g%2BcuB8qcp2aQglWMHNrXakVeognGw6R8j63TWSBKqoqi7%2FXLvOHT9sMGZ7%2FE8me8rkskyQiWdx1KAx0IAQ%2Flz3Ro4bTvW%2Bw0Y3DG4B%2BJUeaimHOtNX0reKtshY0D3GmF26F%2BMMjeRArxeMR5qiKK%2FCml0bPBIygulp4LSLqRQAxdGgCbo98KtozkHHA6i18tuseMwSYYZ%2B72q%2FR1JiOcW4LvcM%2B3mZg5PZOl0vb85V6gFYTSlD0dJw%2FiISXjtKw%2B%2F5WkV6TLVbDsZ%2BupVXnUSHIJl4GgEFj2cF14gNmgQ4xyozMJPRvc4GOqUBBqLa5279nJfkAxxSgAJSl2KLHVenrcnJN91li6Wg2JqYCOI9H6zD3XF2zr%2Fx2w4AVe3UB4QXlCr3EdgVwNp8X7i48OL4qrCyHEGKyZkTEBenmPbvQ80v%2FXdEMUwEemMprRlzYb17aWO6n73CS0QMiNrAnU4HN9paDccA7LB8nQ1GU2xO8gUS3nrkWZCS9KSUTdMczi8avP%2FmTA%2FdcjOu6HI4zXpd&X-Amz-Signature=2c21637a404653ce9626843c13a070d52ab2f8174b6d7c68f949dd825679da5a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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











