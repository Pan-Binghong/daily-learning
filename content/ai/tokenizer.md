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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TE5AEA2H%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCnBL6FXdyar0jhQXpVpxTEaudwBLSRDhTYzulY%2F0PldAIgPVloNSmJuvAQDB09XVnGIe%2Bc0WiGntlb%2FB0AyLritFsqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOR6DDzk0C23s8QbbyrcAyyebctmJvfoZVyBe52co%2FlZuW3yIlRk%2FWa0Ew4urJbbS8ZlklZVPWToZKlK1wjvZROkdxR%2FiW%2BM87U1n8skGonEvauLtiGk%2BD08x%2BiXXkWDhYkgMtAdAWcgHCdRJ41u3Xb%2FWbB0H3eOOzilbgIgMaPONLJt9EyE%2BqhUzcPLB7ghIbxl304FcOYueTX7g3L9Af%2B8YyOvoKC%2Fbj2YuexvoQOpmc0l92P4kINeaI8gbATioqxmsIyKyHh3niPDvi%2BK1noxMD8hgIYm9mFNU7sbBldD%2B94f8xa%2FvLGc1Fzf5ngKCyXn0a1dartokWWN2L6NWIrhhKBhj00BXIagcewm56OYR2oLk4GMYIl7WG%2BvQboOiYSGV9UOn6omnMfqU%2Fk9bVWlzVC43JWGCakJzlO34G%2FHwRXRZrM7CTzp2SWlfZPVNDZnlsJsB%2FLFyyxRa%2BazwcVfzXra3Vbw6oyJu9qBS%2B6pCpA5tMyspfQ2hIszFSvxTbDsZ9kiN%2FXZzY%2FG3gi1uAzcocSA2j%2BD6Gqp%2FjLbvRseWl9S23WjzCNDI6buKRtm0i%2FnPm8GHWRdQ4nYfUWy2IoN880%2FeLXHqvTVejoulrw7pR4OHqvyRa2OLmxJwSkQ%2Fs1tOyIh1Ueohk6KMPWo%2FMoGOqUBikn23jo%2F2aEoRP2mxyVZws%2Fotw0JDuRpwGzjYHvriZgp5savE8OCeFl5Np4DrWCbUqivWtZBisNqxPWhnNFmSG0Qq7A63upOapcmZdvtQNirLBmqldF%2B7h05CBz0n6kn6noOrGmMAIuuBZmgyhnVa5lqSfa7H3rEWzShoSUxRutA3iwqrO5N6vMwq%2FVt0WzJIEConsNQB%2FC73EFIcSvTteW%2Bad5H&X-Amz-Signature=bf6df3513c8699a259909e7a20bf52e09ec11890ac766f0988a69257af1fa2b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

