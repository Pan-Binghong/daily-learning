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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEEFOSGX%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJHMEUCIBuugm39X7aZvKioiWUpcRj5CFZeZ0UX310T8NdFKjmbAiEAi2ErFILRteQ8fnidiyvRjkwCYLpwVrijxg2mq8I%2BdiIqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEgVvWITScOZoXTxJSrcA5lGr3ux00JKiz6hHY4SxdNdj%2Bbk1ZWp%2FxVlSCRt8ex%2B9AZ3se3l2B6zctBBrJkvCt54jDq7a2xOxwpC4M8CC0ieYz75YnpBF3qwIwyGLQE1IfDb1LKIiLsNLQMNU0t9p%2FjX6HtryWmAuLAkXkhSQH6q9tP1CRzuCeEH0jY6CQ9k3Zc9ZBy%2Bkq%2FmcJV7NdXcdn9prAJgDSw0ff2fSknjxDRWBNYHdpZw1pJyNiCvtrg1ybweoOI3DD4x1YM4b1XJ1K9xPSazuMY2U%2FRuBBTDmU9KAxs5Lh9H0lD7DF2LYyPHRBFYz02eeUbOwwboWfpq2VeOxtDJqkqVQxUOOl3RyecJf1N4f0h0ocjcbGNNPu%2B%2FMsZZtQaW%2BIqsN1oOmtyJB8OWVtuyiMb2M3CChCDu5C0VgAGUg7tHmibUxWd34ufd558O1uzkF12UqJPm75TaQF4z%2BWPN8osEIyLVLDXRYrwGkIevu5Clryig2ygFcwPQqeSla1EGDbpfXwr1BteIGLhGXfI1NTwtQRclroWSC8lniwQosrfI0b51F3jjaF7fnL1ASArbhJuj7y69WUAuw%2B5lE6BT6mvvSBUXbdcp2s0aVa5FNXh85KFdzufHG15rJ0CjTpcq23opldqzMPq5uswGOqUBOzZVuO%2FWBbMMVJEttF0kyQHYjKP00McNmCeTSq8VVqqkdj4LOhh1HNRy%2F0sK4kapt4RVwuEhdNuInYpRw0lF0lNDJP2D4KnhBI60V%2FkN5LYvzcLplVsIsjHxvanppZBcgC%2F4bdo5lOwDHAc5Yc2HpsixJG1NHTgol6rHQgn%2FHRBbGKvXtLHeq5SHGhViQ%2FKU%2BywRfmTUsOPsfN2UJgC0g832texx&X-Amz-Signature=9cc237c757e39a2d357e1a96de0ed0f8515d4c66cd498d6fc0ee1c3b58fa0589&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

