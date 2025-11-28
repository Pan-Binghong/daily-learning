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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665J3XMFOK%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDq1KvfKwMCQhHYgE2jpi%2B6KP1hE1Aa7JQp%2B3dZqbCDBAiAmarK%2FWUervMN%2B2J2lpmB6t1cZWOwAWy1nfdlsq1qi9yqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsGFPsLLgncuwDxJGKtwD7fKai32ZSPzj6f4xFMZ%2Bmrc%2B6j7L6pfcJGmvRmIQs0Ov%2F7qOlpMeYsBwd3kSeZB8wQBQ8CuUkw%2FpR3Ra%2FkxVVGbCydC7RjyOG4QPMNvGnDj75u%2FunIct7zXgfrZlRla6%2F4IFpmg9cYDGLsnJo4xD914mH%2F7K7BzUEiC1cgJWOuFyNdJVVARa%2Fl9jgpnvd6tcADqlSqRjik8xxKOaiYEPYhw9isdrzW6K%2Fvc0lE89IHApJ3kDCf00LvQLL6aUTnrZ7ksN7YoSY2bHnjYJu%2BOcrQZ7od56Ausw5MspTLUo0ZZ3%2FSeCBwjMQATUZnEHcaU9Dfo%2Fe1xHiA7eQM%2BaA%2BbQuX6cl%2BPyOArBfNrV5pRAuvpfyeGVdSmDHjNwulWs1X7PpbTHll2iaiVnfrTZZES4jvojZoKLQiH9WNTrvxvXLMbr84uWOp3Hey%2FseOezdNRnX0DUytaa0eEi3aPgZbefe6WA0Wf5CLGkM5x3VVSYVZ%2BmmCd5wZvU%2FuFqXb2YPIwTxum4YnLNKoCSvwKYNC%2FVBUwpr5zBnab3ssFrLSaKHAKJwHu%2BF0thjtBKTecHrzASsndnQzx3WZBJkoLRTMVQTSoUeVCJLvAcwi9qdQsmKq4%2FDbyNAK%2FaRBn4iv0w3uqjyQY6pgF%2F9WobS20ch61sRCfyS2GJ%2BODuG%2FhWhoNz6oFlboCv09yM2eOn2FrHeknambhXbtCzFbfh3qY1nTMKdyh9EG9rRK2JMM1H0mShW69BGR8sezE2SDCzf3EJOb5zn%2BMD0CIXYzdj9jvUR0b8qEKy77SlsiG%2FOX0PMOrSv2XpXpcE55RHNOIBYEkLCLk5Db9ytR0A8Mf4lyr%2BUyOuiW76quaLSnXn7bgK&X-Amz-Signature=77de235e201b32eccec5934d4e7ea3e3913a4e1f0cea94f674c54c78e5ba774a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



