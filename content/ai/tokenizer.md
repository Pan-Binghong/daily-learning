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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466724VHJTI%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFTve3qyCiMVvu54%2BbZ6JmCmkOjjEy%2FKtw3B4K1JNFnkAiBG8aSpPpSh9SiJj0gsK9aeDsCV2ECD6BDyK4cWTj69PSqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMt9UUHX%2FqBQJ0W3jmKtwDPpc3SOj69I%2F%2BleZLRxka13ZK%2FNsttdsb0pr3hHORs0qqJjrzVoVRihYxSo5mWJFJtKTXQhIpzmih8QZ2j8gttwSL1Lfsv4Y3g566QxXQZn9vVINJQ9PFOiewIYMbRfJsTgAuUFfO3lueyF73%2F%2BsQtSAceJ8r29EPzf%2Fz6%2BI4BXtyZd1jyOShvPrKUqjFFH4T8B70NUPeDlnCY5EVrVvDlM0MyM9gDNOt8rmBaWpSxmOZN8RfS9EyHEuwq3zlsT1wbkqwKw4e6Kk0sepUKVjeVADIl0vIHv1Wn1GO6Qdyna3iwfAwCYyKrtawD9YrGuzD91OAdcNs3i%2BdrFPN%2FkEa4ZMUcebg33F0HDd%2BZ%2FokMGL3VgpYILN%2FZfIjRDtzy%2FuNipZ7NZNfxDIdlhVdoLV9Vz09XWYzWB30LfmV8rIeQ7Gj1FPjbfupkvOTPvSfh2AWD4%2BYehD9QNmISFGm6AnLzh8AnP7pj6klK6%2BXlUDqprG80eUHoPZh8OmCpbukMmA7hwvQPzNfog8PWhI081wW1BVanvSM4oRI2Hj9OFB%2BzcfmlFh0RU83dZhr0mJxdSt7Lxz3PYX%2BWNmnvU5Qkp8xArwIOw%2Bh%2F2RmczlhSghW1h3G7dbtrdmBjB2H1GIw2bzkzAY6pgEXN5ITNkCtDH8ieSCTIbNO4KvLzRoBElpPEB%2FYExF9y49SZS1H%2FqCvoxhTHIEdckgafVC3dcae7lFxRYZrBJnS4831fQkY9FMbMJ3tb%2BcceHURaiIfAPAx0kTvRImiVY0LObFVRvOleukwpsweZq2pVrnBHykfse0j6p3kT1TRGSTDG6ligp0IuiWv4euaVKX983UfdcAlnwjOwybtVVk%2FXAcik85t&X-Amz-Signature=3467e875f3d5061d3a9c90639d39a4f8978e35f7ae05910d49e91238c84a0a7b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

