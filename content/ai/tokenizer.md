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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYTQIMHB%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T030002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJIMEYCIQCJcx%2FJaepDNDrECtrQbgZ782iB9bJXT9PSEODTSk%2FoPwIhAP8AG%2FjPenyWq%2B7q8pqy%2F0A%2BC5NsJ0sKVT%2Bkw9y63WYUKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwlEmeJG04fVvyrU%2Bcq3AMijC7m92uWxBP8Ijf6bAG4pYVBpkHHJBNo7Tgd50OqZVwoXmBaNHYumd0PEbmOjj805Wwo02hDptzTqWCLUiFneILAZnGBy376wK3hOXCZ6CefZfjxrIeluh04ss45cylTwFjQ1clnRy8YUJAOZJm0Edvg7CgM7fFXtsEOk362pd5%2Bix8E5A4958BXoA0loLjPCmEBGRPFNwrAFW6tY3F0m2efar7NsOf317eoDZY0ijKQWCQ80M2EGLqy2t7PIlbdxaQgek%2Fk1ZSJV0kfarhNTS0DsEAnJWk%2Fz9tubuuh8M37FGRISEZlojBbK2jkKlpPC81j5N1YzNWAT9f%2Fdc8tJJtOLLiS%2Flwr8KFpdVlpwbimTbREUjCM%2BWI%2BwBbLPc3eF1BylX3tiENUgqU4X%2FPw5Yx8y6pVm7DRqDc7DqR6FSLDOqT17qIyPS2rU2p%2Bgv7DdRdVCnEH2A4AAwPzqiArhi54hmCmejBSipwb4XGZ%2BByBz0sO8IZ00%2FJqWli0k5NRQdzBWB9jcMKFEEZev84fTnG%2BTOAvpcuXscevgp6X2%2BGFjzbajGZhKNDQZdP8uertRryN%2FN2oDR44frnVk1xmqO%2FAHpbqU2gLOqDuubKtN0ZHiVMSa5ln8A863zDYztzKBjqkATyyAvZhSIK67Cl7ZUEgI6WCCjYOvs4v6RitRGi4bWRkRPvotq59kYHsAFgqNtwoECAT3M0uwGhuILCoJslZjKbBvrxKgzyL4PuHNaRiA359uWWa1Mt0q0NEoIPUfyPZUbg2roQjThpnPO%2Bjg8Lv6E%2BcPCgSmoUW8JGE6CzIXXjraGKLfBT3BrknTctxnMBAA%2BGa3s%2F3S28nyqSVRkQYQq0WXp1H&X-Amz-Signature=bc8041e6fcd95921aa3fd9eace762559fc7b0a9574c4dd4ac43475a453aadd0e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

