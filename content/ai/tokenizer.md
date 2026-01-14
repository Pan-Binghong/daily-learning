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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUFOESIP%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIQDuhZaJ0kILNx9J2z%2Fpf2l1ZLTNwouI5tSOfzL9Per%2B5AIgDjUgx0rx2KRLavt0uh2JgOzKpG5pFFNObt1oEID1rTUq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDCuyTmUzKQ6CkhgCOircAySWi0PZOzle76KQNCBCu7c9vaHmbMZBPgL4anO0Wf6Plr8rupHvUXrcxYNauoiOOvOknA%2FXEx0gEESb0UKDP3UXRi3s%2F%2FEI8FCpEqpFU%2FjMKB7p0nJLGBJgdWEhqZ4ODLkcqIK0yAegldDTRPLMXXMUroUsn21szqSLaz8j89BNof2Y3Uz4x8tSUM8N7DsDI8c%2B%2FC9hX7gLPlM7KHt6nwQA7afIXJJAE%2FfoJAGZmVv4LyXZd2TnKMgNfCVX2KlLtUnNpiGdxiRfkKtNR6J0rd2T2f7b720wDe%2Bu1g%2BTJ7TgZgFL8bzhsjY0OmBaKyxQ8paBUribWrlHvVUqRKfGZ199xIet3vIG6Xmt019gKmyt5c%2BjiqPHyhXnoatGA4mT9v0kMwtUfD3S00oypUK6VqSCj0U7I5EsDlOazpwPHhT%2FxuesOJY79v9yJJYxWTGgE43XA2XVkHJ4t5lnZebjimrbB9dfCg14IF8QYjxGovU8epV5lY5o6IepT%2FydkFtdpET206Vxy3oKlhmSFBXN1j4gG%2Fi2a5UyvkM17OLjdt9ugjr4%2FWuIkDbu9HGdml7IPAwQII8AlsilhWR40MM%2FfQjtb5hTHZQGh6d3KtSQrLXGTA9BBdXJv3UMRu4PMNPvm8sGOqUBs4W7REQyjelgkbdCVeGqnTde1NZcBDERsTa3wv2q9hIiY4%2BIySGebnr%2B0UzhzfOtXPrg8fq%2BkJPRwKMqWh49p7OmlnqQNKHSo8QSHkUULc%2Fuq8ZyrsZJ3DgJy2oAgr5fNtPU4cBb27qQ9AOShBcJHctmObCBVYjCQrdlUe9vOfBvyejp4XkohoY4GdutqJxvjeb6ZKmFcgutBkGGCJNKn%2FCJ3nAQ&X-Amz-Signature=12c49ef6314b4dc430eca7b9a7c2d1366c1f4c245c550cc57c66c8e68e216c5a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

