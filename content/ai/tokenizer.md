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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TI6IBYAL%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCAF6cJsAiUIDxvlS2Dkd%2BVesFT9k%2Fdq%2Bi%2BLoasMDWRrAIhAIemA%2FCdjBvOscwG7WXlIQa30lqt%2F3J5r7rR8CJ4nxMfKv8DCBkQABoMNjM3NDIzMTgzODA1IgxNGOXy8Y%2B5Rm%2FR60Eq3AOWYPc8Yx1ClimI2NPntwV4B2AmEmAQkXWXcRbcODJAx72tOAmzy9Qz%2F2bFdsrprfE64QNi6sTgWPOH4f9TUkbD3npc6NN8SWzH4eRZkB%2Blyr16TrPL4HOVNXfPsilEfdej8Dcpe4SFfWug6YHlSuIgwa70A4UtiDCBEzp7z6GEDesP1FPjVZ%2FFQn9OqeNdYtfAx5A8vevr7f9%2BxWwERnJNB6813EhvFMYNApHhhd8Omhix4a46lhXXEWalYICw6Iie2E7Sroi9FcqChXukWQLc9EGAzC%2FQhLmuVnhIeyVnc5IMEBoL2M4wYXEleIu1QB1CaTwucv28yiUtS1N9G%2FNwQCL59mLO5CoJlJVnKRxggvVAl81kuhQOwFW4r9Ls01O%2FN9RLxs5rP2zn0C6PHnwQYr9e0t7lEf3jU4y6D3OVBKy53WyY4V0ughXrYLgh4hszO1%2BzHEh7Eo1xhd%2BZb%2FzK4CwjPisWl2MRF5d%2BNaAT8poinwFbtnhHsXftCJgS6Az1B5dUCvPnVOgzv9C3h0EBsv2olwmtGHPWsm3rabBS5QmqyXe8%2BCTyTau7qvM%2FprNssvUPVVgOJSY6gyrMsGFZP8b2y9D90cIlK2WiI4P%2FBkXFoXLkCRrvJRDiLTCM4azKBjqkAQ5WQeh7yyrUwNwD%2BXvg7xk%2FVJ4CpUKyVunYlPxl2FiN%2FaFI%2B9dBX3QVy71z68fyQOeKt26Ni%2BtTZqiuY%2F1gNo5BB8%2BHo5IUWvw2n0YCdKfN7UMIyB%2FwBTu%2FHoyGhdhDZiqu%2BMNW%2BnC%2B40uIK40HEsAGOYzr45w8Ll6tdizxtiZ%2BbzJ6XkOGc%2Bc5cYcmTiP8J7V69ePO3EFbGx4KnX3ToSTIHCpG&X-Amz-Signature=a0b063919198b14aff72289008289770c81ecee6d9f10e6a47e68e0a9104ab3f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

