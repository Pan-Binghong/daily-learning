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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/037b7e03-6ddd-482d-bf08-6f0aaf7c57da/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKDILKWZ%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCl7oNy2UuK8E7vZiCgRTMXN%2Ba3tA7eb3P%2F8NN8GnhRBAIhAJQgXp5QsyAmsQww%2BpcBwhnmIZeJxz318Edvog%2F%2BUUssKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwx0yY1sCsdZK%2FnIPsq3ANTLdA2i3MbXQlWE5E9BuB0zBChNT4qvdyajtMRhjjUk%2B2grYi8qNBct95dRvUx0%2FgvCcYVuczKTB1xcAZHElYQY1xtOPYfk1mJUfRO7uAGs8LOTen%2F%2FqL6BUiQVoY0F04a23pcMJCmPMYuOlPwSWd7ifBnNBdlJhg1m11bexaBAByxlmlSpxLubmCOfA89N7ptcCCXHhGm9bw1qQZLRmIC2IGUEfpU5g50NqHH1KmLu4duJKb6RR2mwSRjDoyuwCfuFmk7IhuPmE0FW98xsU5QE%2FchhObV86UQh14%2BqB7lVV4eawM%2BpH6o6fU0EbchwXq%2BO%2BXVUISSpx0cShR56zTgpncAnlO5zURuM97UIPG50CYBzTAmz%2BDje0GpkxCXFSPOU1BR%2FN9Z83LLThUgOmnaU2KtS3Iwq%2BBvnXdKmiLfALku8DkFufTDg%2FFIBXAKZ0eMNCc3wgguPUhZ4OfjCPKx7wflrl%2FVCDFP51Qhtq6jOtRZGHdNp%2B6n8l7oUhOvN%2FhOOsaB2Is4ynH3Nxij5WI%2FdJN2BPwDvTp5%2FqRi%2BZ0yfu2YIRzQJA2tuw46fGcQQ0PSQDerF4U0GLch5ZKW%2B5igWjtiGxsVPNDDseYeJ%2F4aV62SNY31jQhKianTLjCR8q%2FIBjqkAWDuiBVD%2FvshNs0PE1rHFcTTR2YpTwYzTTLeGHZ4vmeLL6hIfX0SLjiFtY%2BS74I9MqV4P5gmOC285ZpSWeS0yKeIUB49c9OH2Omv8crVw8%2B1aUrl90FAXSA2WHtvSikpfZOeFK%2FsgTeL8KY0uQ2ucBdQ8LZbl1bMNF%2FPijFaXz0RU344HtLLXD8x%2B7%2FzsrgdTsCJaYkNBGX21FQ%2FkLde7GwUFoqk&X-Amz-Signature=f392ad5e1e611c713e4783ce4c4abba222dce22e8569edd4d234a9d61f408f86&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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











