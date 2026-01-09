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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHXD4HNH%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCX3EycvF9cpFk%2FjPKyBKgQUHmDO%2FNEYV0GW8FDztgbeAIhAP85prtKCC9pPvyM4v584usaHfN7B87u31Nn3Z1e6DP2KogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwiy0g58CQloNxvGj8q3ANWy1DqM2BBv%2BIy9s2m0SIVy62lvfLiMxmpYhvnc4i%2B1fgmLeiVKCXrNd3yJypqGQaOBazlVFPE1tEbzLhismuJwJqlHbrvCtWptyvhg95kEIQH3ZkZqCyvQKpQkEIRUMZ7qiyVLfeaiIpk63ajq06yPu38zDn2Zgctmg4lJ%2B358IYCcJVfgIm5H7QfYrZv75YLeKntJH7kE8jHbTK5nNpzaOWbjNvw%2BlBKdpVvHhpIkh4eOtdeOQJfsL1wwBPl6iFePgyl6Cw769bp1BMePiTFsDUaI7ae1c9NQQQIeu87FhbjT1s71QqYHwllByiw8e9eTdceExNJgoNu2fTPX6PfV6wkmsBYOqSNeBNj3MyNiF3DB%2BmOAEpXQAnyzwtFcB%2Bv%2BghxE7qTsVBL4I83ykBs2C9A5MQPeiWFRiJa06GqlXjOHs01p1TXlAXHEEhs5krFb133gSgZBNGH1vaYmdUvKCLpPV7cnQ22UlRGktt0rifjCnMTjJAIBLOMaQgxa1xvElv2cn11eQ%2BLkSjpZ7EXYJz7us5XRclq%2BeUqPsBt7UgLa3K3rK%2FdRUhZaKeoGjLdhBXeRPnm2Rp6YEoQnyXGvWbLm9xf6Tt5MI09tHsz6n7hvf1tiM%2BWo%2BQEZTC9xIHLBjqkAc5ZjmUTdMpgozLjxQv3FwfsVjFTed0B9sKcbrFnm5Q42IjPOtDecuYC9hlHvNi%2BpmganaXCYwx%2F4XZ%2BpwR31H8ciSUpZejTNFxcMCfEoS5QkCAeM5K8pmZeBf06unkAR8hn0v%2B70G44k16vkZmdQZYxxFpYaFlouj5z4D8ADkVQVE7KlXIfd0fnpikhtZsWaY%2FAwfDWhK%2F082i2vpxwW6yjD7JV&X-Amz-Signature=f199cc7466e0aced94b8897ccc3acc52e6fab68d941b048a0408407802b86dc8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

