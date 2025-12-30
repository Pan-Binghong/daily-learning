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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZPA7MWT%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB%2BwDqNEwsTOg5IiAqyN3ul2uky3L2ENr%2FomyMLUKahVAiEAvl%2B5bYyzCztc3WJ1fpQSL9GWhJ%2B6EnAsQBS8%2F0AVqlIqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHmYMPTZxdGbZOxaTyrcAxn5x%2BzoJQ%2FnUjp2tGp7f4fCrqjgXg1wm9%2F8pMH%2B7TGtf64Wk0fNmiG94bBXrsmpNtsP4GPuDTiP4bxzqlNFUDBsYoV4W58zo4pJT1xHsIUZTA%2BA9zHogRB%2FW44Am8OSJFvtProi0%2FwXFgdqkBtGZNfebpJgy34Sj6TofqGveyprrPE5sfazUaKq8I0DWpmLpJdthO0CnX%2FuDbbinLM1NSIGqRh5y8RxM3aMU%2B2pBplp%2Frq2lEYao42s3GuzwQdc5en8GEJAUwi%2FozGQbXsfdsMVGYS57VEtHm0YGSsjjVlFUIMOEmG7etVjxo3pdZ%2FZsEC%2FTSogOuf3jx3sFeH9HtClwyYJj81zaBXDMoR4t3xtu8ySGz8q%2BIT73zgxzktAcnVCcTQZfaJXJObzxwGB2cbUSkxAv5aj6QoI%2BwunrnzsIyurVgsXQjMDo1QdKfKmqU6Sgof0zEzcuxryv8LTbOJbrIr%2Bw7rQwe7QXWOnSY3%2BPTFPRRwqa0W4myrAAoK5%2Br7GMWVkXI3JeGYyTCioKvovn7RF0RueFSP9oId8JJBpQMZV1mRSA%2BgjJIB3PipvhZTL7hECRN7Sy70HxbNiK%2FBxH5uSRPCqG96Lye4Hq%2BP3MdZMycNwJC9%2FDV2TMO7VzMoGOqUBl5PXqCGpukzJDW5kwIdas6wz6PrILnlb8bzz%2F%2BKFUyAYhTd%2B33irG8P6Kq9QwR4Mlc6sVgFxh3lmxQ4qTjxGleAaKBMBPvabLUvB0d5oRPSYiu69FF6kzDEmn9a7RqgmUZayOrHnPOUSzOgQ%2F%2F4EXBDTUr4RjMqLS11ikCgGMc3uUhaOAP3G98YPec0e4LfmBv6LGEwhWh7z%2FEMw1quc625FiAYH&X-Amz-Signature=e391cf52ea5af1330761cda8a843b6806927ec14694599f1e4ded93fc7d0e947&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

