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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QG5YAAKT%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T030211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJIMEYCIQDBJq6LAMpTzb56YwjKtnpwfhy%2Barvvj86VKmBJCASQmQIhAKeUdUToG3aAQqQsr1d8ldiBGNY82CwbIcxFwlJqsD9sKogECOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0AeFwDUBmoFPmRHIq3AONYHoQxbhhbAKeFwerrrJBlVhsrfoyY1YBBzhHHEqHG0wVKfRv%2BJX5NS%2BNwYzwt0U2VRzaFVrLmSCNN43Cys2eTaJKoi8TtqRJgQRlwzFTIQq5ZxU%2BMMH3rHGmebhNyO2%2FHgK%2FwcEJu9Yd5y0qrZcHcV%2BvawNPCVoscS7iI5cjuVF1PQ%2B822bzqyGRuCwwhS5zPS7MCZ0I3ZY2UPFwmhmp%2Bbg0exq37zkaf2bQ9sr8LTpKKZnzkHfqtP4EKV86o%2FbEbyFllzKda6T51iwtXWUoHWioEtD%2B4c07vIKtPYdVPh5arVkQRwN4%2BO%2B4t%2Fw07KVmwOthIQbVZrzsW0SMOuY9Ub41G8%2BessmAXxbQTidVU9DG02F6099cbG7YK%2BjutT%2BAr2u1zgL80CG37Tss1CnPLwNAHkaQAw1NRbRmvOwbwYRiiqan884tYf0qVrtXz9r3bIiNfxgNCrzY8jD7KOFtdm8BNhZmMdePWKWZFnbwbhv7ixRykcwdslCM1VnfcA%2B76XAgAVnSvuKOiQjixt5UnETflsu28J7w8jQ2XjqCCZyMd243X5WMAGKCaen%2FDj5MkS8PYn%2FHvyokjoOgMyXX%2FaFwkvs%2BTcJYrVp9FHlPMYxT8z3QyTeUtSvBCTCy5aLKBjqkAQ5NwKHP1GnHZdfYh1Qj60oUDbwdSmI2vjTPsu4wdXr7d7XMu7Y2uyalzomLxuQieh%2FZ%2Bj5Q8CmyCA2NFu0oit0srUjvkMz18RKWVo%2Fcr7L0195UkBYxoeKldOuV8U%2BOPIezxKCWxgEa%2FuInoVNPcBSVIsktZOk3vf2NMg8Glgu2eA%2F8gnU3n7Vwa8slRSG9q3eyJlsUH8onSwjiZUqv5wopw2s4&X-Amz-Signature=ba2939a28fe2c7d51799149c2ae78ed487211313dd361d17a72eab98f1bd3cff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

