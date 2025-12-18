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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HVEYW7V%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025114Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHZlya0rXIvil1DzxcJvMxpAWk08U99Ocvnd0fxjrIFcAiEAh23T8P0PkZAIR3f3bkU5uBZKPnjafHpx8t%2FsXdoFivQqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMU3k4pLsF9odSd13SrcA64rD813R531mjyAlkjEaOzA9TTLAFFrxAbUYAgWHZRugB4RUe%2Bg5vHPhcd6Kx83%2FDqDNIlvUkWKklZN7MjpMWD2Hr8hbXQRzjELr2edRAm6ooEBoJcwxywQM04nCDGh8HTJh2w1ZN7bfmSiy%2FUJQxWeL%2BcTMZe5YLfBNSlYtBTFXAjWul7Du%2Fsu%2BXCsJ%2FE5RZT9%2F8yUXc5Ou09%2BuVStjTy2sHoA%2FEoTVtHVk5sixWJ7nbiHoV%2BQcb%2Btw3a1tgUgbc%2FUvLuVYzo6rNgNtDkfonzi0lXi3qxod%2FVNvQ7kETobgHHwgoQQRTu7Aom6oAsZjbEP2JReM0uM02OuzEaHHMSFNCYcpJMpmyzbCAtRuroen1Pz7FOU5wSh2ioLCFMY4KXPB0RrJzEl631dMg%2BYiyHl3xeerERmOjVA2tLoeK%2FAOR4JaLJRPDQBedKSE3K78zrmBAIISZxRMVZ11P9apvYy3ygrmTMgolYuLe2c%2FaI3OVpqC6udSsT%2FL7fQYxhpxbHwbaCQpEsCN3Np2wPY8o1JBfqH1iq1sfbDqD7XYeaneVT8%2BKqO9cDzym3JT8CJJKOuV48pNnSlX10I8txfwTxiRcCoxJXDdT7QQcbviWfSXTooTLq1j9VwqP79MJPKjcoGOqUB3BIk6LgCiiWtp2f8CWmVGww8o1cL3T57ONopSCApX9g9Ql6UZgBc0pukUG9qOJr1dcxUY31sRecmiBWrNP%2BiKwlmx3Kw%2FfvcR0y0%2BsKFCotIa7Php0%2BvguGjB4qvGQaIe%2FtofiCIAS2x7ynTEEcOtKkXSlzzVWsg0Ob06eQDTn112pS96IYalTmz0QS7Gre7ukdaXO4oACVuZVKwZ3b7gmrixXo1&X-Amz-Signature=b6168a5f3bb3e4141ef36345f845794422926a7f3e36b28cf62df6c64e26468b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

