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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCRX5HVI%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T030903Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLXdlc3QtMiJGMEQCIHSId0bpyTB2YoS6hrrlzGRckr9pnYtfBcU8l5cQ%2BpBcAiAnfTWQGGlALiNT68jcj74IQn4RS4uaYXD9OTfiKmnigCqIBAjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMItyuthqcGClt4p2gKtwDNDXr4Epq31%2BO18v77pirLAL%2BKm9a74Ecz6KniBmRJIKcojg0Tp%2FmYgWsSRa%2BW7RtNrhRCU0fN%2BXL7Cs4o%2F%2Bma%2FY%2FkWY2Ok1J3gihdyb1y9I8mITyDR77Rx%2FBdeCW0CRhNQh%2BVO3iyUNRqJLiktIbNPvR5KTagBHfx7y9ZJ7yaXboIEbxC9YlCig0Ag7PVK1aIypMJDvTIp%2FOYFwj0b%2FynSlaWJyPQN6Z4FXrOJrSPOsTRQDS7NeQsMCWc6s4NcmF%2FKKDHNNLxD5qK15ZpY%2FjwqhI%2B%2BG3bQyX%2FwZYqX2a3jPE5o1W3E4fYuxHW3fygi%2BygFzFb5hXkWC4fXeHTeL%2BXs%2FZDYGixU7yDkfwQCxnRNfdxJIQHasdYpAKqM4P8kbMDG6kYAuBDgGr%2Bqa4VS6h%2BVMakuD2ZdaQA8v0jnq06biDpJuI9CGPAfMuqaJrEcf3RU7DSWW2vVWEwivJnvGQqoqBzOIEXxG5%2FcqklTL%2FO%2Fokc9MXoVfWeULXOcs3Ph%2FKqOo1%2F1qf3m06d82bIVZjBUrloTnTJX%2FZVTtHNrUw7oqaSgMmXlm%2BmnyqdYF9MsZjcRYPkj9MIAo8XZn31AbgS4SkfwKp7JCxExIMPi1SdERWoGmbP%2BmoT1sLWK8wnvuyyQY6pgGfE3a6odn8ft3lTVn8%2BZ09ANOAZflYQz%2FvsGMHaNjScwbCzeKn0tm4SfHXlXHZJyBe9UBK1RwUR0mZJP3pu7ZgMkG5LF2f7xuh606iLwqqK7YlP6YWE04ozPJOsj78zTR749EV0o%2FX25el0pJFQTXHybYuaqyHrVF0wYbSGtC6Mt%2FEBk%2B1z0o5vg05ZU1v4WZSimETcVYTrsqr7KCUHfSua%2Fk3sGk1&X-Amz-Signature=a888c5cdf61cbe51de0310be49d4e022aad9bf70f8376f97779e8470ecae229e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



