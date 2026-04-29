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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WC5NZAR%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJIMEYCIQC3Dc5A553wpiGStzFf4pDXbTO96341CoL5qYrb5m7QBwIhAIzsGhqg%2B9nyxJ9cbBYTiUjRUVRATvufx5pJGOqFqNBDKogECOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz7yUmgA%2B0S1g%2B5i9oq3ANA5HyioU8ypH4%2BUgjNG%2BM9PXM76wXnVNQQXexuyCtAdL5iRXMlWdcLKErDx67Oo2idpKdivvx4YNEPBBVINJ1zmMrMbIHsM2nTGlOHIOfprJfw5LzGpnIFtJD6Bz0pqV%2BUKEJpD4IlskxInhbLIk6LvCpQbS9XSwuUPzY6odQBYthHQULYLxkVLV1py4YoQeDFQxxnU8W0eIThuLRnDlyi4qP3XkVFSGij5cjb4UMpwo0sKLRhZmC1YKHOqEAjgJ3igbQc1n267WnRZ6yi9WrHCatlarRWHXLVeRpytE%2BqXOyRR52iSTKwb7QpVrZ8%2Br2svV6%2FC9G5Gbx8aD0DKYKpT8NM%2F1HjXNIFgJYJOoQLyh8jknZWeGwt60grZZa9mWpuRvo8JK36ozF42EWk50r31F58p29YWhVKHo4SY6745faKy5JSel%2FHP7ylHQ9wc1Ak%2FTEjdWV2IblTb8CCf%2FsAB6C6L%2BJ45y0vL6l6pKKtH9l4ZQQ7dczp4KFqjOkOy38bI9emdMhNAlxbXo9WvIBGGVQ0VAiEArXKO4Gt6Vufp6yvyRniZd%2FMdCa8seoFDtPNwAqHQgnXIgbghG3RzVTCaxkrh7HWoZKLaZrNOjli9iN7SPIzdHJQn3JoJDD568XPBjqkAf4vaiS%2B4%2FGHBwT6s0bUgLsJdpGI9%2B%2FYJRbqB1x%2B%2BLkbsCtnkgogXUePxFjh6mrQ8BTawN%2BBJdmfqR3DNWPMmkNMQLnIGUmx3EXBw2ph6px3%2FFUC9C9kk7pYIREZtB73znTQ%2F%2FvdWv6pq6bg5ewAe3Q1YGI%2FGlExtV3gHe27EzKeBFe1ykfcUg2A5ycy7uDdgqv3%2B%2Bxa%2FJ%2Ff7EFPTqyTo485UMtC&X-Amz-Signature=650714e8b9e258656dead6ea57933a2279aa976e53d6dbbef2cffef1b37430bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

