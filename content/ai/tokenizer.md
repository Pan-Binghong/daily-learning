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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REP3ATGS%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQCVmA8qz%2Bc0sgTm6AaA3pMG2tApvmH5NLaRD5hK%2BBhyOQIgZ1ea1Q3SBfEIsgwH%2FL6iB3S8UNelAf37ezqkaJCQ1%2Fgq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDKp2F2rvcDz7DZm%2BLCrcA9JoQ6JLzE%2Bj3ncrL03fPdvUJCNDUHwjXhkvyTOuSIqwR5ZISohiD8dGcRWVFra0ZvP1%2BNMukrTkI%2F2fVBuqGFXypD4zsO3lLiTTZqC3Vd1IDMKjHl6QR3hhTKaYeICnbccHJ4Gird79txb95MI2gAwenImlDM4bDpLVEamgdNTVzI6%2FCuM9EeuRwEinRAAbw5E53YicYk6DLZjN6ZmlEh9skUQ8lzcU86WnEEtkItBAyf8XARwvzdMdSmiJAu2drkrN1TITtWq03ArpODmit0WdLTqFdxn59M%2FSDzdBM%2B2055uEdL3h21TlF6yw%2B%2BflWu8d%2FxOj1YmBVkrtduJKNekmM6JU9zM%2BQ6R8cdLiy1U8AQF7Xpxl7PQqKd9CBGZpN5AGQzMdF7OmI8WhUzANMu3044WG0rnrBLtCQF4%2FWbnhnqu6tO7aeI783uVzK02%2BOLRi9no6uTOTAC2wKH4NND4GNZREc2%2FPTq5vii2B7LrcLaG3N5vh%2FFStcV3oOv5c5h8dYx18oXXDpwGcfcqlkh3XNNkfSy%2BIiVyo7%2F8Ck5qxQyi31pKO9cd1ygttC0rKZZ%2B9iZ8cryCbWoPxqr8ujRE%2B1njVq%2F9Xzfy0zCN0prwVjFe5UIgzHXYJjcyxMNnVm88GOqUBn9hlZ7oq3fOnua%2FBNShQwCLauXFVi1BEhy0OLBWaDktT09BJ9GKFwxULVQr4feMPSPjhxk%2FtSWGj5NdOKsj8bBXcVFjQO4cICA9vhAI4StGdVletuu2zyUFkUme2oCAiEcmgXzBzKVyNXx7TGBUaDREo4WGdYHrHorNnL8kYT9vZQ2nRK4WnU5QMmbNsCqTANwxdw1wm1pV9xbqydjD9xXNmwHbp&X-Amz-Signature=efb02e719a1d1a229b73072d985bdd88263d39d792ed6ae2a3434dc08299ab55&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

