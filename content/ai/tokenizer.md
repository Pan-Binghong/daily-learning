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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JTEL2MC%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHIEJnxkgWmluN%2Fb5v3N2DK%2FHG1VAqb1QtH4ZJJ718tsAiEA0LqXeXvr%2BThn8X2ddtXAogHQLe33UmD3og4tJfj8ak0q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDPQmvTQBWJ99UN57aCrcAxHzk3tm0Jp7uB7SKLX%2F9DmzW9QbKRMCemwQfXs1mmmP5A9RKmUFCaSYnInxMiMUusCV2BoV9e4skaQ%2Bxv6g2MAHpurzmXbjEHirI8uEHslFikSSpGLdWRAeU4x7%2FRugekq8gQddlBndTr%2B5M%2BictEWyPLuilFR0YaQhqZ3FO4nVKZg1bP9ey2ByhszLHomb2Fz%2BcvGDSIKCta5l4AIZtb5wYu5uI5eZqZZXxlIcLEaooDfZICMOnhdrhDRGi6gZHwLmh8os6HED%2FkGKcKzNVKqcoCbr5iNRWDO%2FLscGKZO6QWp%2BnNwjpLGD3iYDWsPVfzMWL%2Bs3zsbH%2Fs6ZT3nwWf5fpeqvP3PzEVO5yZb8863K%2BzAuWFpHgR9gdlHiMOuD9G56iN9sYCg1%2BGw4nFIhKr0NYq6R7B5qHxPYruMAzyzK%2FTWOqz8y1kcUPQRSxtinOQHkmj3Vf%2BlmrRiup005rSNCwYmtax32WbAMpIJs1mhWLrJ6mkNJy%2BrHvqtLH1meFSL4ChBARgczInBQYo46cBzeWwpN50nK%2BYqHmly7WhRyqe3BGN1I%2Bbb%2BG1jkLSWeFCKyP6p9c7Dbbd4PVE2o9tKn8jgOIU6n%2FOrIpDlzEqoujW0hoZL90UUO06qHMNjqvM4GOqUB%2FU9eRpIPCEwtCMFYNUOBQvXqx16HG8MN892HEScDH1ie1pyyv%2Fh3Nrm%2FL4Ler5hgbGqICu0%2BoeoJNHXzulkZvCPVpltOSVoCclveJxtmuFLMd8p8dFk9ehlIIw0ta1ZdbGZn6nquE6fhWn7XavP90K%2FONHbxLNRQXWsk6MzTOpdnu7mC8cQdSLQw6EiBfRfIrN4HPiuPcxVrE9GayH8iUAJr9X87&X-Amz-Signature=f64c94d9dc690af037b71b1303e391f7a8f864d593e729fb7fbcecc53c596931&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

