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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ILDH5ML%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030806Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDf%2FHjlhakwjFF6bwhrNH1XZWhrnHI06YZ%2F6yFTbL1imgIhANIwLNsZzQea6F%2BXhdWvljtqQIqpP4z6ThFsYEtO3P4VKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxB1fn%2FRgKkJGsZEvUq3AMCM8kJBgxSV47RQQaNUlOvIi3UplAD3Sv8Sz0YpHWLjNy%2FW5AgxtZPqaPWzfEZfmsDC6%2BWy9mWfYveIjamZv6791BqOm6PE5Vi4ylWh5C7wZNtofeUK7jwXBn%2BIEU61qGbyhpxiBxKcp%2B%2F9CGxYTaAL8ekYLYcKFJIfPN4l%2B2aDXvunr9gX2n9qsWCy8F5lEc0Xx897aXitZk0XBpakQacUO6B27EQFaYiHG2uBtRYFRN75oK5dzDaMTRnJyXSwKk0BXCDn%2Bdo8c%2FeMi25pGUhWenb4CAFN6xekp%2F7wgQ%2F0m8pNJWpjW2nWOrhtyMk6QX78o3yy64fEl1Aa%2Ftu0Y%2FhCZbHRL%2FUxcpEnx4P0D3hooVJxJi4Tg16%2BvehouImC%2F%2BBnUlEO917kA3lP%2BDSuRrSwJPgu10yA6e5JTIpUCwpcEU5gyGy1ITImU5OhHEh83obN6WmwblJcf%2Fx3jRkxxtU2N1%2B%2F3v7UXJQZc6oaMAPKwMeWD7fqPljX%2B3tG8qaUASBO0mH4a2LQJd6GY58mIlFRQs9XoY9Oqrl3iLEx52dqpniG0%2BsMqmIyTpEp1AYg40cuYQJqESneZedCAaGr80tY%2FilMoT8LMckUft45Fhk0Fdatf1CFcTKL7RVwjDN3LXLBjqkAQyH5AurtQ%2FPC3IDXe27IBswZxiASN6jEOVuH5kvdMhMkG9A6CwHjnFadsoH7ze%2B3VVHj3t617qRixnNSJEbTpqKDFthSreXDPf8sMzmWQza83vPhT9Og7kZpT3XzNSpm%2BixZJ6VmEYcCFdZc9f8Gv1yJjUFwFXY%2BX90r3i%2B91khkuJ3k%2Bah%2BhDCN62TC6Ps7379Auz%2BbPWvo%2BjeOXWmoW9Adyfw&X-Amz-Signature=781b5b3fcf9e8d9bf2db83b255d25e28a68fded523d22c36a6de562f3a2e2d98&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

