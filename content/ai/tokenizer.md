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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VFQ7BBI%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T082133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIA3DD%2FkirWOC0FTAObyo7UoL8qvufFF9yeewr28w3wklAiAQ3KBtJkKN0QUn%2BsX2Oh2XS%2BEvzoZ%2FdToUk7QcyYPRdir%2FAwgJEAAaDDYzNzQyMzE4MzgwNSIMj%2FIDx0Wvh48r28SxKtwD6PyiP7oYb0g0uMkYWumzke%2Fa9z6XixnAgW7UK%2Bmj5qfDRn0XEVdbvymC3jCm5gC1NGrCXloUGwN5iBM1vFQjlqYz7zVvpMBEobffHshJi%2B9%2F1qRVgqe3LxsaC%2F4Piky3QCJLan4dJhUH4sWYGA0yNrYUONyHNckiXix4PkK9Q1c8zz6GpWKcasZkNdJnWcRqZc76Wf9JXbagPxGTGJF8Y6bi7c%2FuJbHWzb4jRlN67OrLTxizw5pgQ6ar9n43hNA0DQSFmdSc3ZBZCKxuz4lqvCKz7sNV02Wh%2BK4DykxRaq1%2Fusq%2F07UvSx0lPD1IgI7BohyIRsxkQQR5Cm1z7QN%2BkZmQSOQi2zFreF3ZxS5ez1tMosG93JegwSISzQUeYViJsO51T3eqojKOIM6GwCBMJtP1q8%2F8WzonWbPQAb%2FoaPSZ7Z%2F5XoKDE7HQiu92HToE6sIMGJ09Je%2BFeaV5E0g2qogXAhfTRCEi0ccueDts6%2F9niDXIuMmtJDRMEoTK%2FYo7mErLVc03vGGHiG3adjN%2F9pDel9f161kOXrf%2FQ4Il8tweNWZc0VpPh8IB8ezquAQoVvyU%2FRhmyQEDfKVY7cd49uB3uclBxHGNcM1rPEBlxBD9oes0A4ZrmJeMF%2Fsw95vMzwY6pgEUw4z8r38CTgo4VLSxQeyug6PvCH%2FFw5MSVnxcY5qMy%2FgiBOLhvg5ZaNOKbpB9ThkWVOI3kZVtHkmsk7sHboLe1M%2BP%2F4gIJmnIQ7gcSZcgaI0GcyVZBqsVfFa3UBQLliyhBAPwiupfM0AC%2BhODo78at0aAKpaAqOgs1uflbb1BW50XF2JvsEL%2B9%2FxzXFcfFLgxKhWFAMrxdTuAufkgvEo6nquxQek8&X-Amz-Signature=08b6fae7e63fa1905485dc5641a8722552d74e692e3acf5e852f82209d23e48f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

