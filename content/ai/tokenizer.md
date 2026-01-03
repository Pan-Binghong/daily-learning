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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2CLAY4O%2F20260103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260103T025119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJGMEQCIDeogC07YEqbmBG7G0e7%2BOKmjPQRSHfbc0s%2F2wdqweeGAiBOofZNqthGbvC5gxihwS6FIL%2B7jRe1TuVAc%2By0rJE4ESr%2FAwgLEAAaDDYzNzQyMzE4MzgwNSIMdtUmScN6VGM8lFyyKtwDlsSLKKcf3lhFnWh4FXhltyFMTTGT14m%2BcEKCMxVbuZ%2FBoRR7LvOHPQdnVjXozlzWchCPL0avHptTCNrextQUOP4Ddz8XK3AzudcBV9QyGjIWKGQiZHcTatZ8r%2BOb%2BS7JBxgHZhWmvxpbnPuJdbK%2FtGCJTSc%2BNO675WFzSH5sVG0Kt76R17Ao8AicTk9eyB2mYQSrkwD4iBre5SKCjwQSlHbD6fN%2B8Zk7hUQ1qZZi9IvK%2F4lqNpJEcMQkggjskK%2FFZO4PgFtYntXyH1wb3UHzG%2BpUY4fuA3T9aAQAybgqYDUvqJ%2F575%2FtvRPjvk4WuxMnggkSG18ArdxiNKkC38IP9PiQjw6u8D%2Bj4gbLsB5sAhiA0uL3%2BeyJN0juRZzpcBh9HDBxHXthr4zdX9s9KwfESZ18cS9f4soI3TEsObIfz1tyMf9F4i%2FPae26%2FGI2H%2B5TfKKjakRkY6v%2F3kvqClYFLVWWVbUhtxIKSPGjcVHnDXi7qp7InIRk9aFfa%2Bb%2FNlkz3xFD9e4QKEsHce%2FNo0tsCEq2JD6Zg7xDs9BcmqAuoVbKSp8O8jpuWv7dYqS9hfxbIJKUQHEsFqKsQiwuc0YC3rkmpvj2OTigZWVziWh7l7Kvnn%2BeaRrjcTs7%2B4AwxuvhygY6pgEyzAchnBSqnPoOMW5fHB74ANqg29%2BwQ672vLs5%2FN17QSYmVDjxY0Rh54L8Dv7%2B8TUKHI%2FumN0azSobuAuPr0QIsghkvGfVift6iM8y8KQCT2Gr%2B3dLRBHtJGuCVf8Dn03WF7nBlpjesAfX5L7foyjJO3%2FUB3c3q8WpO%2BSaUELgzWonD4NMG31qG%2F4kncC275aUhFQO58vt8Vy44RX5qlpbL3MipZ7I&X-Amz-Signature=92ccacfb7d4c556b2bd3d0c0acca1b224e7b66dcbf88841a414d42b32a679d42&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

