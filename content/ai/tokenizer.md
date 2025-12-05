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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672SR4DTV%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T024955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDnqlGf7sCkuZN8NamotW8oDfO3RJb8wZR75NpTG2YA9AIhAKAfAAlPqkHxGDK%2F%2FpyQLU77XLcTAuxtD%2B2n37db25HCKv8DCE8QABoMNjM3NDIzMTgzODA1IgxIQsBZuX7K33YItmkq3AObRYZyViighZ5uA58kXNnVyvZrEN%2FTq%2Fx7WyvRPw%2BGGq0gDPcbGod5x5ykogMyZOHg5FU7p54rpBfQUj9uzoxYEng0w9e4HzZ8BMekyW69BDo9wBJw0zPd27G7VUn7g%2Fv7Ee5XF7L%2BpZ6L5MjTL6JOGX8p6%2FNK98cGq87zX80a5RLVuc%2BoZy63TaibVvHpLIgnBY0mfwfl2ST0O8eznOjWTQ6sLQGP1p37ndEk48P0F45bUwtfGRe%2FtM1CLd%2B7%2F58bfZ7YW9e3WXXt3U2BH8PHUakKeLyz%2BV6mteaw0L0dkxNE0CpW%2BTvv8KrmEjjfNXPvIEUHAAqTROLlZQTvqL5r8h0x1vBn43ln5IyMKhEGbHHvxcHY9fFpbCmvtNR%2BXayyIjFNL5maCsuZHAd%2FWQwwhTzVqEzm7sJVwqMO3wTdmZS4cJ8gjMXUD%2BEsy3%2F8hZDWrUtDPOh9Zr1B075JS47XTO1GwxZ2fbAEyeNVSBJSB%2FKvGEh2GJQiKWVtY4rdhSjcsJ6HJv%2BPqRFn3qWQBMk2tyqLdsUK6mihk%2FZzh3SQAWVGeCPAK9XpHU5rn0lcUK6w1kvxLv5rwOAEz7xqyihv5NDia5MqH20fCWwFrsN7mIx8IQ6mvyQuJf37YDDujMjJBjqkAf%2B5ojuevLas9VwNwJh4VER2XpXWhvKvuYFUZ31C86Z2PouRVIwh%2FVXQAcSgTlau1hNTVjdHlduHKCW3WMkYUgLcyVYqBlNbFGUs83cgQParG59OEs%2BTAzJnMDjiLsQVBi0EwjZ%2FQ2wvwWciub9wOQWLtF5h5JMtOvdwz%2BNazb0FpmyLKJEZqFgELEhZo3Le11ZBoYgWMiIBXIJTlh%2FsDwkPvopQ&X-Amz-Signature=33bf99355f087e83eed54987b8672c10c8d7f673680b5bd937fd9b3a3b9a145a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

