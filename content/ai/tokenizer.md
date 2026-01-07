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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T7RPMF67%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T025927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB5U5ZkFEPU9DjKQ1RwBLOM0yBzAxzLihdrVkAvszyP3AiEAljFsUmqboF%2BlW%2FUhN4%2BVOaLhEaNaDlGYfX9Gv465fyAq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDD8r7CVW%2BmGCBVbDACrcA8NTk0VPCLr6SEg035DnHg%2FmcGwousBOrLF2UQqOcTvWImBF2KeHjHuYLQ3PPdHLcUXSPqi4TCO%2FB78HEHUK%2BvRbtRwDF9aaoXKkxonRE%2BI%2Bq48bGWYcyy7WtZMM0gk1ZSbSmKNAKlPmoERVK%2Ff3qIU6su5fWH8dAM6lzBEm%2FHPyFpFfAON4qcVVOsa1QQpRDdBxvahU4918ohT91eWXYpfCoeXC7StOEz%2BSTdR7PgE2U7ZFW2rDHAHMOgvxCjcD3BnCbW8gz1L5K9X%2Fq8ewLTM%2FPPn1clAHi7UgVkl7jC7w2OtfhnZ13TF4z2Q0NoGB8PouNdOPgxQPiCi1ClIpAsjSu4IwExz%2BkrmOlXhTcm3NZ3vZaS8pEscAQZ6Kck0sAPTeb5QEthQgUcUsWCAhaoMzyaBZ19khma3UW6lVICRge3pJ4aFrgZlPLkJJDOP%2B14OO8zamR2Ledz%2BCv759ss%2BL6V8wDoE2qKSDnqS8Ti4N8P1c6ubwthyQHBglRwcp5t86g2a3KPvtvccVpnUjyT%2FDv8VwDrUXVjOIltihXGcr1f8BgAn5ObKKW9cIBcEjt3yYYmY3ffCuQmGD8sG5cSsLxedSBjhqoMlvKwHvP7KqKdu7f2HQZcKk%2FlhLMMGP98oGOqUBY%2F9OvD0Hg4b3xq5hMN17ZIOZVn16dFjOVQyJfl4F1pSa26d0vEWCKGxeUxRmZQ%2BT9O5qEUARyrtpYDR573d0BzDhr85wARX%2FoMHybegPw5s81YZQ4mCzHlsF%2F6xWzPnMcTFD4Qi0GMYJ1MhQURXi%2FTDexCZaGb4OQjvMmy4qhhBzG%2FOf0uaFFla8QivO0MW6BsVButxD8VmXOGpUY63iXSXJ4YIH&X-Amz-Signature=2e651b4a7db0b3148be1baaecfcb4ec7494fcea397b51bf182e75d399a04f911&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

