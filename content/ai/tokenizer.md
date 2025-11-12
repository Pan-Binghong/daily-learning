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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWL45UM7%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIFvnlxJ5p1EQAi%2B458KvpRr0pc9E1%2FYzpZh2LjV9sjv5AiEAtBkPF0MGN1wlywGHFCS%2ByeeOjSp8aVaSskEsYWr5ucMq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDLI6j5CxuSV03a3SECrcA9tiv1kuWSbHflVCDFsJttwW%2BBfmv0K82Sp7zO7B3I%2B9pMgJthCNnpdKEhin4Ql9hSN8aD3jFq6iBiEdY4NCEPxVzCcEv1gV%2FbFOROocpk6jxOyZuzuFypik6%2FnDN3uKTdvx5ts%2B0M2wO8m6Gyn81ycLXygj3gFmGn%2FJuP9koRk5I4N8nRzgkILg3dh7vMF%2FQGGqghesW6K08WF2porLkubHnzeiA39mvnAy1PSF5liWZfBWo7YcNSO35tgy2vzaDZPnGjlz3E8ORqq%2BXqL6HD57uu6YHpMXFdZUSzhLvMP%2FX5XG%2FzwwFPGK5bLc53dFDJAQ8wzOdir7U%2BzdiCtC4ewOOpqPGjlOBR4jxZNKbFJGL0EBR3%2FRqWr988rflAZavvbcapcAauUgEmPnMhXc3SR9E1uEGl2AclcmLLE%2B2z8mPWwKkseiZS83EnwkOURXOmKWYtTdu39v5iCZDv5lshNmV%2FbU13ZTQIVuB6gQsbhPTGFiG0KLEUHaQZgntDx0HevkvFAgs5XR8%2Bqup6n6lgeoinru7tNiD8plyEOamuC6Za2wtspgE5lq1ne8%2BMSXoA11LJZne%2FLKs72BFXS6V4xpz%2F6f7CMNzctPi7UhBZqi6rZMIvzUNCcZwlMaMLjjz8gGOqUBZr2%2F5xRxB5aqV%2F%2Bt5h5vKIUiCXpLx5a4bkxpvJCfRFG5eiDTx7TQCqZMRXyqixHpEOMxthqa7jOJ4EmqdmWjMqUisPzE1y4r%2FQcQ6DkOADWEAqmprNrwzpQX5xQCCDNH5Q%2F3Bg8Jan1QlZ2%2Ffkc%2B%2FY3GSGZQ3qfob1XjSQVptNFmVH%2BM109TVtApsI3kXQej3jVTVtbqXKehpDoBR9lJ5gZeAgLG&X-Amz-Signature=3131bd57ae66424962a871b211df26d786b6033d7faf900dcb13577e5be3f080&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

