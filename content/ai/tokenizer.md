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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRTAFPYT%2F20251221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251221T025958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJGMEQCIEvHTybjU1y3SIkT0dzbP%2BKjOlYnIvLm3Z%2BR4v2A52AkAiAneunJrZlR2bOpyrg0UYUMVMSIDFd71Ew%2FC6Vahr1ZNyqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FoCFBHvQ3RO5dtAoKtwDEKBHyVhFZb9PQD%2FJkMR35QT2HDR6TYRMUOVL8tEUvfxY%2FT8H%2Fen7MwZKb2ssXXRf4Z6GXK2hNaQsst8pXVh4VgdypD9s0SmDdQ4gg0uH2xE9yW3qJRlY7c%2FqfoTqBWAapohyD%2BepaM7F568lcxOAYEkyoOWxojKxsjE7qfOv%2FHfGtF4B2xKpXCSkpUpO9k73QAsFCZR5vagpNCQh0hS6ohXGY8bWYhG8C70UuxzQ496ODAwHo5nkCzxUFY8hn2jf6ZaaAz4fHysSYiZAIJKic83JbjnnPTny1egdMZFONXbWh4uB9gvLeKDWwOJpvIt6POLwZXGaa5zFTvC%2BdsjWQ3nZpyZsHpL0kobt7YwXu9eImo2I94%2BqGlhZSBgRz%2FISGy9rFCf%2Fj%2B4gPsCeMMhCPjSBiuTYpdMA%2B3tOXa0uSHtNhTSiUV%2FW6mpl49EIPKqEPoFCWzc%2F5hKaoxy6v2csB70LcDgazn0aXK3KzNdH7sJFXUVOUKpWCzRCmtNkDnAjhIY8WUCiBeHM3dnx1g5dc0vAH0nh7Xu15YnZlBVD8Ag0%2ByG%2BHie%2BhNekR2BW%2BAJFIBIYddjp%2FWADDxIzZl03wR929ljKKvzLXLPxGt5sAY48QnlfuJCy699ZXHsw3vecygY6pgFvEfE%2BkVCRlmiEJBWWBs3E0QGCngMxxOsUgQ8jGj6%2FUXXQiuoYCSjD6AbzUJYSFvkWAsWNSsCvVw2Ndxj6jmOxOo8H8sUZrO2OaUkFl8OgayMo71HjhOnPeqfmdwxhcx8djKBoSb2UH9cnVhznb2qGC%2Bb0fVRj4kEM17WkaoVqFDY5MuJ9OlmZzUD0ovvxkCGPaaE%2FuV9St2nKIcV17C7dL0R2maw9&X-Amz-Signature=24e270293ffd0fe08d58a645c15677b3f30834712cb7c8c2ee84d1edddb8ca1b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

