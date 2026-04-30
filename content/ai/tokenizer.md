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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJMPBQOR%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084827Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQCdMfN7XFFDB0dK6RWPe3jCA3PovTbofizmMlCGtbMmigIgbxok%2BhA53JeXR65QeaBCUwvLb0%2FPM%2BNT73upK%2FXNW6Uq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDOSplUTfouZsbQaUbSrcA4ftRQvQNyXeCapjvmyxDAygjwIsO%2FZPDW%2FIONW2IWWetDt2l9dWWHqmbjBHvp48CINUwhFbIRpasfKsp2qIUB18shFuNe%2Fq2qmQmaVrfgkS%2FPDGeDwmdD7pCe4M8VGNgFOl31pcX2hFJ1mmYqmXzhLqvI%2FKSSPSap7SLdZnN33f3lMqSQj8LbpFXx%2BgCRRqYQOeij0Uxp2YdRKp2F5iPXYpgrhERaVYWIXDu1ZEh6FMVD3bdVUq9nJKNEnilVW%2FvAlsVd20tORvblfk%2BH9j8p6AEZwBkqzdO9Wm6naiFTfl6krMND76XFgpuk6JuoARCYc2ojhYL7RCjPgjhZ8MUc5JNnLYStDszPj8JK%2Fzr%2B%2BraYnXDhwe86ccoBu2jp%2FQKDHu0TpdQ3dUEkwqm70OhwJalAO2REN4X7ddUcR7c0nin5PYDBWE7yhIWlmEYQVJKUfKFs3VQHwP6TrAWXvZHr9H7GtqI3cV56jhVpfTEhx3YHYH2p7VaVzbMVvXJ1hm%2BcmZah8zQ%2FtZ3D58XEwHCItHUizN2%2Fxgu0y1YwZDpspmAlOXzskufNhfdXur8O1Fxlf%2BrgokCfqyNq%2BAPOU0ZhIrewev9UsCXzGrf9aVEwxwdXhJB4nNNlBe1hlsMMObzM8GOqUBQxCzoxpPRiOyCR3TRwSDL44IiwTWU5693mCKKpRZ7zwU0QtYtqDfMjpxKHq%2B5aQMbdXWhh%2FfyiL6WiAu7YeQv1QFPzBNSYU35xZ9A5a9jgINeT43lwvbgv0Lqy0ZVMsMNPPl7xrYLlt3LkKycBfIOAfGOVI0UK8PzsgB%2FdJI2cgtaMtTO2OpLPIEhASFpLCD0i5O1eynTtr%2B7CQc4hHcpzaJdTdD&X-Amz-Signature=e3553c5f3142263639b03ad5690d58f96d82341009a408349e8b2ea6c2675fed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

