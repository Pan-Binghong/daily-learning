---
title: 基于LLaMA Factory训练+推理Qwen2.5-0.5B-Instruct
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
tags:
- LLMs
- LLamaFactory
categories:
- AI
---

## LLaMA-Factory框架总述

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664EOGELCE%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIB2hfZKD%2B5UX2KVT7T906kDi5l6jG1LJH3muwXOhURLIAiEA4t0nqtye4N9BDuQWp6FJ7Jh30cSNNz6ojUy2cvsWdWsqiAQI1f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBJbxs5TK4gVMPaYBircA2ffY8URnFgHLxNZDcQ%2BByk2B%2FutXHsejbtdu6pjFSmqz7LGjTTfMS7UCS9Ozgr78l5l7CKgTmUygmjkh3Q5p3p7UKK9pl8DFUbucLWxMkeuVHADN5mnerm%2FC120zbK35JWEJ1Dx%2F0pxAup%2FJjyZm%2F6FNobSE%2BqdpXLH7mIfn2Tl7pqWIwvQz%2F8AUZnXbQp019NBvJ0eO0D0%2FGQOyYAJpzS2rCs5cBO6Dcm%2Bxnpn3NNJg%2FUJDStDF1jFkB5vLZaYbnlFXi70vXJHvklrBHuTr8M9hAyZLkYRmTsKu6KPP2K7xf5%2B120jnyYInaU%2FN0fmc4EzpR80d4R0iVfeJzEE3vwMTap1P7ZJqlbs6I5w8TODUUKDb4ogu4kOPe9J0w6peC8LCCRJodz4AAbLThLkpvB%2FmY50fInCEFFSXzWOfqqhENM7itkdcETeqz%2FR4FW4khLchpbH7bg5%2Bk1l8NqrzAgZJFHmcc67sAnJXJ8mZp0hHk0IUHB5P8FduHnd2Uh1bdLyTgWpdIEB1H7LDiRqnX7u1gJC6wVGcCUaho4F1wXJYaIOpvPl7bYjjrQIrOGo8t5YcS5NaEiYvjQNbq1HZq5r106tIWuy%2Bl0Xoj9uycbkvkkVqhsOWKIT%2F7mqMNCT78wGOqUBU%2FswXXE5R%2F4CRSSl%2BfIRp1%2B9ZhUmhv6l%2BgX5lJwPuzbiC85yWGKw9Ej4iCRGHUd1m2t8g9MAvQ%2BMw2FbQUoot6OdWoXr4gdqa4vy7XRi7W1iUa%2FDukme1ODjXOsKrYeTQCYgxPirSPfxIdyyl%2FZ%2Fy4j7hSEHIy8KYwxkEcoZuD%2Bj%2ByAq8a1C%2FMg3kYNp1ZD%2BUzFVjpokMx851fM2GgnpgMfd%2F%2F1z&X-Amz-Signature=2c4ea7129a899b36d77874b834cb36afa82352606fc35ec6cc9b4149d3c96f1e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

前置条件: 环境，模型

- 模型路径 : /root/autodl-tmp/xinference/modelscope/hub/qwen/Qwen2___5-0___5B-Instruct
- 微调完成 : /root/saves/Qwen2-0.5B-Chat/lora/train_2024-10-10-19-48-53/checkpoint-62
- 融合完成 : /root/LLaMA-Factory/models/qwen2.5
## 数据

## 训练

## 推理

## Reference

> https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct

> https://llamafactory.readthedocs.io/zh-cn/latest/index.html

> https://inference.readthedocs.io/zh-cn/latest/



