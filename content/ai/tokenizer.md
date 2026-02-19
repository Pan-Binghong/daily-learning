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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTI2M6EM%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T033932Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAe76%2BDB%2B5gmwCQqX4uHESdS%2BqsTvmXi0SvoAViPEfGnAiAT%2BufigxF8MaRBjso9msmv2gHjuUrxZtkuDLdGCYMuUCr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIME3JU236jzogOHqWdKtwDqQa71xCSBrGLQlYZ4sM2TMqrMuixec7lbtpTLBcgf0KFLQ9vM3Tbs8HSglbZvRlOjB801%2FXkJCSlPJiRJ26RGhHYIId4svmWydUAK95PkbQfbyljgc%2Brt%2B9PGBc0da3%2Fvwe1RfRzVdTlEoyqgaPRAhVh1WwsdQhZwE3kAiBg%2BZiECh9vgvCtPot17etnMRW55VCF4hNfr9mUk0ZPZo4aJ%2FbsXAwwuTxlxkCgz928rMQ3uJuBaZOKEbgZ85ySVuv6NetJTXYnifHmqnluj9IhCswGKL0aXoTTarOY%2B3xPFe74roRYoJ9mlo7Io%2FBmtCyNQXtwpJdH1Q0yRgkf%2FVII8yrvMzD%2FJYs%2B5Y5FCBn%2FE3I5A186COv4HNoJkzR4IhQoPwbT0wWrQhaXcG9GvewFa7kyn%2FrCwlnsSd%2Bc1jLwTgm7Fl8DFFN6ozbvd9ogLiU%2FuD8sn%2FZKIbXI49esJUaiEHjZeMEWPylbTv3nIDIhA73IaH9yq4jjk4mWspWdhXOVKL5pDpvtIgCTlzPw8NmqOACmga9MnBHP2WCIbMWAfY22I4qr7ORU1YXNvoESDBwSJMYNR9nWd6dwOmZzWzUygfb9AXFMzoC25C%2BiFmSm%2Bz4E7I07yJYO8BBKdJ8ws%2FHZzAY6pgHfoPtPmq2k0nvpt80AgYXUeJVZBmdi42H%2BypMRASuEBtkEZDbS1q2zt2qSUlSmL2suTxlKhIlk4hLxS7ub0AA0wP4xtwa41Xf88DvM%2B0dzosMMqTj%2FFD5OhGGIBmZ358yEIXjqKshnuxYvezAoAQKxVyibWPuzqAlbcN15ZngFWfOvQnrwTqH1GVeH2Ud1SVTRHizQpBlObCZPvXZ1In2qgocDwzcV&X-Amz-Signature=822010fecdabfececc1b00e6a8b86d7da6dc7c15e0c64cfea0407e2965addd0a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

