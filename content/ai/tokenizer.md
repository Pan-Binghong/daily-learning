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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZW5UND44%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030638Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJGMEQCIBNcSYNSz4IFtRDNWfoYrKFJGIsc7EUM%2BPghqk%2BEUDQkAiB5stNW1e0pTRE4H8qda0CJkEzhiPYeDpJ%2F%2BePeILq2RyqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXT9cUHC98mYDh0T6KtwDBQc4Oi1SE7KtY7tldXzwZaueUAy%2BMK3SwCteLfm%2B8z%2FWH5J4pFJfdJSkMt%2FMOuF0tiCB4GMYDRNT23ZZTAoTecBjpmdxDPmF%2FLfB6JuJGxxD1FcOOaiZ8mliDAyMbk4bj6fwwNlScuvEssJHIyprZM9LA1WvDb%2BS7T72FA07rhK8DOInHenu%2FfteoqILllt8%2FBxMWVjx0cnDXq3yeKwNbR0%2BFvQ9xtYUG6GhpPOAIxSjr9D9iV%2F4iyNer%2BEpj0VrUhfxtNe60OSFcR1EB31BsEtZ3aoELLetLEyP111ynNhNd2NpFnZq4kX64Cp8L7IkLucAoFTIVbM004FjXDMfiZ8b43nWfBAtdmOh9r%2Fpv15AQ%2BG%2BLr8pf4p3%2BfMbmkuKfT2SxUJIgRoKshAPpkWEqqXgIhgQlZCwdW4AKaTNkfI7I2oYOh4S1nkM%2B7DoDoSuhUGfwusp1tQP0vhK2YVSkSfDqOfAmMc7IYYpXbLVcQH%2Ffgy7SklakvivExcRtcTXeItOyBU1zBALD2UP%2BQNGWZpjsg9ydB27rljAvoSOB2DyDyW9aLSBOvV20hvCoQWCSEKVz3yqm6pfNnm7LKMIQhOH4NYmj9boxVTS6d8VVrcU2GozOqr10hKoKvYwmNjFywY6pgHb3AU6lHuzOpHwBjh8E53AJiQgtvNmLOQK9pfJ3qDl3z%2FUVkEomLzuHIglo1HYvW0f3Psy8XX3Dianhl3MONbOknHKyeAepbIwp2813utO1kMTAIlM1zi6fDoKA84%2BCM63xr%2BYfFE2%2Fk1HNz04xUHfwN9odAtT6N6z9IsyWN%2BHuRgXN5KrWYwWN5%2BCYNIrVfB5rFSR3orzHdmDpiujuJkBt2oeb95g&X-Amz-Signature=c7a33efda4a03104d8e5cfc0bef234e56847df8457532e700d06e2094c44b6da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

