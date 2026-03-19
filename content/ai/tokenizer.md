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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLQJJRKQ%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T034157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIHWUtyEVfXW8g3oD2vkOudpLCY7zA2hQUj1AuVXNodklAiEApzztYdBvnIOSqyyVBE22MWDDOhI5pe2yOrEW%2BNGJHS0q%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDNhLLCt7NqbE1tDEyircA4VzjcgYGlMBtkYYcbPvV8UWT1UP4E%2BrajIIA0cCVFVIRrb9RlzwVHIdL2jw5mjaM3OGGDiQ%2Fa8A0rAsii%2BTL8hlRkWsN4vyuTxQKk4WSutTLdnEhjFrj5SvJU6r5ms3EXTXV7fD7kncfXu1210cpHX8boF6MjuZZjGXLve8t5Lzi%2FnIT%2B5COwgvM6OmnlL5hyWhBW9%2FjwqBq5ZLaPAlNv1fA5PQoj4DrqfkdqrZb5HQwFt93E1hQv19pUGSdqFdSF3S3ya0%2FT8cF%2BlIOZAtOq7DSY7y%2FDNBSvPOMxAasMELLqYFQ2XdTufXmhiY41oXHkXcEHFNFol3CHsJ9XlBnzEjAhtTbD17cluymd0lxlOlNZFyN%2F0R8oZyk1VVGMZ8HIsP2Vcc3oePIZXtivi8HROeB5uyAb%2BFME3SUptzM6G8XAsPHHQ6l2HR6%2F7KiihVqDClV7mofX1bv0yUU0eknhTvBsY50T6PZ7YIhtZo9kK1m1EqI4mhpvjIdmceHKx9drW0jp6PV3mDF2s%2BWEt7M%2FDT%2BSBIQK972Vkb9kJ6DknivbRfqU9aXQ1UZZg%2FxuJEZSKRkGRzV70V6dMorlIBsSoPGZoO%2FIbBVg0t8ZivFoC7giCuGXDi1swNUsxhMKrH7c0GOqUB7opsniRLQ6yEsCc%2BbE3wDG6FllP%2BhsDjCJvN5u5BSLK3%2BpvXk5UcdYC%2BrPjGyXhXLFXAfdCiSvuPgrZeBv8lxRS2RjiopUy8toRCQAgtkJEmZ6q39pkm6AEqXp4jP7vImg6J6z6lBAmXH4pRmvGxgi%2Fa7dzMwpNjQ4PWrfTEUSydoU8V6XludSyCvWoUR4uHHMPZLncZdFnGZqPLs%2BDgB4NMq%2FxM&X-Amz-Signature=adf78aa09e87ece89a9560ce92bb6b93ae342d76be07647cdb5f6e59e1d57157&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

