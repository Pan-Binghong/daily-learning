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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OIMS6ZU%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041121Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCIAnJd%2BAr%2B0GShCNszDkmbmi1Hxj7lXBKTnqcbnh2ZuwIgY67DwX3aV4aRGekB5vPBkAN2ibhCRVQ7uIAkmdp%2FeE8qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLSZ8epUAc3Q%2FS3RtircAwLpm0K8ZiW7BMNOdAIj9bCUgdmBKfQhLGkvndRaRArT7jWud%2ByZqWQ8bYH4i2%2F4gPARhIAJQVqx8Bmy7x1%2Bm1Z%2FvJL7Dah6CP8U7Motuu9PDfHT2LRZqQ9Pkd1VMNfAfCgdz6k6PqX3qewDFFoVAG%2F33Vnu3c2XqESJnkcdz6vwqiZ5WJAP7FSnkovj4PY7VyP%2FZ6tRcIp3EItHET%2Bmz8lDPJ54lApm5JK%2BZ9Rvb91uJPGwW6xazU18Dl9v47KmI5KRoFoV1awZZQ2visnqFs0wU2wBXeVF2Wo60SBaOA3cYoMNT5qgsoPDtc37ifx6QTpVZ8GsndK4Ll%2BmR7iwiwlHs6UK0ZNq1IL5QY%2BWf4hL6nxDaQBk35id1Rf%2BimOe6IU8jiRzwYQ3CZZibkVV9IoalXmImvSlY03blctRaKFPWqeNfdnmA26SEClC8c0BDhr06zM9RYNtgOat3%2FTPX4MA4UitcAoKbrvlRpy6OgErtNQDl9Jhc3R4ZSrSHFJtQM5S9YUXpEwh7vueV8w1LVS7t0qpnMrlUboKjrhDO3tWpXQhNviiFxKka7AdStuduS3fPuq5dmtMH89DQbb0kcbYRobqYxfrH83MsH6%2BHGm6t9gGTGHULNqVhJiRMLfg9s4GOqUB8Y5SNGZ4gDOfM1vTfQPWAcjYAOPrriTIjpc%2BxKJcR3VOm4xEJ8oJ9dCSLmh5tCFY6PoFqELaWf4fVtgeewq%2BUe%2B5v1cFqetyZ3Rkd8NOxk0KUl1x4aB7vDIwNl%2F5fSNgaClzx5rZ4FTckoUDciUzC3xf%2FRFvlOIAwsS2SKaskVBjspzZ9283YKfOlROCcgLAUt1Z%2BszmaM7FJ4kZ3DTrf1lfCJnH&X-Amz-Signature=48414d4cc6802f2b8b8d10b3a75540bfe06575cf4c488f3c3359959c9914a761&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



