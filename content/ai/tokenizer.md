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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646FVBLDG%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQCGNimy%2FPzEmKHbfBCURNBy538PmCB8wcaGtlACgRrTEwIhAKJoqnA6dHLQB6rDEtdgT4CWTOIFzEc5%2Fi5SF2hedaxtKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwvy%2BdXI%2BeSeAF6axgq3ANwIQgs9BMh%2FQV5CoPFM6tRqaGq5LesX%2BuLnP7wbIA6bdTHktvV5Hc%2Bcqv0S4GvpkY66h1Vk45y0ZMdxDxU6dXlKwK2ASrMJrfWRp%2BYnllHjvNPF3tKc%2FJ4vY%2Fd1o%2F2sya6qasSjWvVdSaRMbmjE%2BXNt616HgB%2BolvR2lAz8nvB7Iecj7V0Jp5y%2BUUrPhGnjkE4JgfkKUu9CAUOf6g7kNiAAwZU641uEqP6t0fSmasR1EBPvrZCYNf4IvLvLHMYmwdQDqgCbvXXucGN9sXKpgWr3lmlcSU4cNAfvSdnG9W8rlE0J63YOloFrZFeL8bGjdROoyHdPWmevxB3W8keRIGaf9miIZmMpA9dzB9iFoCx5W%2FyNKb543t7jTNxkQ3GJclbjoO1Xv6yB5W7gYEpzjf4P1cC3x1Hty7mS11qWgwXn1VsFulrSZ5Q59dNQ7iR6jXRDjo%2F4MLi0oprLyMZ1p4QTu1%2FHYNbffB8ksA6H89ADalDMtB44uP71SujMel3%2BufHmk5cFyL8WeuY1KlSURVEHr2wekUfqeb%2BUSajNipE%2FaLJCn9YPsapzDEPHmf4fMuOOjmIa9VdOq1oJ47RHfzm8kvkA1POeZwFniHWMjtjuOI%2FyNlsbn6acq7h3zDKu4bPBjqkAdGFi%2Fn5rv%2Bsv7AKyYgXT2%2F7pAT%2BilY%2F4JKCfZ18tCy45tlRLudtDAGILzoFHkbear7r%2FCTVqjTWfDjbUM%2FnZaAbde3blDtDTMyUu2neeWxTGMGif5ZE%2BwJL8RYpeHc6pceOIB%2FfaGsUQSH2Gyj8TrSHGX%2BbWkh42f0ZoZDogPTx8eZHmLuE0HdWb5xTd6kSs0funB%2Bp%2B63BxceX0bpaNg1m0QQb&X-Amz-Signature=53b9d311f068cd22f9f52e382a6559f5e925b01366ef4cec8d29a735a0bc47dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

