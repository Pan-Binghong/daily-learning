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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VASHEIJ5%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYvFTBPZgW4BSskLnokAeic0GGSyO4Zq3TwW5yveqVoQIhAMawZDa%2F129VYg06Ur%2BUfMohpJ2td%2ByQNfOQAMPvBpkVKv8DCGQQABoMNjM3NDIzMTgzODA1Igz%2F2%2BAXjKqmeX5QzGQq3APMBiijDdR%2FXufFhiQogahKymXunOq5SU1rUrtsF0FDAYMcmKjlkrckSvl1F%2FMRDoTgxhmAnrX4iGg9oYl8aMdmBQ8qcHSfXwTOBwFYp40cT1q1r5lL9MSQ5NXSfwdDEvQU8lrjphMq%2BnyHVw%2Bpzh7OP6WPNJx074v6O4ay4Ohi6W4ec2F8FhK6bQ46txoIa3STShjLwgE5uI%2B6Ezgg%2BYlU%2Bp3kTMZI5O970JTiv1ffmuiQ80AjJnsAizXC5gHUkIWVaBJ43I7REXEy15v7pTMVYhqpNQyGB6eWuYxlZYa8TZFhnb5Y%2Frbf0xFNyTUBIKtl6nbw5%2F6z%2FDz8g7zERRQilQ1zgkEFSqqB%2FMxylb2Aa5DuLjWtR1NyaQrCWloxXCbhd5iMMuzjavudPSLLyzM9mGLns50ITAjsBksO2ai7ZURaYcex7QppU7qQwe%2FJbBjXbByh5Us3nxEczUzaCGlvMBDXhsrp%2FuiiE0RGak5yyClL8etmpZP6glmVw4fLOWk5NQY%2FYgJDi8fBpQpxzmhCpSPAe79LVFA%2FXw%2FFhxVUstr%2BxafOBl0DHR8VI7v7GNXDR44MuRncokSQk6X%2FYTHMyG%2FLuh8BJArLqCyUYP1d1fdtUSpVUt6cguD69TDorrfOBjqkAW2zGQOtogSOYP5fv7x0bk%2FpYON7wGaiLAX1918s%2BEbM65mJVmZV4rSSsqjlSAfpKqu8S0oLsbEZxPxDlcHvhFqraO5XTQOYdboJp5Y9Bst67rJQrsOByKOSYnxuppk9Ki733Xf2EFgiBNedjTioiPWYEdGptYDXOW27Nyq%2FZSICWlGThIk%2Fp3p9VDl8PQok%2Bb0L38Sr509aKLYq0SLR%2B8zjmrRM&X-Amz-Signature=fc616d661b84f2be056cc5074f6fe4a3ef7d35aa1a54781aa60a409f3129a79b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

