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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466STFTSSUP%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIDKCrt%2BpM4fs2PNWzupRhpUVAxZ7B3nVlEaXrjN8OVAEAiEA23Lv6HLBYJ950Lwn45lFaS3qyUswaYtW0TPS26KJbccq%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDCKPNGZSX48wB%2B5x9yrcA3bz24AvU9CgElrqHxVNX%2FCV58EHB9%2B6sZCkpQGsX8iPGhxytrPeMDkwNBXASRfI8rMKlkyqm3Nqj%2FEzNdp9HHxOqklEwr2bilFXuwt51a1gv%2BGwlnbFFGgAu%2Bb7R2YO0O1Uqr75ph8TQXyIoLv62%2BbKNDAFQLP8wG3CWoh1hwgby9L2zYYKOCDnGEHcw3FWj9rndEpept4s%2BlpVlLIsBeXBU43w86wZyM%2F%2FAsCu3iNKGxB2mpG66vjX%2FnrC1ApwbtwcW4Ln9lf9%2Bmj1K8WjcNgUFxYqW326zn%2FY%2BAlKv%2FYud3Kj8ZRssjK%2FhGQE78EY9g1m52LZYu7YuIi2FI5FJgYOHheBr0yJdgnRSmQIhk33IiVVopOeLeebpD88oO1VfrPq2dtSASoaQV5WbQE%2FiJRzK9tQ4xjBFcEfVEXd%2B04GLdTQL7C%2FuJDzcCE5d3sIpLn820ckbxbGb5bviUp4cKXOvVwoX0JfQtIEI4rsHOc6jDfKjb43%2F%2B3UDCAfms81OR%2B5m6S7mTN7fB%2F%2FI3DZsrZM8WwEWr%2FsTzvry4azR2CSj9QyIclohfED8rvK8knJYSHUD%2BE0u5yfVLRAQtAf2IMTrJCrexrul9A4P6UkS%2FL0m2aP2BYLlFBO4zlUMIC%2Bos4GOqUB7wekB0vYExIAFkAvBYnS12qqspDdnyh4XP%2B3Df0ExEV1wLT8wGT4qZN7%2Fw4dy66DNrClfKdH5GiEOTGE80%2FuaQu7WVCBcHo8k583VZDPDDuqUDpDMLPzWUI0NAl7J0bgXT2%2BhUJgPPOhuQoEoR8g7u0gQUf%2FFY7jFe%2BWiNyjD42Eh8QnLDy%2B9zyfuP2avpqBIKR%2Fe2FvcpGnxpQDbxnZH4PyJa%2BI&X-Amz-Signature=a2d0354cb03c645a771e4a03f7b5a519c2f7faae8c3e58cd54ac30ccb150be1d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

