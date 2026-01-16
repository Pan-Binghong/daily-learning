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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664K3LXAD6%2F20260116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260116T030118Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIQCnOD6nJywHzBNUxn5PHeotrXM0TtsR7tvmQ9xw7%2FyVJwIgZx9bC8Kk8BHPHF2U3diEbfn28khFPH6aXMhPo%2B%2FNM9Qq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDCGz5ONJTI6dYYNGVCrcA0YK2OnEp3l4FucSWUT%2FUSMDC6gibtJC43hXQAM42WUtPUONSqeaaZl7anWfuoIbBG4ZUepoBXuHWGki%2BT7Osfistgrl9c8VVwxbu%2BweYqDvuJkw9T8etJg%2FoNbkzA786rhzaoXx6oh9J9qVtnUStxTUmgc%2BU6lMfSnWh85ZzwWMn4RVPr40%2BpCnAvg%2FuHoTNAmyf%2FaXhA9cf8Mh0o05C95YLAuyvCtdoj53A3mVqeNA07vgLv0jKmLy99PWmcJ2gw6pmYL1ZayjIrC00ocaK1CeMrt8Vf2LqpjSxIzrZxlalydLv2XFj%2FDnJad2VoIRhBy12S%2B2TB2pxdMQ7FJjlgbHTjhblYoE7ESB7H3gb8pLv%2FwsNCJqI8MJTdxKrKxuwLwO%2BvFeb50qiV%2Fw40LKggVZuU96hycIbCO7R9s9ZlanpNmFo2hZ%2FIqi%2F6jQFlWa3t2aHiWgTfrazIFCTTHIfarr2RSnuvr0RokJbSTJiD0UfLUUewfKDUXYR8M%2FkOX9wTWMG3WwsztzjwD1FztoSHqgUVYzj9TamFPzc1whbQwgNhwFXtEVTvul4K6vAdqAWFf5reGPQBdbbPCuMWWckw9IJLzImfOySjCaEq3%2FRhfOHv2icTIPJ7EFxkDvMKG%2FpssGOqUB1lSVIY3zr38o1liFy8KeaKmZLiDHdZLg8T8z1TqBFCVC08%2F9sp2aCzhj9MVswN95QeBwFMP1WLuy2cZqDAHbfYbq0maOPyWu0Nq7Ij0TLHneBEOPzWtoYiwia%2FAjcG3x3a%2FEYFrgWNwrvYXxFImypDYPKk3Wvb9BG%2F%2B3OHaAdaM8r8XlLlNV6v69k9BxtxU4s5gPTiL4FzDNHQ5tyrIYpfMnqgQT&X-Amz-Signature=76a16dba55f1d94ba76782baf9a9f0bcb3b2020eae7fe383f18cdd60c3b9d1b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

