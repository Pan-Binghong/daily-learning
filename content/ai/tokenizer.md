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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3T4TTHW%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T033948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCTUXbjcHZwy%2BnvPBFuJ7EyayfyI4myLfUSk%2FBmrKszagIgWCQi%2FLbT%2BGQORVKGdR%2FYBDyMGylJ3WUiI2eULakAW6MqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCnJTDxJPDuGuh8O1SrcA2Fp5bhbj0fA0tVpES5%2FXjT%2B%2BJicVtFQGfY4AReh846eGWFE%2BOExSzDC3niKntbHkTsU1YSWjRGUi4rrpfzhDqlh5VDXJbmr70%2B5qjU8K1hOHm2mbszp%2Bg5tnbYjwPpzTn6%2BRMVvOe8R3daKP%2FwA7gx647Y%2BGu%2FAmON93f6gF72IHg8b5w4qD17w4Rdxc9pXw7Fym03YUbIMZpW644XBRLvKdW4LxccJz1H8EBCJD2gDc26uhLV887NE8c%2B44jqy9tONdxq%2F0o9A%2BSPlPZq%2FVEF1l6w9qCjz6IjzUpiG6rBD1wtKXLfj7rWSfYbK3gB9nkT07FNKOPldp4cSkX3qfsF02TyZMLxP6I0c0WulsULWJf1uri1gRzbAA%2FGuk6iiHoUfVmrxMa26KX44QH5NBreormRdzeknYY%2FScZdYIByYihG8cofCxFAAI4yKghn9ZnuBdfGLwJFraenBA6sHj6e1LgWslEcvZkvvcvpEIvAtA94J8QZtJXkag0Hqa8dHaU9nBvM75T41WiNnuHcV4C%2Bl8GAqvOxOx1erRWOUdcnpOV0mVkx84%2FKdhPIHG8NUDl94fel0GNJAOc45UTW4UzJEzvSFVO5yaX3D4qPy3aMX6KJ5TO2RAcCDH%2BLQMJ2ljc4GOqUBxJlM0E1mLqZ02%2BYFgybzOAs7vy%2FAUlo%2B9ilVBlAqTrFdf%2FiN9o%2BhS1f%2F4XXToqjcJ%2BieOHJ%2B9XqZurxB5vm6CCgkW9P8t3JI8Zx%2BVy4r1JjBMuh2JSyRTR%2FRkPktp32NP%2FMaaBKb0w0UYzNGpdy6bSaaxYWojf6H4yQHmwnpohukhlV228jErRPozXpD7NbOIKTFX3CLdrNMAwIuLmmU2HYqBPMs&X-Amz-Signature=a69b743afea9496f1c6aafba47005cf38ff566e59fb9c6c9708eaba395d1ca0b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

