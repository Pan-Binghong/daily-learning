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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VSNYHMM%2F20260312%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260312T033351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCToIRFVxTZI9xqsNgT7KiSNbKNSSZgzilYO2Bm%2BdFBTQIhAI7MmpYqx2pCxzdfvOk%2BmWe08LZ%2BjnhX6e8%2BbPLYx5hiKv8DCGsQABoMNjM3NDIzMTgzODA1Igx71kw51aSt%2FOPZO1sq3APGVaDlwbl4hQfCQdVqxgQWEDTTskGYWDr4S7X02fDaIqiYkFSk1blRXF2jFDje%2FHs9kmNfOOZQgZgvKl4j9Or9CJI2C8DjAXvU3F0pI%2FKo2hmwbbijNOBOnrd8QcF6YMDNyhanK3JMB3LZ8GDthWBBvf9yXTvFsrOKiCSY9fl9mFIdlA8sDooMwIzXrwIW53VCL7AohI%2BjYGF48Sb9o3%2FunOC469DsV3SGn%2B7ZYU%2Fpo1meRvlaZn6jrw%2F7T917s6jgQ6s0Ykq4cbR5L%2BT0v%2FOtKdw22BG65XTZAAlojnBkMh%2B7P2CsSkBRTFLk5YJEyOCjhhq%2BI9fOWm%2BuJpBFh3VtbMqFotjhfsHZlwwMYOYqRXKl%2F6%2Bi2%2FGkhH9utdjDEhIG%2BjEZ2D2YWU%2FV8ryTMA6ukRuSST8UYifrDi%2FHibfzJ8ucSGKrMrFBEIIxdTuQaB5QJTLBnHqQfzPgrl2%2FoYWyscB15zz3uPK9LCiOdZwzNFkmTsSTmp9TBY2bXwKCiD9X4JIw5Y1cidWklLLYPrcfhCzOsbwYNmWa7hIBYK1ZHm%2Bl7WBeRr7Egiwo8PHALymK0%2B4dQihivxWV3i%2FMmWnIUvbahvQtYY58ilhEvyTICACpT%2FGp953bbxh5fzCLs8jNBjqkAUbcbA%2F6xB0x583iYjOf%2F3D9P3d%2FbGYytusSLBmlmEZkvzG7M01q6mfFPLlFSGu3z3kiVTWMSwgfumQvSwbPOBb2uGl%2FE1uSw7YIH0aZZFjj4QiJNoGbV4WucVwtrR%2BuYat6g1Ixub8nDgR1DfjtzoUL%2Bxy4k7PbXLbtJEByKwDiBfF1E2KjYqGQj2glKfOXGfihJHQ9uxik0Q2zhO85EFWVQNZm&X-Amz-Signature=779d981ed4e91a93469422baec1cd3689ed71148c4906ade48a9027a8a52aa59&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

