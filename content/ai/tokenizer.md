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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYKC4MTI%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFiKcPTyxn7W6Iva5a%2BdZRHtHSqLdUUKMgRS78icnNAUAiEAs52vlaCtBiai%2FTk7R7gPjyK38zwAW6jgtdwveyhuNpMq%2FwMITRAAGgw2Mzc0MjMxODM4MDUiDDVe87WoNoeWVMb7qircA9pLWcccbTIosHnM6WQiGTIz1wl5qGq31I7X67D13Yu9wFDECWkiCDUiqbkIwonpuHWxoqUftVDfoQP4APCOu4o2iXIAOcOfhrFMShe%2BY7SGZ6nd9TZd9wtulB6CRjrLjH0uwHlPUyoSzYr2WoOkHN77gdpyRR7nO3GrbmBFSDbZEGWuqF8ExIxN7P1qtxXa9XRbTwn78K14FBOkixlZIFn%2FdSKvTQRzlW5IBdoXc%2Bv4ricN%2FoThLWxcOZp77KlJKA1EMSmayOzBL3MzFrVmd3hV0P1rIw4H6MksKlxi3nIDKPlPjwapKgwzycR5bPv%2FeKihT20P37itPzdQuWwlWWArxmNA53E%2BVeGlnPQoD8YJCUviT%2FLwbNzghWCgxO2kjeFmXCT7%2FJZPBxbT6yDdmLT1GTDqzCyZZ9oPowWn%2F8y2W%2BAPpsTQU6Y2w2RxHPsR99BgCsSE6LoCWLBsBTfb1pXnz7kXKLag8T0lN7LNg7YnYC1Pjn4jlB9cseoh0dDT0PBzpGFFnyYI783%2FgcRZ6BE14I2OEl5eaaFoCD8cPt3aves3k9vtOIBfdhwGbPNrI8UM%2BbzKpYXDBws4b5jhHGUOF4GWKXEOPIXUle9bmSvKzqMsnWPeJD%2Ba6EigMNKhss4GOqUBCnG8CU4Q5LEPiwSJqXk9hVtZuwo0BLlnPjtUYbiStzgZosfsqIvyIhmxSlu31gC8RrQipp%2Fz8QotToJkM5iRMl4MhzzHRohL3bmrAIIKz5JunQv%2FYgjce7mfWN9I2ZKYdMh%2FSJ2vYIr922l0G7XLRDFsNL2MheI4xNKr75LUpEdBYZiltp0s09yWPwxncn%2B6SuswFM8JeIncL1v4SudRudY2iqbX&X-Amz-Signature=3abb7cfb16034771af5ca405dd937650fbc464130836a84b5ee06bb753e778a8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

