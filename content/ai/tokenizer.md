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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7JY2L45%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCWCG97R5bn8K2y97P4CK3y5XI1HFVCbWreqgklNE6wRQIgfLXNxTmZprWhrJrl0RC9d3DN2p%2FsQh4yVqxGmJrwqisqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKuPAEoiM%2FUI5bGRiCrcA%2BtGAdNidOVIdw%2FM39LHzBMCkpIqVLXucrgFDlWLyrEgQ1rIXWOmblMjOAVVxRyZrmUXGps9y7T5Fs0I4%2FKjg3pyUHEpeTZBL%2BwnFl1h4Iqm%2FolzM8A1fkA3cKccenRo%2Bky38Tx8BwsA4lMd0WUFmKHHuOy%2FrTrvgVGkbYEXO8M07iZ8rCSfwJKU7H5qZ%2FiSxMHaoZlkGy%2FCoF3pn5GA09f49e9p7yAvcZEFs2DTFzdy6%2BCUR8FmuBta3gYNhx0yV4Ffj5Ue5hOAPkUcduFbQLGSKqPAgadFUEzS5pqCEcloB2euKZwte5y2BoJwzeii6%2BxMatlQy4XJci57sgJ%2BkhLMdOVBUYDRhf3mbjOeay9zgePOGxi%2BQ1YCnBC0K7ADUCwjzEAg6mqf%2BTYAyj8a3VRZTl0Pt15exRyr%2Fl%2Fy1WwV6D%2FPtaNyam0UgTMDGJPYqZz17T1kLMGyAfiCzUGwVQA7FNM7BCiWcnHxxnpn02C0qvsauRxlBayL3gG3tqH7ld%2FOzDNrzUv3qiMIOwGgl0D%2FYw8F%2BegVIM1Doy9%2FPfOGU35%2FGxaXLF8Q3TU9jUm8gL%2F%2FXZr9QE0XQsCVoi7IL1vqBRPR8IewyfsTjIuBaSKzCeUKiX045o3%2ByYOWMJ35hssGOqUBlpjnCNSc4MQgRly88Ir1zi39iv61lvqBAnIYKI4ouBnplL4LfsrDcie%2FVXACqRDGbHCV2ucjXu4ZBMdtXZdZK90mRm11g8Ob4B4GrSvL5FAvJEZjElRbzgr8A1QVJrz2HSMGCSNl4edxCQVyNKee3BfIfXnerPCXPHaAigT18qZ07bKHEAr7V5hWoJL9nie5OfOMDFCVtIEgdaOtH0eaSdjNeR9d&X-Amz-Signature=ca2008b7035b6e63161d9235963e4bf66f3f425875d20550c48f17f1d817c910&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

