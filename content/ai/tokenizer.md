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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YAFGQMFZ%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIADBlsAtxDNNbJaIgax90hMyfSsEkTVVXR1R%2B48QZ0bFAiAbXelvCnqI7GNXBAM450fggfJ%2F8TJqeAP%2FzKhcC0m7USqIBAjd%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FxLEqWkoQnQSySQUKtwDv%2FcjmI8w3tBFpBtW%2F1CPJ%2BKLg1U2W%2BSig0MuYIV95%2B5wLEN9M9r8IoD%2BVwWMPWG0RiCRxq9DNDe1ozNt6h2x4hC%2FTfYqcFPABjzFPsmcOHFWDlmE%2B9QNDHLv6QPsdbMI%2Bm9NpkWySwUrdtVWKMFMQU1PJ49WrnH%2BNl8vl1eC5JM7L2HSRTP2asmc2j7yWQ6oz%2FsxJIEes4PONYhOiJOu6%2B0J8MyW4YDWICCBD9b3Zhpc9t5oITnVseJrffOmKzVrBt19U2nRM03jkaL9fS0c3YAewbf7%2BkkdS2K5DbjvhYKKrqk8vadSn%2FPkBeW9gGEXCwIlLiT7cIcKBrl%2FtOTfEEQkGUYPO2wVcwUSCZXWDbCw6RuTWpnjfjuGV9aBiE3tOaJUEFF%2FVk3CvobxTI57qI8gpyiidgIcOqx6a6Vpgo6XjSIl77Ida9xIi6D0KrvZsbLVed3WmEa%2FjaG377dAyXQ62gkN6Yc97sVzvtfYY46fKoSe92Ntpd292A5pDRAkRMW0Y7bSr16ec0cjtLZGC7LlJVsvcCId3UOidsgn5DxBHTRYLFuCGvFzmtwWZK87c5FTrQwZZlOsjp9mKXVCYC5X6HXxzOAcSsBPreIGAcnrfQUtf4rapC%2FqpxgwjffRzgY6pgGxS0KeyLzi%2BgQvcyttOTukTmJXV2QZmNFETdrVcr0NRUrgoJUr0bS4Shpv25bet%2FyvKKHfu0c3ERMiGesGeUjBj1qBO7CJjCYKpfde5ecKH86bkfXlMNstH26qeyZo7hjUHD9JkbJ0QL57dSVtEP4OAXr6g9AofW2yYB2EOQeEmFIbTUg8SRXWyJW3FczD7JqtiAJO%2BNUNYhqljnuqu%2FnJyoXIcZU6&X-Amz-Signature=5d11a6b6f1a80bc2901c4991e632ec6ec7bc3317b374a6a441cb4d8ab37643bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

