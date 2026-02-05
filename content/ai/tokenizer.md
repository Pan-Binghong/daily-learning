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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2RRJQ44%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJGMEQCIF754x9zTyJ4cECC%2BXvxLvM%2FeRJufggFmEId5Jx2ig04AiAYfGid5MCePwhAuBY7IPdgqfmcxrS3H%2Baw%2FkWVZPEVuSr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMRR9WHx2iymOouZaIKtwDE59ubAOidUCiiVAaunIhjWDvPK6Bw%2B0ywNCqg1D7oFHOV%2Bv%2FRYiCI%2FvwEcO91ggCoLwE66tZT7E%2B2q2XdDILKNJ7dc%2FjltrWzj8qdmRNBH5zZ9%2F3vzzUcAo3Q5QtJLnddennTVXcTVNeowA5hhWQtlWPaGu8nmSw3W8uHfSWiyIzi%2BSfTUKMqzaGhWr2DC2IYtuxYYtjYG%2BBsmm7FT%2BE5N3Rbr0qW8vRBYcplSILDY5xvT5KOubbq%2FZcv99kyS5YX%2FI0o6ZM5zwwhH0VuwzcYJGVm%2BN7Sh6jxETr9TAY1KYX5GFYpmXQbHliEVQLvjzX%2Bkm01KVcZRhufrKXoWr%2FGqE8C4L3Nr1700EH4%2BFUP55bxLRq%2BLaiEi98TTZT8b5GnpIyRcyR9QMBU5WXDO8726OGuKWIZf4bJ%2FJDf6F8ZpMZSNwynoFg9dkU4cPVFNGSmCkdE0k%2BBIUnnR17Uyc93C0bWPvKT3xmMW8jHbucTrxl%2FMi2ZoAulorx1gDBRdN7LT64sNJUYGrDW3vcH9PEXeE8pzmSCGp6KrK9C9G%2FOxGRvAPibApwRM17MpZ4Fybnd3g4zFSjdsJKbb5xgTp7oPPyI41cZPaaG%2Fd1QBlCTJS1SkYDE9wLm2BB%2F0Aw95KQzAY6pgFhxUHK5bDhh8yLqkwqVl7Ry5Fykcta6hisMtKQOv5AhK7gTq891XaVB0URnEqHRX6pKzC1wykmqgsEDy7iob3jQwQKCNYMROoy0r6lnf6yvPPWbEaZJdPwAf6VkIaQeRRG%2BvGyZjsWkY%2FtVV0hakTUdsCladu1xsIgyeSzERgR7AII5Y120fZ8v1gq7Eag20B3laROB2UONz8hEnZTNdMBQeC8c1xD&X-Amz-Signature=8a01e21071d5b2259cf96a91572d718a464fa64d0f0927da10dc9b2b8c5b4fae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

