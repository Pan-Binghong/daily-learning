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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667QXA2Y62%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T025635Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIF3vmXocgXkqxelKozdOeRA6t4ilO7diElbf3tkJisTmAiEA1u7z3nKhVUiSEGelFYvjQ3lM17G0WKIJfrNdl%2F1Hr14q%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDHV%2BvisBNTPdFYOHTircA9AlVwJ9MfgnxB5gg9Mun%2F6AWQ7Hd7qaMLEYvwKUH%2BmTjDjH5f%2FcGe7VpxjhBUEoycRoBfaTVf1Jr4LLJrEMfcj%2BbA%2FM%2FaOv4by%2Fx5Wu6RBzKFVicfW5whd8YokGYhit8lvMJdyNcGbTTD2Xc75Eu%2BvtpHnQHbw9EfexwKdo%2BfZDkUizVcZYvllfTZp%2BL%2BH4yjGSjMyjSdYFS%2BNu4DvEj70VTUc2%2FsD4lAUWboNQjzMVWg2Z9XFyX2W2LLzgmHJHTGemdDQqRC1dpSZNa4DBlENHRHpnIIyeV7dcMH%2BZtIkKr1a8b3d4UKs8ZS78d5%2FGt%2FJB4l6uZ0PPEdALjljop3h0UPEAlG%2F442SDClKlsGt838jRlMxKzdFniXN%2FN31aMHKORoklIt2Im9jfN3IXBR1XQZCTmLMf1v%2BdKcRonbdVNyt3FoiT2PJrE%2FwBWFNz4VQTQgVRzLLJ3O5sK3xdFI5HEbruWtwrioAYPc35R1JKhcPkzZGBmJ7aVzXtkjQWjywmnw4Kyk5ipFL8Xe9JUffIhB30sSHIbhCkbEryOlmhqeLMn%2Fh1hG5RjqjJHPzhUJwxorfVmB%2B1nJ9zxSQKQWjXIoK54CC6j0oLAu5s7Kit4WC6c3%2BwuOI4rMUzMLH8p8oGOqUBFsDFFLB7Nw6IY9w9yEtNVFQ4QI9yn19Wma81p8jzwonZ%2F7Q04WMnDNH1ZAejJ3AQ9jJcJbIACSzQTnJ9U5tTTe0b8nia5xDcdEpobJszAv%2BkaJcoOEPLk%2BevOsiGFf1kd16nLcnY2g8%2BtXmx%2B92q1uFznFeDMrWwAqU%2FMNyPFynVLcQRfuIhR9H4JhiDkOB8vNSmOTNg32iWk%2BRGMdBuKAOWCK10&X-Amz-Signature=a2635fcb284bb95b5de7fc789d99e3bd374c579a12ad5abafa27b82d28427297&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

