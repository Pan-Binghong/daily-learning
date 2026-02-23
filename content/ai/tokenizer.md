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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWIP6ZCY%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDQ1%2F9twX4dvgh0DtyPe8h3nxhIKg2m2PKvGwE%2BkUg4FAIgNQQwQ5dfgbWFVD8xtBt0fKKQP%2B0WjkpfVglI0vUoU%2F8qiAQI1f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBmeFGF3RyS1fwA7FSrcA8WEQ%2Bv5Vghh1EEfCy%2Ba0%2FoJXM7bTQ06CmsrXNTORqrQ8a1OX4R840wmBlSYMGA8T5Dpz9wtjON6BmfbqgZGlK6f%2FsicK3Lb0G8UUAax5mFMysrtbFU9F7WqlSOzF7i6M%2FYBP8TOk%2FOVP1mP6VlR%2FH8vw90dyXeq1w6EUlCXBo%2BGKqOPeeJXON4Q5abWrEJtpJfats2zKsey7SAshOwDb80uIc%2BKY375ZWnznSkPIHak9bb71kR5UALT6QYRYiXx%2Fgrjd5I3Aa3OJCKvZwITr7cLd%2FASchYNSDHBblu%2F97DtzF%2BaY4LUUOo%2FV3ICJisUDPfBZ7vbzHAWjMeWUX2xc5dfLilw%2BUWU3DeylbAW%2FqUU%2FUsqfO%2FpJa9ZronvpiJgl93uqqt6Riw4X9lr8Wq8%2BhShOHCwSygdxwiQHlNZ64nHxL49BtPl%2FyvTvBDBxA%2BENpGfuskfHiK7gF4XhJZUvTihHPlDX2WC%2BESpSsIVYYptdTKXkwBjN6ZWSfBSiXEvOB0PMBwGQYaOQezDplroRwuelKbRIL6HLJout37kFMzwGefoFqgQcIIAeXDpjVhtAV58cUlUmPX3fhwK6Bkxtt93ssEGIQYiw2vVar7bflDaSRlSKAKgRiWNDEE5MLiY78wGOqUBciSfZUuuHcpk4iyMnFgoO1YLjkVmWIbFMKD4Lj9RjMQ7BwNCJPxpFmNBHb64TCbrjG4ak%2BKXDftEoxkuYlKPQWMAAVQsXrQEn%2B2fEmf%2FUkVnOvUBkJTjOXhQLOHuVvzAvuPGXZx7EkLOBOFxEQ4BkPr5ECDASLzlny%2BZwGGlGTmLEvtWmkKdusMjSR66YaPIiUR9vxdCJvmhsMLIRvu5L2SgMzdb&X-Amz-Signature=7fc3512a30221965cab2f7b490138cc87973cdfc79c14b8773da1c7e4843e271&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

