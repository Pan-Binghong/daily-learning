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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662MZMM43U%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEhGPhIFqNa7kSX0djqIVeI9mBg%2BEoH0E0ujkjcKLqj4AiEA6OZx%2FWoctWo9fYkFn1opjqTC4EeD2aBj7aysekciC9oqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCX0V2Y30J8jBHF%2BHCrcA1xaP9AXywWuLw17C7tWchF7CGeP5258e5kfzS9AN35JNFoGHwJ37O6Rshy%2B%2Fb4JSzO3bnb4ZChEPS%2FW6tsGyWzCgjGTjkJMBfiOjMnv19RBHQISMzVh7zL7Q9sdRv%2BdZBkAgv2S5W4bi9sVmeliCc9YE0ooGmDuq4nv7KV4f75mbZlHSLKDKn5BnSeAerRoHm2yRMLxv1QFxJCZtxLBTAxYPnePLGEGf56L%2FL6Tw8bg1dBMgP2VwJ1fqvQ8wzlaU0nnZaA0U8q9%2FRg28ibpMDIlZMUwAsZBU8qHt5%2BN3vGLOE6%2F2iSQ8NxcPiFpHkCPh9P0%2BE5z8ynnkj3V0NGnK7T2fLGqktZeR1b7iccajGMyPsL1KRhiFxFHOcSgBgs8V9hD78o%2BmXJcmUUIhzWU2wVYKrBdSFI4wogi7JywSN1NB4h6F2iXus%2F8gBAG38zuYvTk3tQ9b%2B7qLZFHHJg1p1O9pcpN%2Bd0XhhOJD5i0%2FAKgsiv9ZPwmXk9C%2F36FJuari18RlIuVZMBm0BDHcVGv0fs8LaSAErk4YRRlh52ot5cVPhG7AD2G76RtDJco0qW8QvB04Ro7MUECLUB3xIYHHRtiurjvhTa8xnNDrdCsJytEEjXL%2Fbsruz9wlJGdMMaS%2B8sGOqUBzoIQDqpfyYfRo0PXv7VsoLa%2FjSQaRHpprM9VnBxn9HLZno8KVUplZhvTr%2F%2BD%2Bw2tu2vUUxyVLCoVdAPQfEcI952SSdufoYzDH710Sw5en4LISe8bJIEV8LC8hyu0M8%2FOlqAWziOa4qbieGI6QVi2MUq3ZKK2RCd%2FdCnvfa1V6%2Fw4DfM769uwPn4K6PtLgdJXhd8Bki8fxUzZ9V6eKxOnbKKozQ7K&X-Amz-Signature=6589d45cb8bb116a3d893d46cea207e4a2c58a8fee316f356360f80cfc8e3810&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

