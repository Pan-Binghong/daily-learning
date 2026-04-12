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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DBS3QRF%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041234Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZPW8wm3TuOFFGkg9WGHCqPoM2eKyf8Px08KN6avehEQIgBg7JfPLiaUtXqzqybhqmRZmdDIxOHCfwWjb3MY02Yz8q%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDJFq6DygXGfeRLfXGCrcAyiDlk5eHxvD3KYDlnptRh23JUq0w%2FrNd1hfdjgb8kcKVmwIAsZbTrsLQKPUUC1D0zfaRS8zPFs0qWH54gVK5oILnvdnAZJossNltBhz0K6QiOn%2Fc%2Bpl4jNb5EUEy2zsvwHj9kWOtq7z5HtUUKGU3S2vev9zxPrhn5JAnDjXZ7yBP7RdH7scwFxxeCj%2BpV8O1sDCQZ4PO8YP2j3xr%2FFW8JoXiTwE5mEKjtskjMw2ffMtZPcln2B274CF9b4N0mLUkyoyBVxoVN5Cruo96Xe3HebAn2Jo67btLe4jEtD9oE0r%2Bmqm3kCDZ%2BC5Yx217Z%2F4Q9sey1IGD8zzfJ2%2B8U%2FZLfTtKld2Pjy7W27yhfzz0E%2Bgll89Mxo2%2FVrV8S7Mn%2FRVhykH%2F6%2B58yOmtN5T8ZegFgnSKANeDhiRLch7pguHZdnSYNuRNPlHdqFOsXZllmBgfJHOqcykdXwkjJx1tVyq%2Fiwqta0i5mKLPUixGQMGyxhOe9vqZAk%2FDOHzdFmOB9bbCL7vsA0f3wZISPzPnMLPPA5m8XFipliCAQihf14btIaI5m3wuAsKiTMNIxellYRJBFS%2FZ5oD%2FHa%2Fq7QgFV8I6hP7GQq14cwVIURsuAWFNaHc0gGqIANOYU7JgpBNMNmI7M4GOqUBkzOx4rMMYxtlwxWKlqaW%2B9PLNDXRcD9MC9tRg2sGT8IsnCs61eRC0%2Fcct0u2nXfm8%2FKPdRsmHzw%2BORstt%2BO8ghN6h2UmKe6I3umQZNzpaqekGJOnjRgM8LCz07kBVrATo%2B8lZ74C%2F0XDL55Lf%2BQNCKsSSSLgU6R8Xx8cfMfqlhF9LQukYPBH%2F7X97CWtMC7OomS6sIIa9T2wY40YQelooQvyq%2FRc&X-Amz-Signature=4ca32fd2c60cb73b6a01f0b0fb94efdbce74f89821fbc54db41c3745461ad246&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

