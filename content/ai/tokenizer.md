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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMAEBI7E%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033204Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBwDEngQ6dO1zzTEgDAx7QBBwrm4nRCsyxlIN8lSmJlrAiEAqof%2FkHCP5TTfinlcFRLDjile9hsSiWAjguJ9eIrSMvsq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDLVvq7JmAw93o1FC5CrcAyyOc57AGPWAHgZZxjkX%2FPgUliHn2Q9ZnOhrpFfv8C21%2BOnJNXf8ZQaeyaUNSYeEUIzA9ei2HdTAMPOqQ7o5fWbwC34bt5da12Q214ZY9bqYOVEKorOZelUK%2FM4HZZGL2nPCAd0CeL1P0lF1KS%2FlcsKKShQcnJ0Hw0HnUOB8lu5yNM7HF0qnGYfZvEnCYp6BJFVGqD8ES3FKeCZp729F6r27CZmtyQboih2n5w5df7adHYJSwOFcm%2BXbU8Y4qQRNDPr1FDoUXi5px0bTZLTd1%2FtvH6kgYzzGpjPCS0JE6Ba99lg%2Ffg4wlX%2FPu%2F7bDTMuCeP6TL6bPf8Rr554wRlCBOo5%2BKY1seT9%2BGnam06trr97EOpfb1f7k1b7hFNYQzFGOLjeAXMlZr88uKDcctGroy1XgX1HRKrXTid4bmRU1tc058%2BzzDE8OhyRRkcG5DbwGhci8Tc6DtNrHNHZakVOlJVZwJvk5ceC9%2BqX3BGhPjXgosjF8x%2F7ag%2BlJjgpsFMqcgOjF0zExOn4Rj4m8XS5IPoJfBsF01xgJXJcmWnMaT2MeyaU7ELSI0ZLOG9fa9ScZ86fpWjg4Qeg2pAw09DBauFWhuQR%2BjUZfNSj%2FCTB%2BzuSoUlWwWa9oVN2blBaMJz9k80GOqUBJ8CXflljQsgXd3jOGPxxV0eatc%2FXhhQWaqQckdhpqM76BL7YEnEJJ%2BBbcNEtnKwEdK9rXAmCBrjwxKEABjB82RY3eNU2xHwfsqK931Lu1HL1TggLpyWvrWYMSja4FWIutvwtdTH8LfRQXiKGD2Et8p80tyX4F%2BSoRVscojTCgpaTc8WUvt9pd8pIBz0R9E7OffiJNKMHD2bPMHfUkAu5S%2FN4daY%2F&X-Amz-Signature=ebbb8cd2b837f2c504fb6090d1c930bf17465a007e61cef4dda6d8fe68c16c32&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

