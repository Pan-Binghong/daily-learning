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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTZW7WDD%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7BqUas%2F40QCZ%2FTPY59zYAZUOto3exSkKaq1kdjs%2BJwQIgX4obKLZ9qyeqIO8f5xOb3VIBjufosIRfdgni7w61qRAqiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGVDVCHQXKXzgQ3%2FMSrcA4nLO1X%2FQ1Kg0Drs3gC4A7YPxWiKlJG3JZeGE%2Bo5WslErz11JmLYem2TpSFqt9F1F6Y125vFitVi0tYrK%2FqaRJ5yExtHVoKgyl6UaAfsTNSIFR0GPmgZuC799Q%2BhUPbKO7ta0%2F90k24c78w3q5f3XiXfZLKbN0MHe9h067XbQWA8b1KA1g0vrHlR5IgLLKoDWCojOVndst7OH4TA7ne%2F4A9WAYdfXz%2F8qAW%2FOyVyaa212KxjgTlh76XcP%2Fz%2BQgXBYF2VVDK7J6a5KoIaWKupeGUzQMfDq3Mw96ca%2BQ9Vn%2BCRW4Vs%2FS42AyA9dCvRICNKRzFLgVDxdzVRZaVJC8bMkapkooqke5FUYTrgNGkIKBBGBZXQkw4QCee1eYP%2B8i%2B%2Bn1Oe6vgqrAGKNp5IR2fq%2F401L8ii229ONlhSpUY1N805dzxN6aVTrwOYM4wkmISU6M4L4hQEcuI5RuyzXdjyaN2tYKnaCTuMKVsjqATBxNf2X7J%2B8D02JdFI%2FO4D1AyRvnq%2BfYh16ZdMGKpzShOo%2Bq%2FuOZFba1VBMIhh1GX3Hr2bQ1tREF6BGXePk2vHc2yuN4TBGLKYRT8NHrj2%2BWByXNXfd8ZYux9hmj1gMaeF%2FBYFalesu5B3h2pa5gsKMKTz0coGOqUBePfXQ1BiNi96NeocL5IZNRyfh3XLH53UszqUjzRTjXScKuVBe2gDWTIL5ULnBnhqptjONfDfdiT09lrPv8M5xQm27CQGFJSk2oB3CeJBksYJ4Iw%2FInJQL2fD4o%2BQ10szbcNRPCv3aQtnKARFM9O7aKj%2B24o%2BSVkKh33dm72dPCd8%2FNKxbQEkl%2FDHh7UbYo3Xazwd0hVlhQ%2FJmdMefAbd8uZU08nZ&X-Amz-Signature=b4b4e11c666e8dc9e8c326dc0d51feee279347962ab260c064ec4803635fd607&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

