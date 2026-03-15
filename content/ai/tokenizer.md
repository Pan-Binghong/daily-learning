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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOXRDV5M%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T035206Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCKFqYIv3T2vlpTnhI0Lk3%2BQn%2BKMv%2F2BZW43xuOiAwBSQIhAPZYzogY6HqhL5b%2F84NHSrrRjld6PTGNYV9jv9%2FX3tkcKogECLL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyuqykGn4cPh%2BTlxfwq3APDOJVMhg2nfe9RzaxzK08sAdyKM6F5XGCUSq%2FBv3zsetPDznbBrVq4MSZfWfnftMsYNIrKSLw3QCLBZATfuutHCwSsdVuWAiVwa8AseCXfW%2FODmtxUbTO126DWcvwGK8OtwreLwc6pWsG5srrdDCWjzsSL2tGtizxct5vsIA7guHeC13WuchEUao46xUdLd7XimOiEQ%2B8BwmQKC5ZDd6ABaKZpuydjwXNshfFNkBLzP9TGxjpuR94hc43rpL1plUXXY2mcHSmTMNLmzmwLo2iI3IxAFaTtqBPjBsWPgrvEluzTBIAJwT4S45Wuh%2FGmkYCOYFD%2FUsgzAtzxaUKXTGOLZJ36wSIdSAxR7Q8%2B3Y90kPrW%2F5jTlMdNFOtjugFwmokc0wD4VUpo3dq0evrN0im4dsS5bIdRUS94V1TYeQaQ%2B%2FcEBN8hx4vo3mU03tnJ7CMdxA%2B59CHuCv88AG7zHig2M1x8ffbCp1P4X4ngEk8TAwVbLbSSvPCdv2MU7KZ66r93ELjLFZ7m2aFw%2BBvS3QrnwSKLTL0SxfjTdMk3D3mfHdPN603dGr9htfhhjsGkpu9kigQQcN%2F2p9pydCqRJ8807CWsrkFHlggvOLHvfTVkbKrwmYzqhR5I%2BxbOhDDFkNjNBjqkAay8vaOXQqtatfQ0zjRiiQe6mOn9jAuQz1B4Vw22HNsCaPd1cMYy5Y%2B0DAvfkdnReA6lr087zjnqvLekneEwUPrpe4by2qZz7TsW%2BLH43WituDYJMQKEWVDZNy1fSrUEDrShmy4f%2FN7uGSlH7RiVhLrqxJuypUrK51109QN84pWF%2BRioakCo%2BBu2AgVbYAfxvk9fhV5KZBz5E9y%2FwcFjlXwNITHF&X-Amz-Signature=82ed7660244f31cd1b7ef3363bc8d93a1ed37a6acd16808971eb9d7b8159a48a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

