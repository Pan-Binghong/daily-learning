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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZ5KY4CC%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T034927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIG7O%2FXm0WFS33n6pxV9Y9bVX2wgLDyzR62zLEe4ESPQPAiAaw55xqH%2BoFSV3oASDJyQQdeVFX668slqXY7qPLf%2F47iqIBAji%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsdXzKK8ZvZOlXiM7KtwDJcRPFDWyplI2VAI6WwqC5UeFHdTOKQ4EWKrPD%2Fau9LrRQcEsKG9hT9dKtR2rmRXfr1MG%2B0Lfcyhh1j%2BJDNKFlcgLLEn%2FMGKsz6%2FQQiCL%2FIyDdFoGg3NQJ6ci7TcRecnupkFAT9pfZnt%2FRpd7jTLaQaee0qpuBr8LupHwRFG9Kb86NgVIi4exWqwKrlSx5L13ATRWSB6yUp6PxfuaP6fP58QztBkrZD9nucB4Dx%2FiNX1UotjqAia%2FO5B3rc7lGpZE9b%2BG%2FH2GEPJYuMOxitIC6ZMI%2B1e42wpdXQrZCZmJeht%2BfaXnxlPeeqSNL8F90VlIIxIJtXzEbEiJ%2F%2B4mr71EOpO6xjRF7azDhlys9WaZqpCpwEIPbz%2BY5h2Yqfj29u4N1OSZGo0KiFPr5IUgae1CI5oBepWFQUnm%2BegS43Is77zG9Jn%2FMI%2F52gX6glcjmNss%2FDJzgdbMmOLBR3Ya0ocp%2BDyh%2F66VcLzI42hQN3dutsu4GSbPKzdGTv6JTpIOYkxT%2F61ZIPsLdtafWthjJcAGTUjRPOwbtyaV2%2FVVwegZ8NmCt5nbIseF%2FvAiwq8WYx5mT8arU2pLqZ94ohnTT%2FqH0IylcZrrLJdft1tuR0YjnsmSsNY2a0c4b1NBlP0wgKyLzwY6pgGT1tJMXIsw8aCFlXLJrD1U1ODFt0kYKglYEWtnT71VN%2FtsIVkyACYlUl1x07QuT0EEgc1Zy%2B7ytcEU3QV0fTJd4BecNMZmYHyQPfuZQfVy71BeIbzc32AaPMUF%2BGIQ7FC1PhIoX6OGWLPYyF6wmHgBIAd6TkHxk%2FYMrJY4tdgX7aXF7yvTBcxyCaHdzcznYK5R62OZjMNjFRH2QsHghcBAj%2FhiwFBU&X-Amz-Signature=70ec81f2c2071eb6dff36ccb4fb64e64afc56fe072ecb2551b8413f1c2ee6d21&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

