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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPGWWN4I%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T041004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIAuT8e0%2FZPjtket4JsC4un3EJ1pirp3M9XYSA3it0XQSAiEA0VCkxS1fMhVJgszeU%2BvQoRN1CCds%2Bb62v%2FQgxbKZqxYq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDDfARiWVaP1ciY3RkyrcAxvCeI%2BXycSiHcEgqx0Qji2kcKq1F5W%2FachR71uyE1P5NaSE9o0bKSnGT%2FAW5KzyWiPWu2cYonfic2Vd%2Bl9spME5%2B%2Fqx29S02lV%2FGQiC905%2FjytWQG799vCnc7V6xQMm9iVt4PgQMdr3wEhv5WdpOK2PiFzDFNeK3i%2B7PzWY01YIM7imDweIrYmrFDEFWVxqo3adJoQpCuQ6nDr%2B5BsxwooVyMQITDrbf%2ByIAZQcEBmeZlz7XFVpYj4pGkDnoaWrW5iKeRw4w6Iw1GQy1M2xoVrAAlzY8gfA7EBHps1KDrGOtbxW3zuBe%2FMRaxjcfRMTiNHcepIGC%2BiIiZwY%2BsgPVkygrixJpFrQRGkThxz9M3hOaf197F%2FAClp8OhhxCccG8lKH7TRY0F6%2BoJhAD5PDGM4kTj827tpO288dnvYnjoaK4w8Zsc1H6rWHKkuh3cIjN2nY%2FlFDPlY7s8cpFNXPnGurZnF9zsEF8NORI2o3uYAvuQpOQvMe4YlN6%2Frx7497nyxccj9GM9m09IdtbG5jiZXT9lzeuUABGRpg6wN9QM0PtMhAL8pr3yKvz3nCUPw78%2Fn6fhvWKE7mGWbJX12HrrTI4gcLm38VMWvYz4pDg%2Bso4D3%2BiJxdSD24cTaxMNrIp84GOqUBbziM7lKHnr3IjAQDrbccHFH28%2BKW8yeplJM2P9LUdOImO2%2F015HwgmiiayvVekiTTVZo9%2BshVvmgiHVz5Chj1pzQVWCXLDU5zCCfzSmMOWVb3qaOMYnWt6jVLLv1zpcenjl0yXdnTka7X3CO0vUwqX1a%2Bu11uYxXSfSru9CFSZqTOHfCXJDViiI4OWzt92ln1nnGvPIz8WqUv6R2fas%2BtAT33sJT&X-Amz-Signature=99222e1b1214e07fbf27a192f9d7f83054dead42fce7c5319573c8932a64556d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

