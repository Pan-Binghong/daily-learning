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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVOJCE4W%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T063443Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGyvq%2FB%2FrhzhM1OSJ07yBPSd5NTyPWIm9hwkZx0pMsL9AiBKotU9ihS5VY1c2OVuMSqw71qLmyzh5cEKE%2BIN68VKpSr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMfwaZ1LPhLlaQ3RfhKtwDVJ1AW0kUi8V%2F918axbetlT0JVWxfBR7opqujJ6qey8A3MlOxhutDnrA7IbTfPqabBbQrX5eGyJtdXSmv%2Bn%2Fi5%2FwMTckcHye8oCPLvEPKyIoB54chMFllnpO%2FIf4pdCpKOldqdjVoE5Ki%2BRKDmbA9c89jp1UDc5Co%2BFroFyTlNhrtLRi3RrijuHPUQX%2B2IKVCcaloWjyJ6SAM9VQz7Z8yYWsp8qGVrv1ZD8RS56iLiHCXLeMQcT9Hu07CMeJemIoOpyOX%2FH%2FYX4XxsV7x4b6gpS5QJdyXf%2BHRenk2sJCPO1j9alT2yye9FOj3R6qjR7Vjp3tXCisjkuGmSj0c9e%2Fw6IPEG8LNkLaf5gM2t0KCOLri4%2BWPrilWtPq2zpAKK4D%2BLKiZy%2Flj4kIgzG4%2FqSWjy3%2BUW7%2FxyWed%2Bc00NoCCFe46zUi0Cf1qmIL6DNJfhT6SnPVEJYsKjlJCC%2BQL3wY9U5khKO5Es%2BxxNGlJw7mTVeAZDSYLQxLbCSz%2F6aJc0k0yt0OjDC1fpcyHLxYXadTAp50F8Y9F6tWDSSQGXplrq6CM05i728IqOs2G86DWSdy9gnKwdm56%2BNg6kcYA%2F%2BHWhS2iwy3M6mowXw3ZpYNjbWh4Jc8gM5rhcmmfc9Ew6ay9zgY6pgEE2sTtAMxhtbxClpCqecFoDgA5jdLjh1AxH75fSpMeclCLsMP3wcf9K808hbFMf9M1sTQcvrA8P6qqwIjTUVwNL949C1wdZ1itXSZyvFoL6L1EcT5AZyVm6yS2tVomDoOkLdMtWOuwBBMUwMnvQCxLcmKjI4rsd5WGoGxmOTKR7psfVqRC6en9WOEEvrGg0t230h4WWJCLQvYyV8k5jPsOHemlPJlA&X-Amz-Signature=23bac2fbee4b87e81bd13cc350f93990b631c37e667cbb2cad951803920d68c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

