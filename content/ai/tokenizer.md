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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FRHVKFF%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035254Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIA%2BhAG5XJAnMMZCieyTh72qHa%2FRHaJ9yZufn8VdinaevAiEA21Rol2e3SJ7GQhbffx%2BqmnjBvmdzy6S83c%2FSLkwwnP4qiAQI9P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDtmFQTurJcih0U6%2ByrcA3f%2BBcelFC5RXA%2FRafmxz9uijXwDD5YVrfefx3NzSTm7bZjmA3yZ5oTt6%2Fl22PkWQe%2FHgoWLyVYTebcQYPliJmjHyfg2odhH1eJaHPDwL5t%2Fhj0wA%2FQO%2FWvjc%2FlCoAO0pjB3M2cbZg%2BcKHYigmLMW6edxtagz%2BugLlCn%2FhQSfshWB%2FFqAsn%2BWAQ%2F6pWKChJPqzW%2BX4fuO%2B9zSAA79qyPSYuxNiYuaTjZUPs4pdjEsM7SO7JroNiB4E0oJP3Xdn7neIy2t7sAXnYYuOO5ONTas%2BkZv4mTYb9yp89qDNEZ5T%2FN0U5iTreNruCNod0JH9ZoC6vwY7pkiBS%2FzvdsMfY6yDKsv40ntFcTJICuRovLT9cpU5YAZiWssSTCa8j%2B4Jo2kMNh2PeSews%2FSL6bKQwSP1ptRdGUDES2p%2FJkTAWeVTgmlrJVm7A%2BKkoJ%2FmvLYxNE%2FEcriN2mf%2Fw2cQsX87m2tQ1scZQk%2FXWSIBv1sLeiW5GuWwJg79ZEKmp3Lrj47rF73a6AdPt%2BtBcd%2BrKZQMwrakjRS7HPqQcHSBtDYl%2BQd8VJj39w0UZXpZJTYWh%2BXyIOCg5Bm%2FRFPtmq4myUkQvNgfmdO%2BKI4hQEhK91%2BJ5ofzkqZn7sHxalQPXgsORpMOOI184GOqUBKpt41VV%2FKZLS7onVAjHpaj1Zff37yDEB2qf9SepVPfl8r7euVXGvOQ%2FonG2kjlOuBzYSm98qnK9ryqTHK9Wy7TDKZwzeC8YKnhQ%2FiQ83alI1LsTI2GVaEu9vL6URGkfbb9wBqcr%2BA8XwKqQnGqnCNT8AWCD7gcsvQJP%2Fwc6HVNLig0dAcjkh4pt12CdXsoH3TnztVCqZlw0rxGrD3b1r1PAoE0Zg&X-Amz-Signature=5ca9f20c34e65f54b2527f3490fb1c852689347d1a7a5a67d28b6129677df0bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

