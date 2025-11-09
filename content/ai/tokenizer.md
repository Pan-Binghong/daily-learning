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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2ZE32GU%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIHkV%2BMKRzqV1%2FSRhO9Nlor5qLmfaCtQidMvvDhEUsRTyAiEA8BmsTyfTRmDJT61ORtStrmU2lyNKRzwSZRe7exRwt38qiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBzYWwHT%2F%2BRDlJmaWCrcA5fTpXesIE9PlPSPU8V2KKhp%2FnNvPOzMllZ1r8ANwvKgqSpIRL7aXrw3nzZsgbHA9EBbeqhUVJiaInwp5zQTogCVspeU7aF41m7BUqn3EqMB0zuv3LZ97NkoSbBEbOvjc9i4LVNOpwtagF9Kl580laS02m8qWHPbkRK07U4K8XcNuvD3gNAQzD%2BJbizbUrjl9WsNC6PlmQp%2FA14moNpPEty%2FJqJRv3bHwYwWKejEkZsrOM5bBOmatSuDGBTNAjA5DW%2BFcygbaV1WXpZ3yzvmLfsNcJhY%2FHjOvV9%2BNZ6NHGnuvfagtxKKUKsMGJ4d2yPLfXLDNvSxarDs7HY1gGpBCZYiFScuUC4ogosyGpiND5y7YFHXRKKdykv%2FupGVNUPmIlrhOJ3SL9UOEdnG1uVV4kFK6tWOpu5jbcrGD5xjmVwEDTPXew5s8Nog2sjR9m%2Bi1%2BMKp8RSZ49ggt0JqAptc8NrkQ8XxzWIz6KNQEXMO%2F1Tu6j30pFhYZzgBiFydvUBctwpNNHZmMW2HLJqzfGxYiL1fF9YNhrFsw1tDhB1u8XazMB%2FIos2ei0nKVbQ84U86mWLdA0LsJR37eQpCDiKb9M1K6VqaMqAY1umG1aSNvrFlA7S9XjdE4TiQbVLMJG4v8gGOqUB%2FdillUG8o1oMsK6%2BnjdAJI2%2FmWpTWRUYXe200DgHCcEKsRngJhPKXRm3fI5loDP5SxA5I8KOfbd7cdbCPQ6rRYWkwhLoKW5ICJ2HHagmobNSUukkvNeGtBpXDVuiFgwVPANnpqRQLhCy1LbVfMYpEgOnJJgDSGfJGpyMABYG483JwetvI%2Fg5az3W09GOZE5%2FisJZ3erzE0z9Rlp7K16JHuQCKuuu&X-Amz-Signature=13806b85b0244b3fdf975012167f4e56e31500b2337ccf7c0bf7a4d52f5dee44&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

