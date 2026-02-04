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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOIB2WT3%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCICQtRxGPk9f1RedbVYz7v%2B9J5Kha0%2FfFsBA5DA%2FyYVNaAiEAuJTBHGWfk1dmr4w6Jptms4lUJ6S8kyUKvIxI6P2Ttioq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDCTV1s9bpnYddIhTECrcA9H7zVxVGIcNVmMu6rZi6KNGixGPqElcTu82moJu0qBoV8MHsxF8YQHW7UWc8Th1xXrBidrUgZcDnyH7hWBtaNdlZ5xRS1BfpTpdPvl1nt6JJ1zWdhdAIie26iY50oi7waX9VKPy2xi2jfVG8O0O68YL0Bv9qlTbB2jcf3v3nSflFrsfC%2Ft1JfDbrGoqeN2CW9cI9w0GS133ujJkf4DW1AsfrDxHfHJ9Sqi2v89japrx13fTvB4A3iqSZYk2gCu5hsd8O2UvvKHhvwT7KN9c53qzPWsUfkAU43JdYiNKL7eivhfZ084m%2BUCSDYfL6SOQzdtHtxjjLaib%2FLV3qEaiCcFQEQXI6MYPwTGN2zHh82CFcuoNOA8t02rioP4hJpwjCEUdLZUNwG6O0rfCCa0Dyyi7OibIsM9c6v8rjAMPjlgsUa3N1MEC4uzUMU2YSnT%2Fy9f%2B4qHpV4obOCE9fE1Mwn4Oue%2Bi%2BidrqaeEW3ImK1a0SwJdK5C6L5myR0zBWvg%2BFn9jUBMd%2Bx9lgi7LqQpJ%2BkFDg21MJM8GYBE3qb%2Flx3Y31obuCMuxZGJLWoPA8PNnuhnQGOUtNJyMqLm56cw2JR4SRvOMNtDxmtEjQjLNCiy%2F7KLzSxO60zrEMtUoMKfpiswGOqUBt8yykh07jyGeXOoRkGCuEoxqLRd7S4uzP%2Bejcez6ajMtFOD5ovA5rVVnP%2FS3SpXGlBLskf%2FYyzXvjXmznuYE5W9bTnciN56zyJ%2BoThM2G7mvurl8fV%2B54v6sxuw2PEE9KtglGaN56%2BkOg2M9OqObh4BPsf%2FX0bL4ym1G7tIwN%2B3%2B8BFcOWhUeB2vnnvfY7siYZ67vAwNCK2YUh4TwRSZzO%2BvXmDL&X-Amz-Signature=a58310fba9a83def136be8a04f985973d974db45144628b07ab847440e5c1c7c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

