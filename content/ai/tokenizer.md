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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FYTF3IV%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDrifuVIsT4mFRKn%2Bo1gXEiNEAZqxE1NcDhCNpMwDKx0QIgMNts%2FVoqe0BkahMP6GJYeBNTN9A0C1so4ev9S2itIucq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDPpziYwJVLuLWTVkZircA%2FzDdrOwCzjcYV6EwjeYjxFrUbG8mMtoDCzpOdDWeRtxYwSSQRNk4p9U4xaLanwkRgD4JXMdYTEOWUSwjpXaUy%2B3WT%2BSWSq54FDJf1TdGWY23gqveY9pOSMMwc0dyb6mnwkYhYi%2FKHOby4yZu66fMVOJSQRzBjd%2FPGLGrQ1Xe8PtLyPb4Boo7J51u5j7i4gY1gFycQZrtcLi7QccxkwTO50ulIoS2A%2Fjyq6pO3T1xTcA2kRUGPETtjUBLaz3fgs3AwJS7QvWcgfU7V1ETtnESKGCeS7xYW5KNNM3bFLWBC%2BMUpecQrtIkmuVgcwbMuHMJPUDvzYb%2FVMPmTPWrPN2B2%2FfKeymMwak%2F85J6A0dvSssJkZBC1VUwJr4L82z7PaW3RMgCbqMuwldihw2JWsKWpRSZ9bFik6rc%2F3wo0oJRL0fD%2B%2FmkPgzMe5HUkMFqld9ojOalZrdNrZfCVFTd9FJJ0sgX71JxovUXaHLXa%2B63ct9pxJRcFmoImRtV9Gym7ePj5D9jDikZLwH2j1ILtsydsqPuVxTjg3vv2vBu3eJY6m6Ve5y1B%2BdwoDXGLg4690RJ00qX2kneuRkXyAA9IdrkzniBWY2I5a0VjYwKl7b66VIAi3OwtV4pzw7fq35MK2nzskGOqUBIjEbslDeIlAzNiYyjGBVRCYfpedoN4XJmuXlHd%2BS3rHZQJbixYN0Z5H0ny2fqQk5kobUu%2BDGq%2BR7JQ498%2BbFAupVfxnxSq6lsFDIJQkr9tlweKavKbmvF4mNcPP8nrxVfxLaa1yuOKRmM90QhsG9hN4aqoFR5IWz1hqjFRJQQCtHJXmrElw0DGSS7TnDZiDD9Kms7T6yV2Df4jlfxufemTAKNMke&X-Amz-Signature=89271fb7814821015dcfcd71c3b94406fb550a5f03d258f3cfa16a7c291b2de6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

