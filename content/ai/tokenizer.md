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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFCVICQA%2F20251111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251111T024444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIHJd5d1a5iZpkd%2FPCOpSl5Uf%2FnHS6oh5lOah0JUX2vPjAiEA27NrkfumWaGDjj9ud2KKNj3lRUfKdPhikfLCOcc9wIcq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDPW5ozjI9pe106TIRCrcA3t%2BPhf3vgwli%2B6RlQ%2FrDqBvymy7AIwh2lZCZlPuM%2F40zuHwe7ZOEw2N6dyAARnMxVQg1QqTvE3tqdwARXW%2BsTf9HSkwUuzR9voBZhGMLL9ZY5i7jZYG9cda%2FZ2DQ9eSaKw%2Fb7LltyHX1n1RW9FWyhsps1ux%2Baw4F7eliQgJYhhU33yJLjdLwTXDmki95FKz%2B75K9ZpmdhWxixl9dXYnnfUZnL0EYx9K1LDpycQcV%2Bv7G63X3P7rvpcrYrQtoIsdrcGXbh61ngMoslrP0yBWgjTvhRtiuT%2FgI17mgHMKYMSY2OqKA5ChmreV7JvKYXpSbDOHYEyTsB70WVSEOf%2Fdv8xGKWvWiZRUUwFkjEL7rWc7x9cjO0AQDyyEpKZl0TyIqN6ddgCtMQOb740KyrQGRu%2BbqGFVgF%2Bg2D7wD7A10xZN18VcoIS51mE3WTJtQzMZvNBJNGRUkvMKiviANaTgt2RWGPC6UDAscV2yq0z9y4SjUJVZbUWumIegspzgYQQCsV%2FaT8Pxe0gABjH3uCnfVoz4X4b6kPa20ienofhIn6Fy9kMXg%2FS90X6BhzDVyueuLwgrz%2FuFkadqyrhsOUaP7hu%2FMn4J8j4oSBDxZaN9GkwOg3EOCfc4Vt6QgpgAMPG%2BysgGOqUBXHhhhB2O3gaWV4pAN%2BshD2FEELpIkHK7KdsdNeWpxPGELih88bISZ7GbddzNCSnrPrImdivSY%2FB5aT6ZL0Q7TVqfIuE4YCtZtGqMGUi3jrYZ1JHnxECxas%2F9ePTMLh%2B63RgZz2WJbZifowfkeQu8WgX%2BkgIDq4uSxIReOMwvdYV0i815wi5C9%2BAJEOT0z4zrG8dIDGUT4tt6QTCRqYX1CbFI9bmR&X-Amz-Signature=49afc279124759ff35f7bd701e1d7a62b40eef894afa36d2fd02ecbb7d1f7c1e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

