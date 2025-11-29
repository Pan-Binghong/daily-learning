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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665H3HCYXI%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD1mcxBJtxyHqbfpMN4buE5IZhxgDD0d5zKbCCoqnimqgIgInY3eWwgq%2FXUJGygQ3N%2F632HAxmWxoKwX7JZ0%2B4aL4YqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMoG6oneGPBCEPd5OircA%2B5FimBqzlVW7T0zwYbEPoH7eLUMMeahhfyRYYXPr9v047294cFfTaO7D0OeS%2FxJZCxeXFCe0dbUSl1bDlUFNdKqllLYsEXZU2pvjaXQv2Q4P8AzteiNinIU%2FKTx0DPPPfGs2gYFL%2BEhuQWAdgqDSugZfgIbL7U2i%2BwA2vEyjxTsB74FXdWaouXC%2F9iERSNAYGEndNG%2B%2BFWkcuJ45TV3Wq2gAwjvGn4rYmE52yS4TQGK0UWV6pZe3xbBeyHD6juvTnpZt6XysHTVezlPBQXsZX18pfSqHl63RX4d57jMfq90PODhU0XRikTKUY%2FZ78JsvOx9CAsRfwZVaiolzBPxHoX4rY4cNW5sNAofPyPs03RpWOz4c3%2BzpZ27R2KH6Z9hV7GOuvJV9o%2FulmUJHeTR2WJzyYUqr6qYgojATjVAnP9Vz0ro39ggWkgwCVyuRhnAmsSa7oxUqxIpWskGhCyptuR%2BRpZloU0ouziPHebOEbuBG2h12HVkbhdQjSJXFj8o%2B8tqoE0EdeP911lNRyELys8vmFcVM3LZgSqRafnVBXB3dkrZi93%2BJ%2Fca2WzKCOP1Q%2BwiGvKCdXweWvb4vV2vOj4dtqNZ%2FsPQMRz0RcMC3wKVeKx83MQf%2FWe8JQy2MIabqckGOqUBMS9wR8RY4JtKfnf%2F26lDjGo%2BdVe13RxUIR1lUIB5%2BnTEYbToZoFNKXRDRG8IZ6CXAdD11bPg5f58fkfkj3mzySj0u6iNHbuTqYen3Z5ROHYWCMfTN3mz69PUuyrzc%2Bfu%2BaEBT4K7tPGio7FamUyKnPwFFr00E%2F7s5MxPXNht5lVxAL7r9kfV%2Bjovh67pVQULjjU%2BaBDTmrMXcDQz7WLda2ffHzEN&X-Amz-Signature=81b95ad649cb876e08e98c4fdecc0a79f9860640a7467f4fc3068bd2406e9679&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

