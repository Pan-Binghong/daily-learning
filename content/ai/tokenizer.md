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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGEKVVVR%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T032844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAtoKDDYfTXXA6smsTD2o1%2FGAoup0SLj55uH3oB4ZiCrAiEAhtW7BOy7w5gOB2w0jWgI0Rxu79zlymvyi6D%2FKSj%2B20YqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE%2BxwEyQ6lvM2UBzFCrcAzAGkDpGYvA8BoPDNc1oJnJqzt%2FV8FsQ9T9K%2BmdIzTIB641%2B4THhVhnl%2B3jDZMu6WQxZmArRu6jMNHo3tYsfx314TRubenN4WLggQx7WDkIP7YfG7k8n7PY4TxMaPhHzS30p3asOhwD2yldYA%2FLSgsIkXQ5%2BXhktEqhHv3u0YPZFupiCQeXLV9WnTQJgQNrNYz%2Bp8FMqmUWAc3uoa4NRlVTwLYdGDcrJ1iMO0KnYrmDM8l3HBUcldwiwj7%2F4D5oA0AHGwtYa%2B27LnC09IaT59CEfDGaHk4AeFrwkpvcjcUYyizTe69bpAd3PdWyhCMZKKS41gXtLwQtFUNixXuJaWjKvZkyLKiq8u2EJ%2Bc7dUpTAhMVQnV%2FSvYahW6Z39q5R9whG3rgLqncDMwJf0OrgLFnSh0gjJbOF5K8DzpN7V6zaARE0rHFfQt%2Fi%2B9HbWofV41HbBxgpB8JZS8D4AiUL9as27hG%2FWmuunSThSvg0h3yXhbg9CwB6ioG18262KFoaH5wQAcnqVcG5LFOlBe5tSYASXlBdTCJVaEvGBVOUSaxCMylGPf3z5hRHKzMEoeseIhCmOqQyILtdTLyJh9heA5X3FlT4NSd6LkY2YYqQCox1MOD%2BDd%2BFcJGBLIOwMKOC080GOqUBWTyZwXx%2FNNH0jk2r8wESRfFmB16X7F0wiiUINk7Cb0%2BFPj6sNCQ581oKTJSnhkoG4%2B43Oc6zVS7RarzyJrqbfvzvvQgt%2B%2BKRhQJx4M3qfK7zLMr%2BqeGaqvKoWBNCxjO8FHQbcBRZQK4%2BlgQokib7XRPNJn%2FoWx3jocT%2BU82JybIgZDI%2BXBd38tLKTvJNxIV6ETzALv0O3UEtsGa%2B54bE4g5UarBI&X-Amz-Signature=7a33b4627222eec104e4cd761a7663d3e9c3bb1d0b1d63e066ce42e21267b793&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

