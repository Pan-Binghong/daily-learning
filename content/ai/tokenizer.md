---
title: Tokenizer
date: '2025-01-13T02:54:00.000Z'
lastmod: '2025-01-14T07:52:00.000Z'
draft: false
tags:
- LLMs
categories:
- AI
---

> 💡 详细说明Tokenizer的作用，原理，应用以及各个大模型中的Tokenizer。

## 概述

### 什么是Tokenizer

Tokenizer是NLP领域中的一种关键技术，主要作用用于将文本字符串划分为Token。

---

### 分词方法

分词算法可以根据切分的颗粒度进行分类：基于词的切分、基于字的切分、基于子词的切分。

1. 基于词的切分（Word-Based Tokenizer）
---

1. 基于字的切分（Character-Based Tokenizer）
---

1. 基于子词的切分（Sub-word Tokenzier）
---

## 基于子词分词

基于子词的切分能很好平衡基于词切分和基于字切分的优缺点，也是目前主流最主流的切分方式。当前热门的分词模型：

tokenizer.model 的作用

- 存储分词器的模型：tokenizer.model 文件包含了 SentencePiece 分词器的所有必要信息，例如词汇表、分词规则和子词单元的统计信息。
- 支持子词分词：SentencePiece 使用 BPE（Byte Pair Encoding）或 Unigram 算法将文本分解为子词单元（subword units），从而能够处理未登录词（OOV, Out-Of-Vocabulary）和罕见词。
- 语言无关性：SentencePiece 直接对原始文本（包括空格和特殊符号）进行处理，因此适用于多种语言。
---

### 2. 为什么有些模型有 tokenizer.model 文件？

- 使用 SentencePiece 分词器：如果模型的分词器是基于 SentencePiece 实现的，那么就会包含 tokenizer.model 文件。
- 替代传统的词汇表文件：与传统的 vocab.json 或 merges.txt 不同，tokenizer.model 是一个独立的文件，包含了分词器的所有信息。
- 多语言支持：SentencePiece 特别适合处理多语言文本，因此许多多语言模型（如 mBERT、XLM-R）会使用 tokenizer.model。
---

### 3. tokenizer.model 的内容

tokenizer.model 是一个二进制文件，通常包含以下信息：

- 词汇表：所有子词单元及其对应的 ID。
- 分词规则：如何将文本拆分为子词单元。
- 统计信息：子词单元的出现频率等。
### 5. tokenizer.model 与其他分词器文件的区别

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5B3SPJH%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T094222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHVgdt1EtwriYvUpt1TJhjwTbkvEqC9BOpEIx7Qs6oD8AiEA85%2FqmF9nI4zGGGmUluNw3YoUc3lNhf2C8sYjIDf%2FH5EqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGFygNrWjMx6L1AhGCrcA3mwoXPkS0B1694k0je1MNPkipU3V191OVmzKyACbaZJUYaE0b8Hi7HyFk6CYX4C1vnFnf6U6%2FXVKiTVXFPA6q4VTfnFGaZWiHFKQTuNRX8lm4CycJm8NFgDpWcTxvgyjK5VzY%2BPij1uL%2FFH%2FUyun8j1ufwCAq%2FcjoYwcwGzTLm6PCo5ADpRfxZVaSchTTnYjSkJvDuUzVzPetEAbxtHDS4zt62TM%2BXYg88X0ytzjK9JcADLF26DfBIsFiUDm6tkVr%2BSPQpdP48RiCALifELh3Aml6JMHY0eca%2B1TX%2FrOnT6lidzOx8gEoAiqjJIOcGtRiThx5bawYb3UM8wsNgHjiVbqTToHCvJfiC1f%2FaraVnOBSbFTMLWFu1yYpWQ2c9qaMCblCb%2BxBR0BkUIlPZ2Hw8yz08JVA6WSARXesF0xprVS6BQROT1qoJgALXAh5PAY6nplm4I5PNEe3uJht7bIK66pyNg5f5Rh4FethRtof5Hq3Gp0Rlj6Hbr6cmeN%2Bp8azOfpb5t73nVjn80Y42%2FBET%2BghPKQhnAnixwaojjTlnSFWwKPPeKdtTSvgqdieVOHceOEcgh8sy2yKOEuRSS4Y814dfhR7fjnsKTu5Uz2FudBvmYSZ7y7%2FgHNTQQMLvWjs4GOqUBuYmO1GkHqj6S8RBGuYFK48H1ponwDfvDVPSLi9Eu0KV7woECxVcyXHyoZFkvQXo66EZShAD%2FaUAp14COdJqIGHzDPW3CGnc0bnbQCsSUPo2Oldy0ZcW94bZRr4fmLQ%2FeSNVIl2SDZOvx1d4iLIN3NNvqeRkoup6UfcTLKiOnLN6eXgZLyU2XqgRr0Th9fU1zKdMhpg%2B3Xfd9mghkKxlzdgQx3WIv&X-Amz-Signature=58e3170d67c64f283f35270b7ef28ead3f9c21a136a0400ea8d8217c642e0653&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 小标题1
- 小标题2
- 小标题3
---

## 标题2

- 小标题1
- 小标题2
- 小标题3
---

## 标题3

- 小标题1
- 小标题2
- 小标题3
---

> References

[https://zhuanlan.zhihu.com/p/651430181](https://zhuanlan.zhihu.com/p/651430181)

