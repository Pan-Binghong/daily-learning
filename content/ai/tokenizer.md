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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UMNRBHW%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD29eGRHyWwUhAKJmQpVgWhnWDl%2Fl67rtjtNOO6tdoo8gIgZtv7nHTt3aZJbzz2SRzD%2FY7N8v1atanUUD0LY3p2ZxUqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNewUr17%2Bpi4LD0leyrcA2WNU3YbNm7wQROsf2akbIGrXvxoKq5WMoiEvhpG6ukSOpapX5PHwq1MqbBK932AM4X3AaocYR%2FwdHj7Jyqn%2BEYM7zVTCvQT8cSBAP%2BhTymwq7KZoZthEDh%2FA4M21g3KOdKOnX3As6jzTnUnUoSO1lgMH2QFm%2BtTQdd3%2FIojFhTprID%2BXLs%2FOyhz9vLR605RXOCZQ2ihbkNqyyfNmRWN8KK6O0q8fXj7H%2F%2BVCLApYSB%2BcdRNivU7vgFtZ0MMrpzkNdY9rg4LLiWnvVmC%2BDeXHMT%2BDXmjFV7B%2B5BH6aIZ%2FfJLJME1rtkFAJJYdkNXVzZf9Qt0osdnWeomRKPUC%2F6jnQxiq2epQOTGc1K7BTO8IC9ieSrKCSKZY1JmFIrIM9az8WEj2gp8W5kGq%2FTkVyYR4UBjab5%2BaMVcX%2FvaZGMfCVzuALP0tNXgk7fs0tQgAJJb%2FDilclyMWkS9i2RB%2FxOx01nYEMs1z27WqBFF8KH1aeJKX3YGpfCn7CdrfG16YopBaSasPwktT%2B5jPgx9%2BQ6EjqspaW4eZwCjh84G0SVxksy5b2eolhNF4zpyNqRvZ1yQ%2BE63npIUlZzTW8%2FIqUA1O0zyNAWN3QRcGBc8wwRFaLl992U0Qp8jc5gb%2FlIBMI%2B2tcgGOqUBYNb46iwsgpqdMd6Cto4xcbJshc3ZqXY%2FwAFp7jjr%2B%2FyzlrtuliOpwoXzeZSz83T36rRakcrbygrEqVw%2F4Y6zpwFVi8N52I6z%2FJ%2F7dVCwoTO%2Fl1uAKtbwmJWLYLS6bCzD8mdSqCFBkTJCb1vlWNoeGUlOhVe%2Fv1%2FUo3eO0t%2FJXma6OlYt6x6majIhrGwDIQSNLpXFBochov6dfp8mItaYaikiIqqq&X-Amz-Signature=43fd6d1bdeed19d8e616ccdc54823c32cd5516ec0ddb5536ca42d5ecc37ee0ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

