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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T7BFAZ25%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T025953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCIEZjzQURGYikK%2FWx2YNDJhFFLICxh3BF5ybzUUK4coL9AiBqqbb%2BcsurDtJ3aqScQs3TtlFLotFOgWz%2F5L3ZsJAJJir%2FAwg%2FEAAaDDYzNzQyMzE4MzgwNSIMVucP%2FHk7DKdyEshUKtwD8Q%2FUVZgtziJh0qKVtY%2Bymr50FZ2rBgbx7UTv1JsDyKr9gYZXPqmeLk%2BEXDEDrOa0iOIxDF7sU0PYlSBSk8SGAqxTaMXdCDlfvJOZt9NzqJ3T6Ul%2FD0TDUbtbxs3zO103CYNa7SWa5%2Fayz9Vh19vW3i4cXQX4h%2FL1ef9yp%2BoICWYXAvo5frnRTCpeI2xj0fFitYarPkbDibhDwQptOhrI5tM2f2L4m%2FaMeJCY43ALvA4BITKdZ3f3WBLsj1%2Boi5V0iWhplIaukpBiEIYaKFD15RfNzQzbkfnJPSSBXkikk5dxVuLZtxZJ5w%2Fj46w8EEvnu3njrL0DigDHzheTZlP09NRYPwJFICDdN6A4QlL%2Bno2jBnAkD2D9G7%2BfPg5izp5GNdBvBgjHxFISRRHLJfmH821l7x9C2a7L7PNz%2F%2FhMVmRddyAVQV%2BOGZaLP5eVaUle6LVzGI1GsTdk7jHevWEBsZhxriJjCR8J5rT7GDfeh%2F0DdZ9TDXU5EYbUe2fooRMzZPD3vnCVN3AKoIaEmHxNnMnDFa9kzAftOtWBqQwSOrNfgRCgEVPnmh0gSeTGkSotqXMqtIebQ7CDkLQlMjE9WwaLujR0gltvwRrjEP7tElGDQL02gMI0TtXBHLIwvNr8yQY6pgG0fCc%2FM1NxJGgIVnUbkqFkr6fRIN552JFqXJCtCMRvqNKJJarNyktwFvvMD2LEjpkySwGrqdWIOFDpwGztAJvcTHI9f1JxNtPsX7UIbEi7%2BDhTkzu7x9z2tHuIzaiYh5UgCIIRVh6qqCAxy%2FGjpbNy%2FAGWmBYRsDwJ7qO0ceLr3cwvnQ6l1Scfhgeb1%2FTNaMp4aDvciXCcZ5kB3Y3wBw6gTu%2BET6vm&X-Amz-Signature=9301dddd15db4a6ef2a9c621e8e49b093262b14abf4f78328733d518c5ea6ba1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

