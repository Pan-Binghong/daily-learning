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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROAVHYGZ%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCIBjyEjObi5A%2Fjfm3sL6ti4g3Ca0uv6tOSfbYIRs6%2BVYjAiEA4Pg0D4pjJp3zp1ztmVpxQ%2F7VTaerq90QmBDTvbFssRMqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM5WC61TO0KKYqh%2BXyrcA1MzbSCj2VBMz1PEqCbcz5NWYvqm9meDrPo61EpsBcoT91%2BzE8D50ITP8tI4jDdsH54JKrCJH%2BZZ6CDfJjdvoTbMeEHQNh0wL%2BRWD8QuaOx2TM0WhcSMlqy4cH4HknRtfXdqR0ddOmimnGXJr6C0F11NFCV1LVqia1knzpVVcs%2FiLAgQ%2BnL0JcOMNIxyAzglR1OAyK%2Bx1fvaycW12G0fqiEhi0P7tY091zdQcI4sr%2BIq0ByOb7SbdA0N%2FM6VDFA44TuueWJ%2BVwQj4XLOSrxg9RECXG8NZtROrAyrYUyQgqPJuuNZQZoIjesYD01jFU9XeJ%2BNbksDGLtjfKrqAlHExOfPDGDKSH47k4G49Kfue07fPLfYfwm%2FGJgLui06tRtWzLl49r3RYJ3Of0jiS2XtUBdVXUd4YVYy6aJjRbRjr35eD1FVtJwDoYEeHAkgp6I4srG8GMtVgNPB0P%2F69gdamqcNwpeSMWzwGC3OBVvH16HwfEDuE2JD5RUbzbaAPHhBSS9SaYHA5RBAN5voOQeAj2uVTkl08TtWp%2BWIuu8JwsSwoVAsPq%2FDZZEmT9A3AtQW%2ByY5xbUxK7Evf1qZGAXbzIL6UsGHwzmog8fHJgCSMqcDeqtDmLJ0lCVU80GyMKPYhcwGOqUBgX0JGJwFySo2pWdNMhV%2B6RciViVtGQ7dv%2FyGTO6tj%2FudyJ2EQ%2BJu%2BorrAr4t6Rcid2kidDrRS5P1s7TMQ2W9GuJeD3fmKjancA4KAZ8s0sBeKIh69q4cnCNhMWSYff%2FeOeW3OFeIds0uN2VrIa2nhkxhIlmKy%2Fc3%2B8KG7FriI5F65CY1x5BL2TU0EkrwuHN8TubyfXu%2BtPTI0YmaXWC2%2BchUa9Gx&X-Amz-Signature=453c3510708bbdb099b6a8d60e77bddb262d3eb8274767569d086ab7c77d45b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

