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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KZDNGFF%2F20260420%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260420T042141Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJGMEQCIBEf6q0O1%2FOUZZ57lziMeVCxGHoh1moDUlQJweqZoLuAAiAQmoxi9B4m8J1PiwE4FxfyuMzcb%2Fiw%2FdYPV2IogX4QWir%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMiVk1%2F0aNN8M%2FmlVNKtwDWQb9goNNWJgBbp4r2jTE6URMue3Eo%2FH0wTYCP5QEOBR%2FNYh3eYgADMPRkMS%2FzNFqSQ3Fv5CYiaa%2BW%2BLxGlHiUOJJXKMrmlDdvZgZ%2FPa2KhfwxA242y8oNOMw4MFt%2FR8Zp7uvMD%2FEkZGzEChOPMu9ofE2R37id9rjA0gCVw3jt6MOXqhEuP0X2iXKenn7LYcFaO6hrrX17w6JDPMZykoUEw3sxbgY0gpYBUnwa%2FvBIMLX4yNnfeTpbN3Lt2A3qtWLEaeu8hRNpI07rPXrrPqmVVfYpsAak1QFCjlW7epNDp%2BI7deyV4BhxdlxTnrwZIKN0i0HJV7ALdKf3piO38lpYKygkq8k%2FcBCyot2wmEcILtHYJceHM7xTLTsuSDMmRqKlPaFVSwUdBsJacbq0%2FhXJL15gxB9%2Fd4Yv6JAnQXmSyZW%2BLLKcEv2QrfwyG1ykfNoBBl1wW7IMHSN2DHhRb5JymTDTCASq9sq%2BFLj%2Bwqag%2BE5nOZJMFCkXsBX7lQJNZ%2FYfjmXlhnq0Tw9zjyGPkynhxDypDaDNKEe8%2F%2F3f%2Bj3F9mBBmleijD%2BYrOOsz3Y9It19IwKgBiTBahGho3nENSHbOqdiOBrWteGIs%2BwV27nDCNw8%2FE%2BCCouPCSNzYcwqJiWzwY6pgHk2%2BgO0XNcdpOArckUi4DMbVnPJwLID1JExUHGnHqxiiFNxtDI3qPtQomLfC9NWRlMSYeoZB8lGynay8uLyYw6F%2FV8CWagoDxmhy8%2BSysRD2KnNFgZtfalSFLrCGCPnsrNIy%2BhBMhBNptgmXFwshdDIfLMT0LTorh1YLoeQmVYXY5VqAK%2B5%2B1I%2BwtYXkrV0MDOOPKMj0FIixzWQSDjOxsvmtPbGRuu&X-Amz-Signature=5df6c4a45d73cb9d7f349e5e86ca411c7ae7c93593216271b8b9ef2ece1909e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

