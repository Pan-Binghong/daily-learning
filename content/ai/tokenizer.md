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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHLTMSTJ%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJIMEYCIQCb16Uybgay34TCIVnmX%2FVCTlc6QZS8NZ%2B7YsY%2BXHrPYAIhAIFmn8LmejzdeLsUYoYGb%2FQ%2BCzBKeqjYJRsohJG0GemXKv8DCAMQABoMNjM3NDIzMTgzODA1IgzgTWhOegfeezlvDGQq3AObrdaHDP43slhLSJAbYhm%2BRD872YwyG3wLQiqjWEhK66XOowJ0axWBrgRze3b6U6ZXA5efglIX9P0CLhQX9p3igHo%2B5dm8mDfMsdMfBQMr1u93c2dDgGCX4dNmQ4M0q3vun2nEQ8yv4MP1KBWDfUZhsrkK6YoLSf26Bz2KSrSuxfFCmCFT9HNb%2BvCyV9rRZxsZvf7SpPkefBxFRjI4%2FCIltrTsFhs1UmLAg4pRVHNw719iCVXUcTyLl565u7hkSpmJLdBhH2vq%2FQv3rgL4UP%2FKG4MfokfRzaB2eQM6H2K3n7FbNCUK1TkJIXwALCW8d%2B%2FaoJNLsQfKZph%2BKiPJu1cLgLzziAtAxJrD0TzIf70ZAnAdUYOdbGfZzjyXSQ08N7fXvzKAvEoe7GR%2FtAkhMbXLg%2FliUfEplUJ8NSJQjiidOmBTYCMycSfhvWjRAXAkUWPAGLM3ab1%2FW33pnhjH4YVuISa5%2FB2ePrqJE4sMUEKWCQvHga5NsFNyNtKkn%2F7mUq4RI7y2OsBRZg0YFDcu7bUNOa91lEnnIR6Fd8UitpxxjDYep7YefbD87uVRRqxxmwKEDBRm0x1tMIRHnfLZVCH7gy2rmlXQPuXudfVwYcPi00aJ2gAS15tXDLEaETDuztDLBjqkAREmg1W9QSp3ivp8C%2FHUO%2F7bi6VTBIrmJLmrZzHPkhEhHymDtsa%2BWE1ttqaolhdTyh3lwDzLxqdLBB0LE%2Fdg8LXzmL6WfFHein%2FOfAdRzaUzJ%2F4gLDZpULASgUI964lZc90CUFqo5ep4%2FzGnZjyrNU0j%2B3B5aV%2FjyK3JnaRSlBftJP0QkVY1FlVWDAy%2FzEkCNbYE9QD6f4DJtTL1YGWfeY%2B2vibP&X-Amz-Signature=a2d55d26b4e6d3771a025a5a78dc390335039440adfc7287a5262676e0bd1ee9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

