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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662V7A235E%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBjLIogQ4hxef0rw%2FsUYvfAo1wgjA%2B%2FfYkwD2TYNYtJJAiEA%2BMrA%2BvVmEd3uCwCMHrq9e9xuvYPOoaHlLcY9FslEL7AqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCtF%2FlBsXA7LpUGIEyrcA2H5zWvaYoRqbNH4Vfs2pf7RiO9lpwyiGacCBzT7hKjSZ1a2X3y17jnGo6zsf4Xf3MU1bdbss%2FqF0%2FaodlckGyNvLsoDpWQ2rHctCGW0P72jGX7Wptfrj4mhqkPwnokgFEzI2yYQpjUtaFIl9hHPDVdg%2BqT394aIe8phsO8nbZGZlEfbylQEoge7GOXvNU%2FMo%2BH8e04gu4KOOuAzhZCx2fac3TNako0HAG%2BZM%2BWMw%2BRj9xOed%2ByvMX3PSWMJVb7t4ZgXuUbWKXwkFWf4cXsFSyZ6mRV5RbFD44V0v3YbwfBUa1sDYMl159Bj5KltpETpO7pAhtkXWNmBRv4J1j9Noj0MefZxUWdEFfR34IwIEYkAembHGlrUaNN%2BuS3ZX2ym6Flbb2d6r4q1EJQsgTCGUUiKzQxht3XgBNgDRREyWSE1RzUjQfoQ8kfWSrpscr8IeKLz08%2BZJJZhZat%2BUd7%2BAsA40aS121drnLJ8iqbg4dKWDT3LfTdQl64%2B5J3Cc37dRR1tQOMJOkeGYbsuUWm1xtwWs8fTn5Li0NcZITCFgq0X7mngCpq6MTssQCvYG%2FSo0o0MVW9PiJdWnARd8rTMeGgkY6K2l7qyZ6ZHhAnMRmLS%2FnJ0OLMOauWSnz1pMK7mwc4GOqUBmRaWMWffs9tvCv8ZoBpPgbsVZwXsdihEQf607%2FTpH%2Bi2ZO32%2BNLvzd8m%2BBjwSar75dBhPLxNligzuhM0MW70HfFP2VLeSvO7JV3MHRA9E1fU2%2F4Gh7%2BaZcrSEy945w5A4b7XeTM6M0XjLJ9CpF%2BliEdVo6Mi609xvXFqAEt3AR6FoboFe%2B3cZGyxnVIZVqs%2F60NDpabGap%2FZYTf3sWBhmrenmpqQ&X-Amz-Signature=6a443966cb79dce0fe24b14cd26dd851e97a5ba32973a52e4d330ece2856ae18&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

