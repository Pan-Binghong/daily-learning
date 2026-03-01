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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U52S3MTE%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034252Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDFPUdCTa4YoCy56mC%2B%2BAKqlKgAN1A6cnahbrxbLQR9ZAIhAOgMe0vBkfHh6jVvZz0KSXf5qfZZHcei1NYe8mPJH0ERKv8DCGQQABoMNjM3NDIzMTgzODA1Igw1DmJPJXo9Y9ftF8sq3AP5s56xHc7KrL%2Bg%2F7LnkuQU0Ooht4umbnYtNmrkiFlvGN3Z3IErivA8dwIZbqzI6Ev%2BAeJdg7HacgqW8Z2IFTJsrteyYyI8hAgDmNCusqYM6l4duFJqFUr0IuEJZp2IsSAFojLNjk61ze5SJ3HescAOPBfr3QkDEPyM7C8J%2B%2BdO7%2BeKGIZwioNpE6OeSoIV0cSH4I6TzaZKo4JQWwLDNfN9VuQhDC0rqGC5t40dPa%2FVWKJLv0gQyI8X77PM5AbzeE0DOk18Ew2hGNxW2kUd9DaSlWaI1U5pKSu%2FxFDf%2FPdd4FtWsAznsv5TR%2BTUSkk1rZd%2FshwKCrTuloYVmCyjPaPKXMbTtFlvwXR4tTk%2FWi9GmWYTSxT7ohr5%2FVSyxbyyD9YFaVub9hzttViswT%2FM%2BqKeq7EVJ7213AVmNfL4%2FWVGzpq1tR5UXPEOoa9ySxQwKc1GSWfpeyBhEmoIguR%2F5ho1yJcJWYPWnqOY4WScCmDLB9DGhoiJo8UuaoawZTxpA6rIHFDwdDhad5J2itZF2CGzDfjb7KrBBaai3GFHg3a94G3f4M8eEO1cKX9rVH6o47TBaif3obU1Blr2gVzjWFaiYd6ywR6MuYcKdPGtZ66RVOYqWMnMgWDaPHAF7DDbzY7NBjqkATCaWqriBWpMDFprW19tZv0BC4s8SzBUki12KasnPsv3BrQV8uueUwmGmha7VU2ct5l12FT0dsMbpC2dMnf7lWRh%2Boxh8g%2FM574firskHrIiRtmYDh%2BuMKWeBYidVCxHqQINokfE1Y6zXYO1BhO2DAYadDDqFA5%2BD6Ns%2BdNUyRWTi2YhOfspurT4m7AnFnW0MpzWcEerV7Q0sY1NmyTGiFSsg%2FbW&X-Amz-Signature=df8100e14324f56f42cd334761dd0156fc5ea69031e6dbe03f50f6a5eaf296fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

