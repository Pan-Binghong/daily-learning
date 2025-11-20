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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZS46UNCZ%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJIMEYCIQDW0UAlzdHj%2FwFsSOFhenS5PVOCnx5IOiLvzjVgwTULMAIhAJbwgRcX%2BpS7Q2106y0TEopted570og9S%2FMKD%2BEUrV3rKogECOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyC2HsXxEvoVeyQYvsq3APy0cZLWVVQ9NBTy3YBMKW%2B0vFaJcZXBHaGxBk%2FgoL%2F3hETtoCQy8dbgvUYfvlReDTubh%2FwFBzvpS6iDJ1j395L%2BwJevziHVx2yp6tBQq%2FdwKdb%2F5KvWeHdm4UTWR3RZzjg45FgJdBFha8ewADGcd3tLGNs3stlcXAt%2FgA1jaiyeUFkJUBJJfbeJ6twmQMnDCdLRtl5zE5jGYx2KHI1SM4wsVknRmtUhStLGeSDveHKWEotTiGXehCb6oZmekzWympL7cpCES9RpuQLaPizoi5kghA9%2B52L%2FZGzvmmUZDyHETx4k4fAGEZwRaTs%2BAsAZf4qX10C0R6h6fZC%2FQVMt6RNtnueO%2BZq7BUhWCKw7JQuOAkVpjwItOVDBK7aKrQED1VsDlBHQQ4hIgc8kGoJ%2F6Sr8LrRKCVOQq3kdzoD7oId19vsV%2B8L6kO24tpf1ca%2FfeZ1oj6T%2FzmwMpZrK7iVNOdqwlranhJEtkjyALLDTSx35afYzPVMry%2FuIGV3O9f2GEFfjsFl6RTlaHp%2B%2BPsitmg401sVOar25qO2ao25hPT%2BhPqVKACgAVf0uEuFh4DmhxNvYjpzQkOXdPZQwbmp8E1ivKiYQnWfYIblkIftoVjXW9EBM01mZSJrrZnhUzCB6%2FnIBjqkAWOn3Gb1lf60lIDOijDr4ODt7ennfACB4ynKeoR%2FeYssyYUvU6Uc1wZ9LlnlTQZWGpdOrZ9UO1gISFuDBzrjyb4914letm1jOhq8H%2BIIyG2kzXl9%2Fzvq4KVpCQzYeAuAJbGmh0awexNTlrNO4Z3qAOIV5yr23dDyLYQtg7UJKHf05eftXP7AvOQAFub3WAo1cFmSMowYgS%2BXcJBSHlV2kU2lYviS&X-Amz-Signature=b1286cac23a177859fc9006b242d4db6914b0b239f234ef8b6c56a2760947161&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

