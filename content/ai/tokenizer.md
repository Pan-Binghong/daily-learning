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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CCVMOKH%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024243Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJGMEQCIC%2FjR%2BY4YT0mkC6v0Jot3az7AmbiL9S4V1eCiN%2FZa9G0AiAaQihSEcoAsKClOqV09m%2Bkk3etN3tKQ7eI3TGHNCw5Pyr%2FAwgEEAAaDDYzNzQyMzE4MzgwNSIMKK3YfRhRXSAjYMIfKtwD7DEJ8EOjJDZqpcJo10wXLHuTXfrBqUkOEaGHvZbF6R64Vcs%2FA2thtzwpOaI1osDNxwcTGJQADyXnMOI9hqflZd88FYCv3eEfiST1xN8gfSWI5Kc%2FgtIEjqSIX2vY48blBWhZom6Zp4xCIPQ%2BS6VMgPzuxPClnetNQ6L7zstZ7ep3vkY4Nzb9H%2F%2BrrZC9ofc0mMHYa803TUQGywBsz75xdYvEaIZ7WreVLGL8aQJafBamhYkSZTQujzxZgZrH9rQ1xQlVYzUVDW6RX9KBWyO4uuJOGi2TQkfcmMDqxWKzGiFMkiOlw9HgiHeVP%2BvDdPc3qwLaaQ2lQmEeMY3HYsed1LYbnGkxAuDBYZo1i4WPZGg8SJPbDQavXNbHzuj5rJPI0An8xMlsvyG25Y7wNKvwuXZmZjZn%2BLoWTFtr1PaodWz5ZDn1Br0BLYyre45woZ8HI3e6vNQz0ABWMqaWGQ00eh3sPXZgVgSaWqFV3nKnvGc%2FLr3tlM98IHzhc6lX4K54YTitKHIJr%2FKC0VQ1v81i7YMo8l9QwbNId5vQrFdHzbsnW18OcRr31P4VwA9QYs%2BUDm%2FBTg1efnLNxOd5wtP2LvASkBf1WcZUph75xhOXO%2FwrRadqDTmY%2F8JAAAYwrp7%2FyAY6pgErv9kfRv3xW0XJH9DGGaMfKngJ1o68z2XrUsX1pI7o%2BfRVrLWA9mW0lLh%2B1AnwiimClu%2Bi26aCA4u6dfd312oWoQzG3ZfF%2BwUJ9%2BBIU2MTTj96VnC%2BK2bbHriR1ZN3CWn11VhKNlPPEvfRlOO7whYFoeVFiZhPWKbgssAx3UjjJaR9EhPMRETRiUZO3MbTCvRIiXVlh09D29D73YDeMDnLKv31DqS7&X-Amz-Signature=4f052726ec90d8e2dce2c9e9c3a29e0a63411226a431952c1faaa6845a305037&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

