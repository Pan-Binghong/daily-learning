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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RS4X7MNH%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC4z4%2BN2F5ZyNox5d%2Fwbocqc7qLaczIYbu%2BYfWt5hbxfwIgcXHbOAKqag1YoklchLsWLyB7sH5DlWGIeYNB%2Bk9cnSQq%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDBGz3mpNbuftZE9FDSrcAw3kBOXpHDljRdiOF4Yd68cp8ahjfjioMc4Hp%2FRjh7ulL1prP02wNrTrqiGGco6VJAw0TZNjTWaZWAdymOOWWoGVW8bwIgKzVSRQNInbcvxspDpKmE073OrqZtLniWabbeEQuqzP3oyxnOZJIuYBYt5XdVWR%2FcqcUYAQujp%2BaNfscWc64rbE6cBp09g0Vxc7Xv668LKF5JXsxjrRvkxvFK7C%2FNUCcfFuMRLwlYaeIcF4ZYF1co6KYMKQmUIdixe6%2Bsu%2BIzNVCls1TEPto4wC65zgCxOxNAagXdMStZ9UpYMoaGRGGJiCdHGCFmJ1Wi2mtzJfyq18UFTPRJNUl8D54hXkKEC4WMGSUoDQa9OjyVHEyvL0q%2FBgOtBVM3cP5ZhepOqTvDiA1kwO0qxPLiYPkAGk%2FhhXyki71A0EkNL69g3TgQt2r8IeX6Kz1SLwyud0D%2BtTiEkD%2BDTn3zPqrQDF6rJ3aZMXX%2B8eaT0yf1O29scOP%2FR13eSo4hRPRNWyQ7avZim4aI%2BtA6AcrYfwfxQT97vq67z56q1VqW02bEJHqm4rnN1icA1ASImjcpZEOa2uuxk4vYTXTxaVsKIisCb7zPs20Gb2o36OD6P8pmGwl%2BwKszXozrlZDJIJX56HMKPEmswGOqUBEswPLdrtw0%2BAckSIUCa9p5Qd4e0B2PgvWs5hc11yHIQ290YuQN9gDdqHddemr6QK9cco53Gdu38OOXrpxEOYAUyfAZ7Sk6Y%2Fuxbk4Rb5e1OvtbGsv3n1e6Kx3Ou8Mq58QWZqpgAv2aYQoR46Bsqw%2FUvM1zz7cJe4bbWDJwkr5qyTJiJVdDLd3at1BlXpK%2BDTsZ0Vy9B7VX%2B84OXmcSQL47U9dK3Z&X-Amz-Signature=9c2cab467c72c6897c0257831ad08f90c5b41fc971a09bb1a0a38094126bf2d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

