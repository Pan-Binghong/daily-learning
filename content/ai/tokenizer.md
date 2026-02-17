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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623R2EEA5%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T033735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJHMEUCIQDXpus%2F30Cov1bxZEkSHOMl0H41xGUZeqqMLD98j7zwkgIgeaFhSbw38W04dz0ILFmcL8K46uS85s6Q4rT7URWKQbYq%2FwMIRRAAGgw2Mzc0MjMxODM4MDUiDMSc1Aloq5U3O%2BiOwCrcA4piZgL3ymF5%2FZC0gzHQivXRemhQTEtFrZYJ84BAQ4bQ9%2BZ3qttjN5yJs%2BKJJPRWexwqB7wHMyaFDMDKWnv6u7xVadOK%2Bs3B5eK5pYbTFTySi3sCim3YZOXUMeEC%2FTngHt3v7S%2BFD%2Bms7Ay4sBg9UBMhVg%2F3tnUIcP2NcccKP3%2B9TaidclZ8%2FtZWxXgR54is7i%2FU6c7szJDJdgUr1Tm2lGcUN3y7rrL1HUsYCv4awdCeFgYSb2Pw%2BdJvagdNFJNGo0uxg4hsFnwrRre92%2BolWwXx4lkrAnTtpRAK1unFM8kx8AGgiGAPEmhu1JfXkraTEzUOE621gIUv5u%2BFdnGL63%2BkRJBommfvymjA7dOU1%2F19P0VVbwhjp2fzn%2BNwq6GVbgHCBy2ebOpk7JGdkNfGvHr1%2BLw98us%2BGzsKJx3QRnXNJaEApRuJzeEyJ2Q%2BoU%2FpUzuvw7Do0VsNdui76tJsAXPZMPZOJ43YUuXwQqnfV%2FjpZbhQ2tsqsNq5LF7a%2Bmi3e6mDOlmVoUQjGrr7oulKzUd1pw079am1tmmhvp99z0VLLkVF6RZ90N7hG%2Fqn0XA8jfcBQ22690R5m0sS21Kj0D%2Bfoy2N9P0MHcnZa0IEQ55tvkVJquXDZJUHEzZBMIzAz8wGOqUBUBfxQfYxSfOf7PXhO4LGxJiabfrsI%2FgrKL%2FbPVE5pFdQPZPGmH3upxjXz0rl93Xb11RU%2BUtiuY0s4A6DgT5%2BSMsb7keJBNeKhsAX4q5GhSzKUM%2BbILcqHVKHSn%2F0CWAT6sZk%2F%2FrdgJ7ER24rFwDUkCBmFnyG5P176Zf%2BY%2BOMpf1xlbPxCH41hV7jkNolr15%2BqrgMtLHFeMhauixx5KjjB3PWPW7v&X-Amz-Signature=95aa5bb57d39f2d4734bef35378baef6962016681b1de13a1b0eaea242afc98f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

