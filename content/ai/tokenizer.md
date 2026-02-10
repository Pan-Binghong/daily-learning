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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYSJ6EI2%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035154Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHp%2BzDB4iM6PgivDltjcw1MTzstZag%2BjeMsYdVLTpjFvAiArdRLo0ZgUbCeWsTKT89GlSZoe1jTgBQh2aswVfFizIiqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlARNaWBLOsooOReqKtwDPyP4PgCgQBb4iYZO3n8kId6aIwuv3nzSWmnTgj%2BMqhc3wxW%2B8ovf9FMY9I5OqkYiTC24YYt%2BymrXzmzeJdgRcfvBl%2BO9%2B80Zb4n2jR9rBgGD7l%2FGEw5QmC8kL3nGT8mvg%2BhNgIBiKv6EJv9hAbzSRtuq3IyI9nAafvfPeA7lC4e65H%2FNDKciYUMWxuEhsHpzYTsLD%2Br6j30vzgdJStKrDbgDr7v0s0n1g35BrVy%2BqObrW5LtMIDCklMNoRyooU6RALITjtP09eFNgBBdWAh%2B%2FhIQf8Wxh6p3raV7xSWr3txfrDkiI7UolJy4Wwv7PkcvOqAYi5QEnHt0pf9vbFfJD62xG3WZlDLWySWgKCQrvwG0%2F8kI3MIGPFF3G6RtVEA%2BiET5v083z%2FkHGbZdU9zlvvXbzuY%2BhRXKVbwlcY0ENZQvd1tvHC7TwIft0fr2jqHU0ggSuBjAQZfGG0VsrPtKydTWt2qPimWXMUalGP3Cf6UjEXJURgFXzV8RSs0h2TNxts6Vao1y7QhAV7YcFp13Y5b1QImhFim%2FPaJKiODHUbUqJZ42m9q%2BgUYNF79nZYAf%2FJawC%2B1pnkPTMKzkzjv8hCJUkJQsC6VoLmsnBZfgxqoHEX8och8CE9Plafww3sOqzAY6pgHBT0XaGs2JClGuCyabl3xyAIw%2F3YrQu2q%2BM3DPWCCALzlOpcZFFfzXtXgBZFJ2VwtauOoYoLAJh4UIpVP%2BLtETe7NyqOwnBHpAfJI5fvx3Tw5iUUZnUywCRVn3PnWwy8QIbsqRQg0MLI4n%2FQiN%2Fnxyco00KZUwPtTKBc%2F7lwT3ZZN5wJSwV%2FF2C1IWH2g5CS0%2BvnfC%2Fgxhu3e7KIADH%2FfO18leSA8o&X-Amz-Signature=c144a6252d0ea9a68cae4b69f98e72ecb93ad7d0906a23a55a2e7235af485987&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

