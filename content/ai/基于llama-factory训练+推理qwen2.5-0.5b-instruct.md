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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3EITIMR%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIDvk7u%2Bchpphg%2FClEtq47e4aXbWV9kfVztc%2FktC3kLXcAiA4JsQDwnpeZa9ZkGIaTqvNniygvxGb6q8hBsLWuSvRgCqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0MQXIXPofkDZ%2B%2B%2FuKtwDJnLFiqBnmJ62T37lfxRMQC1FZAZN5%2F1Tz3VKP7GIuGCxWdfuLB726zn3TXJSOwikaXcHM8%2BDTI2t3xCfPwg40%2BC8QXFOMvfyw%2B3tOIOXWd%2FGeE8mSEyxQbLmtqpKd%2Beq0A8G6vXdppvjsy0N831rQuUiYsB%2F93r5nV%2FEuchChPQ1Ga0CsjzU8O0VFTbOV8nV%2FgUosur8PcD3iv%2BgoeIeBdWfNqn0bR92s1j1h8HNSKP3GIQse%2FeJapzpfLju16b8c3nkWVjn0bc96%2Fj6JKplOLv1Mn95F5dzeNKLxZhkZd4gQijLovQzLn7I9W17krEMEqXlqjzqY0YtJCpCxMcoc6P15S%2Fw7PRibdII%2FUrMtR6JRD4IFylx69juLbqPgqKDDRyqrA6IsvHl1vRyx7vLcGLHVVjqP5lSS1AwMhMHQJ3CsrthObMIuk4z%2FSSjO8wxg%2BcbJyELxoL5mtc4Zfe8V33AfZTNsk73vCUL%2BwQQ5Qcy%2B8zZkNGu0CfdzT6HiHRkDGGJPXt8unNu0IMwoLe5oFRsnBLOxzQciz3zOKqeO%2FOxmWvRKkDH0oj%2FqUiHvc1wvNXBkWiLq1%2F%2BV5RlasqYQ2Bb7Wnld3MTHH21SqDpELfIdyRcHfY1OXKf0ckwvryGzwY6pgHVDyDFHK%2FO3srJ1S5Q97HC56b3HV9Abez%2FAdlHL4cKbxr1a6qXpfm2AMFSpZ5yDTmw03hlYTqHMxsbfhfWr3p4xEpn7XHMoUHK0HcQoV6qQDqe0nWAeScuMpxagQbv2z%2FceHEuS3BlfH8NdtHhsVmXAXFBwZaxH6CKYJTjbr%2BWigpmegRm4J6OmX%2Bk0yVN1ey0NnCUXsFowarY4Kfq%2BBSpEbj50T%2Bw&X-Amz-Signature=3b98fd9fd1b78e0689fe386b46d2390e82656caccadc2e51c551a998c6413627&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



