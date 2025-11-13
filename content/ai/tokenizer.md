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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666R7HJZPZ%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T024652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIQDB5Jw02dnl9LGcoIRU%2BN8TMTvJdeWOvhmkULJqAFqK1gIgZq2faY5%2FXza5kkMrq78hs6ns0mW%2F%2Fq3REhz%2FMn4XsZQq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDGGWMq68V7pkzgZCgircA1x6yx6APubu%2BI%2BlSw7ffd0vh2SO0C0k5%2B6ru%2BFDcW%2F7bdPIad1jEeIalxYr2Y3jgj1qjxgUSXIMTt6r90XN5J85%2F3VLkkf90qwIMKadAFbG4J65PLzNYcIEQ37qjbuSTj4z%2BL%2BKQhd7KKgrruOzgr5Irr6mMdMAybBs15dPtA00Msl8Idv9gs3xYfFzCH3bwHP4cisdzv9vYvhWDxjZc5ukZD0%2B60XAJhynVAFcKH4uWENrRfD6Fx2bXYfnq09NOOH%2FC0iRPFlP7oGC50JU%2BahirxNmnNOMklRau9MtrT1a4bOZlJ1%2FP4TNXidO1ZoorjQnbFnXOv%2BJ7AMdGAGf3Tu9LOhYCPO8pWr95WzINGmPj7z7Uno3a56IqXYYhARrwFPZ6kbn8eIcksp3eKPvX%2FQweKKLz5fvx%2Bk6vW0J1Siez1jD%2Fv9sHSsGpEIOdRFi2KZEvf%2BpcX3GpG9d9Cctk8xFHM%2FNbOgsR0cXMyIYQhJc8orExtCioPHkg%2Fp%2FIxAiwgoH9emJKuu%2F7qntf0LjLa6EJVvwKW7x1I4%2FXZ23KhHFb%2FhIspOJeB5yFjGW9O4ORmWsuzM8e3x2mVPVsxXFAZgiUyBYHt%2BpBOM7NQJoMO6O4w8LqXXtRD71g8SMMODw1MgGOqUB9O3QjJk6DW5g7I9Pw5WxHmQFaXRQg2CZ9SvzSo5zrkIjz0RJ9DlT%2Bao%2FPclsccga1Z6d4XO6f6IAzNDbF%2FB%2Bcc5w%2BHrqPiTZonKSOL6ixm0SdueLzIaJMpcirJrluqnwfry3CmfJuXhPsoI8flunjLJRVAHmzyLDXPtaIj5kd4fwJlP9jfnfQQrrkAR%2FrsnpZix9MCpGvfZYX%2FIZjgNsNNw8Ng%2Bn&X-Amz-Signature=6a78313e8ba19f05125664c47bdf934e0c7f0951c9972ac77d2f2af6169f4fa7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

