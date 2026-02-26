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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJN5U2PZ%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJIMEYCIQDrgk4dpkLdADM6IA4BDHpCue1XHPDSGU71f2ItJSVmPQIhAMhQqjlqivWECHkYJav0FKtLOwqQOtTUXHm9qYly2n9VKv8DCBwQABoMNjM3NDIzMTgzODA1IgxUu9zKdnPvBxnuecAq3AN%2B9PXJXzHnoBCVRyPkp%2FRiSkSGDZmArXmVbAQd5ZBLtWKEhmPHzQ84jQYrzput80Bw8nsBlCte6lL9sDsSGYc5yyZejmeyrd3%2FyEjDZxte52MbC6VZFMBm4L1kMol%2FDy09lVBuZ4RorjzyJf9RYrMd4shNDRso5phqTmKmK2%2Bl1QzEnpmZi2Qwtp85pORiWnISs6KOwUDX0wcf4Vu0rH5PcGe%2Fa2vW3yEVLgakWMYi%2BCsFHV%2FTHPr%2FlHXhuVjQIhi2ZEsHO0DbIs1%2FGpoYUR4DwgKxxzUW8jV9hHCCZ897LbhUFqGArRoInH9b%2F3sQRgcUhSFZSsPzc30eQQRjJZXTEFeWRtmm9%2Ft5ztxzjc%2BqkjioEkD66W12coQ07VGNvsj9OpwjggjCE2XNSUl1aF%2FAag9QMK%2FdJi2mVEMsBrcfpbLQRyksUh1XEL2Tb2WfBUxExuHJOY76kkImZiqkarJikxnwFLn72Dnx2TTLcJ29wJbpuenZ7mT6PqherLHJgqtHGt9CDZkDK5SiNlwU6rNSQz1%2BnSd5sqH8omtsSHU7GQFcmI5ywbNMyj87bOcvOYw32VHih9V4UjI9Tt7k7lpO91oM2V0mu2ktBjEHrw3pIsQJgLrYuthcVT5Q1jDS9f7MBjqkAV7r7vCRMUhuXNabhSbJKiRE7qRStxbpkmzIT5UeRPf1GHL%2Ft5OMEuEm6cQs9juPuhY2SEwPFBgIwtnkIck%2FCm%2FsXyLIds23D3S%2FUWvOUkVSX7uhALvR%2FxLlSff1nmfflpr%2F8i32%2F3hYD9Vmt8K9F0eKtYVZhcSyaXGQuz55lPrObDTqFquwVGtzdOyQ2hG11ZCaCIdhBN9Lg08I5rPselJ%2F4HSG&X-Amz-Signature=855963202a20f7fa3fbbc935442b8b7b2ad294c02b8f81371fcd1ca407bc25f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

