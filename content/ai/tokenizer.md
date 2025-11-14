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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGTDB63B%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCN9ZMz5mV1jg%2FFIaswTTBuNrfzseso7oFsCgY8FF3oxgIhAK1dX0TV1gKMeNomoMEWJkMCFk%2BOZtJmVSt09AsCZCEGKv8DCFoQABoMNjM3NDIzMTgzODA1IgwcG4lIjt2qmGjHC3Uq3AOHtFdHCZoijdP2kMPeS1EJk7Cy2Q9NN9bcL7w%2FRJ0z3a6ynMpFAJ6tUYloxr0vT0u6zmCR0UJ8DAnJEjASa97qkYPM3JRotOQKN7%2FMdsz3q4fhfKCY%2BNWjiBkqwpSzUKSL%2BmT55WV%2BC9k8eidoXkIIxG%2FoyJmPTRePelTBO5eXKHQTGsXHptrVWl9n1ldyXQ8Iq72Cx%2Fcj6xBl3zvxC4odFLpoXvwOU3dPnbSsofHRP6UBQbNhODDyMPX6CRKoL5w4wIleEmd3mWXD6795FjRp%2BjKxXL4mZke7PF%2B3XZBoT1%2BWla%2BItAVUJqy0pyMPZJ4VGkE3HNrVr1iB2ckc0fVjiZv40722Jc0T7q3fmduPwk9qtHls8S6gkw1T3z6CJxE1om0Rtc7RaE6f5JC44GspITyy9q43slAOcIAQsappSOW0VRWI6a%2FH9guOG1hEyF5ZBQqZoMDfbD3M6cAYXNE3QuSak2LHVScXTEOKbnY0Ke802H2PuhlpzhFl3a1CPYEy%2BBiu7zpInRG0T9QhFMz7Vtzb3wCHJV8Rr1oU9hO2ZTOTQWRzCXO5O3NCWPTYAgPqRx1L1k3rcBGA5wNjlsUe1Z6kKYfR14zaoQjCvq0Q%2Fkr7rmxN7nX4kHeZHDDUidrIBjqkAa%2B%2FrB1FPZCRpaunAH6aS3zpJ7nZHv5XbUAfJ4HC6uymiD306PGy1WN7rVVze911Lmz%2BJxQW0oDEf2k9jOxvTw4FTd%2F6RPB8fNz4teLWwuyrwN3Tc1SZ9Oegm4EvU0zPyPOJd%2B28HFWqUUxxl4RGZ0FQ7TGZqODJSOqHcN4tneXu%2BF4%2F2sdje57MFy9oBO%2FxdBZFBjdVnzA5dlqvwkowzt%2BaVyab&X-Amz-Signature=2f574a2732df0d98629adb512986c469d49880d7a258f6dfd364dc252c021c28&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

