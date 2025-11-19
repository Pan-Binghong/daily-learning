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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VLT3IDH%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIDRlDMdu4%2FfHowu64xm8iO0Z%2BKpt3ss6%2B%2Fa54nGpYL8FAiEA90YiJQU71K8BKq21SU0kOiLGPqzIqDMV2gNcaikltW0qiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGCjRN6NcPnWMw6VJircA79K2E7zkjKOQNJpTq1A5rqMMzoaagFrvQYjPoPMGLG7QBXEnY6NPG7yDoJAVJHgIUf3kuHo4a2lW2Wn%2FoF7kcyNmcbU7sYwywcKOWGmN8cBczqqrIlz%2F5LVYUGl%2FDmY%2F%2FIU057gI%2BgA5IOeb5VanFwuVadm9w4pNjhoQ6S0O1v1fx4lsiehQDEsySmv2IhKBL47Lxd3uAe1YkuxenelXU1ELTikGcye7hmW4TSLmmR7AMa8JZZGCiC6ubIrR9e9T4ExeuvA179GPSuKF9uY8toRjfWcVeHL9tGUC2hsM5kdh7mubTw39GX29Q0YPnPaNAvxKV1iVocawN4Gj%2BNqsMC9BfOZ7Lj6SpAmH8eYz7NqbMgMuVumDWcB7o2LYFq%2FEXPDFgBeGv4W0fxhL8d%2FaK6bbzpNSoTmZzryP38Z0Gky%2FT%2BvM42oGjohh6VnHGT7ue8WD8R6rWR%2BPgzBGlw6VyL4KOGZLpS%2FD64kQA3BWfFtec%2FizFGa%2B3NvpNz4PxEByGBVRRRThOs7So9O3H0n%2FT3H5N00L0h38qrj7IgCL21E0Wb4m9SlliztljGuv%2FyIYP5x8PbtL6XiID80TXYBmp90oIGCVXnJrO9Gm68yNcljdhC40ETEgW0iAKlMMK3J9MgGOqUB%2BMpPifHxVeGQH3gUmLVpj%2FyvR3rjCjkG1FqqHokvSuPnIFicqV6YfzN77E5%2B6wm%2BLUNIO86AmzBkQ9BjzQWojZJMD9DxzuXPJVzPrSV93AXCWUxXTt4TgOQro6Z3s9a7fMgWvngDyUh5GQ6sjpTZMtN9j6ZqOvT%2F3%2FSNjryLCHl1g4LytTsrYqO4KE5IF9ap9iAM2G2fSYsO7c5lE6LOVRNuP%2BAQ&X-Amz-Signature=6a78fcadbe491e5d4dc00c8feab5cb60143e28555009d35b3c57365b7bb2fe76&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

