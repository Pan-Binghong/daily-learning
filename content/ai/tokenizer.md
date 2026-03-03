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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJNXNUVN%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCOja13g5YKCjspnCJHIiyRRBi388oI6JnP%2F8n%2FpV20CwIhAOgdbxOIO8yc2D5Gs3Wm%2F2wRA2DUexWxtawFk1KxsUUkKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwibIS0Fcr1smhKMqQq3ANDjpbpQJtxZyO8l8QYv9yYFjQnhRHUTFb7U1hFC3PcpO9P41Y4yvnYHmbsVk6IBGXLZxnl9ZDoHTIcNiTRKKVS09%2B3JUmrg%2BBozDfwzuwzvzaIoAeg2vmWuPKr032fYurtxAVLqipHSzCfoHtRoMYERLzUG7aIASrfK2Bm5X9U8DkOAB751O7818aBiEs0uVSfUKYDCW66L8DZQrfsS%2F4T%2BTSeTTkuPTjVzN%2Ffb7ONt0xxuEn9l9xz5NDCY1qeDFWX1nUv%2B1Hd6JiBbVKofhVg7H7X7pk%2FIyqSuece8Z8dcHSrL2hirwKafl56YS5El5CUBkxrKY2K9MtBGX%2BYmDY8eVFki0USQXi%2BZMU%2FMW0D9GbPxAtJ73NnF%2Bsoxjghn7Kne6HH7Mdt1KlMqFsHz%2Fw2OEyFVCLxSlSSpkjud%2FJs3QliuPdVlW%2B90iPReQf2OVyV2OF%2BAF0BevOn%2Bvx0iVjvwL4nhsGKMt8gkHTcu55grTjkXH1X%2Bo11AQ5DBpBfXNyRjMzQVaXVRxIHp7SxuDAR%2Fc7Bi7CMbPe8IzPcfc%2BUsQ%2BpZ9Gh%2B7kXDPKKfV8ECJ%2Bs8v1fDFVMx6iP5UVmZixJJeE14e0YHVQQTVzmrSHduj5YIJ%2FYaY6AuuxK6DCRtpjNBjqkAYPdJwNxEathaFoRWbU4F6QKAm9ZpoZOieNP0sFB%2Bp0HEVTusMqMnCiloDneyegncje6AvVxi5jmWaj6gWHYqx8DPYZFBD3KPzUveTOVGzZpeCVvnRAQBQ2i7s6yZYsRN2ETm8pSYeX6OA%2FBjYYeNEKtcnvkRUGtbHdyKi2VAAauy31Qr6UfCBKILwqsQJHDGWgqBNEhLS%2Flm2KbJxiKcZzmfABv&X-Amz-Signature=c502e208867159f43f48207291202bda67dec8f50c66da41cb01f8d2bbab2199&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

