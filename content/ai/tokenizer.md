<<<<<<< HEAD
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png)

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

=======
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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XI5I7GFU%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCICArY9Mnu3zFgCGxaqo8uEdPWuX0lIA1aEYcwKlUmOq%2BAiEA0zpH1zpEyC2xfdJmcVdlcFRvTMFoce8tLEGS706%2BfFEq%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDLjHGiU4t536re%2BIrircA4YdW29H0AFyTxiLbEmgcZpS2mjyyGf8eyf28n%2FACGjjsteCz%2FK7XyeKaTnfajpYL8t4GLV48pupWQDvO3RAhqfspv9SkBWFi2xE12W6hb6MwDZk7Psf5pmluvflQYuD5cUHcxuVyJqHQy6qKts9La7sduLy35X2VZcM0%2FAooQ8Gnhu0TFB0iVREYnnvaLYqoIF%2BV3v26oOslfEhjCUtE4Rx%2FxBPMhyUptwxzgZqtnO4tmLU5KfmCE%2FfVuuZv%2FeM%2BhYcFnKscSSUoCkXAFGClo%2BWoCvI7B2ikg%2B3Sp0VGQlA98x%2B4HjwaYb3CtnqSTK1UJreWzdFOJtaWkwspH51OzAlcKo22dRlgtJWjF0c0Gxx5dYSXr3pKLNcK9EPHtXh0UXdpBC6EUZovVhao6gc8o2YBA28nxHK2K2ehYV199GPccnpKGdITGRaflIn2sNXlZzb7G8%2FHRnbdvDU%2F47K%2FtPfy4dawwFHM0NDsc6%2BsvTXXrT2ejNBua75%2FK7pdF6u3siZH8c6u5bPcHoKIHbtS6f2jeGlkr0sJ74VnobsZosMySX5zyqdMCQTo5L%2BNYq4sapjBNtjAtINUnhrqPqVumxhzXR9vhZKR4flyBjMxKpO%2BC%2BSY0nQSB0bB%2B1SMK%2BdzM8GOqUBC3cfeN3TTCJzkvNksfT9%2FSIHfxy9BYgJHoqHIgUayFaHqWaBUJzumT498JnyNB31mLEaikq9DlfN4IB%2F4UCRvuSRebwHCu3KAUlW1ZH5a%2BdWGpUmXouyKbCHUQGA2t2OR417dPH42x%2FTbdLuyh0q6LgkFDHhIS8%2BikOW3UsrK2jXmqIiPP5nAKiI9JSTIxgOzdo6LcxoLZkqVv6Pp6yMJc%2Fqj%2FAU&X-Amz-Signature=48aa478d3867724d3678553fd976d4179d0fda2c8a0a5606b9ea9a14de47231b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

>>>>>>> 67e2e8ba81abbca0065a5254fe8b7b646ead6176
