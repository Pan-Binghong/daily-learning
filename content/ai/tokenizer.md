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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XAJ5I3T%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVq59Q%2F1C9%2FBcCrf5ilZZ1PNfHsmLNHIhCVGXcV5sBzAIgI3v513fpLc%2F2Ez6djYFaOHxzzIMcocWhHH8QAn8%2BzwQqiAQIpf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLwEoXlq8zSSNmMSECrcA96kUoQ%2FcMERFnMIP4dDEZ%2BQmV71xEhl8D23EM3XNNmSTeuHbGp40MI6QAha77inyxTla2fVvHE%2Bk4yzUqaQ%2BiZ0Ull9qw9DpjNKA9%2FNiF4glXmdK65wToQqU2hPXS6elT8%2F8N1vk3hJD2wSwjBo%2FlzaJunZ%2FSaX6b%2F5F8WuP53QJrZOB7EnURNG2hMdXBn%2FMmhkuj6d4B7AINiXakxvRE7%2FglpaFUxd0cdk1rvtSHZ7gkisAo9oSJPteBLGCWtTBH0tXY88Q0nqN%2BEmUbZWu%2FfKaqnPOFC6o4kmozAjgCMQOmfQSRPZc39dDZ0mQTAQmiIQUDAU2wXycST6%2FD30QwwO4RpYC%2FbTP3ROvsGSdq1XMyU66vnJ565Jo%2Fg5aqwNPkt4ECKwcRamNGdMZFv3fpMnlHCH2jhc8CnSewyC2WPiQl3GsdXY%2FMrxsTp4Qmu%2FfG%2BQRsMIzmbPTHVWwsxnkxn%2BlJnMIDr%2B5t8fEhpnA6rJ%2BGLASUTgI8qRfiO7zqZ0Jg7ujOZJ18%2FfrclQBNlBN8XCzN5T9dFQ45bAhX%2BAEWnakQhgW%2Fmvm4HuawA7VpW5g9KMBRFEzm8gz4fpo7cvJuXrhLVVEEHwVjA6jIaCJDjlrp09FNFewmmUpU38MK6Qts8GOqUBEawjFplO5qOO6ragSBSm%2B0M1LbjTwgFGQ3jSZScUWkkVGfBzBAG42xz9wFJjp%2BS6VrHe4sjSPmSwwzrH2rQRjJxEVy6X%2BigdEG7dEN3qgqLhw7FD2nd0WpHy9fEQwWormEDLZ2b%2BTcU7bVuBPT1j64jjzFChzdJV122uHO3QQj1FpMJpcG3lqxe47vx1jQdvO3v8xBtVKjlnjSOZjeUOB1xH0JJX&X-Amz-Signature=859b0c3bb035ca9a65de6df53ebd3ac60916133311b5502adafcdb5206469f85&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

