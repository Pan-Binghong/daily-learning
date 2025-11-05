---
title: Tokenizer
date: '2025-01-13T02:54:00.000Z'
lastmod: '2025-01-14T07:52:00.000Z'
draft: false
标签:
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVJFNPGL%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100711Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE1yBGS6JMDJYsIX3BOMmfFw%2BJJgLueZbhhK77zSGE3%2BAiEA6MJ8ogVmUwbZ1%2Bel5nz5G7mlgW2V3Wm%2FQubbi6kcUo8qiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFYGUOhfR8iuSbgklSrcA7AAmQwDYoI9yTZB39Hks8VAlqgxTDfRn5q%2BRRodZpDEh6pFvNgShUKYgJExVIOGDfRkgPQhtzvhNHQbuwZSzs%2F5C6oDO3cjTiudgS7K8rIm8xPY1A6u%2FAXIWTMVhdhREz97sVa%2BL3KsA58ztvddFQEBduS1zZbMfRVCIy8XaAHDw75xhj%2FW9k7HuyRhIkLKOB9c7IZYt%2F6fmWHfysJyr8AFOYK%2FnKL2iQI58Ste9KpdwLjABiFVxt1rnDJSfC4n89g0KP5PFcdfQgm4ax9c0%2BR%2FsPCV%2BhWgz%2FOPazwaXEjr7cBNvldbawrFeJAE0soC%2Fp%2FdBq5SlTc7p7V0L9u3STaH94sVXV25BY2Vt%2BY3GKFn0aGhIBv0LaDWLdEEh56QGlglbW725UYoXCFw7zKDikZrKveUKwZTNx1VoeAhwsMfopi5rsVNOB81ZKvYvSk1Ux5CoqbdgNzOZDFIhGWIA7unhP9oros3%2F462hDmYqAZL0KRZHZ6m%2FKz%2BKS3h%2BsJAjVTnCSIAxRJO97KWVdiXzsSECRgZPJh3rZyw0fXYTocznKyMOjbEF64NdRr1ZQPy2qjXIvhKZTeCqwdMmUIToRJBbp2GFfwKzZmZtMx4fjA5RV%2BX7njL1uCFglVIMMKirMgGOqUBOFnFDVvURLOoFiz4iLOLAVri2roWc1z%2B%2FIwrSfbUWO0WIJj7jV4xHHE%2FC8aEh41laKW%2Bfzz9Dbvbyk76tobc0rrzmhXJAHm9TBDLYtxO%2FbxZ8MWiRCGPAleFjO4o6G6JqvKJz3EhSJGIfS0oWJzDPOiOV8gStm%2FrqrUWs8cgjKdHcivQuu3nsd6%2FwuklkyO7zwRH0TOM6iZlm6Ye7d%2FGMSx8GZVq&X-Amz-Signature=cd72c991d2862e708b478debc45599a5b506151aa9b1230c2ef166aa5511b5ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

