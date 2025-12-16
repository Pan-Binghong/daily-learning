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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637AKUMAX%2F20251216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251216T025511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEMzQ0CyXjNhFTvXeiCL%2BK96qTYEABiXk80JBOtGjbi1AiEAxOy3RTyqWUi5GGhblmdiS6O%2BROXYLx9r0DDfd%2FVZ6Hsq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDPBJBEC0fo4wDBFw0ircAz1fWuwO%2FVUTQ5VXAead12rxkfm2j0IAsrTTn6cUtEXa9j0j8ga3wbEPxZyO13Hdf1bOrAZzt%2FE5kVv2btT27UleegZyqK9Fwax8RzuXiKFL7iaTnbw8ef6zjb%2F8FlHsvgvVnrhh5eijvmpHQOomb4Lnbrt8xQWfjSsWfnRSEA31Ue50%2BvzgMEfP9j3fSeDVNGHyALDdgEUiyVIqeyKjeYsnPWBXOvZwnhxxmS7E6Hya0Cm5bLriY9E6fSE1flTRT5glU0PEO7NOb4oEt%2FRy4lAmIiD5DvEwYkft3x2B%2FhKGG0XZb73T%2BAgjEMTtyGd2r7yg2Sh8kUbXUHpWVySKI8c%2BxkEwpP8eOvAeTzqlaKpwLNAuWnxlXzAJbE5555N%2Bh%2B9FBtQxS1Zjd09QwEj9XODdSPKCcI56OTRIKEl1pdbfKeV%2Bj7snEV4zsCB6i%2FVzL7mhF8isJH2uChw8UwpCYsMB0Q7d2%2B%2F9z1cYq5vw%2BpDwrOlgoG%2FqCBlf5s9KO8p03hVLmq7lTD4xLkEScDpHBqYwLvxxZ%2Fa7sR2jx4a4swm2s6erHtfhDOmBPHd0tJnggqWIrXfFD2KgMblrQ4SQx8HV9w%2FGhvo1DwcQH1Ykvrr68gsXqB%2BjyYaLKv0CMOSNg8oGOqUBgGLsN5EVXYaix%2BgnQETuX0g8Uo6nb%2FGy01WztTh2PKOhlFkO5%2BKBItvHdStwRfhNzdgcnTh%2BHGLjj%2F8rfIDgptnOVUXDiN10BeFE49PNGO1s37P1KAobOpyg9GHStSlNboLFOuJ9WTi6kkP6rQ6zA9cwBT5pDWBe8ZqW4mSR66G5cgd3kawbJzrwF4yLD%2FqkPhdqdY2TJmJrwqjM1RtNrb9RB%2Bfm&X-Amz-Signature=c866b3a02e87f50e8235330323223501bca9fbf860405c0e8da4373f15151c04&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

