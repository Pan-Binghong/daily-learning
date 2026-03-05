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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOXSJ4FD%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033027Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE%2FXQ7QB1r9MJvyKfMbf66NI0w4%2BZPp8anPWj6IYbH2qAiBsldtEdQmnOJbA1QFK5muv3j9Na32tPST3YrUPcuWfUCqIBAjE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbJUzFZQnqgh7EfuWKtwDAem276LVzum3s782jAH94PglkFajPya%2FOtp%2Fifnr8DV9oyKWLrElukwNGCGXx9LflurazRAFPC4Q9hDphN56oBM3SSwa6rgGDPY6ZydkHG5fhxApHmjOUaN77PtGJUG5UAURKFZm2BiI26e2Rqh1f4X5Q5wPgCoBZ2BIJgV%2BjPibFyClS1a0NlzRIlBigFy6R0mdyf1L1drEmOiqtxOv%2Bj3aOaGO3jR7VsK7LrtkX%2F34nQQLc%2BCiBt%2F1LLvgS8numTm9B8YQWW4y0tjN5jrM86zC3zqCaO50I%2F9bqhlVDLNub32FhSkyv40lqG%2BPWGBwcyroN7B9AGoxCdgeW0SN3AYt7SrGWCRvfuW9hjXSS615js8pTmLDBa%2F6Cwj2G3vozJnBCDLzDm65e6WPIPt1lBp7jBgYYgH2NZ7IR78oFj4yQbmFSkuItSsplozRKNE4MD7DXOLFHz9IwFWLqQ%2F83B5c8zRuZKfajdtKhnCMfrSZJRf6DS9DVEoWxzCM2FRQXqcDD89gzgOHtjxgHAlxyCwXnKuLCSvK6DKe38eA8pXjIFUDETwvLo3p17iCjWhA7f19Rg8yCqEJ4Lbm2KS2WBxGbTK456SikFHNx89gcNQgVPoTbQVG59FRfOAwyOCjzQY6pgFNqj4TmuF2xXQLI0YNOXyvxdhwGgLK6saAojvfDmIuddkuJaOTuAjyF23e0eg98mWt33mPea9%2F0JlOKhZVXmjZszLLAVbWWgEPYbq%2Foa4syVbnzCQOa57gNo3hfPXpnVP4TKa02S8O1F2mqn8IB%2FuL5zlysHj4e5vOzujk8kL44aT58qrv0k%2FCZtdL6afXqy3ByCuCpO0Cm%2BxuldcqIUkhxXpSgYqh&X-Amz-Signature=d575cf30208eaad841fe819e1b8c6f6a6816bca8c7fc504ccecf450ae8a69c4f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

