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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/9ba086ef-0a20-4cef-a396-7405407cd73f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YOK7THL%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T025904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCShqk9YPjExw3Pg51nlhubEsMrjmK0pqf4J979a4OHgAIhANrkE9z4NlWLy9VGC%2F%2FgBq1duuzWgOb7qYHxEI4L965hKv8DCFMQABoMNjM3NDIzMTgzODA1IgxXCAVIuUFJfbEHBJ4q3ANyS%2B9%2Br1xFAXu6AeXDhMlslRR%2BZULGJp3ANsgLPfDQ1a8YvJqC5wq0N1yNSNRz0MxuvNjrmtWgM%2Bh9bi6o7gxyJWUIaK4w59J%2FgIHQ2ZCFWPYhrxxfWWzleA1PADy%2Bdjau%2BGqnkZ2t7zsGj%2Fr0ppkZDLAqcXYb7xp4hFdSEgiGM9MHEpmKBhvJeRAZlJyvgQjGfFE1AXktJeFwiVynppWSdJXvu2lwtCVoXCRmi0VHYIXJ7jLvpOwYMNi0V%2F1vMkWYwr961S0vAkBjyd3x%2B3qECEVgLzIyUctAkazUK6kRc3zH4%2BevEQ9h9Ssndhqecn0D%2F84RlpAAegan90Yh%2BztkwIoWz5NlEesAcyYX8Yz8456SuFBqaNeUcTPf3LV%2FXuB1Fs1reXpL9nY11Y1x7IyK%2Fna3Uh3rcXaaOuJ8aXeslTl7TSe7zZ1ZVueHzfMXy9SgjsxtUeU0eaRIK%2Bt%2BUVUAzB0jNXzTqTipJDM8Oe7X%2FnbYH7KrJXgsDvR8lE1ltE71JyTd%2BP2AqQiAwm7klbbjY%2FwyINLNNk%2FUAYHPM9RWxE62wl8e%2FPYVg5povH4bcbxXByPfQhb5dF5mo1sE5FXNVwnJPonFZCvdoveYa0N6U296PPIF878mhDNW9TDY5PHKBjqkAfGz1BzsoL5QJop6%2BpCX8aKXFYrEspYdX0czb6kou%2FeS5Eb69bhn8BJBrYsI7kNYcyqOm%2Fe3n7qZihfJm4MZ%2B0JTKupaQcnop9AR5kOiOS%2Be%2FjfkXe%2FfvHjLDwjhNowX5tAn9IbM9sDUtWtbNgRGS%2BXJ%2B8tYjEPypmZ49YGPhs5%2F0LAKUw7G6L%2Bg6HVEkQH1PscD48KQSgXy6vCRzWH4Lpn2CEIX&X-Amz-Signature=672b157ca6d4e3f47aeee203648636d92908a3a0733fdaa9297225d7dbccc9d5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

