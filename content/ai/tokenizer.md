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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSNQ2LKC%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035112Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIEEStS0DhyRQiavQIMTVMQIsCXXcJyxBUzaQJ0qBlcPBAiEA5PIyOj1Ix5tD68ZZ86X2A5oYD1kbutcRzcy9VMEn9ikqiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDL0WA6dw9IWb1zOXSrcA6JLQodsta%2BgL19ydqf89lhSCp6fqZDNyyHEWo0ci0YZeI%2FgQWqK6XO3%2BFtDGc3xZNC6IYSkkRjRIiq4NvCYAPXLgMiZOmUbGAMM2rxYnQTZJ7f6QYmallV3ZlkfdbSyy%2BH9nDqqa%2B0M%2B%2FqNhi6PeYZ1pt90bGaria4LDJWlOmZIdCVrY2GDv16rkdx85ShccWe8sNDAO4Xh7SE3iLPDqdvwpPohJj2CDRN5Tuke78Uw%2Bq%2Bn1p4as4%2By3%2Farf83nrZQ3ZU9Ilu6oc%2B6KUK%2Bh1yVxqU6Esh3kY5qfbdsKNn344KANYw6B6t2bZYuLwWQsXtnIcWR9N6gXBSNfV3RaeCk7dqWk%2FYvt5Yhea4vM6NR10kzP1OVORpGgOup8YbctLTcALHk72pKh%2FixVNuhKrWhxbvyScPFtqmzDwjhWc4Y8ZOhVExHdszdKiGLq%2FdgMQgTtF0RoZjkq2GTVYbk%2F03N%2B7Tel2RcS%2BHkdf0rn6Z4I%2Bu4Tu5ym4rLn9CM8MVuujE5l7K9DsiUhKfk6SyHo8YZ2UIE%2Fz8TobhHB4Nk%2B7od%2FY%2BhCOTO7tjGGyur96jPUa6VOCbzfodQF3lkemIddDdjVAWQrgzo82F3%2BadCAZbsdYlycuV8bjsC1FoP6MITwls4GOqUBfYIobpeYnqGxleUf6ijdX%2BAhc3QK%2FvNK9HDLqi1SB86M0mwGqVTCuYdvuvDqzQ1%2BkxOzo%2B1OwELZ6nB4EyWiHee%2BBSDKBJsageYfozud4PWWLHhVE%2FXFdtVSwnSTiEoM9ECgj%2Fi1V3Ebevlxp9agINCbL0DGp8whVyoGn9Sr%2FjgxKd5vVXUAe%2BUuO5EtiA4f%2F6j8gaTfOz3JpGP9CWYVR5%2BciT%2Fw&X-Amz-Signature=4c998e7b81c2760b8d1a0645ce47a30ccde704db561bedd04d2b8e3f4524941b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

