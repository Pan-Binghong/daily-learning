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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YWCZFDK%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDjHTnS5k5%2Fb3XADr2GUrCkfrr%2BADGmonzLevDFR%2FNLdwIhAKjnGdF5FpIiiYQeHgcynkpcMF4ar9cOvVS6xP%2B9JRMIKv8DCFwQABoMNjM3NDIzMTgzODA1IgyDLVNJxUnNpQB6LLkq3APvdMDQF7QTraoZRj%2FglFPA6Tb1ReoXHBhN%2BLT9cN%2BEAkapF46lS%2Ba0k1AvKnfnxNY5QhV4zhVxaMwUh2hfceWJrNYbJ057C2wcr8EXkVTZgBCrbvFEpxuYzL98orXag1U0mjoTc%2BcJX4kwWiekmxeWwqmPCQL1%2F6pTj5%2Fl8NcS2d3vFXJy7i%2FuZ1k8MMUEhmL5JJZ5qvNaQmU9HxlU6oKFe2No4QQGdS6dOgbxg09MGPNU4zWWyEKWuAlh42P%2BU7nXp8Q9pnAgOUJBjVFO%2Bx%2Ba1jSw6UqNxZ%2Fly7Gq3AwJc3MGqA73FUmFQkI1ZbLlf2OpjieFdi2fOgZckUDMInKitkseziEXJEZLcfWo8zSCdsRzGWWTg7Pvx7ajW0voXX7DhzdZm9qudYgNmguqfd%2FdX3apQMAMNb4ECTuJzbiWQsGUzPtS%2F5v06UFsmXOHzzetne8I2RTMtgA673ExwAqxZVoDF6wzuH01puIcQtLHlWz%2FY%2BAizOT8S7mGgEaZb0kdsGTk3AiKTo2gQuqtkmyHXnDQgWf2treYwkQS8zqcqIlVMBw%2FKrwu3%2FOWNRyEIdsbSqwoHtTMqP8OpuLu5AijOBfPIFpz%2F8iH0R8xoBAdO%2F8quKBbjrKZjwkK%2BzCzmabPBjqkAc806Rdb2A5EwVvgQGiAC6VszVe3%2FbpJcMfsh27U7FSeGMXuakPXHcniotR7ap2N6x%2BRt1dHX94zud6gaeag0EIBtybQa7SjeOtwdhQnxAq70CSQ%2Fi%2FyK0KU%2Be83nAfv95kO39yX5MRMz%2Bq5wTQy11lmSdHMF0696f0OknxQMOIz7pa37lUSEHIR0CmvpUwifockCb%2ByY7Fens1%2Brghc2EixRCis&X-Amz-Signature=54888792b3c60e0397fdd9f4b7e9e54b4b83adc126ab64b376ce82e217b3e205&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

