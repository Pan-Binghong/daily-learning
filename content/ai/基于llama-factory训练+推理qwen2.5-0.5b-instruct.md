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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVTLNTUC%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDFZ9fjMcoYYrxDUv8wf6ofXcLfQRbWUs2l%2BIa3blKhfQIgRwlo%2FPU7CqAxZVhMdtgZXHC6I%2BOrXgGAHez2uUaB3XoqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOqBFpuu23WiBaTa4SrcA8yn0OUhpLg0kN0%2FEgX9f8KDNMQ690TS3HPHpHSN0h2pwcg4l0u8HjArM%2FknuL6nru0SgYB%2BOHhB2aIWKgBF6b5AxYvG%2FLAj9eGnlR%2FehxwBgAYhq%2BZz5t0lPecLyTTbS9W8jvV27Te47BKGZP6A5iR9w3%2Fogcv2AqGmgBrCzQEVNt4Dsoe8g3SnY5hMFT1DdvSB3%2F919ibJ9GN36NaOhr4qBfaMY7gEAt1RoBmtt4L7hzJ%2BlKxTktABVzPnmXOXNsCPpQJJLT9nQUj2E0b8KMvDHhr2ooARDU2TMfq7lFzlR77vRiYU3LCEo23nDsgOITV4gq53DMp3qjikL7GkMu%2FuQTdSXWPM8vOQifRX8Yr91lavZiBx9wQzZ5Om4sXc1u1F6Yuo1jnmaUXd00QMudDcgjroeYBrOH3hSmcb0ZxTiNvKWqKMknsO1D%2BPh0Er97WjPgTZXO%2BMGAM1sXit2Fwla52jKIyyXSS%2FLYbBAFQYH6Zhn9J1NLmSbd1B9sHMewXzAWXQUSPsxJh54iVRLB6rConjdgH5WFOnRyhJhmIa0ycTy8DlE4s4JeYmrJHrx0eSivrlxjnwBMwBumLwQtb9EoW3Dp1wG%2B0HYcC6fQ348WXo87Ibdr%2Bp3iLrMPbwr8gGOqUBpidGL%2B0glAFesKa4ucbmbQ8TkSgdKv%2B9MjpWzC1z9m9kp3deGTAWFftHQFnsK1pVdWjkl3a72lwUYEcAGFujaIlYISIfOri6AE7YffbHpmpLqNHsDNnsif445j%2FP6Zib67AKrnaqcYWnJGbVnQnDCmH3oC%2Fnub7nu%2BUJCj3pWwgYtGJOQXr%2BFqvMcELImS0JWCDUYpoBvjzaji3X3Lzq6IECZ4pu&X-Amz-Signature=0232e757330db25ecdc21a7e65506b1d02679c73e37cf4786e844de70fc1e7ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



