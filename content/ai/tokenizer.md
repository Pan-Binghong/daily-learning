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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665M2I4BQ%2F20260310%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260310T032751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCIA2oyX8NF2ilXv7Vms1ZrETJhKLOljsrqOwfGsjfknRiAiBKYLmNePgH8tV8ao0vbDRwIYN2P47nXPT3AYuMduWAKyr%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMDahpBFvmyr3JpGr%2BKtwDQpFOmgOd9We%2BT1fwbq5mqC8onT3a%2BMG6H5kCPAZS4%2Fy0gtodCfIZqjmG5vBK1Dn2nq4jo0VAAYm4yyEzUENFlV%2BNOceFwWj9WqBlqVlvWXNqwOvIabE9Z%2BPjDv9GtDJZODo3lpLJhtfv99B19dwE8Fe6%2B9b8Tm1En9qVtUcaE2MjmrjIonGtWmTTfwTfsXxt2hRQ8Mmx2XpmQu6UFxesCA5dDkDn2yz%2F7U3ZBfLNHzu6f1Q31678Zso0CSMdpWPfc5%2Fn%2BpAIahUHNM%2BAC1SCVEOi50edWdSVbiOnuawMOlZUNtxuhJRjq%2FLv1GOVYsHeiyqg2a8EaCv%2BHT8wSTvGymPeq3bMr32PukfUXiQ79zumefuen1y2mq8bupyDgkAlvtGe8kVO6jpADQDq9Yql%2FuFZqKxQqTDaQu8k1EJ9QSjKrdBzCUOX1DaFB7yZnLpqnW1aKzPj9dh9Ydu9JMNeIOijijIPHuQ%2F2WPJlFu7GPVF%2FEjcZO5ytXEPBCRpYA7%2FFPjyad5Tr9yqJw1jsyWN1%2BiKWt%2FIRktDZi%2BcWMImLy9BpNRK9eAH%2FmRX03gEeIMgGjyjI2%2FhOi%2FPFVccWY76NQAxKwYLh74SEWWIagEmA6lpVichKL83cbqv1kMw6o%2B%2BzQY6pgEIrSAonfECWnU8pspg4s4EJj0RAoEUj3ZmksdlLehPUQcP58258Hj2HGTAhut%2BX95K9iMEBRzBGRqPM424YcSKe0Ps4X%2BVLBfcLH0ipiGdShEv1s3dSJaBhEbYfOFMlkZe40eLkGalwPU8f%2B1Dnl7SjrB6eDWJNUk8E%2F3gPmRrBW0Wf%2BdBuKw1vPvyk8ZGf1AR796dwDfe6I%2FHzKKRYTR4S4dgfsdP&X-Amz-Signature=35aedb377ec4ec7fd820ba535034a5ad1cd9c9a6673f8534d54fcba8d28d03f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

