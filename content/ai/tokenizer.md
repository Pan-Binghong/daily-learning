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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DRPB5DO%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T043417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIGHmb6hdcqoGruUSFsqJ0DWUzRsNofH0HODPYTXVEQCKAiEArzDRjusrFdoLPlk0HXeKwzeqgs2hs4Y6d5dge7Hh2CYq%2FwMIBhAAGgw2Mzc0MjMxODM4MDUiDLQA8PKtUv5l2zBnZircA5vgOw2PqlvupRI0rmW3VdMSevdUr7HYwDia0WkIG7YStdfVqYLsSis4CJcngynlvP6h%2B0%2B2r7Eu0Ce9eazSVBfbaWv%2FVx8RtSjSCvtSNEMEGws1eYAzIpi9KW5C%2B9wWmcSn0rG5f9UNBWwm42yjSgirMEYA9HGuhKqfyJB153tcQZs9pMt3zybJGM2Z%2B7IBy7eIthYBfEJaIUHI0ey4k0V79sGQJH7SXdRsZq6PpH2Laxkvq9cvfKm8Uf1nDye5SoLV5%2F3jcoR7RGaEsMtzyfxKzTOhq8wrbb4LXtUNGHbnJtROBpcczO7BhDYa%2Bqi%2FiQz%2BfihXcxjeeF8703gx%2BgK6sYEbA%2BXNFB587SPpVOQwjo79yjqKuUhqNiR19DK0HWko%2Bg2fiaWV8vCfBiNql3sSKRS5M8EoIPf586tHEsFxWnjq8ue8mGbS0gi%2F5jC%2FnbuiHfuWUXeoIUwUVuu%2BLrZUcl0AVvw53rHcbItCgI1C%2FSkiRn3QqfDJjAyUyvU3n0JeUDkuy1ZWDkAQdH6CPnMAlIarkVicsGFmgDEarzMFeXKTrzhRQKORO5FJHptoUblIxv4maORQ%2B3T8UnqHXdNFzG9EKf%2Fzv4bVoIDAIhbZB8sQwjNggYN41W9eMP%2Bzy88GOqUBLud5U9LOU%2Fx2W81l5qXc%2B906VvUUyXN6sUHczRWdDMJPnNlYg4JBE6xDPEFuYpLnihinY189j5i0cbWQxnrfN%2BwCthmODQodhVfasrY2Vn1UofTFaBf580Ve%2F9VoRd8Oip6BefwMjQekfzueidZ7EFg9XARtlO3GSJdAovK1F19djfLvBq5RtQ239xNAmmrbkB4A2rbMpkL05gFfnBW2hQFC2gIF&X-Amz-Signature=7ea38573fc344e099db06fa37c3347d979040565f3d40ffe10f79940851fe3cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

