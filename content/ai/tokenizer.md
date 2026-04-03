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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TC4IRM6%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHqnCYg7CD9D4g2YN3LFjk6tbTlkSM6qdsU8WmzaBk%2FRAiBl8cszHP%2FRYXoa4E0%2BrKpk9IMAx%2FsuEDvz1a2ni20Z2Sr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMopPU46CYBIkfs2KsKtwD5QrogQcav2SygXD%2FzplgKbacaqucLRvEfhxFhubLagvfnQY6gKi9xbrb%2FFN82edRm%2B%2BO7nbGWG9GDat52Ipw9rpQGEnxPta5ireFEsVzGrhIx59nbDMjDy1nMwMgfGVEUesathrdsIqU%2FdzcctytVlYH9uPfWsgtxY4TVBveNwKffBN9c53mir1CHvRKOIxBfF9VRrMzmxf14sXEt%2FKWOpi5fE2WaMXSrRODRwXzpTEAsRft%2FNF99YdS6JaYbbnSu7uo6mRTLDny%2FAVCdzyHcVB4JY%2FoRprvj9VS%2Fm41DyajA8Ac%2FYf6nBz6mZKOUu2dAgFFnHTxRJM1hiwqNriT3Ub8TYYWvNG0D8wFSry%2FJL2JWvUi%2BC7x%2F5yj6mBOK%2B%2BINY8tho6x7mv9ebd8A%2BGsYzBkDW1AxthbLSNGGFq3OT1cr5agTwiaSqx2QIsUoD2lJPlaRRv%2BMVa%2BDnB96lw6%2B%2FDZcuv3gDB2mD8kL5V2edJOBEiPffqsiD5ValvLYiernwm2sAkgLO8xbYJ5RUilygs4PnU3PpmLZ2TmNqA%2BvCy8u5HCarDV0LgcEFNX5qX4YONkpCLDyA4roIJgrwm2rKFQ54BuQwnIx8D1sQh%2FUCmQnlgzLoRUm8t44uswv629zgY6pgHDpS9BlZ7uyS4KjQu1KFrVW5UhmdLKlVGHl%2Fs6lQ%2FxrXrGG%2Bg4cLIrJrZT3bDZaKPH8WgJgRBeKD9e%2BPng4xRTcAbm7w4q7IaJ1osEy1hMjDOad4M41qNyCqlqBv%2FVYgK9BJC4k7TqH8rier%2B8rIr7Wt2pro%2FHFrsZikvZ8s4h%2FKSf5hMxt%2FyDP5ouglXBFc%2ByucB195zpqTWDHFLj%2B%2F9a1nzmI2SG&X-Amz-Signature=72e7c4d9c2b9f522eae9529a4cb82e35546e33586c604464e7a3082ff0d80f43&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

