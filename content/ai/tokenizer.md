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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WCCMXIF%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T040908Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCTUyyIzv59QmLoj6zyNEDK3Ax2ldW%2FJqnBc8YL2A8bawIgN7V49LQHMPUddC%2B0gQR%2Fmmykz%2BLgFaKBD%2FirvlVMaZQqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEVD10t6aUC%2BQgWw7CrcAwtm1zB6JpQELLS8WePmvgihubRAQ5Hc%2FYyK3WTUsR0NUN%2BiITdLBIP2leUH9kh1I97ZMN29W5v70ANG9mBGdPykMCqp81ryaArmf0RzGKDKpsB7DrdHR3IB%2BKivv3ZWcz5Hsq2HcmeAhV%2FoKX8JUkNZBbNQtQayO%2Bl8ijFPFc8VY1o7VGwCJ2g0%2BDq8pVXiwHqkhITtQlWUwPQP2dwTk7DUH2K0LazlOJfQ1SXh%2FE96bHiM%2F0mme7z3GuMPe5r7cnuWlZjUH%2FdAwoS1aUsKYmez18%2FwJwmYdoo1%2B%2FlxpXqiileateMJcxiovMvp0X2TGkyJ0KcV9uME7iuBEdx32ljAm4OKyrANmmBZbXL2tm9Rp4iVA7ZPqgRZ2%2FKv34MkgTZMFkDD2XwQDjUYjWexH0HoDZc39z6HUiObMyaXaXGnC1Jy94og6eiKyt%2BUOzyPPHB%2BIkacnLeZDJUdapmRGCAkTz98kiNWaXzVDQKpR6WGHU%2FUwkQokHnZ6ZPwgtPx%2Fu6FddgrlkqDNTwHbHnoR8aovQ%2FqWe5qf1zT7Vpo%2FCxHypitObAkqBDzXzD2NmDE1i0fDOvgIZbRext%2B0KCnLUx%2BFC0mZ3HmesFebeY0Ivlarkvd5HuH3c0RbTImMIawzM4GOqUBOd020Y3sjTn2ez7PKOuGqRz7gvhf28LtqSSaCVXi0yjgUwmE9GBK%2Fv6nVrw%2Fl98GZuExEiLdaEgpNZpdXakrdB2V47CUPl6TKNk4aUhnHf%2Bl1%2BWGfh9HUsJoAepF12NgHi89YhGxwjROJu5NSD6kNybWKf0R7knd2AzayRjqLRKNoStTynA2NXUCOD95v5PTP6rXXfaYHPU0Sk9AGaesdJQwqmZ2&X-Amz-Signature=27b8974a040ee0243a332cf9bd950c117bfe13f0c51fdbbc69a050480f982236&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

