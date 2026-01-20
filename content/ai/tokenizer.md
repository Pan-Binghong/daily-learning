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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TN4J64ZF%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFek8fu3Z7trALLQypypy3p7SYrzGnz9SjNcf%2F0ijJ%2BoAiBi5jvIXsmoUP3t9KMW7y3q%2F9mA1%2B2Js2%2B%2Bs8nDhpYw%2FiqIBAig%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJKDt5N7NWNvxte4IKtwDwOPXYjd3wUQAChl3HpGIBVAZCApRwgyusxmAuP%2Bp7YyBhMzblvClqOZML57qHsIYz2fnEeVoMTZWlyHsb5lULSX10QBXshSq4pJfmbvQ1nwBfKbfTlZpJPNdO4ZHjkzpnbO339SsZ3ZOcRIwP%2F65lzlLRhBpSgwiOCayf4RS7diLRLShiDW4Lvp8gPf6LeJTCHiuKUrQlqDo6x%2FQF%2F7ROsCuhybinCeip%2FstLvR7LPjaIx2lYN1VMJTm2tbFT7JSfeDm%2BMuM6qTnIcqWRlhQDpjab96gjLQ6pUzhhsqsIr6LOAUZIJZxz8r3ODmDpiyTirUjeARyYUy1dUi8PyALI5kfuQDX%2FYfDHnBoqv9rR22CcXn8UkiVSucweLtUa8F8djcSzU3h2Fnm7NeQV3ore5ujWlj7GjqrwfwZRZi2Cs0gHGKjRVUMmTZdaC6movP%2BGjTfISIw43uskE37QrNXDIkjOotSa01Nm7EcXd3%2FxvhPRbqH9jBlj2BMetg8tjB8yeymhCz%2FYMRqJS6swG1whlbwcSLi3QYh7qv034cHtwupUm2ZNRlrCN1j1S3NEeRjnYFMx8l70NDiRdKiKMshuwr1GRdYhdFXwk06WNDGUz9itGvIp2%2BPvcicJzgw9PS6ywY6pgGxbCmLzZ%2FS31zJUYnAa5o0LOQRxTM3ku0wrncCUD3YCvbYvIbEEctSqniRnyeHSLoK3dkjfJ7A0OTduy2jVPaE1z15pniOPchJdzp9ocqfQwPGwxXaNH05c2dK4tizLoZNtjAhHHA5aSc9TJVhYlBUe8INHjohQ10tvJfe9JXF3VctHNbf%2FM5%2F%2FB9e2DASvrRl3D6A38UkOVjCQadxeeMK4lfxwfsP&X-Amz-Signature=a732fe58273b345e5798e55ad911dc4a0f0763a2a49c2bd9658a09ff5777c74f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

