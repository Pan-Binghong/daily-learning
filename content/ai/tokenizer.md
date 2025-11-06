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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCMNW54S%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGw3NWg5sHrjAVQLSpgc3zItG6c7fHL847fmpdmJry18AiEA6e0OxLE4hjA%2F1CXwb60w%2BbRob7XOBgTS81tR7WVzHq8qiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM9%2B6RTQPNEm%2FlJt9SrcA4XfkS5U%2Faoo3Fr5P3NU3sA10CRPq7oLBhCKYTDPlLdzniPcIexa53NhVnicxN%2FME25w%2BGOo7ccL3XuaOVzlDEQ4%2FTKf3oLeAsZlrJgLa1uzUCp7md2H%2BpRtFTyn1CJFBVkUfTJHhrwlcOjKkSR7S35AFfOFaQVXdFS1mN0fzkgm7YPXTrbbY5%2F5rpI0l2NzbXd2DZwxA7uULBMtPMDIcTczuQTWm%2B0ymSmFDwEP53QQwwfaXq9qQ7FyQDE9VR8XNSmyngJTwkw8dYKUz5KeVXa2IunVE8LM5Ha15E%2FN0ccnX%2Fm09vvNirhC66%2Fm8ITxXQNpED99n8mUYpJeCs5ocBWpbEL2ZiZTprULzXOM6t2mOHdrNgtO%2BKzqTS0wcCh5%2BHkIvT4kNYF9Rc8Vg4g2cD08tDRQE3b5C8klk7eCNCdTI6MXYm7aDTfamYy7WVGag3ZIKof9NB4lYmTpUBN4V9eO%2FE4nJBRK%2FB2kXDojeFAWKgy5LMUToS6szAlFOC5afo03e74IYafCWn7ZoupgJn%2FEbcjJuZFiW6nE%2FYDWhWGk8GAQ0WuZCNlHRrkjaOzYix4%2FUtOiY6Rv0YZUXrVEUGK1DKv4ij9DNAriI94ySyR%2Fog2tUQ0fXZP6K6FZMILyr8gGOqUBTk9Yr4qj8o9Kw2OXBg3MqfQAVtMvjEwCWZM%2FRv6hruR0LrqCOC%2FhGgfSK5oZpi1qbJMevOFdp0vLebNEZWQRTWoBwJEoN7HSJGujGAQSVPDQVO5kkrJ7TpZ1qq8yXqZ8hHe72EYknNcU6HU%2BURl6XQ3tuW1WWyM%2BjYwLcDj9%2FKfrJB%2FdXVW%2FJco9DENxe03hiUQVDst69kTb01IPSb7wK%2BxhWGK1&X-Amz-Signature=dd0e26646554b0a51de41e516e9bf16558c3e4b7935bc615dfbfc2fdcd675d8d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

