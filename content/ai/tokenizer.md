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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GKLTX3P%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIHQGZTqUtBCkPLar%2FHFN1jvJjPiPTthURwFKCT%2FAcr0AAiEArl9vSYv4hmUnOukjTz4MWDqB2XnJt5UUGmznbVpjbQYq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDCkjwKQiSSXMcep7dCrcA5sFyGwvz7LEpfThEgS6Yl2Yi0uilCIGPdaQVOiPlr8Bta5x6QS%2FdnVX%2FRoLroYRmw01b4seNrNaC5AseobbAGo2m91ZHQmriU5%2BJ6H79LXYYXV7qu%2BtuqQElAuLaFun5J0IZLtYSjD%2FMXW%2B8uIRmpp2cI3w7FDh8W40JJFIIRZOiNd4hOAbo%2B8hxWRiiBHb0Z1HEDyU2cQXED1y15ZJb1l1sJ%2FBBnaIKkE9%2BE98uLsSm3U%2Bi7XF0PyyEAscyJV3DpVG1J8WgtTgl%2B%2F7ctCF4Ew7HKrOOvyoNReQCkX15pXDFhSMwMPrrhHQL3fqetx3Ep0FqIAxvrwBja0MScNYfdfHR1ev8X%2FEiQqlsvdaXjdcAb0uKKOUV7xUlNlFh6FVOn16F%2FxmMiMh5eG6RY%2BnGpCJapNkI4VFAQH4q62ycDd0KEADjXdn%2F9uW92%2FD39Vzq3M7XEIyWuiIhfbirSCzeJ%2BF5tgY17UZDaEgASIqEVDzPpHXcjN5mV%2BUWXvrEuDO9xj4Pk%2BvyhUDi20BJZdmwYL7qUvmLlXin6bLYL34i4Mu5kPZxtrrcL5qqDwFuWr5kLvO7zSFQk84sQd1tit1IX9AdX3TyzO7D5gwkX3WmyjmbgSc0PWEpzq5AmGhMJiexMwGOqUBh0xjCnZpp41XcP8ln97S%2B%2FpB6hp%2BqfzKqUy4lcXWfSqJS2RVUkc%2BP4l1R%2B%2BQ7P9jZ%2BExv37Lnm%2BRetaBcBhkK2ik1LyLZvDx2kJShZNfuvL8UjqExw%2FRI2f6TzG3tU%2B9CYthlOVzpDTJn5bqnurFmohZ8WMo8ViIO3TRpyIKWV0U%2FwL80bWDwnYnvetmvgAL7A30OXAWDyzLOTmQ5kYsR9KIYPj%2B&X-Amz-Signature=f3b97697a0edab73cafba143bb9120d1f9c835fd16588b4c07c03dc4e16a0495&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

