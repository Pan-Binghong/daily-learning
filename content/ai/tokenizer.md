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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNMEDZU3%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCIEnH%2Bt3dZaGz79MEVYpKNjSRs4Yo%2FfNSIfQrX7yhf9tWAiAxVBbxIAr4QltFspW9ztsrNWaWTFF9z67EyNiQzZqlLiqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuj%2BJPySfcdnrL2qFKtwDq%2FdKIaG%2FXEc9zVDE0cYPd%2FG50mPYrpaV9Vviu%2BbiOzmPNthT%2BsAEEV3Ga967C9GDtwBbkzVRN8JRXtwh1j9XpmDjqDZHDYpbyxiucHqY1JR6aLAjgWkhC6P1yDbwLtvAs480xdWUnlM2Iukb%2BQ%2FKsyQDwMY0qpPY%2BHxMUuUN2%2BvAazjkvjtj3nZucqtAZhXOFUNgMqxU3j%2FbmIOJ0f1M7%2B7c1gVrIJxjUWTf1h%2B1CmV9Wr7tEqPf7%2BdoWfGxTG2GpFJ3kNjLTx2PydjpBxNZo7rWgOmtagfLeq7dOi5oA4VA1gFZ29ENz60%2FcKMpQJ3oJ%2BzWGV9Rc0wl6c5wX6EMz9rpTy%2B6tJU2kkBnOsND75CC7LmTvRSe95t0MFYccBsJTuufTJZ0CD9ihRNO5zOPe5iU9sQJs3D40mXmkEqzddAvpjBT%2FqWl%2B9KZ7JKbSzoFtMRJ4VNoNF1mQEy3TyR2xuk9wLJPFpfPd31wgYVw4lRdy8GJXhqkyA0hF35ispyPonH3oR4PA2Po5iQHa8f%2FfPVj%2BFVzVJ6%2Fh63RyBaHLeLjR25xe8upiZAqG5CA2aIAvKx3sJrLj1RftT36UFW2N9BHfk27xhCZbb%2B7llSpYP%2FeCg4KDNSKoSIkoH4wpa%2FLywY6pgHNo%2FjmEDMLjBWD1KLj768V%2B%2FMy9OYlnWpI7V9lntVWPXV42OlZHnCFEYtjX55XeMcrdN%2FCT1TzrNYPAlBDEZzTjassAiLp%2Fl3vQOzE3K1xI%2BVLCDAeW77eqbqqKI6G6hyaMV%2BDCEUhvrmEmF0kgRbaSTbg9%2FVVOs3suB0%2BL25rBIKhiifnr%2F98JatMMViCMl6VK1oFqg%2BQB1nVXz2UXa71d9G2jBIF&X-Amz-Signature=0950c839afd4743d831bc5e895861c028f186b535d10b5a7725589565dc78dd9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

