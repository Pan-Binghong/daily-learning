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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RERQ5QUH%2F20260317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260317T033523Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIQCa2j19xokdNOWrvyabRlK2Xx7RnfU3x0tvp4Y%2B5Jv87gIgcH7BDcEzDBtA4uDkIi%2FZsD6OPmkaVQGfl8TMqPpR%2FA8qiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKIEcO8KVuLu%2Bv3n%2BircA7cLl0o4z8tPyxej8gt495jbgnQuiGBUpGRYjkEBlQQ8fl1ASRT%2BJckjjczrgVcBzW%2FgLttcVXUg8wod35Tn8oHG%2FjUYj838S3%2BQRk4ZUiqMGGVfcF%2FWNGBMLnLrBzZGXorgN2Vz%2BA0nF6z%2FcvvPZuq1TiLL9uaf4vaQxTWiWnQ07GT9oOWaRD4gU%2BmBc84EJR4CLC7ixXqfQmjdi4Pv8rDuDklFDWA3vY31V%2FD0ToXsZ5j1vthko2fv%2BAEpSF9nNJWndmhOWPx%2BBKPeQ%2BBjhhpyu2L0g4QmDtCNH8lE%2B8iT4cxH06g6aL7C6JTdCmRfsdpppCJZ6MfeSkJ%2FDTicsRXJ%2B2ZyRQsFN7VRSnhfJI7t9ei49kiA%2Fc1zx%2BYs5%2FqNG67GCcc7UL55iuXk5cIXnJSrsurMwVI%2F%2BXDVw4nMsG42cDRMSYlIUH%2BuMhcAjomwcpvZbWTe1P%2BP0AvRgGgnOjczSmfJMUnkpXMmH1iKuz1QCezTl0JYS4ZUzof0oOXelHqkUE11iBT7G24NPyrMvyXFZLVoFPVX%2F5mI1LBXosie75GVDeb8ClEdPzOJF%2FFUbgpeRkZOLEaFQig32p8RubuxBrbhDqAeM0jz0GYVzY02AouBKAy6sT1vocVLMP7n4s0GOqUBH0oRzLNKtOkbsngevTUbRBKnmfagUHWcUGR3sEzdrpugPVVXSk3An9g3i%2FKBo%2B7FqAQJBYfTy0nSrXcBDIromDZ1Hkqx4Y20kMGHOWWWSD76Slk2UYnKTqEjrU8BxhymU7roQNajJddt8mnMu2g8JzrSVrhKXxqQFInU%2F4LQKcw%2Fg7%2BTjuteC2XMGJBLiGvLetVBNhDTNCc0m7w%2F2kPwD7eqY8aP&X-Amz-Signature=d8d66c3a7ac81c9847c528fd9003eed5f78e97a574e299fca517d104e8d39402&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

