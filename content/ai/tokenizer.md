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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZW4L7P4M%2F20260321%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260321T032356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIDdR%2F461NvFq2bzqgcmV8PzJIWlcyo3yXd4P8seChbc1AiEAhbneJIVFqXEmqtdYVC72%2B0vXamb9s53bjkX6KZ5IHxgq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDMkRR32ikur%2BtXB7qCrcAyIAFovZDf8wQrtr0TUokNDLff6%2F%2BeXoBgVHxZmPjCisvJDYLN5Etde3PmXsI9U8O%2BbQ1NezlWodDjOJc0EvzS3IYp2m9y5yah0nb7qwHy18HtiTfPt36e4t3MCocWbkqigUzqIdIzedhnp8ZrLyiAEp1JiIozKEf9%2FHOpdFJKMSmRmJnN9Lan%2FvE%2F%2BD%2BlODIJahtLSoGDeFX20fZrwuDGpFcJfoQXSfaJFc%2BXus%2BPB7qI%2B6fKl%2FXRllC5HmoIy9RIPINKvTLniiPjbc3GgBRFtB2im%2Bad7vNr13Wi%2BTxSd%2Bk8kU5isIfuM%2Fr2FYDfUKRtQ4mVibpl9wUEZz8g0w0wsOO9sqcpU%2BQROJ5npze%2BaRdvQU%2FEUowscVSiu1aRodCXd%2B03nZUcuivzCuOq7%2BZX0Hdc%2FGflCCQmr%2FL5%2F4QTjjEYS%2F5wf84%2BnRfcQ1Qa5cUIwO7lEkBuxk2W8VfpReEpoltzGvEgFm%2B5sK6hz3VeHHYmxhwjnFBGJzzmmPnpIKKcuIAVH4zQ%2FlhJBInmwqr0roS12RB%2BZeh9HxxWpJOdTzPkDgjcm2ygddedhsBRn1Z7VeYH%2BI9Tq42JYprWCArV8MWy7u5i%2FqkYYpfDHSjQqUT9yef%2FDWOqM%2Bjjv7MNeP%2BM0GOqUB1cRSNEzWDeMRtSM8JvIbpM5T1nsSUllVij3TxkoVOAtuqMyDJhSDGkMiRuMgTdn3QmFzNjlRBlBTy6qIvHpOVZGk9Vk6wfPb6aE75VAsA2qF4Gsy%2F21JhDcQrnsilraTeYOK%2FCCPfhE7CR%2F9voW2XE2207U1fTNEdbCKO7120JRlNraXmTzsUNIT7vchu9sMkDPuo%2Fu7Z5tquwXJD0idRzsPN0GT&X-Amz-Signature=d046e3ad2baf3b150194157823fc8783013f45498807f8c301104ca1d9f1dceb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

