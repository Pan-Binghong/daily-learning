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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VB4YA74H%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDHaHQ8QnXmRELfGb9fs5jKlX53NN14%2BQ08AnaKmz5utgIgYAmN5dJdHCOpls1jZHxqAPU%2Fx9q8OvLYCWaaXxGYXJgqiAQItf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEDIXTUfupxCwKASpSrcA056OR7a2gpsyqOG5V9NVEbq2vVIYqTRSqzYIKdSjGF0UjlYjAWTD0lsrcR5LmVjnSTqZ7xTh6P8aDiUxXMRlAQUFzwsyaWyk1bZ3%2BG0i2mOVLkfPzB9To7sY2TApZVGzSOLrwc1l1NDM9AlbLynCTPw%2Bd8F2L7w4OEbvomAV3ZITE2c1LSHGG%2Fp1B9BwKfQM%2BG7WKgelH1scVH8YFxd5dDcoGlqRPWML17EEwc8u5I%2BA8qJl2xCTSZTdR8oINiO8iFK0W00H0DaflALg4xq593%2B%2FZDO40D79dqkRopwexx%2BJnjYf2H6xorJMbmuaikIpp6C6wrWHkPIrPNzs044qM0ukbQyT8%2FcVhpcuK6LSvSiRXo65xDTcroXmrSK0DRu1xE%2FOAPeS8AavwiBR4B%2BeAef%2F5sAbY5yel7o5zmfexLJcZbPSll9xKG96eljBy6DDAyO2yasx7%2FOytuht7SCYTLWho5h%2FD%2BYY%2Fo3Zz1FugBNdj5FOEQqnp%2FDgVk9V1qT975kDfNsNuEqdc44I4B7efXLfaEU152Fgxl7Z%2Bhrvx3%2FwiYHpPsPafzq5e58kYqUrzjoY6CRG6B68fu%2Buq0ZxOZi4LYwqnFwf%2FYceU9Jl2%2FLEsvaylocX7IEqSt0MMS1gc8GOqUBX9Hdh599dptkLWlqz7oGV8zosv3MKuuQEoQ2M5xgzZcEGvFsjHbaWLbE7x5r4iHCmccKpOQ6QFJUJFH%2BisQes6i%2BAMd5i2bXEzNf1mLGg%2F62DkRIao7Kb9Oi02P0bN%2BWrnqfBr%2FfVIHf3W2NZdvELaNYPUXR2e9phNWia4tmz1cMQPrURQTpeqVD2yRiJqQ%2FezgkL08dTdZR8TzPrRgj7pL0Mgi7&X-Amz-Signature=4ae716ed30370f7cb71c7450c907bd1be42c28ddde6438223e8990c010506ebd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



