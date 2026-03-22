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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YY7PGUFK%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCRUluOT1u%2Bt7KAX8kB4m2Tjvf44TZopm0dXdnTqxvBpQIhAI2IpuPlInzrAigDXCHIXvE8rKMTidez6eEsMp5qY5a4Kv8DCFwQABoMNjM3NDIzMTgzODA1IgwzVlQkpul7Tqriuz8q3APrd8DK0b6YrY9qFVJYcZE5Xvm8OlGFnB1BJxZMYEPGo5%2FYZxPpieo889YlpS3U96CQFmxonRsSnq90yJDe3UJXPH3xOIclto2LQQdp9aly82RiHJTqNdR4JpmlkVTSH4ADHSPIC5%2FIqkETIsaYDsgMrpdXcppRRp342E0fYUKXa4DPl0wWjXCIk9S%2FDfWk1o2%2BByH7HIb0m6ervLmXMUUXE5poPA1q4BAUP0FSBQM%2Bc%2B8gkRAklQnmoXLTpxWNSegHX40WCxhW8NCHvHnV25WFOE5LTSZtHkiEe3CakswvQCm1SjpTJLnYaJugK0U4m8a3OPSKD6iGUiBUWBx6PYdR6taRAg8S6eTlm4%2BhHhdqofjw4nxIrsJew%2FRqU4rfOzq67maEkZcHyRWhHWjYnnVjX9Dq82SPxzgrtrhBtYRZwU2rOcL2vG1HoAvtWCPJQ6SKdCeoL3G%2B1qDDB%2Bb1flymaSDyLBtFwEKUoWQqzjzfgnVSa58Q%2BZNdi1dMP4SDscNKKLi6angYSihZ0Q7PmbIivT4Yw0yFqk7S5yeDcYFyFQjhmckuj3%2BeGpeVMJj4P6sywqqUdh0gH0bNQ4bz60BSqIdstyBxLfqcOyDBoA%2F2DnTbETI3uJFMRbH7tjC3rf3NBjqkAXn7kFfx41kYJs5ecjF4iE1KFl5TMlrcczUm%2FFDSc%2FuNBNpvjFnE2svgya4u5jYKotOUqVxXnX8yklnPVYFAHvPWInyWHCuA7bW%2FJrp4yqjOiBQe4r6%2FnRNtWTgcQE2d9h4bOK%2FKT04EH5d8J3v6%2BwDlWGB%2Bz6d1Xk3nnljCqtehvLf8avxufbr4LCXPX1Te%2BoPKngs3y%2B0gEhnNrZF0k%2F5osaVY&X-Amz-Signature=0481b739d6c9a5528e3462f9342f67ee535892dbd719f12cf5256e982d78ef70&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

