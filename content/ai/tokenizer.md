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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QXXGGEC%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFsa6sU%2BKe3TnJv3AfisVwkV1DR0IdDSenHTGJv5PScfAiEAjLoA46MDlsWHM8Lr9rBmCphApMN3LUTotYsBhCdQiXMqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKQ1LyKKO8VfsPAi%2ByrcA5typG4zb9kiJ8xnMNEFQSSyQjc2rYxm4omDkZ2TJ63NBFHeoAbA1XtI1ZrRWAc6LrpFw0ol8qPVXff62JfexxRRqZWGNFBaqv%2BooqIafYMg%2FL2peBf21U41Amzx8%2B%2FOQtZGBxjbZ5NNCCY5l0th2eo8brFQe03GhBuznrIdcWIcFCdyrd33Q24r4RaXGb7hMNF3uLqeVtA700KZh8wWlpipzWvprxD5v%2FJfCvULjcCwsXjifBdCkE4FKOJNp8uKarpcgDHWW3%2FOEaKNGcfSCyHtJzbRJwXJnBwDOire9LnyKJ4etqbxuu0rCqLPgpucNSrZ6HMUp37UR%2BS1XkqdJqpAJEXYEPwpw7ZT%2Fy5rLkxuqGvaYMMrIVh%2F6JntF74tvHMlvJnnbFXUdebWbet3uUyasQYhwv3n8saohPyqPvy%2F9IFpB7ZOU2XZNbcTUmmSlWAz47p5wWO5%2BRv6oZTZynA91jzgwIQ67o4fN1Kx4lrgKzbt3jKvAxQeebLJu%2F1cSyP1vgz1VBD1Sw%2B36cRpkQ%2Buf60jbHSAnEHGhvQV5S6Dp60TowmEtlyqez2kkNHBdopSRyYsKhp2TOXXu8L6nCK8cucuX8AJT8zKiQik2iapehy8xa85EPVYlYzqMNWix84GOqUBJ%2Ff6RFQPDyv0xFRHyQ7So7IGhFDMs8oIGVVKffLnGMpW3zTMlPYZxVmJnkqK53tztwyERkDZDIlUPan47UPe37Sw%2BEaUtrdXUvHQZG8lINA2ipoGWtXePtD6tppwoj5Tinb23rIrjVTlfWjaz575jMDMxU2Y584lNqyMcRCFb%2B1NkTsZnCXmPTLkoSi7hn3%2FoswNVgPalSkPF7OkDZIB%2FoL5t9Y8&X-Amz-Signature=54173181730ec4c102d33be1c09bfabb9f03c0564b2def3219c9db09ad3c241e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

