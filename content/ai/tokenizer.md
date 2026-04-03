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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MPSZU3V%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071445Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDPfV%2FSIUtX1TDRiJwDl%2F7jO8%2BazjXkIb3%2BoWA7ybmPKAiEA%2FuHANLm26gjvN33%2Fc%2BRB%2FWTOumVN6UjSZK8IL1dY4Ywq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDDdDpEOI8h7xOssoQCrcA%2FMJirhM6MPWfS7WxrUlTmE99zTNEQPmy%2BrUbfbt6yEDDD8kwo1pYn%2BU3eCUNZUAx6uHwhBWQ1zthb9mG9xt9oj14MTO6OBtqRtT9ec4U4GHqUaxJMJmd7bXJp76Zy9U3BtZhh4HYgEEN4xpI4uGRL1U5x6VpDUNqaGCZ88VdRhvQDAn9ehIPDaSuhrVe14IBAyzOc7Acxw40hZQggXBDStlRKzhIn17oGjijTaqzbZxsSY2GrmbbnKfXSkpOLtM%2BjqF%2B0l1gE1nJIU578BqazqnKGJi%2BOntEXMx%2BoZGu8nuOe7jtl1a0pFQjGzlQT1UnuMCfyFfWQf34lVv60D4I0D2wilan4LwN8lmnXFyjIDhebYjIZdx0yWYKlz08evVXTIFEOnXY4TekHvMpnAHWow9QfUfNd7qIUMvJ1VgRjAmsBhUvMLLRZb06SQfvDx%2B4WFoHV6XLqiUdJXgGdkDWo3JazR8z9%2Bp4rH9YQiUrp5ubRjsSgO6G6FoWrq9Z9q6F3ygTghM%2F4vthyJQssc4cAbtImToT3jLPO27mGg0vHmViL62XYai%2F48O06ppMkAz7NrT0ghOz3H2DQxJ3NKOytPLoYr8ADxARmO69tjCUXVkua42JxunxZ8AlDQVMNyrvc4GOqUBlhEV4gRZ3u%2FJM58LbK4j9vILu68Kh7Kk43vFo4NfbYDgRIoUFp3quljPEmTxqPUHNRYxbs7PCLINKgJYlEYTx0lWnpVA1yI2cp7zWPV9wI6u9RIBAZd80T2NLRMkK6suaubqWM64OiISZTjAWjOEkGkKyaPNEO7Tif7vLuHR%2BGKSEMvIZzpulHJvj1m3GHBJfO019e1SNUTf%2BwFlKwOdDtbYsH7F&X-Amz-Signature=f3776abe27da4d6e98734315925e664cbb09cb109236e588588268f1e98ef671&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

