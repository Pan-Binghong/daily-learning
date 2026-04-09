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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBLMVYLJ%2F20260409%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260409T034904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCICxDKNjdnmtNg67tC2I41XGE6MDuyL7JissZs3L3COOtAiEAzeiDW05FAqRTcUyRd0O0n5SF0JLPCvtyAAFeT439eIUq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDJ%2BI5qBKdUUh%2FLh8kircA7Jaj9o0AbVw0UMSp1KzoGfMan7Nv1%2BQbDu3bt3njEk9hdXk8NqeJ9g9IfUuVunc5rlhWR0ti%2Fyvtx4GfLhLat0T9Ih3CC4xd0fUs85gO0Uayn9QLuYHdNh4s2mjVfLmiw2DOcJoWUiT1RJbovMkLoiog4p8r8QmvDs2yLdeJfS7WT61hZQVwZzvVaJiDAWUdeIuOwJus%2BWO5z1tPb3a97Qcee0GuQE%2Bxn92JGQZ2btKn5PhC24WPaknU%2F6QJvJwNUy9heg%2BucqHbVCOcqsxHHL3serbnBV5QD%2FEAqXLq1AXKNbHMyMr4kx%2FQElMcrkVzf%2FwIEyZiwH0N2E4pU%2FM%2B53Xj5dzlhSAPDlBkauLH5v2ugL5uDebUV7529iuWTfR59A1%2FG1xhABW5VA9dpitezQwfoNh2XDdiiFowzlO6I1JdftE3nQXHZ27v1czTeehg82iYsRXF0n2GtTUFmvTrPKNQ1pL1wAorKZGbEd972c0c3iU%2By3XdG4GFZKNifsAeencDOCqU6nvNLRBeDhrXCXTrATrxdO%2BofjuJ5dTQkdZ6WrMSDWOgiE3Bs9dcI84zlqsr%2FY8NXH2Vxd0ZVkpDEfDf65CtnYlr9FumXsx9k4%2FjdhBBuaKMR5%2BPmxJMMOz3M4GOqUBlLLUUaYqM2slfJFezWL5TrhEtBRvdxmG6EC6JSQkkaSRe8dBP1sxdnJl0riBKQV9yTiH0NIKfZp01OeSf0pwcuW6ex944yhjQcukGpWvAELXGaID0o9dI0qgnl8Q3FbTbUyEkshG5Pxw7JKaf%2BUB5cB9izFWVRu0ePlUzMkqPynFETFTdDknAFq3%2Bz86lbBmWsQD82ORZzlXGOD9dzD53hIE6QnV&X-Amz-Signature=4aa70005ea17cbb467d8b2c82ec53baf5d1d9fe022399b4026e74e3565095515&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

