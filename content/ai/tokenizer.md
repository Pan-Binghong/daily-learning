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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YP35OAN2%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031234Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJHMEUCIChWXBnGoh88Ib0jrBvO0IlaSYe%2F3GnWTydP%2FGaQx4T6AiEAvzrJx%2B5x2HTqlde7gWBpwSktY7vZdrMBpNlgsEkMTDAq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDLhU72GJ6K3qQ3QVlyrcAwNrIIIGZOVsUSStcT74X9dB8IqgC2sdaVFe1Zl1HlMc2okvx8cYk7CnyZdPIvL7FfoWF%2BQIizuQdm25yjDk%2FHOy895mFDuALd28MWEYNwPJaMvc2xbEezOdm0DZkwD7Hk9DEatiXUJRf90KwyX3U406QocGgyRA%2BMu9oYiRrVscT4zZ6sOV6Xg1f3bNx1uUclrHXbTWDzrYjtc3r1T11aXsiKSC6WIWeGc5RIk4KbQ1O2HzFeeXVLjnQZ2DBlEkSH020obJtm1vK1aJzGz9%2BE%2FApACq6zkU%2Fg4r3oRR3DbEVryiGq35XrvLVo%2BB2i7DO4wcp3BWfKIhHYgo%2FcjiapscgbDyI4pByuiMXihz0hHslfVOsnmZl8GlH4KdNDfcS5LvTx1%2Bz3xYeyppf6E0aGMvas6F3lfLiH0wzmCIIAGil5FvweheHMS3iBu0QqHP8buuxmrPk2FeYCqwFMwMhch%2F0odXbz0ste6%2FLiXN8soJdpFb6LKSm9jB2TStaLYX3Xx09Cd9LoVFtBGt1jRQu329m0w1msbzFDYeBE4PUpvGGmleYkyjQpAEBpJrTnMP1Ns1sGAVBlGCGkeIyFbPqeb45ISbaEurDgPIY%2FFDdbNfR%2BqZ9SURcO6j40oeMJLO68oGOqUBRj17jjNbJq2oucO04B8IN58Y4YQEhEuAAkQyKxPBIBcHbBYMajJfIOyEA7fZLwvAsZzmCSqXfH4ksLkeTzitPu7Fa%2BXvUOwGVueeEba3PrDgRkkKbHAD9W1qhiVWG%2Foy04Kc80KHYC%2B4GoQgf9K4YlglI0aIxy5fORCxYcBkWuXPaU69Raics0Noc91UnhzFnyxSgNQShsfTQAj6CncKmzhgJyRp&X-Amz-Signature=dd549312f69b10d58e76bdbf0b4b29766f2f684c191ce4f278452f2b21316836&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

