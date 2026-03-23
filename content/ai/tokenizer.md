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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GTNKN6J%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF3SqrafiA9AeDMrJ59q%2BY2eXHaGUE5NW4slSj35%2FvulAiBqCWJmXejBnz7P09l9eFoCKKGdsQ33O70p77mPjhP%2F8Sr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIM18rXu7GzJgeEnJ4qKtwDqZOe2iJMKAxxCM8g80GzizbleDyeeYJs9eBWLcNKkRSSAsbAHBCdTqWLPV5WvmAzy3IxWdRpiQB%2FoKg1TdkLlX2vrK45lvmDiDnqhJb6QTsvQtYpIzsfKot3nmsXAmkxXwvz058EDmAjhAC8keC%2BXP6DnRRjLX%2BXZ4hDvaXnm3ucislgeh%2F7WZTDjlYUw4%2BXivacJJ7E%2FY6Ukd56OSwFRASYvnNbY7IdHS%2B7dKhUcocwuA7MlY%2BHIEkxzfO5ZDsJRU9OOWqRgI2NImtHCoHL3r64ZqGroxKEavAqjYCqwsn4aDQbTG7l8I2Mqy0hw6Y%2FtAMwbB1qitS%2BLeLGI1GIbApUtTHwyQz023jY9f0iyxpctJi5wku97FT6BO7XmHD5gmCoRKaIkVprQgZ7jz%2BEdwij8STJgO2idGW28E0Im5hhgQMi704wyf4GgsPBXlnf37dD%2BHEuCIUavoefGGdhpZGNu4YPuQxVbzzW%2B6oPbxsZqrLn7fTWswfkBfZBZcB6%2F6B50KXF3qa4URhi6tbkpZeWtQ046vbSEleQ0s14s9cZWsUAHiVvGCtBcmgPKba16fG%2F612VkA54jOK3jnlHDZI8UHmaIVFj8Oypkigi6M2MizJER%2B%2BqAvPKG%2BEwuOSCzgY6pgFg6a4tlmTnFw3WuXyOqBn2m4Eh%2BPDLxqxOZQ3ohXg5skE7864jQhstTc1xeqt2bgKp3bleFyRZSgqy67pvu8CnCvjvpK7Z43ZlDM0Mecv%2FfBzT4B2QS4bzbpRafHX6tizKTT1pbWnztaSW2b04tJVjlFN5iST2vkHpLCPOQJKoGcpgyIw2ANcydwMDnG72XT5n3ZeXPLQYJsJ64D8%2FcjomFg3fn5c0&X-Amz-Signature=17f5de9692a7025da7e0ba489f9393ddf397fd079f001871d5f67c2cf23f8fc1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

