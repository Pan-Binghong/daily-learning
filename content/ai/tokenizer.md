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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46653T6NS6W%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCpP%2Bt4VHeW6VuaRMivtXfnpgxUr2XwLwVi9coUQODpkwIgHPiNFUeQaZX4%2Fy4Q2KetIUVuKGnydMPEvqDwgHqj0oIqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPBw%2BOk56gyMTNmlBSrcA4KzZof%2F8%2F2OAfTeIrP7sa5cCYonfrgtYsaeCVzOtBKVw66V4mnvY0bY%2BNOhOyX1o%2FBSvlk%2FBNFX4RaVOFBsrHhsojJpEbe5ool02e8m4X6RBMK09bo02Zu8QyTx2immS4%2FlhvsB0VPL1LkQVdE%2B%2BrpqUFo1xT4MJIei0puFukyN1yDlMM%2BvxeCSi7s10nilipns4RAvEQi6NC%2FtogFw4uBRM1tVSgWvJiMqLVXD9LZgUK0AlrZGyEYkoNeSxyCu%2B2Or%2B0hGkKXBPGlX5mZBWgqaF2aT1dgddkjd93Hj8pFnBrE6gjfluRPvQZJc1oDG37tzuKh1AaTE8Z3MXFgf3C1Bfnjp%2FGjREc5qqb2TFID4nfsovewWciRxylJCjl0LibY2VfLt%2ByvEQOEIayBL3%2BZkcwn3wPKoRxEpzmWAHaDvdLa8MYToavzGd5d4L6DOgcfSWACvtmaRLPUpq%2FMAKpPMzkzCgRZd0xbUSv1eekEDn%2FyGUI6RU4nLaWFuDepzvuucJuY6W8dyFgWocTvTdF6EYDheq%2BybQV5JEemmhRlEJCnmY%2BGivYrugGR%2Fls%2BnrvJwW%2FhcXKqsQGl9ulxIpXhY9QfLyhtcYFXRPOcB24FD08tg4a2Ca7WUlBroMO3YwMsGOqUBmu18O9GwmRq17nGwCtj5UsEbeI8tb1f%2FMPdIt47hpQc7Vuv%2FZJdD7ZurIWPqTzjpU7x48b2I%2FiixRFDXTDMegmWQq5GV0eLa2TMzMTQEaAlGMq%2F69KDMJ4MbSrRvS6TbSSvNBhRDh4%2B7MhyeragEnEd1og57l7cIYvbiJvVMC%2F2O04DcEIP3twsMTAQZ8UJQTmhcAYWleE8YsrG25MENiJPGqID%2F&X-Amz-Signature=f01827f4f95975ffc7fda3f129490b500acc15dbba09effc49f7223f1a294a83&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

