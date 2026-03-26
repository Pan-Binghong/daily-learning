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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDSPQSV4%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T034941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCtJgroQEmxZ8bendKVeXJgdKmCxx%2BzuZF1xnbfsjboNQIgTXSeOzUu6GEIE9adhcoLaga%2Fpf7O3Vt%2FKj6b2oybsJMqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPX%2Bz4dQbLL%2BsTMf0CrcA7jsAaevuDsCS9vUMKa0wUW0OJJdlXL5uO18XhW5uMDnntO1gvlz60jW5qogMgfF8P6cUNFEto6ZvOPGNV7w%2FYOeJWxyVPgNTcaNsu6ArsUb1F23qb0CBv5bJkZ9Kd3p%2BpS8JPKN2CsxK46CyUnELMZXEbCy7%2B5GBWxRJRrv1TL9xrXxySpzxUTFm%2B63ioa8NHYdmh5cKt11eVPE5tYmG2Fc9AHP1yGTMug%2BdPFzCighX5yREXb3cb4AXVGtVCEbAcNC4Uiv5FswEtDA6slzTfxMD8fEGp2Sc9Z0ZPldu0rPHT3rJkw4RJRMjF1uLX7wbmXSt9QqoQrEEXlQ4wp14Bdll%2BX6rRJpSvoLPnorO%2BDY%2FLpUsPB2EQmN%2FAX1Se8f7JQ7d3nVagH%2FHRrP9FwQ2w1QlR6TgHShrNSM7XaM9UX7z7B4f%2FhWdkoG%2BqGmQzk0N4%2BL9PhNCcjzVUiORWpuMS35xNMyGIvKj7NqSS84rM%2Bf1CqbMO45lkdHHqg00R8ppYG3kImiaRtpiSzTY0kSx1l7PdwEbGmZWT5bIHFxqRo4k87Z7VVq6QqexW2jAA9efczalkhekEk2Gy6184Cq%2BoBtLwE8euWVeqK1SwzetbdFtQmtjXYElNcbMpOrML3Iks4GOqUB0RZQH4BvUIkgg%2FcJPmJC83K8K9IxsyxO1dCHFARGvqQx%2F761bEbxIoYA%2Bv0VwmBHTYLd3kg7vvr9i4Hsc6R5RVedbWAsNzJppzySBfr%2FcwbEivT5Dndj%2FL258%2F98U%2Bh8gHAaFittPIS8Q3Fqv8ykM01PlcG4P%2FTla%2BkTrhxiXShLC0pLszXWSSkL3V%2Bt95aeLW8ybUuuRMAjJAAPwwiJbB2w3pAj&X-Amz-Signature=8f8dffdedd0272404f9be948cced1353da7daf5db41ab80be18a0d314cbccf3c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

