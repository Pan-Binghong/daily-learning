---
title: Tokenizer
date: '2025-01-13T02:54:00.000Z'
lastmod: '2025-01-14T07:52:00.000Z'
draft: false
标签:
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNNO5ELB%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095850Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDpvgyi1rQaIr8REnq2jfQtVUrJOCTjWt1Ps1LrNKGhiQIhAJMG5T3i9Hzu%2FOMkA66NNcpw1S75c1iHpDbdz%2FUYPDb6KogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzA5TZoZPU%2BorAmar8q3AOXMv42RUERH%2Be4iDg6w91S4I6VWR1wA8qS7nP0zgYQvKBHQ%2B5jMDu7AN2ZGlwXbrXk1iTo5May9bLlYYLYcsIH03uPs83ag%2F%2BfP4D5r04h8J0iNZ8RrM6YV3vTXCgR%2FqHJh8gv1wYucCH7lSitYeBagJDs7ReGpnkVMDhFL31RtPnuS6I58tsZMWyO5R60xFnX%2BYBF%2B1cOgNAiT4GPTjKlPQNL2dFL0ThnUd%2BMNb8%2BP6BHr5dgKw6JUDxJ34BERpbZlt0EwkOnxhlBTfQGb086rTnqUxF0sZty8vM%2FmzPECU1fsdvb9HwwdF5NiHxC1FAYlvYSvm1xQNU4fhK9dG%2F8qUH4XQlN5fp%2BilTrqBzVTJOYz%2Bys0S2wVP2HJhrEq1bCeHDp5sBz7%2BsUsDOYRDKk%2FgZCdfTZyKgPHAzWW%2Fhr5lqGxgeUsG32j4ME9DMd2%2Blu%2B84tvt9E6M2Z9WTuNbHXyDzZ4q6pgr9bWpSkWlL8eU%2F7V2PHt%2B5HhE33q2GNxCco%2F%2BBPUEOOZSsEvWBRzET4CToFTNiy9YHLuMMsyWtSFWPLTC1zqaZpO805sDXI%2BUsmSuUSAhz%2Be5kGt8hgXgexmaPZjhDEowsyI0Qt4Ss9nzE5WToyh3b7l%2F6g4zC5oqzIBjqkAetF%2B21w9jRUBqyo%2F2jGBxHxE%2FCQzbDraUpKXykrWmYdz5BnxZFKE9E36JBwhBL2yqtqo94MHLsgr7e1Yq6Qnb1y1OA5Q2CSJBQbhm4dPKaSdn7LQyQ3nJ4QQk43xA1wyRiq1a5kIBg2%2Bf75ZFs0e%2FxCT3c7bmzvD8IpaNRjtMoDgzm%2FCVRxJ9loxxIH%2BCO9HM%2FOPXwBVXadd%2FV4g85BdeZlP%2Fh5&X-Amz-Signature=13853693588c4dc38dbeb00a6455f7878d1b2ddd73de13d26f1688b72295118b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

