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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VE6EGGV%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T034922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWZeN12MAyuUHVVCokDKVEtLLWmY5p9RQPY0pW5fWqXgIhAPlTzDulwk%2FoeZTNi%2Bfh8nijgxtygCz%2BO3W0cNRk7K9YKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxOCx9a3A9uIVLQ6QUq3AMd5QRbrWa4FcACj1H9ONbjQyIZRgRqrrcblv33tVJrxeNCOc8NA2BUUg6UOpMBQMawgzQPfJfAmM%2BJPFHm2OtXN7vt9NoA7rV15C3JixcIy4SzJXOTtAnKZpJnWwXhGYCwTEry8zdIq%2FeZHOpflXtUiXsRXiVY4ltKI7geYxndnN0UoDi%2BpCDs6PvNNZP5UkhoHY7mY6WcEnokJU5E5Ec4fe%2F98NHTZCu8dzAF6ANix%2F6CP7PEbVaV7Csq%2Bnz686VwJNIUKpTx9HGnsnSEXFnvwPEuqs408x32GiBW8DNvpUpVqpF5LepcAW%2FZ1iecd8wRHxJ1115jHsD1fdUAu1nGWScTnQIE7IpkFqb2Cm%2BQqdVtl9yjhARj5JaV5187K4DvBK5ZrCydtgSYugqxtj%2BOf6UmYiCk91Y8a41Fc2HU9XiZ8ZNy7Amj8rmnJdj%2F2ttcwk26I8LpQpXYj40bZPi%2BN8hYWyQix%2FyO993BIw8VIawQ5M70yPdLSEf3SL5aj8KgRMtAHTRKC6F%2BC8%2BcG9PKQJFCHQr%2FK09g1YYkRgmE1pnVdjJXkIK5PeiDvreLNEnZBHmEhN%2F3JkxJzn%2FJ%2BlPw6hBgwqPo%2FFryQNL0sHctSWy1YEtWgblsK0DalDDQypLOBjqkAY3DgzYR2xo%2F9Cxzk7SWHAu%2Biy%2BCwOVR%2FWQSHc0zdrd4tNYw0ud%2F15agpCraJWoZkcxbyKt5YlbsdfSW3Tl9FS9rQW10GlcUaH289ikeFpm6ewGdMnGDz83HHxN3IYqLrbK5cDvqib24PaeIX4UY2YIBhWkIy1Zem0df1c66mq1pkcd0G%2BqdoBmrgdmGQmFpByVEvtQ2H%2FCQx5OjxKuY3HUp%2Bqbw&X-Amz-Signature=e2f6e4d754e7c7197bc00024d86e2446ee0dd8b84e9062c2aff926202e6c28e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



