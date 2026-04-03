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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WHRLO3EA%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCaOOIiIeSwWqqBlVxDxnJCXAUQiTTBdSAV%2BAyxGE7nzwIgANrLSA414%2BSQQrjSm9i8vGdYM4ax6bIoXtNZTZpcoQcq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDHiqmPe1pMnN%2FZLeTSrcA%2FU9PXgdbLPjR8u76tDN9DvZYRPIt4ZJA45C9zZnEIFuhzcPCJLhYZtUqUHmIoiMmMs%2B2IO1c3HDN24GAgFXMTIEf2T5Um6FRq8rjNMC%2FvgBeCjC2Zw8zbJ1w5pqJHybwgqdZcCQwBMNEcx9De9nMF1zHUZy451iVUNJVmCHpQAPL6gvPBf0PTsebmTf6gel%2F%2Fd18cp5JuZTI17grYcOcUPzbn0xG4C6pJlm4Og3qqel2ibaHgQPL%2FlAebXK3oDN3RQtRMSiBdtnXDahZh%2FgSZwTSbpMHl83IzKoK44I9Sl6ddGWjbrfIPg6BxcO74EAjHVkyrHjQkT%2B6dL4GIqdn4kdvcTYKYJspwNfv02DC8jnHHfoS%2Fff5lUGrrAjvEGp6gWopOIFz6%2B9dys%2B8wrDq0RctpB72EUy2%2B%2FDiunTeXuPZU2mJIRoNt1UEuqmKsTLU8sadbQdAUoGOLgCSvHl0ye9sefEwi5MY5kbQfJBHV4nTWdpLrvY82at3ysr6nnBBALtIzGxY%2Fuf5ObQT%2FZUWt0NrbR%2FKuExnALHahrtw6C4NzwQ2z9LHYlESC%2FRqbYyzFPWv31hNm3MERMN001bEIbawJ6KwiOmT9JJnsl23XYy3unRrUxxZGZsxzStMMSsvc4GOqUBQMqHkahahG6Vc7%2BIrAPh5Sba4BqSrVdmiFtVM%2FUsjv3EuNqcSBDd4BM%2BYc5%2FPc8Uyc83yMM%2F9zgHV9F0hIza6XoEc56csqOop9GabH46ZzXzQ8Ld%2FZqb5CTcElVuvvSryOu%2FCeTvzZvbfzlKZ1Xh65%2BxS6%2FOHLZMXnnCx8NqYE9jza2oZQLU9%2Feiawk0Y%2FyiMaltQMp2KcNJQ1BWBPJoTJsRAmix&X-Amz-Signature=0025bb3ec69ec0dd837943ae154ab9b8aa6c0c8482a39556332ea95a4344aa0b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

