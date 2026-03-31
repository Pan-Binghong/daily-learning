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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WMMR6UA%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIF0s%2BLoKfjiKibnSe7sokgLnXZYbru3Qf7kRE%2BtSGXnKAiBqkrZ7LE3JNQmr0p9XL0DMqzM4ZqwkadlXzKOsUi%2BzfCr%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMPGbPnkJaBwuSnzaAKtwD2%2BoB6QcQtZu52JqDhUo%2B4mW2XDLQuFBf4hcXovX5%2FSUQvl5uCMoiUFmw8dikEjt%2BNmm3jHjktAnVrWQLnLbR3%2B%2Bynv2iJXUk3eUBAdpy8oyAaaOfuLkzxAO4mOEZKo7rkeacGXHVb3O2kWV5cAZulJnbNc8hJ58HPhwq4Wv9ToyM%2F1gbeL2Us7RreGI5vEI%2Bl533tI1%2F4nVZGZtKdlmyNNymfpBQP%2BZdws%2Bw0trAP9t3MGxyw%2F9qqm3pGmJ310CDC58K3Osg5ASbCMUvsDsIEh4cd6FdZhNttHWK4AK8rGipIYcvEMe4swqHAQS1kUM912bfx14oWpxO3Q4KDzasP0Tb%2FRrYBUxjJ1UMzR8cPhbCny90f05alw1vlG7%2Fp1XdJ2PfUHbW1YBBbeG89b9syfDkJHAkGOL4YuqCgxP7Y4Zhu32dyCna4oSHgEOGIVi%2F%2BVYV0ZjpZnr4o213VQA5RlfQtGnbCXouVcB2PkscivLKfzRhBJkeIoVfByhmJ9L5beeBmNepXlhahIVICtT13L5MrySKHL%2BOarOUlLj3utaHQeX%2FJoeCMwRUwZsuJ82qDD1ElwojakM%2ByO%2ByU9bLu0ZzX7UDuBpB%2FjQRKF8%2BT3HUIn78%2FlNm3R9%2FXKkwrfCszgY6pgFkxzpuwwuSicwgE%2FjhPLof4vgi0E4j5JM9t3cr0bx7GJkmy0TU73aMy6BIBqmpvDdULkDHFfNs%2FSv%2FFXx9jj%2BNBHOPeYIlMFoZNxWm9dsqtZ%2B3m6bfa6sHIDzWaRKdQqQWb6oExOyGW95n2cbIJbPeu0seKf5PQzRwPJsToF2eCUpWwlvjt7ByYJQhpdV52IWd5B%2Bee%2FC1%2FrIcFhTHsFiiB9pzUhap&X-Amz-Signature=47e4ef1f1c3de84d3d5fe59c2301dac9403bdc831037333bc9b53bded1d0a1ac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

