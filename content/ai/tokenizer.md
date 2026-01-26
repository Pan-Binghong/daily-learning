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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDGV2FPJ%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031643Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJHMEUCIGwrSkOMG9rfnKRR0ZABK0UK%2FViIwDG6UGsqG%2BZtfXqDAiEA2cqCDPVAxVaKO8ac9TS7MvbLDN%2Bww3tV6vPoDtxvcfYq%2FwMIMBAAGgw2Mzc0MjMxODM4MDUiDA%2FgkHWus6puPjwerircAyrIgxTLqsEYVTZT8bBqexiXoIBlCd4ipJNSGRtlXS1nKNxqgxua39SyEGNkFM%2BSnd9d5S%2BjQfYS5RErSY26rJ%2FnYOxBs4QvIV9Wd4ry3Pb4rWILklAW0SWjfGBs2GOtVk%2BN89xxrZpkIeNpHlhiaU3Fz3%2FWbs4iUuVqFFrwP%2Fb2bG%2FMFnHfZrk3ZPFrvriJroAKZDtHZkegTySeasJx%2F3VP703Q5sOXRJ62%2BL5o7ZkUmhTC1bbAMn9uM3zq%2FPmD58F8WLUa5zDR1PkNSVAvrS%2B9HzZ%2FA%2BDMuycBVZCGQ%2FG7vA3UW%2BAXdAjXprBvwUSiUh%2BHcP6rE%2FJKYTHAqKdwuvG2aTrhQ77hTizUMsIOWtbrS9gwI2GYbjOqIkIppCkhjESKFnjJwwerG5PbTVUN2ALtRLzE6BrOx4FRcvTQZZFYyPoEOGXLjWAT4ivOe19hsnNs3BR60VqP3cA2%2Fgkj5bbrC79HW332l%2Bpbf6kc%2BUH4AysZ%2FtWzj7YRCXe7R6apgNsluDsbwXmDjpaghf5lW3iNiL%2BYhUXk%2BU32v7w3Ymbp65o%2FHf%2FgvIIyyESqSPnswQifCviDEIZ8gB8GlGfpzKd2SnVDPMf81bs%2FPoJKb9jegQ%2BFondG1h7ARqbbMMix2ssGOqUBJWXJHNUqt7MUfEdyargzifcbjY%2F2KGvVi79YCCAEN7Up4JsUvKHYf1koJr2Ort3QtZ4LjPVGygDLsbepibti%2FMR3pNVMuN%2F27ivshwTmKHgcBv7pcgkxYn64ke7u%2FueSx7YRtRf4tDEvl5ffign3AHdmOdB57KfhQVL%2Fu9HdY2LhFyjlA3SR%2F3LnoC%2F%2FV0yRCQbWDODKuXElyLG6dhLNYuecv4FI&X-Amz-Signature=d456969b113eb01c5773a08833918098cf747f7efbf9f480b522b979b57946bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

