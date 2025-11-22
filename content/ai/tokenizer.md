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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REPYQHUM%2F20251122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251122T022634Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJHMEUCIQC21zWhhONUY4XWrHSBAdsWrwbhRsi4qqCt6lSbZqe6gQIgG%2F7oyTjHSM2y2jMEk1XOGL3Ya0K%2FxyPOpRM%2BgtWd0zEq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDNudjCUgrs7f7Pf4cSrcA6%2F%2B5fI7gB0Q4oiNZiGSKE%2BKx4%2Fz4mqIVmdVrpeFHJQO0OeF6Fhow6LDt0DwIDyld%2FMaKtbpsg8%2FJXJYOgS2lW7gXwpgjldyvN2d41nGi%2BrbsM4b667%2FGd%2BUrC9ytVThYZ%2F8dOsgHI1cLCIw5upD5HQkMtgYoU2cKwSncjSnxMBYHuttkgebsM36QJWMSiaskSFLHDDYarnZlY91Ln%2FR1E%2FrOfJbG2kgv4R98cSepO6eOmMKRtK%2BHWbSZtm2Jhlwbnaw1gm8L%2BkCQabhBNFY%2Fyd8%2F1lWu7hM04YHbvHPGGrhYb%2BDuKg%2B4cQd1hXVYml%2FwITzW6oP0JULQi2hHkPNkVd6mfOc08j71jMyjgoBfso350Js6vHyh3jnpdOgaiBMfwORs6CxKEGbTIetnm59iAHJOhlPqydEuWqrmWLwg6l75idsrrYUKLCzvDPaGuszCOz%2FX5mTLJXFFNElB9eJW5FhBRUUvP3YWFHas3x6Hi20ZTJg%2F4lRbdWxrZgFKa3yCdIslvjautxO9clSmd2jv0btOKxWm0DFQBO%2BNpadGooXqgIECQfSjM6VuRq5rEMufmhzHZOsc7l2G3ydydShA5Kdrhdyo6Uv8o8YafJnqWFPijF7QltT64onCfC1MLOhhMkGOqUByS6c%2Boe6B5SlZZ55Os6M6jPjGxb1M7J8LGwvRh8WXY3Bly67HGL%2FmpUxhOkLhiguPjAJ8Pzcn2A4BF4%2FFfPjYg0kpTIKqSbRnBCi6OurSu0Lsi%2BVu1WkteBjUJ1DS4EZzyRr%2F1tp53fTXONf8M5GWsaejRjrxgU2OH5EMDKZg1kbdxZ2bTIgAX6KcZKWnK8fSRRp6I32jwiAySWpEF%2FBO%2F8bUyAJ&X-Amz-Signature=12409eee384407283f39f42169a96cacbb4a5e8d0675d31d1a8b70ff1f6330dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

