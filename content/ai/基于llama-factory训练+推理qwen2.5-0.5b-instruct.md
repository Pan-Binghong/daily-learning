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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNA7UVAL%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024111Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGnE6A01oFdm8kfJT06pL%2FkoCETAJX%2FL7WWRGrPpfpfLAiEAkaFhWxByfVc2Jmx%2FrSQtAT4JA3MKUicpq05DAXqpe9Qq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDMiFW1PQYGur45bxuSrcA7%2BXDB1ZTCO2iN2uvrcDWI6O4zp0yQ3XoDmonc2oyKCHtR6J8FKB3E8ItNpgXj15uJflQAaApWSdIkiz0dMXqzj7Er99Y%2BNioX6Em8ZX0Y5G1gq9X5QGYinlHXyLc%2F4JNbTqwrD96IS69BuAbsNSkNbK2hEH54jb5nmZi7Dw5n5g305y65LgeEjpqsGk6hcGdIVU5uXNsizqiWHfOB2NXvJnUcYYD4KiLCDe4J%2F6AT3LL9jYE9xlLh0onM3Zj1kBCgcYbS93g0BIy8DKTDt2BvtQUvc1t%2BGOmYvJgomsDVsL43ztF7bE1C9jzhGR02ecFdntYCwVOJS12vVT%2FodNO5VTj0I7o4JxsNfA7zU6EPemqDLdsn3tVNU9zKF%2BcDod%2Bg21R4ZmefmH8p3Nr1u7PZjkk7Lj%2FwgoOpHeG4Z1f0omrFf4NqtFAaeIPF6bKqyGylhKIX%2FRRGYbnGRKB%2Fp%2F12vHpYLHwe9V1b9P2h2dNOs0ordnKbo5bGc%2B%2Fa8U5RO3DfmiVPBLR2ZUaGHWQy61FT%2BeYFYm2fguWKYOwHNWt8n3NB8cB89fwKzdpJ%2FVsvgjHYMNqULKVp%2FzKL8%2FtFmOXnAqdRNivrC0usseMNUgBvMf3JCFe%2FiUxAngRYbZMPmnzskGOqUB0xa952X8CRvYW2Wu3RYGl%2FOXuWPuSX%2FogoS240EZppEIYcuIm%2BedZJOG22w56S98jIS%2BCH9JpvMlzdJqE7EoNuB%2FBxWeXRD8VT4oA02w9cfGy%2FN8p1YvUTZtVsDkqjDNfiPT%2Bjq%2BSW0%2FIXU0QE%2FouXxnLhK%2BoQQC%2FEk1OcI8fE%2BO84yBAsycQ1ftYBPZQW3HU6DR%2FNvxlo%2Bt892GULB2jG1KIO23&X-Amz-Signature=59e6df4c97ad638541b2a24ec89802fcfa65ba206dbb4fc62569631a36b9d241&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



