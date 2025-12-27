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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654UUDYGV%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD9fsfQKKrJHx9O2GWAE7E37mS5q2qNyPBjgaXVrq%2Bf5AIhAPh4Bwd37rkcJPiSSeCZMHqsnxQK7EqyjHSwLIPynQLUKv8DCGIQABoMNjM3NDIzMTgzODA1IgyvgAMrFGsyrTJbjPQq3AOUPEd9TgkWonl2Nu%2FthupyB7bj4G4z087%2F6LSH6cGeJNpzeGlz%2F0nXq4oc5RSpUg1O63gc%2Bw8ZyrukskHbYLNWgT4Ff%2BlBbjsiLkKyQate0ckwXE%2B9h1VG9Mpn7AU96DdsXQLp3wLWjyo8xxZaIq6UV5OkN1kOhfx8AlY8PkAd210nkDr4q4iWa3mzPeCKP4rOguERtCuOtQP%2FNOz%2Br28VD8mEjOOnlG1splYwWlfDw7L2kAU3oJw67HFbNz%2BtGMg03dSewmSLYjEz3S3GG3I5cblZvVTmk9LcRz5bJ9rkuEs5m8tI7gbYZHqGkzh8hzY%2FlN3WXDrkoR49o%2FyZ%2Ba%2F82GDQEsi%2B2GD58o%2FnykDL%2Bkp8e%2F%2BMjNJbF%2Bz9C80RO397fNaOqblAsq0JX9%2F8JDbqDBWe8QJbsauj2CNSYKUQC39XY7ZTJFU5ssY6n5F%2FGDOofkpyIxthOJoArJ0GfrcYXxoJYLRNgpMKDlOJWeLLncWxEoSKSZ911EaAE3haH4Nm%2Bp0o2Dh7GxymwSylUn18BoN4eTf%2BQwHvKXAxxVRSWogFSh%2F%2Fupu%2BIv%2FG9uydIDuq12POkXx1RLG6QEF9XwVxF92aLntF79Pd8jz6ckuU5uSBR26DO6wsF5V0hTC65bzKBjqkASrm%2BlJFpkwD1HK5pNRpvsvyDP83QrUL%2Bg3tz1RpvmG65BfWUw67e6ExUabrqST%2BXsS6%2BOhbA8mogze2QVMpKtsjMmbkHWUxuv2g%2F0CItQt%2F2WcW55J%2BvVBdg82UuQuiQ5Gs47exHAtItgjzbAfSs%2FpGR%2FFQsLh6NqwfsO5jZMl1UUXo5sk8XkYpuLSEKwMgQzBrZnJ3Msvj%2F3XL82SCumQUffyj&X-Amz-Signature=abf888ac6f48e7f08fe8d92fa625f12276b60004613907ba1b924bebe1c713cd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

