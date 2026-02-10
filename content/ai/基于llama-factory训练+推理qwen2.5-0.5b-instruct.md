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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZ23N3W3%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEOhOEc7stE%2FQSNwg5FMVy%2F1ORIJ9EJaPaMRdk9zRmzCAiBz1ElFeDovDDgY411TEDd20rBA1EVtHZMSZZle7FQiSSqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMu%2B66fCsphILg3XNnKtwDVtTgwUlK0FMplknmaB3CzTOQ596FnfXpd0Z852GzE5Ds%2BTsw9VZbGn4kTMpInD8wbwHY1RUquAOfUpdX2iqaroQLVa3W136dK%2FNFttP8AP0Gn2mlzdGngoQIgqwgMUKlkOhOJuV68c9mxyliAjZFfPK%2BchwBSFtbcWnS1oE7wuctdpverC%2BnicVMWR6uumUEXGk6CrJ0yRS5Czm64xR1YGKT2Cl26kq1%2BP1NrpxMYQJPCwBcATNUXMyu5XiJYRse%2BFCTUzgbTA7%2BREA4YHs%2Bycn%2BMe1ejZ26qnCVIXa9ujxInNJDLKl95EI7qmBYBvKApXt0t5muLubxmufiIZRXPkK3%2BV18ioBdmm52wrvYWkiUyH7tlMXUpXCLHCyx%2Bzfk622U41UPOGF%2Fl0wG0SaJdr6oW42%2FPRV4bGzIYjgxs22FGarKHbnx8YFeSYNtCEIb79NI1pLbRzF1UzLUu4KLjeC06pQD%2BbALOWVPaBifQlf63YAWfTplvEoF7QSzR9uy1s6N3LLJO6w65%2FeoidhlpbkIVYw6a5HJJ1d8WNU3J2rU6W6AS%2BygULCqPetVtQPcKBc2EB9j4%2BaW16vkaRC0092Pdc%2BKPjdvCCl12vMlL9OLZJqyCz5%2B5HPsL98wj8SqzAY6pgGhYIjMvnXC1IPHYT7qlm6kxdDKMqCywOLnBeGvV0H9ug3FQAQEcgD3Uv%2F556i%2Bhy%2BlsMvNIIHlBUKZYXH2J2xd5BlmaNmIgRaQcN2p16hiUHO6PLg%2BGp9uS6a4s68DNdOQ9HQ1RCSNyM9CkZCN%2BwqtDS7x%2Bj5oloPY32jDDcLjLHRnhNrZ0Y90Z2C1Ucl%2BxsMy7UG%2FHX3qDrW2jXfW885BZahLEzfM&X-Amz-Signature=1bd3dad76c04f7f0cee9cccf2300fe2633d6b5e4da99e362a41aee8a9d62c0b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



