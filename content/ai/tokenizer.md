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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YECIQBTS%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024355Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD0zJE6qSCIAcaTQKkGwXB10CGdJjXpTjTVsPYbmouNSwIhAKUmUkT1vA%2B6aSImQCW3YHf1cD9rcjuALW9PKErhVN4kKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxUmT%2FuyYKYgPpEx1cq3ANY6Wva8QNV0reivbf9MhYgsnYQMcCllGeLj1GWeS%2BhHo9Dbda56AcQ8%2FrW3%2BVmBSVbAPP1dXKcnofh%2B%2B12RDHJIu5a4Ryv4ykCmBBAFTMy0gfYtWH52JIMDr1%2B8rUa0%2FuaGnLUGo%2B7frF98MxhS5mxJUtp1O8HzqrxZsg%2BNfAh3b2lfcVlfekK9OuGCcltsl7dFoE0BvyDBo%2Fw2DsxvsyUlah%2BG7%2BNuXoA09H5FpP5BJziW2r4DT9W5D5VpX%2BdGPvyYvoVSHvNCvs%2ByMybE1gE9HrS9P2Id%2BjBexIyglBoil%2FTe46AeuzxLGMVOg%2BlnTgn5i01AS0CK0Uc87A%2FCxcNoAlItIB2wz%2BjU%2F70ZBRSQ81jvuI%2BaRqSkjjW1f%2F%2BNSDSew%2FywBuzGct6ET08%2FjMugEnXhKf%2BrG%2BMdJa%2F1jcssdDPEXHGPRLVW1LYmGBwggTJ6%2BZnIVFzhE8tPDb2pbIZiY8QzRc0JRNHi2SasQiivL9ddntajJjwNcZ1C%2BX7Si%2BHdRk0wMV4tIrBS48DHnXT8CmyR0Oruqwn%2F7qxuixmxYVBYZZXKIwoPZkJkhgopaUhvfYYfGkiHhIDU%2FOA1RRAwFZa8As79YLvqVXv0ZrWBLQtnKaaTMpvy1gzHTDdl%2B%2FIBjqkATwE4KRhkrUiK%2FGmp4JMSx%2BkhpYhFwX8yJdqz4G2BbZ6%2F1t3EmILX72lF%2Ffk81dQOPWqLYRYzOhRdOeJWnaJr1bqaYQrHploCWTrH%2FNiorZeOYiZjq%2FuTbSsaiINB%2FTxlxNBJJXoM6mKiz9%2BVhinDsMt1ZmgRzg20tFZuiIlTyP6zaiXsMWca6C33OtORpTrpLYtrnCacChNbaf7is4%2B1h1CG43a&X-Amz-Signature=a10d94b4c219f2494c5947d3806c8b0114c473646973c9d6dc42d59544880eed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

