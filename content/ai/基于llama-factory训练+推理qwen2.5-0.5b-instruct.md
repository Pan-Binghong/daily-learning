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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CDBGCBA%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034435Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEUOvXQYWEkleTz4YpLzLHwOvxEY%2FbR%2FhI%2B0LY9kL0elAiB%2F68Is63ZLDEeDjbrqLkzhsODWaD3TgEi7zYbrNi1AsyqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHxXjpPOLgTEyVbmYKtwDKv76XJDOhgiH5HdB7XZu1m2bvYyryfIfX5rhvuxfHaD1yjb95L5Zb6U%2BBXw9FTloJk1WodWuPrePuYQjwOa3IfyQAtimLrFGmutRU1zV0hlJtLJSV3Q6lBIE8lrOlJy5%2Fbv2qF3zQX1Z9fwxLbZmU6p2FHqcyT2V8%2FdbJ1o6fKKBqrUCX%2FDCkaSlwffAqqjpreWhmu%2FIt2Sb6%2FWT2e%2FTleiD81bEjpCrBmR00P8WJusmOVtGOzWxSx5WA2Zf%2FIRmnaVhdLvGXdwNUrhbm4889Ep1PgOuNKq8Nbt%2BjYrcrCu%2FSfyYqpC3OMTSy%2Fo9xYksA%2FkoVgw4U0BPQIiFmGJqWH%2FRoh%2BTpPyKl4chByshHSI%2BqgxVvSGb%2BK1p%2Fxl4u65%2FuTnYVDyRGwzXApbXPo7seD8F7pS6RRb6SeM2l0FjBEmV99AvQw74CNhU1ZzitHzCTZOGJ7XGEBelWOfiytlB5XzW5UJH1JVgZzAoJliiAAYMUHOW0nh77z4V9Np8EhkO7ijJaj94GnUr0d7Y9JZfwSQmn31n%2FvIsW7ln5dWLzWP%2BIYdi6CvYX8RVbu8oFSD%2FnBg4gbkq4IdzeyrWOsKIMsZmDdVK5LrgssHl2c7pE6ryYR%2BhEFiNYPzHmcswmpelzAY6pgFwHHj6T2iTRfRLiEePR2zJwD5IL74aPxAZiJUzi4niH%2B6IdHyiPady%2B71G2Y1zxSV2Op3xuWegcFKoz2f6Y16CmAvj81bVVjMq89SREm6McMNvGDMXxeMrwM3W%2BKm2SEwQYEkpL%2Foykr2%2FnVOU%2F5ohzHPBv5sR9IAfRo2DjCJgazVspqUhdHPK6skV%2FiWWURBqSf5Lj%2FG%2FcK6RW6bbP1jfATvixJDo&X-Amz-Signature=5f4c67c48109fd0ab040e6437adc1deb2bcb02defc28bcffaceed20ec5e517a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



