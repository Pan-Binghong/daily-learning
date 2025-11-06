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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRSJLUFC%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC9sRFijdDpHOLu8niXgT061UcfQNtwb6H8KrvjAcJ5nQIhALF5BshPmwewsBIZiDoYXX9ndMPcpg3x6Ra2ev%2FtxKPXKogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz5Y1yb8MWKX6pjIsoq3AMxGZORcfr%2FtaBNg%2F%2FAjdf72pPgf%2Bo6OrtTYs8CZrLdXX3dduGijYhwy9rmPKZJhZA6W377xDk4B99Ov5vI%2F723bTxYhVmPBY2mYIgqEezN3tRvl4PkDClbwE%2B9mcMaF2%2Fc2RbozqhAbp0U63rxKMSe3debRZnCNE6VAphjxEqQ2EgaTAopduyod8zO%2FFrKbPdxsbxk5o%2FUmeSB7qnP6OZRR%2F6qF9Q2v4C1JPUggRf%2FwSXgXZmw18bDvOjUAvnDrh4Ay10GolRR5sIL%2FIWf4eAzMvcmPLl1atBnFUW5nas%2FhyVABBibhSZXGG1LiDb%2Bo7t789TxFc3jG1eSRXD0b%2FxqVOL66DiR6RZtmRwiInhwrIqCkREnfGolyTZff1TnwdBUGcCaksPZNW5%2FwDBBlQuXbTvGWwdPaNB9PA%2BsM%2FhPzuczeI03SKXG%2FHyDEgNk6bQ28itU254Qm2JigImJ4PfldbhBjfnbt662bSNXhopa%2FFP78nIlF87u1uIQw%2BJ7wHEyhYB1aQujPiCBwmF%2F2NojmHf%2FWCrxppzoSDv7nRa3WSdjDy3FpMME28fW19A4EmQNmfrYDxi2N7R5pJnqI4JQNdLmLriMc0ijWzwrml%2FiqxCFZPiIQLl8KKs%2F6DDm8K%2FIBjqkAeJcQUjW7GFpgx4mIDcnagkauCQUJbn%2FwtBK5%2FG16D1qSpJ9JLM7KtpL9qs%2BZN%2Bpzf0%2FlCwJ2AGUCXcxbyABI22kjm5OIkTszbveDqoNOzNt8eI%2FS3PQCp92M7QRwOd3mPt2ma5DyoSLQk8ke%2FbSxtTlfm3q9RqtFeGTB1rOBH1rwUi04YLEoTVkBK7cT1n5HA7QYoWJstCcKlRAYsCi1K2l1PKI&X-Amz-Signature=db7972fd06b9e57ac77193e0c8a1d4af577d2e3c328bb74f95957acdcf17d205&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

