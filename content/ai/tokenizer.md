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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YH7DS4OT%2F20260320%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260320T033216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCIFdNt8PoR2BwaZYQgpiM2cRpNWHxb3uR6PPr3THj9ysIAiABTXFtV7ww8BzkiVTBf7y%2BBvY1Hea%2BvvfgHXv%2F0bdYdir%2FAwgqEAAaDDYzNzQyMzE4MzgwNSIM%2BMX3rEgyOkrO50q%2BKtwDYmIpi6ndcYqmfBLMxyPtqU9Jf1KJnwA9cTHQalwLvlSG9ZGuvEIaMrU41Qsu7wLMcUsTrw3V6tYOmvQJXzJuRn1Lq5ga2Yyn3kxycRspjNgvSsHfVSmJOaiHUk0uUXRluZNxCEEm5siedBy4dfHK8CWstINlooVYeNvCSbuAXJxKtWE8%2BtTnygDFmGxHChZtlu3o1smlSjZOced6jeJC6KoG%2F08YIzJO60QsY2Li94LI%2FyIzgRLwZ%2B4tebjlj4CRUDd9rolMXF1b3TwVMNvRtP4s8z66fRbtD59RDUg0%2BUiDjJqORowHmoBwc%2BldC2mDK3AyM9PsZuEldB4U5o%2BiUGfEkz3PZNO6ayPvA%2BHlS7LAb9YlA2ZjUCli1M2TB%2BSeSmwR6auVRZnXLWfSkhNxGX219qpbEP2Ep3ul%2BUPVK%2BDrsx3IwzsoVbjQfLa36%2FAn%2FR%2B%2BCg3lq9hU87C%2FPodYVuT7wYdVHtkyHASZk%2FNogKVbDZnL0eYLB1O6gtgVV5zD83ywp10sxoVYfqne1Qt56sQTVvw09gg4K5xLEmIfFXRibFoG3wgjFT1viOQ0M5IQWoiagtLvSfsuWAb4FxevJwdvofWH1R7gJ3DjuJKarGUtNtdqe%2FDVS1ctRM8wyrfyzQY6pgFJxPiBhV2j9Cddix7envB0PZ4E4VKTAa12lFhwgtdwjrzT9MVG9XBRyMwfyIonnfLghGm4ubDmduciOXF7zCCWcMrB1X%2BOEPMHXevrviRaSTv2BDsy5TnYWSgzf14QXw17vsFDpTqG2%2BkWLq2OkAiExNMbtA1ibspGzdEN8i8z4YfG0NooSCVtKdy9fN1f7EWtAJKDNQI7TzGNFXdIfjAOoiv2%2BHY3&X-Amz-Signature=407e072aed777c332b7959ecf023b7773500623654be780a66ee1c52e185ac14&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

