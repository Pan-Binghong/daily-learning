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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VNLSNBAO%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T030934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDvR8I7XFmtRpUyo3ZOgMIanD14G8ZC%2FXZTcYLGOzCp4QIhAMy1cS9vcUQhhGUMKHNmtnOXYWvi9bWZeIBJseC38IXQKogECNv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyBAMrOz1A1Md8Lj2Mq3AP7CxlCWQpBwwOZ1f9cDSG8MbGTMvBcPSQ18hEWMqHI%2BKxHO0lB8W0f90d8dO2OJP9mwJacLURwb8Q3gpWwe0ihCnfrcFXk%2FbEBlf7p%2FPguMtvFbBO6vPreCETRvLz%2Fg1DxWSjs%2BeRgqVK%2BkN1c%2FbtKhFNT2%2Fopaf9KMeRgjB1Ja7s9SbYAwP7u%2By9CDNrv%2F1iHjYhcSroh5GSiwqk7Fk1vsVQKF0BQzpTg%2BVsoUZETYO62Q29UnHPoLc5WC0MrY5I6B4%2FWSH%2FtEBv9SyS%2BIqKJEfP1jSyB3Oy%2BK8Ci%2BuVl3fw%2FBXgUWs%2B9aGjjMPgdzGoH%2Fn3RLrV7AO0o3i%2Frl6c%2FyE5qUN53qFlqHl%2By9TqZmoW5EM6u3fVilLa9VtvFq0rO7WtYYxmQYp%2FvRI%2FUGc87s3gq4MuZaYB%2B2eslFMV8aD6KZ2orLyykid14aJI57e4YJLX2HGVE72zOhghfUimz9foSl%2BNuW0NSzBvXbJ%2FkJuvFOxmBJ%2BtDY6hwTJ1BtXLz2MPynId%2FfT4hRuoOgeEUA5VGhZlKu7CTHXNPtk81nUei2ZQniJvMPsBf5pHPCBuQ82ce%2BtFoVhjXOL%2FzJkcEH08yl8BO%2FekUjioy2HJuZBphyrZ8hw%2B8B7zSMDC9ptfKBjqkAVmeEyJxgEQ8r4JDZAlOi43nMr99ly52blmGc3RuWi3SvEdQRpqA4kbrPFmlEYGxdWYBrl672v3XkpEHyIsTQo8O%2Ff%2BhpQhQ3uyjQqyzfh7PLny7TxFDhosQoe3GaXsAgCFSzt1KbMR1pKaP1n30Roxj5pqWFYi3Q8PN1dRqoJoZKz%2BN7BeAYf%2Fwy5UnIK4e82olrTBC1beBErJfr%2BHouPf5r9pS&X-Amz-Signature=d400473c21d4b6c33829ff96f5603440ef450e099e31d3d95b3d2af86c0dde8e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

