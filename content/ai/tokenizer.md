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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJHX7CLK%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030709Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBTC4nDFYVkJ4UKFcMOegc1oHU2zzk%2FJDg%2FuUIu4O6w2AiBkfzy4lmMz6l%2Ftw3X3JWipR1YNoLeZG6hf3w5mNM%2FnKSr%2FAwhMEAAaDDYzNzQyMzE4MzgwNSIMtVSPQD3XaCzujqX%2FKtwDxjgATLjtiEV72%2F1coWhqvSWmcg2HyUrfTlVr5PtLg4MfNgdq8erqbxBAv5o2TopU1qbfPBnuSKf1bCOv5axUB75IFTpSGTs2N7MFijVIdeg3kaO%2BPgXC6RPsDKal9ItPXCrcIDg6is5o858Hb7YFME%2FkuevMpfi21nAc7HaArTS1xuqUCzsw8xccQDXsYTWcToYHMtLOspRzwN0Z2e%2Bm5wy4msW5JI31d77VjPVsLQMSotaNhwqbB7mKmLsTX26%2FEkNUgvOZn2KGwMHeIyNfdz0tK7NkTQxNODt4K%2FNRAlxg3%2FcQfDoH5qs37cjtGqmHUXryuoilNziWWYysRXRjeBwJE59sxo%2B4xvKLfGyBEYnv%2F6fglxjtKhuABy6S493HFXN0bHxkXpr8ZKO9XQl4o%2FNgKhCKOCkJndvafRGlBay4572cTqG3hKO8DSXuBKzapw1z0sBJkSFK8iFZpd9SjgoeSDjL8PEEtY8K105E%2FKm2x5uCYCqMq3ygYuoFwl2UwIrRLg%2BqxpAA73XjvlW%2F9xMa3vU38iK079Qdb65S4SL%2BIvkaP5SXYSnw5wMEY%2BzX%2FlnyuYlHaLVjhIRKp1cAyrxU3OE%2FrIGML0q5ym3FbyKKacFGeh90EI124Jswt9LgywY6pgFKbp%2BeVj5p6kztVeuqDc00Mj4%2ByfHnRzySi0cz3naQMyCjVqthZnYJ7QcKT%2F9R4JeqvPbZbxr3LcLa0tlhgISTs%2BCQPDcaqK13qwh8lChiSYbZ5aqlNL5P86PHVnNHLMRmA46M6%2FKkjy%2Bw6QEWSVYYMoHvZtkzgzNq3DlnzLW6PYJZ82jCTI6JUZjGyIcTAaf6n7txqgF4p07FhDZTC0XE%2BZyV0ALY&X-Amz-Signature=6fe1393e3a63b3164e5eb42a02816fd3e378b0579f4c9c8274776d57b16f821e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

