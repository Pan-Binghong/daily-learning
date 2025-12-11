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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AY5KUP5%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQCU7wvYBRRwNV%2BY6UK6%2BKP%2Bu5yzkFVQi4SyXNCZEDorsQIhAKtxBc2lAkNOMEjd3sL6uhI1Vmi4Ki1q16aYXPZdYlNIKogECOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzCGZcm031mobgMfCQq3APE7ygkMsKAC%2F2Cgp9XNK2E%2B1EssOCygXE%2F3EwnLFa87AssVZPm%2BZmwKbAYkLvspJwMpEhh7s0auoXdUh6vVEgFVEd6PGSbjyaaZS0gx5Ul1%2BieQRLAUhRkPBKZwcad8Bf1AiMwGpEy8pOuQqKqksHjr%2F2dLYAWLket%2Btel886lWOvwn75Ivxt5MEjLpt%2BEUcH0LoYAcDGCil9L3phl7Aa6RNS5irGFBM%2B%2BuROTttql0Pd7GbmHZFu2DHmJ2BVY9nxAXiwLd4pWMDBQvM7CU4iKBLgGtbw3ze9qElNfXLAkvH8wk3a85n5%2BZKM63n%2BpD5QUUU0ktYk%2FkCikk%2F645hdaprDHpIHcmeKiVShg74XL5Qd68bY99YMDBuF6AI7cKgm%2BeoSv%2Fd4oin3H5fEsyG4SfEcFkB63jY8HfpPbIoeZp3DUWNgZEMYn2CC6XvZFkH4UnP3e0kWLUE2gZ8rF4g1cRNvVrdLxvFMpk1iKNXj5NKo%2FXVcTLyC37aVLmLkqdyZZ5q8a984I6L1nnsVdMdiTVIrPVm6HG%2BBAtuC%2F5M13twHkQ7KmhOuyXvVd9OcxU93GEkOyckXMkypUN%2Bdbs5%2F7Bk7AQZLAZtKDPqa%2B%2Fasi48QCGKE%2Bn3rCdR1VZjCstujJBjqkAX%2BL4zuCoea8MoMSjZN5vpQUilOaDtQg8F9%2Fm0eCmuLU8g%2BXZoy%2BYlx%2Bls7wRFTC0Gv%2FB0uQR7DMY%2Bnlonodx%2BBJQMhpRbg5mVtuSa67XhloxEYcDmvmqOf2PZA1euBh2Uyt0E8GdVm3nGZX0A8FmzwfqST7bjlhaDEtHKiziTBx%2BF3%2FPKEdJa%2Bwg5pQ1ILmOl9Ac6ON%2FvhusEhVXch2QFtUBYO2&X-Amz-Signature=7d2e2351972d41ad7166162104fc9d36d9e3f2441659d9d5cd9ea33bd2ccea4d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

