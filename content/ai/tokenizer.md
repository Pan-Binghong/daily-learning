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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MG2O6RV%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID9XcG838OLmZ1424o5JVw4KEoOiho8RzKdJ%2Behkz95QAiBJniM4rLEVd%2B%2Fzg7G%2Bvqe%2BgFbccLnOFtONojmyioyfZiqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGRprF60KGdwPt3OpKtwDF1cGFj%2FTZe8X2BJCivbCO1zk6SWWlX7g5TzwxD1M0REsQwfmJkywKQqfmHRWWAQ29QR9B8mKqVQ9yB5KVVhN68PeVniuhZ3G1K3pdIeyCsQ2lO%2B%2FYmb0ShL8NoKlcrysRFfUFVJKBSYlWOFiikx4YrOyF951zagmBvDAM7De0rfuDD1KL6rvdh4q4azWKIIFWYQioA26JWN1DYSa4ogjI0i5n3IJbIm2xaG4Vy5oayNEanPGSwqs5jQGUQinf3QhAkbsS%2FvdUYPaGnj%2BoQMWq1ZANxXlZwqlNr5XKBy2LAqJ9H9AA%2FiDuEWIhz60lSA8DBOMs1t8JHuO%2F5YucMNdgenpGMdLOPnEioW4QYAkgkT5p20jPKbVFQR8qZp2aaphOLYMdaT5YkSmgIDgszECLy0%2B9DL7kqqVCwMssSAKSBAiQMa66JFGZ8yT%2FdlCtEkf1JKYjuvHXn59dyDyafb8IXnDjcQZfmNGJIWwyYGLpm2bF7jwKnaIlapU1FChLpSWXvhAmllmOLljUiTPSxjmd20HMU8I0FV%2F2Y6uIL1bgpQXuYk7YL2%2F8lNcre6G%2Bx%2FGbIjCCWh4bJrBaekPazEXrAL%2BGQe5xQLCB2uuArqQvWxS6bJblmVkLbefyF4w8%2F3SyQY6pgF1z7BjhFkt9244hgh%2Fkl2zbMenKrcBF7YYEgzkfO%2Bo%2FT0iXeF60d%2BHYvVCZLs4T6H%2BqCsOflXGI5GfVc%2BGgrgK3Kz8PRdgQu6cEOHyVIm9hMp49%2FyBtlynnAoLltHE%2FIIepOkP3%2FNJFhcgf5UlRJIVLmzCPxI57YyXcFe3aec8p0IZvZA%2FmVu%2B3aiP175EgwugeWMfMgoYtaRcUu7BU1AmD08sqsIu&X-Amz-Signature=ac461deebe3e8146393ec516f09c143a424249755af65e66d9b7191d07b9f97e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

