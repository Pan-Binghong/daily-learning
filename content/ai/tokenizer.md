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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNEWLJI7%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF2r6790bzZhg56EqIyuhbqkGm%2FuZv%2B1qxZ9md8GgEhNAiEAkQ41YFK8nnxiKfxDEtBHoxpFYfy42l7%2Fl8Ut2G4RoIoq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDNnbi9zlY7YFMSrK7yrcA0%2Bxu3i0udzRHQ2BUQx0tSVw%2BhN%2Bq8zKLutmGralvHok3i%2BHcK5Vv8%2BwGWRJRRpo7gYP3Te58BUvafeul0QXBKlIKapIk2KF0OnvR65IOoKQoZISTW6JTH4nLydSIskA6p5Ycl3yDoMkxFHNqV95L38O3kxAeBssAnGDZfZtvRT%2BIrI8sYwWL222w%2FRP%2FKTDeYdWSAqNQ3e7dRdeLsKFPSKdgtICiU8adQqdxEoip5n5xfrmnYDSCGBfWK%2BFNpb42vD09wrSlUefuig9cILO6MuUe5rVrwbUfehO7a4eyWiX3MjUOTulduMG7Gy6oIxuzvJK%2FMiRA6jOjBCv%2B1qkqLwD79u1DVskj0gBJevYfTDUXqYSE9R%2BZZpsRKjU9A9OK%2BJugt78Kbf2UoJRUjxPFBlCNI5r%2FAHzxfMNDZ7OIWvp3P0iHjoz%2FDWccl0lZYhP5xjnfnRzoU7eBLVSEXPwxt0PPDazS%2F7OuXjyPW%2BbrOghUYP535jM3FinxeuKp9%2Fi5w7s938HbT2MFTbVpcy%2Fl4RI5vZW4zafX6LP7AARHwy54wLkA8QEmhGqAeuD0uO03ty1DLSyE0UJD7vech%2Bt8ifhi2acRSeX4KopNZYZT7oYyW3e5gaAR8PLYoNFMOymq88GOqUBJSkKDi1ON5tV43LJFGyb9USCWxV9KFM6pk%2FGt2%2FUu5Uj8n4BXBpVTFpc4orwP4unKoDrfLc8JBeqjO0YbUEUWSm%2F83uZzaDPoi1dr0Z9v373w%2Fj4nUmNSgYJpqW8dvfSdJRdkFohnr1nW5fyVehpF47x%2FqfSOnY5hbwpS1MdrVHv0n4t%2FDHnJAoOK6O%2BOktBBVCtoK6oEuoswbR8f0T6KHsxXHlC&X-Amz-Signature=8b2524ea9120403464e36c8e9779630a663754ea4ff52c5b616b2b36c3ba9541&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

