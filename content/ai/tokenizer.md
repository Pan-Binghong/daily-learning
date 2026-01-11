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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWFRMOQ2%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T031006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQDpMFFahODzzP6q6EWDtiDivNUxLoWpnq2%2Fffani0iTawIhAIDKXmurdZCpUJSu70%2FeSZvvHCO2IXUKXz6KNgZi%2F7n6KogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgykjoweeZa0Rm%2FvmLwq3AOZZ8AgihSDzTtLAhzQXcofvhgbF3LlqLdcwAJoNz%2But0K9j21QDjKX%2BLvreOwUTFtMFlqBaQ65HDPE02k%2F%2Fb%2FculJiBc9eGTLjdo80DlZz08KHj%2FLxLGFnVj3xj7cz8zIf6SZNoCOLue8CTALTRT0%2FO1IInBrvry9Q53ZFKu6odjcMTCqDXR39GgBCdLOatcD4ivyy1scRmv7kcdF1uPVsAlMOYthGUJcSEZy0%2FtADWIJ%2BJfKI%2By0BOao6lprp%2F6eLfX0GdTjZugwy4fY74MaKwWBWg4a4vBT2jAHAA5XgXSieO%2FtBv93I7oNvOd6LRo2c4sUUASkg3FEFGe6DCsjAgrK8MwggOzqXHF6%2BDuwM2Q1Z%2FHpLi2%2BXXrvGmxnIPIdkW1s8lnLL9I8LI2bXd8ZT8drAACcynhpJsThs0KdsIV670BCQZVPJJ6%2BVjI6CDeB%2Bk4wGO2e3hPpK51PADA%2FcWdz0jdrpgylDQrclLMimrBZc93ZWAsk9yvsa2Uc0lWQKczr4ntnR7aIaxabcBUzGzjVjlrCx1%2FG7e61SRfWRfsXfQzEWXS73534hcn9d4p1biNJ2JKAL9sJRsJ%2BamiYMVXuqIYUIaTJtMsVCOs4GHaJbero94ncAbPvezTDC%2FovLBjqkAWDIBswiDNxd5i%2BrVn1LYdQJDVOkhobCMWaaRg1%2BQMMUQea7mWIU9OOFVMldyWPkX9wrVwt7bKtNFR3J1sc1V3hQh%2Bdn3R%2F3MNOzuMWy4xEU5DdxaXwp82q6%2Fu3oXuQ4F2o3XlzxcnO1%2FRFylDqencrXgVPRqaedcoTj3dwaPPCum3C8vsZ6%2Fd5EpscEv3TGtQPalk3QuogqS1U75XC11w4IrxRq&X-Amz-Signature=da984d1c8e9eda994a2b145f760b4796cab017a41f8106d3053b0f561b2ee9cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

