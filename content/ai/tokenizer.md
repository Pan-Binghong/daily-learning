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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPWDPMZH%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJIMEYCIQCcPBA6Do22hzrwRJOv1%2BWtRaEr6Voa5KzZsH6LtvAJXwIhAK1nKkcYHBS18R0QVIVKcZPqwP5v9yTnZ3X5sNBb0OwsKv8DCDMQABoMNjM3NDIzMTgzODA1Igy%2Fx%2FZNfE4dHvq2PA4q3AMtKUQC3iXk0fOnAdxHBNJKalkjqwXtXTVjeGmPDNHasglA1F1NmbpXuauHwcE%2FZsg48dmMUfU3AGzK2R19sC6hdeHTGKB6GjYuULBtw%2B%2Bl5Jiz565L1hpu4aiV4fef4zD9dfqfR5rlD2WkfK77VH8nMNGQw9NcSd4b87sPXbXIDvO4oBNfmz%2FSAAno%2FUKGhew9wFw7yYfEpNlVzHwtiUXWevZGMnhVCp6nZcMwSHpD5F1ba2ybrQ2lvP724HUvNpMeH2yi8FWswB04h0iamNo9UyEOfeH%2FmBXsqqeUgsEPFn1ajJsJJwIxuASZby5Eznwyg71fGjOXZXXyTYgQ%2BJ0ywU1zXvW3eOGW3Dc7RI2zgiPTznGKg%2BRqYlpzhK1S6K7laszN2RfCYecNjIWnW6FDbKmWOUn5IzlYfJGGWpEuf%2BLf7T%2FJQhLKyRxR8IxDrqvqCQAiOXxdWghqbPQRMk0x7zzRLe37NZHoZPu93C6yaTfBnf3KacNu3v7NwsanZT9Ctn%2FwUwlH77pRbaqrJDqc%2Fqr%2BO66gd113WUqfYJzfwY4x6iQgCColDmKcPrup3SmtxTxqlLeeezGOrHKJ4mEPp8WsujN%2BFCpzpXEQmavGzK%2Ba2g0d37ZAD%2BQIbDD8prLKBjqkAbNbN9M%2F1htRJH%2FtMIVKliF7VTFZXtHFq1U%2FzR%2FANFlwAtxZivAr%2FYHPvp11vsc4SFw7DgZ0pa5FJ%2BQZBHROQ%2FMX3pNNYAT11yk6Hc1cESgN1k4KQ5QRezfZLkUYaG4nZKUx6Ahket6cOrNRMZRMeWgj7Lu5LKN2ae27dUGlu8D%2BGaIgkA1%2FbKzui9ge%2B%2Fhmwlom4TXjX6np6av0li437kbImNgs&X-Amz-Signature=bf81c594e7589b09dff101aa262205121c867e94a3d76806eaa118c31872835d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

