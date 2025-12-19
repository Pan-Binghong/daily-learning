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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5SCYDTF%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025423Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDNX9RX2fHRrmmffTpR6DoRRha57Tm8pSkrUk8187CJdAiBeP%2F1riiMSXhklwUcA31BCc5MPwBT%2FnOxy5ANgwO9NJSqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FZx5k%2Fd7tgjRH0coKtwDFwA21jStkE5RUPjpqXkwCtvEeM5Z9Y3QHP0d4FWI%2BxDf3Nc%2F7ejnd9IZbOpLI7gDATBM%2BZtcyAC4sv7ZAwBlgtYodFV0ZajLdpqfsBFvv%2F%2FD9UzHo4uhWNdiyLRFWbCtIgOtD0XFUl3JVk2WXWZmINd4e0q7xLz0bFuC8jg0xiNZ77CwFfmjpURbAgrhxl3nSrgyTnmUoKUHx6gIjoXw16StUokWEEGd%2BspAvOLAw2lQnbwrZzX9myP5WuFDGrCQoGiL%2BXQsSgcDZJ4TYogzNpeqRoLf%2FK%2FAVPXZ5l4h%2F1gXImYEEyYRycSbBRXXmmZxIYByNgl8%2BK4jeGkHfIj9AXW%2BRCdC8Y2URMJqdd4paWcDFh%2BCQ0X9%2BpSWgA%2BFn1NLYlSKz4i%2BJvccLKM8rItw5YvbUT0YlbSSs3%2FA22LxN%2BodaND8IKmxcQ0GqGE%2FvHa%2F%2Femed8MtBKld7C%2B91IrctLc4s1VuevL0yF9GgDthBwBNROSFrXXhnMU%2Fr90NDw3%2FSYdsHjAABNafdfR%2FsyejoWPc1aKpzzU8KnhPvs%2BeMJAczFqde3GehsBQ%2FW8UjzcIN9awxP63DED8%2FTnvkmmdimdtpCFTiZMT%2Bc3tLMNu%2FtQ%2Fwg%2BV3EMy%2BudWF4sw1eGSygY6pgEJ7XXikFbIisfCDkfqEBuhcysUbB1DlDtRULN4vH2uD%2FcyeIB%2Fyfa%2BG2rRsvFFfvpDhWEEnMFU1B66rVbmZwtZBI%2BBAB43kcpBUNxumNEFZtMLP%2FSYeZt7JMXrvfB84sP7aGVljG0bxjN1wi4roj31waYoKszptKY7tnpO%2BBsRnmnfb%2Bln5YzzhE4GKlQBoDMlEDsnN%2BJFZ0x%2FXlP4FPnmxahdw5jH&X-Amz-Signature=0ea64678ccd1bd2740fd9211b38cef037320269cc44bd07e904d0a496814cc5b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

