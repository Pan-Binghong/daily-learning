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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VEOCYILM%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJHMEUCICgvaURv7e9sQLZAQ1du35t9FoYt6DDW2S6wE9vcd90lAiEA3tN7N6F1IVn0IdRcy693tBfc2zLxIFjO4bdnMHHntKMqiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMD9TsIjhQmJA2DQ4CrcAwK8We5g24lzzXWQlEGZOcIrLEfFuVGUQ8oQWguaTiiTV9wtxejM%2Bf%2B61RgrRaXWIq7OTCzPo2a%2BB5aSAWHgUMs4fsPUMOHXyFMWeKB8EIryd2I2jooL7BCkx9AdGCPDv3HXQt%2F6vLrHQnjWq7%2FuWoNX7xpxwrWoWZd7N5gqq88bo0S1N2AleixQVaSahxj%2BgagCYfwywtkOA5iaY2hIsme5cc50KM7nLjYDjn4X3D64gXnZg0qxMvbWAxeUFb5grE1GZXe5kAzB9lq7G1TwjyNOtIZ%2Fzhr6%2FSaJ5y7CaaDQheJUZv%2F6RHi8sa4qmg7FFro5yn1WZatTv%2FMwwHxcfRfQjFUNofObt%2FYiiWZjmoHnJfanPi158Mbby2mh97wKklUW1Y35Jig2S5Jr89STDIrFGNSMex5tNn8cjTsO43KvU7xGghq0Sbjfn274L97LzxgjvxhlbMjINC7T7%2BEsu89KKHnlR%2FzHoaY3aam7RMOZboYhG0sy%2BCv0pjU%2Bmc%2BH351Rsib0Nf%2Fey5BirAynt4EUsaMRN831Cls6fF6Fdkm6eAc9H2iEIpM7XWaXusrBsY3kwzaGtITZPTor5OS0aOzjIKMNmzcyH%2FKgdUYdyZ%2BN7%2BLc6FGN5M97bC0CMLq19MwGOqUBmRCewtyX5I2JCReemTIjuazobZ3lkjDWhxpn9tcSKwlOJ8CIByrb2xCGQClPn6HqOnA0PaaHmNtqWYsKYnvOwJU4bekOwI%2BDYUHS5VG9IA2ui3ZRr7dYsInOJqVrvASvzbl7Lnt4Gm3GhAgFHmfLWvI1a6VNAkTPxD%2Ffg5y6dmXb9Egy3re1avx7BEaDxUIkE6Kn%2FUMT%2BOBtHQvuuUd81rEihzLZ&X-Amz-Signature=fb447f395409599d2521e61d1865a08d87af81f807cee20f36a9fceecf7a52e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

