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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2ZY5PMI%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCsl%2B%2FlJnTTGz%2BWzfDQH%2F8FGHsH8NMjPB2PhWH%2BgkbMdwIhAJI%2FHjqaqyplrQWvBeyKM%2FA%2BcZFqFuxWzcWXUTsMubFxKv8DCHMQABoMNjM3NDIzMTgzODA1IgyD9EPmtYRSnHkV4%2Bwq3AP23gtNqF9t5dp7hlGLxym7Az9WDSRq5O3z0vgyz7b6AfgVQzBraP4NMZwvp1IvIjbTBmmCY02xXEEDXocrjWzlWgjxIOG5O7ttSmEPhByTkghH0R%2FwwHS38MH6FULgXIj8pY3KY63RW%2F3L4u5pIey6ADTcI3WM%2FKViK%2BQrp8fTrJxi62l86Isu01ZW1DcCB6eUiYQ4HB3XQUSdvsWOlWGCiBilWj6NkuKCdDCocuBTfXziPgfh9QXxSviiNKRTYsaK21YZYsyAQ1tn3K3SIyBMCV0Ik2ZnaelfHRnNY3Dw0IddEqMQjO8x13%2B66W%2FX0urw3%2FyDsVLqNu9FEt4rvVLAtswa2Mv66L0XXRKuiAwXtmfTpkhVNKEXBF2uM%2B%2Btoo4y4cKL5sRtcW%2FGPKpAiNnzl5HyKKUkMTZPnCs71T1qjzo6BzB40VrIc7PhM4PLxe2ltJpFrQlD1s8mZUzUuFB3cWVVbuFQ4uVMdA98smW9b29ZsDi4xZJXbblxhggioas7HWKIY%2B71J5K313rBewy%2Bdjkh4NWtIaaraxuOdZ0bxdxBD793SmcphHv0IYtsOx9I8P2iRMQHZ4yihe%2F379Bbk2HYBPbRxxb3P8l1BeG0VsmN%2BGFy4LgSaPPA3jC6gbHLBjqkAehV3tvZngEY5J5OVo66AYPa9DeucdugTejiC77usv7Oz1iP1saAQ7MH8dI32sHtTEMigrLg9SRTc8GThCiy6%2FmjiVmri2pg6iDOlOHz5%2BfpqNn%2FS7FeQcha9%2B5d3%2FQM2IVGIpKzKgQbc9%2F%2F9GY0Wx%2Fcyl%2F%2FeP5LJPnXGrsuORLwMtinnugtTFAiixDLHvYmAEYtsvX43hgnuVGq7RGPecO06ITo&X-Amz-Signature=7bde2ad4df8648b7a818feb10167aedcaaf7a7f7d260528ab9c4ba649619836f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

