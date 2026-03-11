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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JGA4MKQ%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032746Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGgwKsiJ%2FxIH6wHfUJOz%2F8jrETQIfYww%2FCjtmImxaHuQAiEAnjAtgrsSPNThZ3Gig6diPf1Tz2StqoKbBvDM00N3Bokq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDGWPkO%2Fp5baW4DNR1ircAwnWNWMBgJYFWE5mt%2FdXMuXayVGQn7kOXeu0INYwLfdIjKObuK%2BxTzlOM%2BN4cKD3%2FLHT36WK5hPkXcQPnFR3k3%2Fvz5fdELwJBewdFxO6KKpzk5%2F4iLIgIRf7qFU4J%2FJna8jna%2Fy5KqdAMqtXJdi30EnP5zpmjK5T0eofDy3er0BqdK8i%2F%2BUjp2FipdC9DxNYlLzBv7PqV131cswB3bkppUG9HeQKFFMmQc1DtBeKpmpiKTC5wpRwjJGe9Zz4IB3cR7mLllKbh7G8omCnVdGdKHdVyiR6Y4o7Nft2gzUrzaOXFOC0AFekcus2nb9USCIBVZySJLpbtVib0u%2B9%2Bimp2kgLLzhmg5vPIRppAiyfH61v7L1p5Sjo%2FXCPZeW4Wna5HBfpMmiId0C3SPLyvg7ygu5G1iGWRXU27HLzuBLFhPfjsAF2StNhoF5pXgwq4cQ1hulSVdXfnC0Y8LnTBL4t6SJEsFZD%2B2N%2F9MbGKXHZybsxk%2FQrBZjgpRYQBUa5rN8eF8sqb2%2BIGRbsF9eSQUvNwxUXSHoAFFREKe2Rhf3%2FJVwA3aHRMx4H1xd2zus%2Ba8Nu83tV9Coo8xdZDitturovWPhlkwHPMwcqBBbHLiA2UCGjom9G%2BmNER7EkQdI9MO3xws0GOqUBS9urfrdYjdGDOqKgYC0mKJ%2BTbbaiHqR79Gz5uXsWxJKId%2Fcgi%2BavQYZmfYPjPhOqljZqWxGhrkW2RXqXYmYvjBl8f4METlYOfyTOiF5Nz%2FSAVA1bTRJrmmexM%2F93ktFTraigQJgfQv28Hl5WnsckrN0UHOvpONJK8ILi0fs%2FtCbeKIxNywoB5x2F36ITbpEdJPhEoFuAKOJHsW%2FZHwjhjEYz%2FBpS&X-Amz-Signature=9471f7be0df2120c79dde61ecea4d920565a0bd30a03799b61b2fb5b3eb872a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

