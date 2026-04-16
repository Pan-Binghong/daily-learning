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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666BFPFSDR%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDSNxzmOnjMiV3SVtpFvKL1ceTQL4kBpFPkifSqRwr4jAIgDy3TOvTGw6NOB%2Fc8hI376l24Jn35%2FtvBcg5gOZz2z94qiAQItf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKMJkYWbkByNed3XxSrcA8zcUN9ju7rBAC6vOv6hKt%2FPY1kbro7JkUdgv%2Fi7WEBIx2RXkKWwS0h6vXA0POyu6IIFvPfaZ4J7wsyILRgGQ2aEdjoQghmO9%2FbUG%2FZihFJcMsGQhvl%2FuYk0BSFMVJdjHohuWpM1Q2x7wSHwwt1eA9K2lcL7MGpLznm8WM7j6bCySdsxKMkr3XoCKwAJlbnhqTDIBKx6mHyRI2panTalFiLnu6kNjFIuekn%2BOh6J7NfUltbfybtV4q1Joa1msR1Yk3rVXiub223wZyywTcqU%2FGshlGszZBkc5VGxkySXoV%2FAOUlZj6U6eYeFcGOcuqbcZ1ydeioGNNuY8RlS75YbyCPnvLL5sQxI19fIFZpEo%2FiVnQIrmNDcX419evomH13tN5cVHrZqEVm%2B%2FhaltPSObRip9GDn50vIzLijZXbTkfR%2BvQV%2FW54dTwi4vTOhHWjgQr54wZp4Yz5tg%2FHQGlCaOKwJHLDwT1wXbWyQ7tiocatYEwGRSFj%2B43Py03s1P5aBju230XI70G08WanrQYHNW68U2l5zN6cNrZrVAoOHy20RhYIb2zoDGN20Tz3IwFemwsHH45cso8WQGhZh9arXIZCpHmcxI33YZ7s%2B26kzCHiNhCgUN2O9IXHUeRC9MLm0gc8GOqUBeCnTb48VwkP0E9UVQuybXtiM5iCUcVt%2F0u9joaogtxszQy8qcK7Lefq1PoowqgK0rD1Jyzh5fvloaK9cWzyci53kkvvA9snJ3Y1Y%2B%2BuatL8zY7zhGqnyCbn%2Fuyz11OBjE3H4J1lWxoB5LrUhiQFllMXUfJ1k9SoKK7OmS2iN1Qo9N5aQ6kt7AwrNcGYFDmhTh%2FQnP%2FvpqVdUglLISKvVC5O1oqSM&X-Amz-Signature=f704c71c5ba9ed89034e58b79427792a18f31de0e42b6181260595f9f706e3c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

