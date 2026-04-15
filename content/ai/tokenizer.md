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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZZVZX66%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T040953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDv05wxwtAzV46ZyUxt7emYuba3Vyx8WgZoCGjc7yT3ygIhAJeylIyJ2nC5ubekrN0JC7m%2FP5CPcgsKrWokHGG3kLIsKogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwlQZ1Rl9MbkIwM2vUq3APgC75tjmQVg0lFMPN0VSv7Mmaab4s%2FyqKZ6n%2BW4%2FeKc%2FehwhXf0Var9NWVbtj41Euh4MAflp17YFgv6BsTX2ByMlAMvmq2478jSgkK30xw40gvRz6Q6ep%2FGMUC6V%2B5R4WqZifKNEWfyovbr%2B3euHFauntBwYuVFrTPj6BDoXCyUJRmD2mfNzFUMLtL24va5MAnwglevW%2BgBXgWlDvp9LexeqSGKxgQqmLNNvW32%2FL7hmRU3mqcnD%2Ft%2FYXrNb25PEbG84z09dZ62oAccFgR95ctVFhNJHbxMON3JCaTHeEO5j842PuphIw4%2FVE67XiDH%2F3aQkqUJUt2tZ58vfP8kOy57E1MINYA0f6Qg2H1ZaXvcFXmnztOITjG3FdK5H%2B7R4Hc6ka0YWAfVdbDogWUlTu60ZwppYfPzwjGePpn%2BtkzXNQV5z1QLOqSQoV29LGVn4xh%2BMIsLEffwaC0JNv6XMwYlDbS4rKe%2BXzM%2Fh4FHdsvHtukdpvwEKcpets1coDreeb6Aj407HEUkLkFkPS31PPw3LnsZcj1L71yBeEa9vPizUsNKu1LSL0sZ67mrxvSNtUeUQVyIKzHiQ2a%2BNio4d2GlPDJVJ%2FbQ1vDEUG0C3b6S5LIfPW3mRQy%2Bm6xNTD6kvzOBjqkAX5khJwvW8lH87CXS%2FeLfTyvpoNycO9M%2BhFmYnEOvFlTs7C%2FX%2FBlVbZL30v02Cwdac%2B6ZKc7dtJndvIm6PEejfFeXc%2F1zMPKflD4Gf6HK1JQJZEsV%2BKUilT5vDBNTp90ElY16Ogvl%2FuBLr5zaZ4viV8roK0igi7VHECXsCp5dWqrbuoTmqkwIvnpULqmbRy9OB7vj8OZwuYx8QQL4fW1He5AJoaU&X-Amz-Signature=d314bd61bb31ef4b06d03292396efb99da57ac8a6a09d2c0f303d9d00dc5afc5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

