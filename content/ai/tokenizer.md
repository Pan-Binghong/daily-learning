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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHNGKMUP%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T031249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJIMEYCIQDHtPJUp0ueWpI1YGIHvQBWcZ0oK3vQ73mcf%2BWoGuXD6AIhAPPwLRlhRaYQpFJDBNLNKFveZdxw6GA9b9bKKsozVJZOKv8DCBwQABoMNjM3NDIzMTgzODA1IgyTN%2BIIUv39ivEjuHoq3AOFMqY5y9CQo9niegowEIrjRiV7pu1e9HCFG6hptCG1vw28pLY3v3rMAU7hLl5JMAkLjFVneRfaPU%2FNnTdU53Z3xHgqXEF0Kh2vMiS3%2FG1iqp7y6wmTq1JQ8tLotg5WMYUXjUHczXMUuOR4jSMtoIw%2FcM9QhfoyTfYwsdC2K6j0fi1yIYs2cr8Lo8IfM3cCJ56iKesxMIPdH%2FmRh5svFJqg%2BDd%2Fuh%2BybggPQQoU5P%2FujC82QTNc%2BlCwpZhJ77rY1msDTpSbwZ4VNPjDKvOn3QzjMQd9GoOD8rMPqJxwnIXLq7soODlPlzQWzis%2B%2FamZHE9%2BsMdJcR0DP63vTqw6w9usUF5C38kVlp65vr99JKw8UkuArgW9u9zKOtlLKvh%2FsW54fgGKyOC3FxlvcRujszWv9AB%2BeRU8A0AYqYYKHOEHJGINCop3IMfjBEmhuGx3p9X7RVge02aApVFaIeKGjE6EHWXhei%2BdPfWKlmeMhx%2FtosSKD2xxRGe4SJ0J2kcWlDFjZ%2B98gDwgaDzwc2G7nuotNhF%2FZyum%2FExWQO8uOl4IXPqwafrGoHqrVbqpZlt887nnqqDHVQhoLiQFivDUiAgbmZcvgSwzv07zlJ3THbc6jmHT0V9cEIFYstxg0zCChtbLBjqkAc8eKE8zMagnAHKZTdxmSbL1I5xOZnzUAHV6%2FzcF58XVea4BkWjCpIxjhh%2FT0Xiy4uQj0xqW5Mh%2FtnVeTwZUmDzCuGi383pHvW2iEkmZQZKMXyA9jrPS8Ukll2z7Z7KuJ3IGCs4XbNupcu0Al9WUPgxdUJdz1Lf%2BHjhPiZUMM%2FZbV2pLIlZV2eMJwPa61ZbOSk7VURHEEUPlVXy%2FfRQ9w3zCx5nP&X-Amz-Signature=91b27f2cb60e174e058098782cb2185a490bb814ad2346d6a9ce185f7a6b4b99&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

