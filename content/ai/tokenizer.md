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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQ322I32%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025202Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCrRWTTHEpvojzi0lwrR1Nfayu6TOoZXUmN1v3PjeYxwwIgJP4%2Fc9md2A2fWKkiA2Oz8akuHQCFHJ5abxvhBmm3BpEqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFimPaSXQMK2Aqa%2FwircA8lfdYjDd0VEaI9CcoYqSwJdICy603mTMTSTSozkNExSkjD6O%2BORqcU3JmPrQ3wbeN%2FH%2BtJCkYzP7ueF1DnKTKM%2B9Wx%2BWAuk8VeQqjVah2lklW65w65EI5fOlHPCCQYLDEeALO3BD8g3Y6VwFWO4v5iIIkmba%2FeJl3%2Fyyy%2Ff1yacOONfdwbPbilnbYoaIRX47YVza1f2yxVxG7TtxGSJU0VcWGEgOePhwZ%2B3E%2B8eVazDSyJeNQZlilClItGpj8VqmWxXSd9ChWEZqK2UH5nvQyilTW%2FfXb3bO6Saytw9pHrY2cAkC%2BaISt7yc%2FGtTQ%2BHqU1f4FPoRtSGoxF3DINj6%2FJKkXayUMfgORtg2tJjEEEDle%2Fmb8sDf3Sqdv2Mvr4urHpL9yu2h%2F1ezzTmPeBInMHWayzko0LSQZMsLLq0jnFaaZAarLHsH6n98sMu9NyEeXVOE8D932XQn1ldOyLBzASTn8rVl1dV2dSSAOWqK5OBkRM4JbI0pXN59DrZ7s6CrH%2BTNvfr22WNNcqOxaFkkn3G1U79EbNG2DZhWHyH2jtmsh4YZ32B1iAzXl7cV7JWn9oOXefpX50m1u62iSDt5LKcJRNnrl5MV1Xv01%2BSez8gY37xLf20aoXKVgKLMKHv2MkGOqUBAR9iFx4XrQQvY2BDBAUCryBGrK%2Fadm0WGnKEi%2B65A6an%2BQJOOOv6siF0E%2BXSftjne1j9DwNZWv5NIrC4CPy1byI4DBBwP6Dd4N8ODpkeinVRIZMjEl11ngSBi2hSHJIdZ4rq7qo1nD0PXieOon55vJ%2BxZAtxe9pQh8%2FMPsJa8n58PAHhbHrxJZVaB2ef3uKXr6H7mXxgI7oitxZ0xWAVHMQ%2Fo%2FVc&X-Amz-Signature=0f75b673630f31cba700c2499d24a82b7e97f656b5701ed49ce0d1c9ba5b1fab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

