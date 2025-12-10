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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWHTJQNH%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIHZ3KZBuJDlzr1rtTfzXxeGfnvHKSBO4hqF0eYbG3pl9AiEAtbHA44jw6E1%2B9Qd8bbswLM5qPtqgfQPROBp5z9C3ItoqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMHzzL%2BHnpR5ybkZ4ircA%2By59gz3sLE2TFZL3WoLSYmerjLG9xBwZXJoSEzr7dZGZgKyCeWIu8vj%2Fcqtcldqa%2BMpobSCGKq1F53g1n7ACV%2FreLc1w6V8x6wJqJgGYp7tAxiZ9ws9G%2F62fNaeEzWwgjXYeC4kI6Jw16IwaBY9o6%2FinROOSdyauRxB38wBvhZ%2F6X8kxeS0V0n5I3Oo7YOUZTivSOpKeys7AjdwhqGCe777%2B7NRxiQB3MC%2FqdlMkgssREU6gRU1VQOsFjmYZHXYQkY0ho6xxxDiHEUTXpvdcXLXYxZ14RypwevZaKzdMRZfkkASwA3KDypr9izD4uNOwU8d4VMOCQ3UegMQmABZnCGBvbXouzgixAm%2BuXW519hMeOKNI25IRzMrUeZHESoRNstW6g9Y%2BLZN0m4WquEWzpgMw5uObZ4uZ0XH9yVBuA1xlddioTrn6FGfwbaqY8kkoIH09kDnOX5ATQnFkWoY0izjFMfdCQp0LsJ97jw4IPO1m7%2BfdGf%2BwRW%2BRwyTfm8kIGe6rBG5LGtWl2FeOzn2%2BkYxEbUuLmvCDS1OhnWoyYaR1zCxr3aEIdX48eAy%2FwFyKQTwGdY4A7pD6E%2Fr59JNks0SkYKfsIy8SZSO5Kz9yHOnj4yaO2GOKyY0oWnyMO%2B%2F48kGOqUBiAXLRsT083PNoYs6IN2qt2M3IcTSfRJDclSe35u7XczuXHA331W31F17JSSiZYCWfZlJAO8ZFXtGtV7yfl8a5wy9y%2BoboGEr3mLoMwKwg5pbqYzaUW9CUrHGQlCY%2B9ePXFOrNG12MLr1RnMtTxUKY7p1F3om33MOm2PaX1R1ATo0glQPAmoOrfREZaaPqXDNP3sdgus6az0FX9SgoIAH3%2By3GQmF&X-Amz-Signature=a0bb89c5ef36f70bd0780d62bffb49829ae92607806cce8d558e00a7182508f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

