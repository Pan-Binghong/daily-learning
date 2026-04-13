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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVFRKH3I%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAXejIDFtpsdmeIzF%2FOORmgjw5ZmPHbT7EvwFCUSwriIAiBy14o3dHbPkLtFG90szhqFss2TvyhSH%2BkctpfA8%2BW%2FbSr%2FAwhsEAAaDDYzNzQyMzE4MzgwNSIMCW86b1FEcakAOrfiKtwDpVK%2BYBrRTJ781PZaaHWTEBySIGvbHghJFJqz4CUb2w396WE8eFxUfhPeriHP%2FSx9EKejB3UazF8i%2F77gaBuqxqOZvQ8hxW6gscfTU5xAP5dwb2%2FMn2%2FCYkQhXvV3cqCWZpmm5ZNTmHmEIz14GlteK1jaD5ZF5z6Do%2B2ivoPP7jZC4fH0K5HFQk1xfP5Rk5ofXgbXsQKroNVSxKzfGufySmCsHrs0jQMMZsoiWXgfUGf7Qa4kmsUKurjL%2FwljP1pMKhTBnlMjcG2XMhDB0SYpli7JrdkwYbr0ewuAOF7KT%2FdNvpaqhi1nTr1X7HHh2%2BD3gPOwjdacp8ErAmIiT84K%2BURFKYEYJvr1askkpX3bWQXSJAy1O09b6he86ljykb%2FFBkodIbvdJWhcX60b6%2BphlqnifqkBmquGfSPnHi1VKP1R2hv4cwZJIOjNag9bdci%2F8aPEd5qemoGAuhF4YPigW5b%2F%2B7pYM0Zf7EVKG3Ff7A2ijCX4Uy%2F8T7AdHaID70rlTZflpxRsh4LCZVAE1UU2UvesFyAV4NDvqw5FvFjhucfRrYZH%2BNQplygJCSE9BS%2BfTwBjFEQp1FCBmThpcg6qINRNu8i3abHIyt6At4zbZkeUfqsz0IQpcQtTHvowuq%2FxzgY6pgGvrr7p19y%2FoF5lJIBMrLdbd9zAfDiTrU1UFnOPm1RDISUXgLHYe6NjOY5oGs5r0re0Z6DcYqkLZI%2Fxse6hf1tIGVrMzKmOTqutx6XuSdBkLA3vJ8GaQYqLrNLPkO0%2BEsoPE9qWDP5ifQTWMzsWgKCrFTp5XgPB%2FehslTkIYsr7rnAAWAjw9ZoUt12w6OjvX6qbaANvPPQzvUlbqpXjROFXo%2F3vfYHZ&X-Amz-Signature=7dbfefb7d7dac2eb4474510eed69cced9004d4e0ff6164126fa019a0917a6fe2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

