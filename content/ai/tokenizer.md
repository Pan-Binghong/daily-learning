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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2F7WEWB%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T030913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCICuuV4jiNqoEyoYDjVSdESv9v7N%2FD%2BVo633urCJ1QEJkAiEAr79MvPH7WQCI%2FdJWUs8RK9uLEMKtFwIvEssMsUOu5PEqiAQI8P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHEjz8KoVXkrM3%2Fw3ircA84%2FPwVe9T0pR6XreW5ibYDxNg2m6oxN%2F2mF%2Bad1F21ZXqhiAVVR%2Bc%2FbXiZdip%2FmgWbIJ2lKDDgDZnt26ONbRkidDHimR%2BE5gfFgN9YomUvPqdzD72P%2BCsVv5RI8AUChycOC1JMpAd2nwhTnpD4AkjRclqPiuK%2Fpve4OBtQiosZpyistdiX3m8T9ZBxfR2917i3tm2SWrq3rU9IodxGvLZtXHcQl4tjuj9rhjelUHsLHtmbEVDlWwaVDwwGAc9OwtsYoMk8smSl4SyEjsvPVwCYQdj%2B6SgQzcajBcmjgcTODeNty7Obb4j1%2BZ9wJk7du9bzod%2BT9hcbIIE15pspg3AGgKotpmh8cTBrFDW4KSw3TeMEfpaE3d%2FjVz28S1quOcN%2BuPe2r0xQzYp7qkAX2HcvLwjDKSxBNEVX2IfbDWxKFi4%2Bj25noAoQdY9GyOHDwKNdzHpRO89vGTWixOcCb%2FJwqbGxn6qSEEKGbjt5oghdJhPBc3TXiN52jdpMpCRSYkyItmjcseGFaKx4ER0d%2B0eic7EHCF4sSALuLFbYh9ORbHZ%2F0NBdaRvi3v30zY1T6dOH%2FMHHh8mVvOdiDM3tS88Un4qyKWo2tND5SXOe4NZIo6Wu%2Bj380E5YW9TOTMOKKs8kGOqUBus5Cp%2FxyfgNhvOSKvX%2BRItqubNSHWICntyNuS2n4hJtcQ0%2FXWGvw23YJ0w3wCUJ79P3KNPJy5wEvJiO4oyrbBKXQ7jPWKQVb3cyKBvL2lRqK%2F2kBHZUlqWOg7b%2FtjL8Yu%2BhdnGie2T8Gw7Nrn353T3wdTXiPZxlpH8K4BuXzDpSHW%2BggslEA%2BLfQ%2BZZygSqhYKl4FSA%2BGt5SjjOj90C%2FMiE4aEJo&X-Amz-Signature=b700743d77b2c8d2f351e47a512d15b6d6a4a6aa9aec6d9f1e59c96355d5ca4e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

