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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WS53L4I%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034001Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEB3Amu9y3d44kkrWKj%2Bk1%2Fk42w19vyC6fKGSGy1dD%2FmAiEAxN8vc9G1aT7UpTG08dikFMFs4PV0NdaohGTp9FTlJgQq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDKhd5%2Bf3yQSehEyncSrcA%2BSdW5LgKWKmCORayOzk5Glj86vGdDqHieiUXdZnsBOif1LYPdKljKXRQmOvQd6y0Fva9l3O3wGy7lVWfQpmYCqk51Gv6oBV0xpmz2tnbTCgxsbC1m307SCjbPEfwaNtOMkaXhta9ptS6TFBtjys7Z%2BgeVOinluwBK1ltQv9vb829HUlqFTUoEyayfhcj09dKgmbkPUy6vR4JEMbxm1UUmrZW2EjITh8UH12SdQ7gFhtX8M6ait54j3CIc39hKS1StD%2FdpRTFELxueW91k1ocIp5%2FachxUFQETRkh6BenM3XZviCsXO8VtAtBfOagJCBwECmCYcbHGI%2BhXBnqq8rTM0QdtQPLFM0ausYpXDOpqNGGI%2B6k5m9df0%2FTep1sUeN8k6jIh7GuNhoLUHbXtpGRxTXIFFLy8x2w5YYPrfRJOqQg4Lk0Hk%2B3Wl181P2R41EW0QLAAC5hsFcfIgatVN4Od8lHQ%2FQg%2F7NFrdHEZQbELcD4zOhX7BagPqZG5ufEXFwQP2YDoVzviFy7MDvCZHJtoeb7xTdcAkFmEy66oUBe8Fcp8Fdubx8VMGSh%2BMUTiyzWAclJ5FYmAy880kyuKCzC4zi8n5twFFtddak7K3tbQLLl0ZXh3oO81zy1uB6MJif1MwGOqUBlUMVZH%2BaAcb2Lh%2F9Y2q0kH5qRDoPvcNVFd5fuOs3hGmhm6X%2BoL3NZelEMkWU8AG4IHF4bjtyw21mwQMPLQN9TVAhBoA9equsCYEqX2gJjVcmefjDIDeI6WqI%2F6Jd8QK8dbRigC0oK1QyzdFdxgQbodpYd7zfIsKUIArHkNAYvzJ0oIFhxGPH8ScTsj4wvR8LTPOPpxZ1hoXN4LdACXBueE8MatMu&X-Amz-Signature=75bc8d3418a863c8dd584ca76101075b899f91fc274be4a6dcf86ce8fe8bcc94&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

