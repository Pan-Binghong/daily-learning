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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DZNLM5R%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAFZS4j9fAVS0YAcH%2Fatb9%2FgeXto09HJiN3psiyCEsMJAiEA1L%2BWDq4qhudaZmBUMEiRaMQmhYRfZBhkH9m6eC6vpE4qiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAxIV45z8Jal9oJRrSrcA3ZppKvyQshPBh0ItM04Y%2BWV8TlqPOtG0tPTt4aXrPXLWUWObyvra%2FGEL8V5T2wewNLjLsluy3DWu5v4Pn3PEV8FzMFzU2pbm%2BwPFh4%2FldaNUAz0TEcatY2RUlzUIwGE7GiUE0a3r8xlZC7hbsBh4ggH9a%2B9pFftVx%2Bwvhq8DYnVTgxYNdeAe8Eal7CEPneiuTseH8UO92PwHd%2Bdy76btlJU5tWKmCjkyAE14eX5KNAgousbHxu5RWhCeKaL8GaPwdwVtTKXmtA8zWJTNNUqw9OMoTx5OsnXnguIVFTNZKbCbmArgU37Flk8T1jpkK1ir8HO3qJVvIK0cf9y%2FYwpi3rx9UTQbxEXbo9BHcamVS6h7sNihDZq%2F%2FymqZG55LgABAmtLvpZziHM8hbyv6lf4HUgOk5G34wH9i4pmZC%2FrGGAxYb4yqFJE4jtGkVWaCBdSGA%2BaXyZ4KsMC96Np0LtYqg3KjhqEp0o%2BTVRnfMolb%2FWkG2A35n1NzFI0rQY9NG6Gua8E%2Fu09t%2FbPl4Vj%2FeBOOqDmfTL6865OPw4K6jdjimenEbLjMAA9kTqrbuocnhd8tZy7U6E2koJoVVD%2F2TY1HLBLBsjmBG66FDR%2BdThxksrwfdYiMBULy%2BajSfMMMjyh84GOqUBG8yjWIR%2F2OZbHuoy3pmsaymlgMIinX14NI4d2dn%2BLY4QWtGig7d1sIYe43FdBTwst16CPrVSkiduJ508w7KNy0LyhNVV0QEETUl%2F7Uy69Umg%2BBqr1CqMykfwpEQC8s8HQ2JOLJ9WT34ppNZ%2BOnKgLRlGb9611OiLppQK5GPLKE%2BJKx8azbzq%2BoNWOrM14PYD%2F4K5vxIMWZhsH0iEQKc356dv%2Fr2J&X-Amz-Signature=0359cc1f92a3cf718640a1662b73e8b1437b707451ba04a47f40e77fb58f823d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

