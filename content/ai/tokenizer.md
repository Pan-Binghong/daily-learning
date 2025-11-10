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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YT7JGGL7%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T024951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJIMEYCIQCnbHBpfjC4%2Fh1JOD28Qy470MhGBN1i2FOiJKwCuwV1oQIhAKOWw9w8%2BdK9As1PbOwYqTJfp1aWj0W%2BbYJl8AsU2fUBKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyoLr7uaHLX8UA30Okq3APISfcEdrrwxtilimQQDgM%2FIyn3Gir6h%2FNkmu8%2FzabeKUFsRo1Qu3KuoRCUpzTIpZbgeriFppA2rztWgHyHngSyxdhjjodUqV3s5apXyF2u1VSv63xloPLfXaBbK3aE6cVbhqxccLVnhz%2B5E%2FeHGqzwpazij1YBJ%2BG6AA6WE75aBONLjDqlkn2RNm1vafbHWh6n58dpxmU2ptao77Krf6jfhE8kbnluZlXekesLqK%2BX6%2BtEaLYfS8gC%2Bak65SnVyjlKsMvSWwChMmPhfxccidI5Ygc7HN8MDyr5Z9GGidySmbCkpDW80XyrBStblb%2BkNxM%2BSVQOxEB5t2wDE63Ly3bMA0U5wIW96kDIHt7YNk%2BIvDUkUf2yztYWU5nBHXeHTDmZ49%2BbGQ1L%2Fx5AjaYqgqgCqgvxhSerSdP09ZjFLwvZa6CtsTuntUbUqdNAJ5znEkyeUNsB5hct39trUgpYzt5qf8pFnZgoCJ2SDsyX0z%2FjtpgeTzJjZyGpN%2FMOzsoHQtNTaDX6J1gW7Cwfl%2FKw54%2Fd2LdaGvzMX9WQqkRsP13qcs63jtGklK9HtshIBKxLlixdJqesTG1zxtXVorvdrnoGI%2BiqkTl1Gr3GZmlaNUAU4poBPQtA4swLRgDgazC9tsTIBjqkARZ7xTVbyIu7m%2B5Biw3eJQ17Zm4iQU%2BRc5fsHdCEL0H7ZLvBSIrOFqBfb%2FD1LNLC6f5RmerRWlllQhRh0Lt1mEUrVdVwJUrnV8l4trLuhdG7BipbXkTeHibhFRz2GizjPsCGrOBrJ7OEjXT9DnyZqyztn%2BFv6ThURPIumviG%2BYj9H4396C7cH8HlahEktTPcI6KkP8JBv9EvMMzl3AkW83%2FE4yRE&X-Amz-Signature=a7690a5e45159c035defe42468f429f1453d3ad1924a92be110f82fa942c7c75&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

