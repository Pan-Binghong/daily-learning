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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEVOIXY5%2F20260427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260427T043238Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPi%2BiG%2BtAELCgNX6vffgNZp8yqDxalHXUfzxEOHVzH3AIgUVq1DJClXcvGoo%2B1NEiy4z%2F2kI5X%2FplxtciSat%2FIfqgqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFFYXqHGG%2BtFtOICeCrcA3wxujB3OWdsTXQMQG0yt9DKBdbEZivtrnBt%2BWuQiAozn0qGMGoGwZwkLShyVfb%2BjVEcp2n%2FOIGF39JzCXAz5JdpeyQTlKvpwYxdAaHiItr1ZP8YYnrHjNk16BGuWFgEoRYw6dgwXpuDZD002iR8UR2YnVC77J%2FEeB%2BAHO8PbyX6t9K4UHWdaSBKo3hjnoCk6IkZvIvq%2FrVB9azGhJJO6D9E1A8Hk4W1UvLqaWKejb0fE54l3wYxa5bWuxXhwPjNxw4R7t4LbF46uPKurA7jF6B2dYQO9ojiZAeJop2Io%2BPpq4WSZsUt%2BNVR%2FHMLfxxQZ63KU9B30W7tuRyOZSUOquuc9%2F%2FuwGAIAANwFNOk2QUrS3YmjOVGH7iQOkqDvLa3L651aHOmG3chNpxn44SHo4QGVG9Dsec24KYpE8DN75%2BuDDZzpChn5GjmIc4b%2B72g9XcMB%2BunneqTRQqX9cENc5sT%2Fnh%2BQIB8Sh18%2FL1U0qLiHv3%2BrfU%2FRL84ORqUvdCwoysqcqIspYoGkOv0%2FNyQUA117jZJVctlOFwMUlICfmDLTxBFRk7zPNhzZqi53jI9k8z%2FdF2R%2BsStOGcd2gEDySW7V%2FRGF494GMBldW7Z%2FHYpEacStZk21QlwuerOMPq0u88GOqUBcAI4mj3HSdH%2F60EW2HIz9HwSqRdd5UYuOyZtMR37squ6wxiOaOBvENsX40edgAGafct%2FZSnJ696xe23tt%2FQ2hjf0tNKu4Hv5SGgPyCwacFwqPMp8PiLxnMIxhDqR90WTFk2F6Q9Y9E72GGYvY70WNGQYRoDPbpRGDWEavbRQgaE5rEab2LIQUc5dckIcTG7kqqYw2SG8u9Zx%2Fawl%2F%2F1bZnLNj%2Bry&X-Amz-Signature=1d7fea6b82c327690a56fbd109a63c8e1aa4a04dd64ca26ac12803d8a716191e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

