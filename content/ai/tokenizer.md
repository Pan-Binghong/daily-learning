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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JDRTPP7%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034506Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQDbUS4indwrj8LdkN1465Fd5iFQbNknmN8qoT1PNOZpuQIgeL9yoD2Nj5lwJhgo%2BfEeXzDh1it9HOzsDH6cK03ELTYqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOeO3vIg84VdeXdcUSrcAyJ7QATdZ3sT6ntUOHSpAsLTZcUCtzGCfmWU5ITuoaNf92KKdn%2FbIOaOV2wtDNePnM8PEFNdJM3%2BE0VnLqc1bCmWsyzGGxi6kXlOQXeK9sof7UbzMrUGdTPQgT3Sky1jGcXDDfkmM0lAcKYZ5s9xZW3HKYuqiI7uAB%2FeKMvKGmEnSxmwskoZKpde2bm03GuHlGdcUcn4ipYoasp16iX3i9B9GQSXLn%2FqFTlCsbEzqiWU1o5W7DpjGTCppCcxZ7Q3qj27DpX9RivUVgYOR1M26qBQNd1ikHp2%2FqA4URWMb82QaUY6W%2F2%2BdSQWgS%2BopRx%2BH09nmwf1VCFJoshP7cnqK5c28dZXlevXpdro61HWRIm12s%2FA1PU9c3waHaA6Wu9C3jERmht9ac51LowsI75Amc%2B3l6iE6HG5xKicRSUokiJEeYhGksBKAcx3GgSouyWeesdSMiS8vyskoD12gf1VHmEtEMPfO1gzYoQLXFSSlx7t49VgmO2k%2B0UJhhpxnh8a2m3qSOij7V0dpzFltzfYWc%2F4LgWDEGnqSep0FeLt9v1%2BK%2Fs%2Ffx6MDSbyudhNb72TG9f9eDsVEDBP%2BCU%2F4wTStyIQmHgOOUWphAQduqZ3ViyoF3sB%2Fgqe%2FA492v9dMOuStcwGOqUB%2BhVfM7H8R5NkNpUxQjRghXw34HlmWwtyrXVUxOGH%2F4p6luQ1jAu4osGbasKDedN5b7N7XAY7VLw9hWsSXIFktN1J10j49cUcoFcWzBws5ES2ELZS%2BxX4YqmsigduVsbG116g5Mxd7R%2B7y2lWxUzdN0NA0XgBauHUwulpuONojMiyqBXNSgCSFH2RgWCfVLjNogSfh%2B%2BOGIoQp%2Bw1Sni3LxLPYyYs&X-Amz-Signature=32046e19c09607fda6dd3c9efd964194b3869afb50181168107affa725f93d83&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

