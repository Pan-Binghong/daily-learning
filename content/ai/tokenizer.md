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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJKMMMDT%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIED%2FMCVYzmIqUNQcZ9HVaUw81NGw3KRSNwCj9hkUNgLeAiB6Ng3JMgQJ72lRaclq2UKSTr0X1GxebvUAwgkr%2BabOKSqIBAiC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMW%2FnowX0Y6VH1Or3YKtwDIwZSY7nQWBxQcewsc2pmgXRnyLG3Mo6PlMjcTq9wd%2BZYhuTpwIJ%2Bhnlarwrd0DjvrC8QLZcx2hD3XFrsbQLKjYJEiLVWN%2BIE0Qh7LQiTo0AgAhQDM3DnA0DNu2inj%2BmgGPwDELtLRd9ayjgownladw3EA2P3GsxZ9%2F3nqCxQJcn99sOKhaeiCxnJ6OsLEhzCqvSCdoIsmTw57elNI%2FRHeKZHqpN4QHt3EZ6TB9mh4jJRqb8Gesd5DqCM4wVN9iYd%2F6P2t916AINqVF1yBc4eASb4inUuAeErU%2F6GN61dZIfkxBy7x0NR9ZbDaZYU6aNU8YqqKmh1bbYCLzcpkryfXOvznqCIKtkHEEzquiZA0LnARwk6LuKiYtyLu%2Fo6r083lYb%2FbKa5anmGrGPDBnAaryAypOaCfvVoDnwCpuqWOE3TqmU5zht8gSkUxtWOrmavGW30N7MgyKGrIrZbKvfx3WEug3g4ig%2F5%2BhkZVgyuEi%2Bs2RTYYXICEK%2FIu1Ys70%2BZmi6at%2FB%2BPePysNYg8uMcgnPg4dhH%2BQHgz%2Flp%2FKTRS4wkSLC5kkiAnIhPhCFQ54cxDadr1JXjPVhup9Sc46b8ejh%2BKhpXo0c199q8CHj38jwrYQKZKFvqEYfrq08wgLnNzQY6pgGJL6FQbRuyCcyTjzTMoTMkTqkBDH2ruRfDTA5gJJfKjOAcrXuZyqs3CrmDJDG69Y7NMJindIybCR1kp0rGwb1cRbewK4pORu8VlJalKW0aXbed0ag%2BIgTcvrv8lA6jYfHbcwiKXSdpl1%2BM8QzQnhDtECxDEsDtkLKFuB8mRVebgyp03MIQMiIMEoppPh7iA2ayqnOuLllrKyXMygnBliHWIIvVVqv%2F&X-Amz-Signature=3f6282fa4aeba5e3883214f6460a09b4c2e3e5905ead2cc019608a332a08aa3f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

