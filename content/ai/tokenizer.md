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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466US5URNYJ%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T024933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF40l%2BzJcp5kjCovywdNfTEc7yuF0c21151io0sH9Jj8AiEAtNzUVQlwiNIuw9pyuFPsLcUp47%2Be9Zn%2FRzGTiPdhwOkqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCGXWjM5IFOWEkmtjircA%2FeHklxanoUqpoAVbgCqwmcrKIh4KbY95Tly%2FC6aztceWZuzUfu7J8m%2BPeGWUKRevatoGs%2Fzi%2BTKeIcAKaBIeA2zar%2BClvNYN%2Bd%2B8hP9j%2Fooc7DJ6QnSTKglkqLA0Qt4JoU%2BX%2BbRcLtcDJ1W%2FtbSjb3Iv1s4cTQfBB5A5MwPhr1BkStf25jFsq7wqp8inTTI18Cuju0I9pAYJA8pXI4LfejdqnShbTeM7j1SQkLtBYHOw5dNLD6250R8xuU6Q7mOUkGgqv7Jl0fMpqOaHTMkClo%2FC7V5XkzZpkjbV%2BBy5MIgVf52IPnVDX1CUvqxxbvWUE3%2BHmXK%2Ft3FillVTNZmnZDoeinS3SzCXxjZ2sAwz8a24deWVEVB4xHc%2FPezXt4VQERqvUP%2BIQt8DQ8VDymcMcWgu6VeWD5n6aDxwixsDwijLF52Paaao3OKeUw5hqfc0ZCf9Ve2VKxXnyOH4T6YVYzgt6sIUqzrr2l4%2Ffmtkh7SFfFLeihB9lIrqg7imS%2BWRE23bxZG2BO6Nr3KkBzE1lW1X6SJwXJ2t%2BxUYDtC8a3kkzqURbHezUi2%2BTs7mv%2FNePNnK8H2VHvomHEjHsmbf2kbiDrDK9T%2BDiyj6qO4tbANiMIR4PNiV7kJ3vTVMNXg5MgGOqUB8RQPlQttAzYF3XIUsCZ0cTzDmSO8Lu8BAUIIzIFLVCSC5vOCelpZcQjxvr64H%2FYLc%2FU8qCT6QZQzgEXw2Q68aMLoV7Qh9ADUC0dDORAS7nAQ09%2Bzdol02MQHOQ2jNFT6c7W%2FO4DlQGCLkP0%2BEPJk2b8q%2FEFE46%2BOkSIKsljQnvjLCYGU4P0M2%2FAQ%2FNjIwgNTLOJfutsdOIyQFGW4%2FJIWpOCUDTGN&X-Amz-Signature=3c6f6fc3d5bda54adf5aab168d69cbb8c2945b2eb4048a12ce7697291d0a7413&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

