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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YZWORZJ%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T040922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJGMEQCIAlrYW8VQNoeESPVHy8b%2BOVxgXYFcB6Jg3Z0XRlpSa7YAiAF%2BZThmWeAK7v%2FZInxqeet2F4Csk%2FRLcjlteSATh2coyr%2FAwgkEAAaDDYzNzQyMzE4MzgwNSIMouhQCoMMm0K3c2IEKtwDx6ylgntqEpv2EZPJFJ%2B%2B3fMk2vBzlVhyk6D3L32y9daCf1TTa70wZrWM91ri8KSzNxWUArmC9wqKeULhXgEcK4z3EJcID7dyU5mEnJNmHCT7rkrdWE1nNVQAn%2B31ZQMovqMcuVZpPOJKNpy2A8jV2S0T7bLz4ZM7qsQ3NkZbGsd1n6n%2Fdz6OH0xogPYNUOfEA3O74mJHFX1zHgEf1GefyXfcEbo00mVsfhkOQt9WjK3xBztDig80QPKeSpx30Ap7u1nirmGawn5Y3x2jVyGvm2vTAZ7Esm85BZhMrIX%2F0T60VgmQ5v7t23tn7jD9rJcjHr6OlojKW0Wp18Ftj4ttHYMgI4nli6VpZ5lQqzzTxTp62S6%2FYuOmDzG%2BDEePMhti8ielugpHv8NSkkSUt6pMG7VX8uYeRCVfwM9Hr4unef9ngylSkLyjO0coxtPcn2i18g%2BHWTGnevb1X0XJC8H88Wg8uJrXh9umF8rM1ZOqfhXm%2FfljrS0mQEVrfa%2BSxgGw2QJc5TVxp4a23kGggFYTES7AA89iMTiBVGam3fJyPtRFb4bHpf4acd40qfneFeh%2B01nAQB347xY1YfVAMu5sLhrw7SPmGFUnEG9tg9PbZxtIF1E4Ny3KFutTfG4wjcThzgY6pgHDsz2HIMcAyMRKm0WIcFTqF4I3iwlKpvabThGCRv2KYDkxkcDwfCRJS7xLt3U6S3nmJazFhCRqQg1dgC6DtTNSNIX5Ws0Pbggs0VgXpMv4BQgfW3jvIXvzzMbkaUx88SmD4pApxD9JTII%2BZyz5ZEqLV855z0tL5cLgL%2FKfKHAfd94ZR3hxLHDTN4LsFmBAAhVyuzDmzJFORgCHR0TYVfOhqlP1aumE&X-Amz-Signature=2d023750be546ae2bd5abd0db840528e218cbda1172006476f300f25d436ba2e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

