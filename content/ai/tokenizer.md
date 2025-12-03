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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672QMFKT6%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T024836Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJHMEUCIQDh4g5ikp4hlZ8uT51bzeN7nulQVI7qp3INa6Na1QcJhgIgQto1gvsGnQ3scyJ9aPjvz%2BNVJuzd%2BysDNe8bQx1XRPEq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDAmr9fzHG7P%2FTgHGcyrcA8spBLWqPODAa544CbYtTEnlVYcT3LmvjV9YeOAmm64Pqf3sTJxo3RJe2hDcQEWY6lZJIssC%2FLA89DtGzxa1nXsH3wKqCbjFuNMcl%2BQ0r0pvtflNz9RelNATu%2FZhuSqEczYvmp7jYPSstc3iR9Gv5D%2FDuLja6wLbCiGl%2Bf4r8lGIBkjfq4wv77%2F0dsDmDxWx4S7x8rG5MXH0ke%2BpIO2ddGQSCW7ZOMYxCwshJUed2r5e96sUoE8fQOVT9tyrVVQrZtlz5G%2B8ASEc1D9%2BFiHX%2FdXmtUUUi6LczOYbSMUPm4jR3%2BxBT48muTPQh%2F%2BLwuzRTtA6ZVJcDVfgbxnCmZbclIG%2Frh4PWK9dw3geQJRQYREbm8NrTCvwRWaWUAfzzr%2F8MqqNmdr8OMQsVrYxfKlLCasgF2u%2FiFOb3aLiTaPeXiHUsIJTtFkH6eE0eZKxa4snq%2FQLHSMwkpzLk1i4eNirkQbcMdaX9ybMFcBuMCQe%2FxeRjTIEgch7JQS5Su0ropXRZ%2BChjiqSIMceCGrsLQHFrKyoQ6VUeX3N6WY%2BPIGB%2BtCFe8CqPAovTxsK2nqB5tVXseWqG0Dux9whtXtMgdf%2BV1diVpRNu0avoPIolBc2WiUVdHdelXEqE4Dp2j67MLSUvskGOqUBM3lStiwx0iWh8uWPLWC5jsh92vvgLAneeXl60UA4AKSR%2BwMt4XgvE%2BSEpOG4Kx6aQEQCY737yUdJ1wuZOU7bu34%2BUG6Ye%2FeyZ96socoTIzxCeNsHFtUw5BTwTc8cAVKbF64einrqWqT0mAA4jr%2B5sKrYrNHWLNj0EY8nM%2BCBz7BiwVaBZwLEvM0ZWe%2F8geSC0fYpadHIOXbspYr9dDc7ElUvgW37&X-Amz-Signature=3e8d297cbb663c1bfaf066110b9fd386031fa3ab688c18a024c54deee1d3eaa3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

