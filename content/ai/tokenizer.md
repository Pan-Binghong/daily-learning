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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667W6VJEM5%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDhGHD1n8RnEOJC3foIiIdBXw6k6u08z3kyoPsBaJ77JwIgCNvRN8JrREINaMJ48d%2FcIQz9%2BroH6r3EbA5lRWk8m%2B0qiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGyYz8T1yRQ70JNeGircA%2Fqpn%2BBAw4qFdEySdLGrdMSP8JegQYUe%2Bqystbi3k3daidYqU9XxkXjulDotZ02dzCtFnViaE74ydWVzeIDv1IgAQ3JuI%2BvXxOFfONfwOlxbyGW7PF2TW%2BQA0TeCxwe%2BFygdU%2FSoteNKCYqDLL421YYeMf74Dp30HSOfrgVo7jY%2BBOeDUVxU%2F0T2oYMJntb7YeJF9SN5PCGgAuOgKxmCNMR2kO6%2Fuwr7bbkNV1j3kBZvNR0d3sxSRLIMvvxO0xDljAhEV3f2KSj999hy4xWRWXEZ0eliEz%2B6n9Ykefh8x3DOVeweYWN2WoSNX%2FJmmwUmxTBdnl5ouFtcSy7XdcT%2F01I4bHqx6BWdk04AFuKpJKglig6gCxxWMfJT4Ey2okSJhBCSeO6ktHXCtjEBKyfcPnoHQtI2qh9cc7WNapdSW9mZA8Z3PQDtnvVPGx6TrymQRYqzaH4zBi2ztCdCxwMTV6Jbb%2BN0l1t4Dfi1pW9hrx6wR4Bvr7yElWOxqC6Agy0WUtWO9McpctPPzAf3MgmOP1VVcJ0CcNxo7nPaJezZ%2BgQj3bIW%2BJNcjWqBkAKh%2F57dnpPVh3PvT%2FFhrhdcGrbocJvcRFfLR7u%2FUjYBmzdaTcM8ZthaP8JMAlFudoy5MNaYns0GOqUBj1LABsQ3VJH%2FrMoMgH%2FT0rIKau7uxE6qcL1Y0WJDvpT56Dw1IGTTU1hrj%2B50S1j7md8BJh%2BX6XIYe9rm3dP1YK6%2FFxUFwQDq8VPGZzdNTf77vi28cTreyRrMxxHhf58H%2BlUMA%2FGpYc%2BH7p1mnHByZrMsJtXz2tSH3mP4fLv%2FGrSCbvCDy6jeRjo2hpNgvWTC4jGYAxkHF6PG6q2DUeKkP5%2BQ3lFz&X-Amz-Signature=c1c55225c3fd9b63152dc30ea1a619baf61523cd129b3be7e9d151b0b30428a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

