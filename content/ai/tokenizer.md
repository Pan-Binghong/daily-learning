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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667PVSTGH7%2F20251204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251204T024942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJIMEYCIQCad8FbHFugFVp049SBpciM6WJ%2FADvvlcFOOQF4p60dCgIhAKla52QtTz25J7TR%2FHk357diwNPfR6M2y7QI3bhOL5FSKv8DCDsQABoMNjM3NDIzMTgzODA1IgyluQXYDUBVGKBLES0q3APr9VgyMwMi3cULOziTsVQzgohEJogUs%2BUHLuH%2BI2E9C4aL5CndybaZGus5m996EabRnky8jovj6zvesYQQLH4fkLIR9IKEU6Aoe%2B9zQqVGUKF33Ckp5hFUubMlSFxRS3POKIsW0VVv5Ny7CnWVymEY4J4Wh%2F9sBd1VS9Pn8fJznNBaqgwpni4ciipH2%2BZTE2lhn0%2FKKdhTSwpKy1k56q1j6kg5uMsCpummndfW9kdCFwDImF%2FpeWCM7Gmc7kGyq5TSTS01%2F60%2BFyM7t2I5HJy9S7dsPZDIf7jBrNdyRwC5RHiyL1iM6ZmSNIv2krJe4ct809vE51caUPflldIkcbaVA88ltz6Z3cVQNxNMiloZbGwxnpTZBxDTQE1gqNW0iflQzrairDrGqQBKgc7HZ%2FwA4soO24kSycsYKQx4YgYtd%2Fu6UCYXt5WCNoXy8Mi8C5Nc6nSVzyoNqRSopFaVrP2cy60%2FFLkFhvdBU7UahN7tiaXAP4r2rTOhzVmXftVQGrddktcDeqW61o5ISR4%2FHeyVFThgHbI%2BB%2BHu1lN2a5lBKOxGZ2NyEJI4ip0mrlCqEEZeFFNQoSJgus%2BfNBao2NN29yy9NCSjj9zH83vab3Wm31aESSQbenayy9sL1zC11MPJBjqkAXlP2u73qbaBxGivRG612yUA1G6esTjfm9%2BKZKHq6guk7vuGrvOZGgf9d46uUm2ATxoovBi7WWQ9UEVOGUbMnnH3CbHtKqclSo2BMzB9WU1ZexarxciWSGFHOqHOt4fFa5gTHVjjsApZZSR65cGoPQ2nDieObJwpmjjbXN7bNJra6GNXsKwXfSnnku4DovNE22NibLDnGnLAUqmHvlsnUEgLET8x&X-Amz-Signature=5a25f0392e6169d9c574d199f74a8fa3bf62d5691e76ddd9a8d6558975d74347&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

