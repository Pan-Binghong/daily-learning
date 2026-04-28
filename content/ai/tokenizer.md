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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UH6E3ID%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T043535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCID6snFRNwi%2BeJbjIsj5vDkUTtvOABcc7%2BnLF%2FQViabPVAiEAmYjU8eEFWRLe9OLFkrV0ExWD7L5Gah4TmkkMXccEF2UqiAQI1f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBckkp5z0E9u9groWCrcAxW5iOMI2u2%2BdIFzFMMC4jOsZjUVE30sSio0K821sAW1dUGDNfFafSivYWIL2mTfVg%2BGBHRmgZ90uKI0y7GRCgy0DCqb08PGhlHCTu9MCGR6eR22U%2FhNL%2F%2B%2F6Hmfds9IJqSkqxSymtzG0SF9dj%2B%2BlnJbfbyC6ObJqGZI4BpJ6jPSsWPxsBwFlu9jiIPRcr2%2BYQCfOQrqHYh2Wi84djFwFPGuSRbgxI9j3e18mKiwOizZh2mWryaKDw2GrAW7gzNNIK7ZxYr5jYhAkuqo%2B9xzfh%2FNrxEWzJpiEV7yCXK1CWO95To9LI7TiZOiwzMNTs1%2BqutMYiVwzc4AjPZJQgciI9vY5FjnL0d9BiDo5uP2jfF1Dqq80W1kueFNrXCnQXjLLwIrknOUhi3ou03Ssp04FndjOI23sNltzxWySig2UF8lAaVLttMuXAT2naYbHtLByILIlyXGEPHCybdFPacd%2BU9priSaNz0Z2EJf016p863XiuoqVUwLT3gIog%2B1xqPJlaCmPylkXE%2FVh3q1pvGZGscXdzVMfwDzpvtkTmKOA83faJ20ttjy%2BL2gHs35lmXA7k9%2BZRw3tg0TRaM3TU9ugtt9r7VxUN7YZxniG5Sh12JegJ8%2FX0Lg8%2F85s1D3MPfrwM8GOqUB0kV41io%2BDWGMCwl7W7o0pzqbfAFBISA3RbHjk8sJUFHAYiL7EAl8kfHiX05FX5%2BNDzLgJ%2Ffu%2BRBv6JGKMcMs%2BsbOrFG%2Fa7YUPUmO8OCU8Ph4Iz9l8uzUqmRhc4Ap9IBbW8RB0h%2FRrCDqkPxt%2BlU5Zoc7zwm%2FzuP%2BVqbJggNHQrE9qpc6ESIBU2ra63Rfo6LzjkHDz275SJZZt%2F9Hpw%2B8iJGyZGdY&X-Amz-Signature=57fb9d74e8fd65aeff1807992bcebad15217d20a653f02f17e4c7568b6659bb0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

