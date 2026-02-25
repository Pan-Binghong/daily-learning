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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XE5DFSL%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T033816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJHMEUCIQDIuiALRW3GjJmelUCz1Hu9LMcdAvVFMGW8q9b2xzYHIAIgDCWE3CxDoYN8OedMekD1S2S%2BXkGe1yQtaIn1CA3sBt8q%2FwMIAhAAGgw2Mzc0MjMxODM4MDUiDFx1Dw8TWtOWqrRlCyrcAzkq%2FRRMbjb5pdDDDDY0cWKP%2FGe7ebYxyV3sT6J7v2LLCoIkv8FN0PSvqgHsYDc1B%2BnEkjkzgzEIAsnFOOLMKNNAb8uKr8vji%2BMrOEdjqdUk9QzQcUhe1geD123tpOLn8dlWQvgMkuWBnXa8kG7JeGHkmKfcRix2K1vD%2B5D%2BDw4WSxqWxwaYpZZabrm2Ww6673PbOotlzWtrFGdEQmGihVOA4Aqt%2FHYb7XO2kemHFOxmzdxtoKohae2J82ymzuN0deNQLSj6ohsoLOY%2Fb7OPYNQwiSpeai%2F83KTZWypYCOI09f9ICjkmjAyZZub17fVT2vww2ui1DJi7ew%2Bjvn4YkIsDfkulUn8a9a5AwtF5%2BYc8%2Fr10MOCl0qgCple7QpW3IX1GJ%2Bc9xVddDUDlIZ7NwoN8xx%2B2TLgr7ryNSE556eDKk1IvyKgdrUwuonb8oCEIOPaqqC2HndwXDLx6HQJOblY0SR4yBkojRUv6rE%2BABbsIsU3mg1CZHjdZGkpeT65DuTN6QE%2BeLHm6VmyDYp3N3B8W52Feov6weqktKDzTVuxlzIKGopItNe5Xze2xXYbVa2flf2rD18KPfGeXoIMY2AvXN%2FDLUEU2itzm9tQpJgR4VpknfDLyRDsULCMPMPOD%2BcwGOqUBBjH5ejxj2duQNk3AvReeU%2FMfTlFwcrqcLPkCo%2BxQVmG8x1Vj9WnB00bU277Inhb9ZHVONdq5OdD08Yk0dxOvxS4sAYw8lX3sJQfLeLQBWZNnjuCGuqUi%2BHBW%2Bsaw%2FH18dsMA4Ki4h%2F1xrvaA4eq%2BjI36j7QESxoM0Cl%2BP7lfs%2BT5YQyXql%2BsxOkv54oVLvO74%2FrB%2Bfmcofy2MuXD%2B2Kmd9GQtaVP&X-Amz-Signature=0f5cde06dac8f666a327bc782c37cbc64955a9555c3e4c92835d66356594b9de&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

