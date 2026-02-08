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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZEUWVAR%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGH7pJJDWPEcU6r%2Brsp6G6xNBAi5CLn1%2BomRZUV9fi1bAiEAuoP6MexAzvLbexFWepsTfSHwmtSrxqjWmsXBIQOXzxAq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDNlNxcog0%2FJ6jDaoZCrcA4Jsi5XwWX%2FQIi4Vg4W8VrIOeqn4xXWacLL5i%2Fywz2qjQN52EpsGgijN9CSWsKUTy0L%2F78RGAS1Y4StfLdFmnMijzgru1J3r5%2BwO%2FWoqzmCo5BgdwKAAxS3juG8B%2FCPUfgdihvqkql4DR%2FDZ%2FO%2FLUfKrWpT3aZeSOcSIEqZRIqvopaTIPeYWCFIzdmwjWcdhsE%2BdHu15CsJNqmCC4wMEf0yJ6IcVVLv74kNNHHeIx8QqMPCAvJ%2B23FaKeSi4N8wXXIaiZo8lH4F1aolm%2BfYLF5G86D1czWdaX3DuKcT1QcTIc9WSFlDNDykVdUBovT68E0OyeS7mePMnGk2bRTbkEzBLabAx%2FT0v2rZpLfIKUiT1DrKKhhMu0s4BQsMFy%2FRtLhS8qHSxFzxoG3bEF3ssf9SU4p2kfOFWER6EM%2BuievSDF4MRAXHrl8xm29N%2BUIsW%2FPDPyMsxDkRQQKhq5iCFROkl6%2Fgfnl8VTVY98PqjnaySrXTVAVcfMNc%2BbOz1mWg4QJh419heQpeZX1KZ3Ih3N4SwY3c8v2RSm9OpA11x9QimNRKTU6yrB%2BPeR4r9s4T5vpXxExExvIfqCOlMRJAzMBrWgkdaaO%2FgGzJsTfU0jk0jJWt3Hy3ZAOUQzFnaMJaNoMwGOqUBioTqGAC587v6ffnc65y9qh6Z96Xqwi8bWuFpEs7O7Ly2sgnjpDLVGhtHNCvL7fWCX69Y1aWliUho43KVyHC9IBmmTbCddY8CqgDGW5zX139Z3UTGakOe3inuf98%2FCp2HnilTbFE8%2BS8SNS%2FSniTIWds6h3vVSCpUQJGHp0sqcZuzZCL8MJP7LkYF8j3fFwfX8899woUFQe0%2FHYQMfpA6V5WBKfsW&X-Amz-Signature=3c3bb2228127ff8f14f0c8d4d639027761d91ab26c8cbdfa7acabacbfd4104a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

