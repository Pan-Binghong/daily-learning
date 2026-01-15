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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRQJ6V5O%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIAW3d1qm%2B84IIyox3jTVM5D%2FsH6k8lnT4qfVb3iTEHQYAiAEj8FgdN9%2F4h8qIFMxjLTxvPQFsDtptiMlGlDjlLjjZSr%2FAwgrEAAaDDYzNzQyMzE4MzgwNSIMw%2FVDZoSd3M8Mh%2FrdKtwDKzph8xPEI5aeEkNjTWsrI5AAeuCMdVmOprcFyTAST8NPZpJMgeTtLFu%2BfL2er%2B0xSZlPYRFzLv%2FPh0jbh6bj06diIUtxrV5Cobkr4b3t41edwM9I7Bm2re5of%2BpJfLKLJxN6Cs0pTLHMADTTOBWRUx0klJHGivnnwpXlq8odiHzyUllKdYp3LF2qhdG2cSSXABsIStuPVZYuAMIP7NVKdO2KbSfVMF%2FdAzs23MvKaPSj6E%2F7huPyvP4wMh0QrmwQHX%2FJcNu%2FT5yEIMbdF83mB3MAKzXgK4WTiVq4KI0h09TWWxlHyzJ6EmfTfWq2eLopxFcf%2FtoQy9nPg%2FqINCzfEu94pPpnPOjwLrsuisknLUqA7te7MuR2FUbKEC9QhRPZ6H%2BjAwdvwsFUs7qOrJgdh0nQCru%2BITH9uK3Kh4TzlySVjMMvs5A3GrWMRiwqwejpHqYvJ2roggDTDDrv43%2Fxrpn3a8SZJWLJg%2F2wIAlzCVRuxpBCpRpX1z2B5S450ESZ07xiRZTz8S8fmjW7U%2FZRp5E%2B7JJu3YkyG%2FkAtwah24kLi0r9q%2BAF8%2FY4HSyGKG66IVi1NOJC1qGqxhZpPYLdr7050vpuTLFFNAm5%2F%2FG%2BUh%2FN4DoqZYOCaErHp74woZyhywY6pgE9T%2BTEyJH5TkXb%2FaygG98taQDm%2BJIcWLtd4XkU7v9yJm3R5bsUkB55Bo%2BS8Ij8gasxgq85aYTUJVQHPzJ%2Fg6vFhRct9cNDyjUp7TO2S3QCxHW3XyCyyoWm7LWd%2FuPBc1oOpi%2F%2FuDx2Ycd8ls968%2F0%2Fpb9fdZoeXmVul1HVRl9pawpIVd7fr4%2B04O5vXWWdKGwABi5RioTDnCGWk0GVCLcWexMZYlCL&X-Amz-Signature=14c9749812f4caf1036b07c42f6a0b8298b94fb77ad5ac9301d084d366704217&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

