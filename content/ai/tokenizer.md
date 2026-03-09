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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QKNKZS7%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIQDej6X8Ty8sydy7ZEk1JN5qxOmtzjdi1OaK2TP0%2F65tHwIgA5BDjzQYGXYl84QznKxnKb3Szc0cGulL%2FEOZoVSNKI8q%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDIy8plphp1EDvozWYSrcA405OF7OcrEEZJp%2FjgcnuuITZXn45eQrwFQzrN%2BnuTkic5zTjnTV4orzCHwvEijmuFlhHjRPGZXZDm9NptjiDkJvyo3feSIwk1SF%2BBeCc82XBrclg7izJ3YCxJLTo8uvgyQGSTaJWT%2Bwlu2MPBYRMONCi%2BraZJUJ7TkWnC3p66m6z17EIQWDiN1MJmyoh%2FbhtNH187ssiwo9j%2FQFdTqFpj%2FyKj%2Bh3eUEnGIH0y%2BtkvKMRKoCVLk3e5VX7Sq3GORlNW8IvaLRGtbbqr%2FVnzX%2BGIGhqrhU6KDB59LplWPtxr4VPpaUWUzYJe%2FmPn%2BvUP3Tst1TltV5Np1UV%2BSQv4rWSWE9QkwUXRp69kL7LL%2F9m0NCKrIJoLxm%2BehaLuOqx2xnsRBwk9ivHX2q61pyder9J5J0m0jlMiQcs2Ua41pG686QwA0N1MfvNYZGZw31Pm7onTC54b8ujTPDETxSrNcHwJC8SFggMBi8ZIkIfoN9Q%2F8Ko9ma3rdm2qCFj0RtzLBKpycy%2F5k9QLEiJZyZbKEqp5toWVlioHRNvruGnRy5fpRODyf1rZ9fVtjIwwqscNtB7EKMfI3b8CN0cSRsK4Jd8aJ8HWA7Bcswtm%2ByU2QMOTt6KkAewoPBBI81%2FaBgMP39uM0GOqUBcYOUJfq%2FxMqeZ37HstGwHLC94xh7fm4%2FiI1q2vAK6aSkYYxSSiSwYelbKbO9%2FV8WleQl93ANImA2BdBAJDLzpcQan0bWLbucDIFO6tDBzp7TP6jvs61owzFvbYkhWTOAmLScWFPwFw%2FEI5ugcpapeSACJJYfOZfBAminBCPFkssuIBGMu8AgtNZb7zIGoWDLzFvR5idqh6wNlf5aZj1ULkJgKXeB&X-Amz-Signature=b97f468371080bf558a5fdba074caf455662807dcb408999c3b1b9ecbacfe138&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

