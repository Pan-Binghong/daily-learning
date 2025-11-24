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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ABE7TR5%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCBlE8pPDb6%2B8%2Bmg2yH7gUXF2WwTD16jmqg0j0ptmP7WQIgHXz2LxKL0W6n6HXCHlGr7IOty5jBoQN7p7bOT4xcUQ4q%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDFoXaWqpfbAg7c8u6ircA3fG6xFz9jgHjx40fhQma4jTv1jfUcEuNA92AhQbvbANDd8UqwbZBK3iVYocx4E7lm6pqQ3%2Bi6fbvPAj%2BY3pIvq7mlqEXj%2BNo7EtIaPe5VI6hI4AK81BEyCj9yNrLfFTWL7Y0eS%2FJt1J7OvaeWUZAfGqpz4VeFelbT9k5v943O4UxW1kIN2Ury8ExTXuhANnbV0TvoxLGjUGpu12%2FVZRol3izXH0RWyv%2FLs85NoB5aC2E9sKz8aS3dhA8FzhiKZY5LGC6tokZUQ12AtBeF9zQw3SeXk8A0UqnwA%2BNoymzdO3IHWt3fG689P%2BwZJ5%2FZNRMepAqZween87Y8ugy9B88D7dNuVBaMZrhaM9FzHkbgDFK4HLuDurXUQhLwFB9PDEz%2BGAbnJu7LGAvUdk%2BVTXBRPlPPeX7okBA%2FfZCxtM%2B0GiY%2FG3Ip3%2ByMu%2BozVc0iLPKRCTwkH6gnQe4A%2FFslTyvwV6clJc7FB1IGKtxJTsQrsXRA0YvRjolJe9Mbq%2F77JpvFmDlxaoy3Htp%2FasdBfW0oKgMvzUpNIM7XBQtK6EVivOV39o8zo8nZKC9iYbIL6gC4y92O7IrW58sf75xy5nQLAfK2b7VUB4KCby6E%2BDOLFImGZznwr4QcXo0UPwMLrcjskGOqUBkgb6KhbdNwct%2FVBiRuW59yRjInjjNR5vYLO2tue1nojTmC2%2F%2FrUxr1eI5t6I4QalbgOXNdbA5pm%2FhUHeCmJNalf0ZJR%2FuRUTFsxDjZDCLH7eNFAaISApUtiCRxJQX3oBROtqnOHLfhZvNF8fVcfbcnpLVVybVHC6y4DBOLs%2BySZG%2BraeQUMcBvA2%2Bh6yyWHoQXjGHXVRiA52rAEjFqtJKzOy4oBu&X-Amz-Signature=bfd671c9c6611f3e2e7b1b8fefbda3d436c7a97a477234856286f292f01bec9d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

