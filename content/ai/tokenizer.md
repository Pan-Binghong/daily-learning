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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EC65HQX%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T024335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCfcgyxuaM2kFFqWUieulHXx02eA4rayA%2FNpWaaBi795AIhAJyojjgiW%2BFU8OqpSGnq0CNTxJUI3A%2FIOjYorHN1xunuKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzQBLBbmsmwibdHUYoq3AN%2Bewc4KgFKeBpdKuF%2FUAYfcHHKrJb6oWt8XZ7N10JxSg%2B95UzjwSiRz6lmy66EHcwbdO%2Fn16bCtciyb3DQLWG%2FoIcOOL3rY3pPJcwvm6TtyyeUqGW2%2B5KS74yGtxZ%2FuanWI5rGCG9d4tmLoESdKavcekgDaWP8rqUKuYJkHS%2BomHNzxbWudPzws4lT1ZLvQA%2BuyhsRg2o3ScXta1aarwbV7SSNjKK7NcTaceVOIF0aPCTm0sR5L7zSGZV8DcZXeN9bxMNZ3BPRlQI1DSABYyN3t9jMgjBXDymRVES9tKV0A1tuDEz0UxDYAzEec6jUkuh1bG5l%2BsHqyTT6AIyaqdQrnDH4VyEv%2BWcM7JQzGBx1V%2B1ohFLJxprjXIpSDdFyWa%2F%2Bb8mAjntvV6ZOiFbOcGmMIyl7mjnRsdbDF8WcvYoxBLgscYywMB2WIWdEOX1mbJdXkn3cqBQqxTqH5nkRG%2Bow55c6i6ojb77ZA0GshYkFevul%2BXb20pAqot5NGd%2FeRa1jX%2FWmMW8T0O73Dafo4M%2FbBmPAeiSRFQZ%2FVs%2BQPsxc%2FHv4mcRqwolpst%2BMsjk5K1BkzeErYgrsIkDxErzGNmLu6jhEBC9i5BHdaoh5MQ5sBB1kZPlWwK%2FPivNnTjDrzJ7JBjqkAd0T8xpD1yinaxJOnadW2LyS4QkZWhOxaEvprqn3XPPma%2BT6SAiLRZA%2F%2FoTy3cPgVfoPZDECMHA%2Fi%2BHq6dDhkNDcZh44fSz4sREYJFeda%2FuxWEs2U%2Bz%2FjC2zEgaU5NebCO4BQwcwaUqNdVUK1lXUof4Ts%2FvskCxCKqjabkgWykyysiNg7q1dGOIkxeP9%2FoJG1x79kzYFhuBr36VUhtiUZIbz4Uns&X-Amz-Signature=f19817bb44737bec7706956c9637e95a81b2f3da29a96de672e4629bd1a0ed79&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

