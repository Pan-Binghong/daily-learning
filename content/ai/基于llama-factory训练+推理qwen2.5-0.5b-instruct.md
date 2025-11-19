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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SI7XCD5M%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024347Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCICI469j63LPEg7ySNdz0AUjuvFHQ0NaYTUxtNF%2BAvwfaAiEAs%2Bzy2be9%2B0aNDpTaayods0OLYgzDJdy7euZ9FMbhtyUqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMsRCqRunsl6tawt2yrcAysl%2Fz37MmNx%2FjyL6%2BV%2BHiYaf5QQ1Ht0mGLmqxkxGjHtXahEo1CoVVV%2FLX2ZCqAlhO8nvdwjN6cml8kNxxms4oCnzbHlghT3pyLVULY0sQ%2FKhRLPWAVfD0T%2B7y7asqmeEucnltQb3gMQtCEKLjJR19lsj5gy0uEQddpVFQRIOPpopjmtU3d5qN1KjyEpX6OyaEs6DFUcqelpB6yV8bl9N19k4TGC4g5GFYMnu%2F2eZmQQmkP4gdemFq47zdAnhpCjQHU2s1ibZ1U%2FW29ltbPUnjm5LY8VhHhkH9KLAe3D%2FWUt5CpmiT%2F1EftkgDH9T33jAt3rxY5Tnyr0HW46yyRzq9snOtZ%2FVAaEqe8PuKhm7p5Ojfn4hketOO5YyWL5VqztBV96TzfcbaMRjdJ99aigJjHtkXUJj9tdO1CQPmKFjAdfH28ORWTjtUTbp0YYxs9cdP%2BHXxbd%2FormCocH%2FXiIU%2F7NNtbN2hnU3sxh9Nt8r350q%2FA78nZhMYdgRNDhpKFf4nbu0HZAgjVTGJDfNTEa32u%2FCrmhZHcr3Cni9t4flikK6oJyjVkJM%2BO%2BZ%2BUXLk9Cuy6Z35sy88BxoTNJA6KJMH7YBgLka08GMN9lVAQ7TKKUuC3hqxTt%2Fvw1%2FJ0RMJzK9MgGOqUBN32yKHk21jCOBoaMmk0purdQg65y0a5oNeywg2O5jwKG51wAhIVS0JTW%2Fb4kK6br9tDM8vhQEa7dsEuJCaKuunlfJGJn%2BXDblP2%2FeADn2xc2y5Rpr%2FOWLwtn7RvyM5a0edoCc%2BZvwD2R%2Bk0Hs1ZL0ACDM2t1mTNa4%2B4k6%2F0PwFQfP1GsExQflCfalDM4BirHeXgcNP59R6mMrolWMt9VrEOsMrrr&X-Amz-Signature=13e96f00d388888281dbfca572712344d5a232ae12139666a57a7355aa26b5cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



