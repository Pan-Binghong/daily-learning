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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626XROHGS%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYyc%2BP0WW06TvM%2FuiEgXGCCB3wb%2BD9knqd4P55MeyUIgIhAMJ%2BfjQNL1UWTYeaLG9W%2FtlsyBlziHJpnPAzoaOgraA3KogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw65ilvBjnjZ1obk%2BIq3AOg3rQek%2FkbqOy2U0MqVs3yDUp2wkJq000eOu05trCw0a06Wdab%2F45XVXvASwDXGlyxYyrBP5quek7uowFRP2UU4UwL6MBmf9skrjyJ6IeIaX0H7QUmXs17ruhBIW8%2B4NJj7JeET5Syv%2FEveFJOZj9yRomTXNRM5%2Bh94BEuWyEW%2FvdGwqcrsLZ5l8jsjNNc63A6Zf%2Fd5jg%2FDfYk1WR5TQraazg0K0FM04Ji%2FLgSIjIhqorjSpGonz%2F8n0sElj4fTe04BqO29vxxsiF2SdW1ltez2PHsEa6tNnJLnoh8QHnZzhSFW2dF4gwdg%2FWFIkYr22Tj%2F2Zphb3KjJk8%2Fwbu4BavlLJVtgTBzsq6En0clNhi336yGoM6VaT2zt8RLGW2DmKXs7MR0AdsQ%2F5COkLSYd0LH0kNcJW6xJBnNcaEyaAtWnmUY70SlT4XJvaVBX%2F%2B%2BPCPjVBrX%2B%2FKyKS2u8d4M1kTjdbn4WGcqqDCv4hGzsi3ALciS%2BEeJ1JZ224nanOsUy0Jn0MnKQkULb%2FGG2Hv1ycVtXge3jVJdWUuLenyqlf8P1p6rTn%2Fo1pLyzrVrEhO10IgiJbORRX9zfPgwexfZxwruasxhK8H3NAcp%2BWHzNzIGcjBeZp8TYukiwrXmzCFzOnMBjqkAWXhd5%2B%2F5OMnVc%2Bxlcm17ipNoQq4Uik%2FczuDfaWJDO9K3qtHHV9IHwPeKzCkpHP4VGOJqAgREJq6yYXNfWb%2B0707TGWZPhok3Pc0kgBmZfuIGUJnefgq07lNutHnGKOPO5OgXEhXbxqGnewvvZbgepw8s1obIf7Q5PxrxNvGd8q4gEpTp%2F4Ry%2FV3CBhBYAtK4h%2Bb6rFLGB3Cx1bEDYSFp072cE1N&X-Amz-Signature=e77886d07c26437ae2f151ce9728a7c8630aa58b301f2fc413ee209fcd1ed181&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

