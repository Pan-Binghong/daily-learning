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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4SFJA6F%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034000Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJIMEYCIQDaMa1FoV8CgbH2%2B%2FTW8lSkziCgEFd5fP5%2BmmXDErQE%2FAIhAPzRu5GEsq4KW9DppdNdYI6PRqSaLE1DhCEls8jcp5LKKogECOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyCjXRlPe7fY3pzbckq3ANlC4aP5%2FvU1C4wNbwT7oPQL6d82M2suoJaz1RW1nJL1DNWtkgNw658g%2Fv5ovgM%2Fr8eV0sZSliaNraeOXojhw9gK4%2FRl4e4QgOyg7O0HWT3QDv%2BZbICkaZkchXu1UCP%2FjfKFCe2HWNTgnWCNh50mfMwDNvCybJlVYWrA7%2F5KxAspwoOqqZC6DTYmBqYgniH3l5cNX5dW9wkHZJWkHE6ZnvKNaGVkYKDJj9CvwlG2sENA5Jyr5NoE1fZk31sxiqMKS9TUuC78DfpfA7q90OYw06vIE40x1QhJNZ74RfN19qmhVEKewdKIXKuDIIqEHuOy3knn%2BPIcLJ379YLVLpYDl%2FxeH8TycUbH6fr8bLy%2BqfOZtfIZ%2FOWsdJU4rWNrQnJbt%2BFvCo9Ja95stp6MKsclS1vGJfedixs%2FkTUcQ%2BiNU2yOqeg4HfU1SJpf0OUBUrZHsv52kUmawx8oYrYmZatB913dBxAKxmcAybtvyuCHbWsE6H16k%2BL4rR3qnDupAJgCelj2VbAunew6AAMBPWn6anWotUUmN1uOZ%2BuUEg5OHGTE0eMhwCeNxbPWZT3t7f7GqvikFYwZjMdhEPL6eYUkDcAXDRSRZ61z%2FLEt0Bm59G8%2Bccr6wU1oMWcdQJ44zD%2F7ZzOBjqkAfnz3xJ3WXc9efeBzoOl9hD392snPQlLCXM5Khor%2BfE9noc4sowOGOSZnaelw45zvVzDTv9egnw1cOoF89JPz7jwBSbH1OIYKxODvAUg5rS%2FCykxIP%2BIu7OirQgXaYjxCQySzTeqRou7n%2FlcIVFVLId3CgQFXT1sEcZihmXtc0fVisVH80cRvoksvww0lyVOqbzw4W1bbskmmkd4wPoFWuP3lwYZ&X-Amz-Signature=d7911d4569cd6748a391c0cac20fe5fb9a8c08385c145ea14b574b7ee2fa8dc7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

