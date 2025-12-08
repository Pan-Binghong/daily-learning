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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TD2UNY6Z%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDBzC42zSmHBmoa73%2FmFr%2B3Xzii2O6%2BGbUFdjFFBD0inAIhAJtsY9SwfOHNOF8VA1JzkmDG%2B4s1MVBrLqyUtEpKXA27KogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwomJEPXWlSH26K0tQq3AOBV8EKdLUoyg5sO64ztRBAtYGWPBHcFgeLH85pMc7WWmCUGs6TJhrz4Hy9lViPAydRTe%2FCJdkziEoKzzJmpWSzQugfo7Sz6nFpplyIzbeRACwManic9XiuFlo%2FWwo1zZVpZhXej85Qgnq8HB6qeqwUKZfGH5WpcDrNXT9NwghN%2FG9qmA7jvCEZdIzigSdimjeSc3FBZHdtntUzDcAhwBYGHAKVZO1N%2Fk5ABp71LLT3gbwOJbhhGCCC%2FnUPfnEbohkUOJ06RxWVwdIYO6yH%2BScxja%2B9Bg1aoZAoT6eitOQohkcGGhO%2BJDsYMr2oZA8wWfNd0IRkcdEF%2F0yW0nLpWkWj5A6pk8UL3Bk6O%2FKaC%2B42vuHBBzxKgWGhCFCqYo%2FMUPMWMGOIJMvV3JEN9QRbIQkVSdj%2BzYJ3il8syXOK%2F6drXNhOLJ%2Bmcq7q%2B1%2BVpDfvWKwhZ7V%2BAfkiCKYc7R7Uy6mlhYuJlnekwPMAhoXc7e6WO1ta0Szu6ZsNelXH6eXmZpatLW87qbmYwq1y9sYtG357u%2BSsRFYVRQAgV5vbFTiq4GuCnVlLZsN7En%2F7rcWgMyRfxQiRevJzJA9omVnJZEvn%2Bm6nbq7vy06u5FTB6RIyUPdj4KpVGJzoMw3S5TCt7tjJBjqkAYKIfyIlxDD49RBUkGlrfDpGFPWTCrhux2t6PnMVi%2BUoWoh%2B%2FfF2UB0p%2BtZxnMAGwVVQmmA0FtmMHmYUhlFKaLs%2FPJdbOkvzSEm%2BuktejhWHgD9vEezJxxQF%2Bq1BWeBv3xCgrmB4A4asI2B8ccWqcl64d4dZctqufzIcwR5CrLxJR3uGMra47eqeu9%2FQ7Dt%2BIXpgGv4bOc%2FcMnB0mGJgtPDbYeT6&X-Amz-Signature=73688b919ca144bb6e14c9fd233b87cc8c38946af5b42bbce93fcce53864f247&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



