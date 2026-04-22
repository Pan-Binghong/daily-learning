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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCMY7RQL%2F20260422%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260422T040935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIE6rnQMdYSgvcQUnJ%2Bq96wqv%2Bz9q1HFotAOSI5IHjTF5AiEA9W2NAK68L70SH%2FXXQYNgIhZqo39N5u1bSYKqbG7FlnYq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDKAFJ1Gtmv%2BOCOwXLircAwKuyaR5u6CU47RC1GEfQKuEevCyCrGctN%2FcHezi0aMNngK9KrmVe%2ByeAztc%2FgW8qd4eOTn11Kst7XdA7Xj2P7XBlCSYvpv1NbotxNakdgbGaD6RuvD2p3pyd%2BxwRVdwpDKRZw41%2BURM8iXU%2BVccNHZKyH91QPcbjUua8hxsiVSbKVa3BGl1c4eqM6nygL6QSKfmJ0xJq5Vb8I6ZDRLUFOsgvR0puk69BY%2BHmjUadbU4u8ABend57BYVMiXYzhrB0iBNmZpeiFz9hf6ZWmJ2Ww2yDQpXfpcwCFbeKGRlqLvTlMcFC8HK94KCDuJ5irE7C6ZG1dUP7LDI31lYvM%2FB3x6SxkEYQ%2BFtLfgcJcdpZV44RjEMSwaoauYwgp0qOIOwvVVhE4UCYVa1oB2oLdVnhfuKwFFSbStQg2QQUJ4U1Tgm6cwINoTIRAQ1Yclce3ka6SOaF9XrkYZD7AbUXFWsa%2FrccjYgilD0VCr%2F2XrQ%2Fg0LaA8v%2FO28IPyQ2BB8l2ijkw3g%2Btk0u1qQvTHjphpEVqreqgdJGdOn%2F%2F8i1Keh7Dm2OvLpn70rTc1ZFajQy4fS1R65DDA0pze6L9pg%2FmjsYeX1ouM2rjsBxn9zbiZir6sgeVnU%2BBZxLvujLMKvMLf6oM8GOqUBEi7XctIYRDDj%2BLJm3G0%2ByATYFlgg%2FiUgRIlRXLQ%2FcifXqjWEaQACt%2F%2BwqaiJjcSr9xWYvPGEUYTfiSoYsN1ARz1n5VUkZFliPAceh%2FJD1mcPZ1WMex3EuqYX84X3P3ZFeC7gYR78tbU5BltOLdGPGzTJN3S3j9xJU1SlKc01MFjH0fIQkTGLxUqlP4GSoJf%2FlPPURT4%2F4ihzW4sHfdQJODcf3V2z&X-Amz-Signature=89c00c1e4f0cebe6d9b32b996f053a85a1cfa4a9f8a3122c9b8582db226170e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

