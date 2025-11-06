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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUIRB36A%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014254Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCCpoK61EwZkpHWm59zypr%2Fc1CRCjNArFvaZYfoiWmb9AIgHaIzYuu7NulDWaatqG4kmju8DrkNRN%2FMauyjFR%2B7tKsqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLKEnQ3Y63Cz2SBCJCrcAytHNq6Vq%2B2u6DtRyW0R1sg9DG4nZv8%2FMJJnnbvW%2B%2B9IB18v4EiHQDVPPE4s80tpr8fanpLz%2Fh1qVjdebvL6CIQj%2B6CAfD5cSowMt8LdkfKJRA4wq4tAYEEVUesuzskFmJamxr2mY%2FMqHCyIBu9ZY78WRpx7xGlXOH1FgHqtG3n3jv7tqh9NTHdpM2VEMNPcFxbkRhNzNhGrLt6agMZ%2BaeeLPUHs%2BpcDj87AY8SFa6SJUkspoopMQTdH92d8aOk6GYvtneGjhcqLuQEKQtPOUpLHxS1%2BBYi4fNvtSwMPEqQFoWrsVHVWj4hAsvCNoQ5uD519fjZg1xAnq2CmOezewZFS0F%2F%2BTPjhaLudhP37EQNZxl8FNoY7Ntn2O6ugavIdv3JKesAR%2BaRDXjFO%2BjcFyATP%2Fh3avj463i0wZuemDj4Tvu%2BzcG26Mc97EIMAkkxQCYgSe5hKOzcjwqoohK4loKv3MPSba4rEAxsLokjVjwxOg7PEnC3bzMYzp6hPK8%2F9sOOfDZDZw42BMIhLWqoaXBdZoeNmJPnx213pqMahP%2FN2ysvVJmejggEr7BCu5MoVt0VW3em%2FMmcP91odk%2B%2B2ZexBaLdlaFb3%2FxB4%2BOV2W7305nECMEHloqgKwNE0MOHxr8gGOqUBQfvnYP%2FoWTei5nVF1d4Ios2XOc%2FiEuoqUrg2k7BI1cHTbaYZU%2BNfkoibg8KLfY1AiEPnjFcc%2FvBZYOb926%2BWZhYWM0oBvd1b3tu07fgHJd8Li7tmmZaceecrtlbiqPpXMZw2W7vxx%2BlFZ06IzM7QRHiRQezEo3XinUMOwZsfufCh1hSBQdqpljweh%2F2nglHwajPWiPgoCN4QLu4%2FLLQX1SU%2Br6e%2F&X-Amz-Signature=8b1f1c38dfc3700190c39a1bf95c791a0b1858306a711d5de1e9ed21df366506&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

