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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKG2UOLY%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T032827Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJIMEYCIQCH1gkXbdNAqoUxbJBtJwTl8WFvIUfmF1zIxwhDvFyfRQIhAM8mRK7rDL25ESt9Si7WmGMngRmgbu3o4xcXLXa%2BBA%2BzKogECNz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwZrtmaInncmyTzJBEq3ANu0J5oBOvo0QoenqdRH07Sb4C2RtArhRp3FxkPBf2UbJLVFF8gEGC9NP9tjxV7dNkOyUyIIuypfxT5MNQpWfal8ggKzaJmPhaw7VtV6AbO7UnON5jgBY9ELdoONl%2Fvc6QCUX24f3HBgWj9VB%2BZgr%2Btbxu66Qal4xy6GhyTW3cIefmEcRBGrFRVNsFnzIlhKat2MevydUcXpuVuSVKvlB2xcw74kD4uQCJ0Qm2q12FGWxfXAPuxyqw6kd8Nxn2FKQYwrhdZXiefCLY5r%2BDItze7muLJQ1IDi4cLfp6vdJ6PHpha3%2BapD8Niqm%2BFObFC%2BeleXbpC7vtmZ4%2F6oMQMh0WEBJWsuwM8v6wIfxm1DyDPBQ3C5Fhm6AF%2FJE%2FXiUXsX9uxwN2l1IxXWjgHeAvVGzkujCenbwxxMrFAIRUB%2FPiQ5H%2BhI7rO9Nej%2B8e2u%2FyRcFlnKWwxE34OqJZV6KlrhQZ7IRhsib1cnTiDD%2BNl0Wkoe1ufIvVIVxbSBF1DcKdc71YSZACsgtssvCMEgK66MReuqn9YnvMvPr1pkqH4JpAZ79Gs7xuWxuKNKEaBvDREsdLxFK%2Fuj1dU8jhwABmI%2FelQaKjpaXN5njoUZqNnNus%2BUmUDC7g6qfcM4VyFVTD5iKnNBjqkAWkZMQHC6abEsene5B4gOHq2kavOKoNvBYmd8WmR3D48yBWe8nC6B2e3NlcW7UpU3fbxqGo4sn6gPzOI9yYuYzecXBEXl22lFChI8usbjT1G61Q%2BQ5p6zUM6VFdQ6V2p3iuHwSkfVcfIb%2BQ5M2pEQceU5POz5QfkzHl92avhXwu3qQg6sD3tIzLqeohhR83gZh1DeX58%2BLoSSDVAOgCeTbkofkSo&X-Amz-Signature=f811c497eb5532e31bdac9f9edeeee9f1000dfc0519a476b28e1b08427339001&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

