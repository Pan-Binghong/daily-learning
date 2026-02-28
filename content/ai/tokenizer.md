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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VK72DUKK%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031113Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBHDyPTK5LJcQVlIjLCfeFIZP88lkd0XoM2OiPoA5YFZAiEA2ElF289mNJl3%2BomhphXrFZ2q70CumPFDM0XXRrmu%2FCUq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDEFjB3LUlbZQYHXhRSrcA5FNUtneXOSBl5nDIUUx%2B3Wr48HO%2BA3XJffKXCJoD2%2F%2BGF52pYOCoK0VHnuxKSx0Ap2Mm63OtsvAsymBxNddn186Eid4Cof24S0fG8Xji%2BoQc000NO44Mcf3l%2Faq26aZq0u6LKw%2Fl4r%2B%2BjJlpPYJZG7KuarJSXlJkqZA7GjBBjbPfdCD3OIFFe8NtYJicx0Ub8h6kL5Rveoj%2FG6iw%2BIXWIviy46GNC5RPvu3u9VrH0Mm5e2fB31AR5YcarKco09Oef1Kf893DMmmCsR7rlyPOfVfzCZr3auskJMYiW55cWACFsdi%2BrxarXPaD%2FHvv6lilR4FiWWLMn7Cdgf18daxbNFGfDRgkHrSnCxTl6Z7S2bH4o0395T46sOiviIzfcpc0DFKr0AXfnuXPzY2H%2F%2BlPHX9uGXki6HRhu9aC29iDnE2KA%2BZQ7KbnUO243zkD6qy5VdwvUCRrJfhi2l%2BAAzWKzds47sPCk2UpBgWLA80QUNeAjlV3AMxQ21b2xNuOpfF42FNrwaKvYo27Rte4wJunR993lsq3b5qAmdOhEYbQxIMUbtVhjYQv26oVHOQ749bvP7oYoHMdYX19ygPSyLYs3yM9BO0KRvifcgMUHLMCg%2FTSmiPdawOiMFeGrYYMMeVic0GOqUBoZjHvqm%2FqeH9yH3QNriwUvbq0bmVI3YaKCK2UNC%2FJJIqXXeH13sQcm404%2BZ4Qfw3MQv7sXwS%2FLZgZVkvoRIVgN%2B443ontiRiYTT3TOwZy9OHFvUbGXxCLWX%2B73mqNx2o6FfZw%2F6AXMefLSx4p0hlt5Q2zxvru5wOlJtFaMo02kAcH6x4Ncu1Xyvrh0Q9p2088c1deSoUmChPUffgs1K4FudSY%2FpB&X-Amz-Signature=1e0e9b5bbfebe271711b4359b9faaee2904a9e0e54abc6c977b06dd2c472f897&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

