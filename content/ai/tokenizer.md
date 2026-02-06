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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRAQF7H5%2F20260206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260206T033335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQCM5M6dQG%2B1qntpVqNPuZjVg7plbLPAiXp3Fc6q9eePEwIhAO7TdJrVAgQ0v%2FhyyLhE9%2FkGyHD5iGcIg9z2IFuRC9CjKv8DCDwQABoMNjM3NDIzMTgzODA1IgwDfeARDQmoK%2B38w58q3AOxCyr27I2bbGlVvECkzvK4vObIO6d2NMJdqdapp%2B%2BGy3TTWa9TmVgdB6xc%2FyL%2B0KLWsHx4km7gxC3hQCnZbd7DG2ElEGWLZ0MRBN34PWwDi0VZi3ST5Ef3WnrE3M1NsZMFYPDtsaIr4LWJ4%2FiLjRr8cbAuB0z17qE73o73jqEx%2B3VY7ZCj5Rb16n1LDQt77YqGpMajoQmev9kXoCQaAl6hmFlz3PgkWR6fi4lSSM7O%2F9Vv7TPTWWwpDDjD5Jy3xFseUnt8WqZ7svlSryq1LeIw5Gza%2BHgoNPFEi3JFzQ0In%2BoazOQHfGbGnfOW8ephonC8iFmA0K4VvTEhfFXJo5%2Bba60pcvv%2BwmcxoFikdL1nt1dkfwljyJwvpclhpLmZ92YxFbsgSiP5ZtYC5Erq%2B%2BjrZgNqMYUjbwnTsEpVpZ3B1vfgwrOHIHh2xykimPzKh%2F%2BlgH4Q4OFZF8%2FJBO4GVumgNiKMWtACKZqogqYjeduqT%2BJD0Vy5vzKnPFuG3u5eUMS4CJ5siivLOCu2RWYG%2BHAXyf5USGJg4pDLmFIE%2ByrfQbMK%2FfGh6yQ7GseggV5wcAw3J14R43yPRD%2BGWq8wVvJCDlHoL97IjMbj1Ao1qaY5A3IyiDTi1uAXQfwOCDC%2Fu5XMBjqkAVVorTSrDmUiPehC1Rc3TkQpZ6my45VRGPSZGE2bKha5tOiPpEXJNDIGFtvsRRhyrz9pMrxi5ph7NN7WJSNw3%2B7FxKbaweC3CZMQMjxMGXp50ZH%2FWC4i6LxxFeEhyH51nEx2VZqgy7kVduKkhrrFrzZvc3YTaONLZw4gOL9AOFawu8iW3sbYhBqLqnSBYb7Vltw3gc%2BUm1U1CH6SyGMYA5CY97ik&X-Amz-Signature=b464ab311feba3cbb5b25aed3262d0f2dafa3adc2116f7bfd63229fc4730d84d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

