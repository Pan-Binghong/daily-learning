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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RS33HEST%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T041621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIFYS8%2BmotA3E59jXZ4sk2F5jmCLGEMk9Ulu9T9hNi6QUAiBmQrpOrOhzkt4um4J%2BfwipPVmx3s8XN4t7%2BGg%2F1lgnTiqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZgGObp5Mde6mh857KtwD8mcvQrRkJQrfXm3ZpBJJAqTu9NuUxc6MSM143HiqQDebcpzd6dOfvKd0nkd1zec1bvh8QGpodvoQs7C7faLiRxqNyJc2aNcteJLebjbyyHOtLgrOkOtgORNIjF3K9tevb3pNAr0MKi0QrmH8Q8UiHiVBAR0kzbRNSs8EgPi%2F4cyb11Nt58HOpcq884E1N3ec8byWG5T%2B3FNlvSkA2m6YPV7B%2FJfG95VVFoXN3yQ3Uum0%2BqKjYvh5ivpqdBcYB5ZMPV53gbYfy033UHtR92c0Yg%2BkOmCXAacvyV7m%2B1%2Bza2m2iVyqzcMCnzwjoEbzw5wvEaLNRDKWmX%2BBxTD7Fn4qKJMDmMoc0Xo0pU12tMe6z7WfAZNsJ2HeqF0iZG64g%2FqQtCvjg6OJVcYoqokxxxKwMylTHY3TbBbaLxfGISyw70AJASd35CFf9tTjEmzACilc56NURnDMglQNXud4T1sIb5qi3XTarygf%2FCYwTMFFkvOMDxMIDh48ohwzPG%2BKg%2FXWpeZlcdIIHY43TVkmQPa2gNcxsKqK6PildTOAUXZN2fUUMXZAe8b47shPSYynu6xFr0ZmkJmxwwHpyNFQiqf7KdaIyg2H9oGiv7ugGLrBL32MR3JncmRnKyPeAEEwnt2QzwY6pgHjqgtjV3vesKOWN6UWcoFbhVmbGBq684b%2FwP7v0wrQA16lylvIn1WjjSEjByy04uOPm%2BhAv8ezFz39iYRVsFfoeoZFSEbge5hy3ZGecatRWdA96U7ahVZTQophrQUYpMgLbUWAUWAULWANfmfJAOH48LH5ds0hgsb%2FGl2oO4uqdo4JHS8DUJSUv7sV4Qq729jXS%2FIMjsKHl%2Fm4uVwTX1ZOzmFBc6Z5&X-Amz-Signature=9e4363a1f2d1ca68817b44d38262fff151f527f9b9432ad09cbd5af165af6a2a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

