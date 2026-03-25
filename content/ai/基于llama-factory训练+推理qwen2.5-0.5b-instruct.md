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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YI2EMV3%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T094213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDHbcrE0ttHgfglVcYi%2BF80mhnCzhvUZkIJ%2FsDguzxAkAIhANrSHPrfpQuucg%2Bx2%2BD%2FIzXHlgu3C3Qn5vvufYS4f56vKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyPJzR2oTI0FqdKbjoq3AO3FIWlmvGsRblHWa%2BTiFJUymqMRxoILWuu2vFNXCvNtq%2BHwnfHEqK%2FoWD6GiSta7QT98oqFWVpZaoUgBO27nGRPEXOWvATlFh2nzEWFuUIz4VFCPjZFA7yB3cd8IO5doKFzOsYOHMBqYmlHK3XSqtl5T%2FC8%2B%2BiVBRfH4rXdBon5ti8VFEPMmMCf6nqRqpNrH6RXjOYwNemsxb0DdcNrPdvshcLqcXRoM7G6O9RL%2Fbc44ZqtPJVD1840FEumri6as%2BjZm%2Bk4dMaE3ANxpCKqEvaVcwnCH%2BBdj1ueupRgMNSg0g9SO08XnkNeQebojLHbPQ0ic9pJBvMQ72HoW3sjjGlAzkfmnLQAVnOYJqDWp%2B2qk4L5L%2BOlSgZ8GQi8f5WqFNV%2BLTEtr5ibQPZE%2FGYrmV0MJucpHUIOzt7zJ22BTt0CwQK%2F%2F2DbXyAv%2BccR3YtM3baQNG9c4Zkamrbe5cksueobuV7JmcTbHY8GCvZ3pk%2FuaAgYudyLJ%2FGkLSiopZeUYrUdmxvbEi4xwLIbKSXGKaLgzEcVrElrNaCuzk1AI3%2BAyi8lZCdEg7OZqM4Ill0ImcRRHXj7qON234RgmLvhbqG6ila2sTC1daxZanTAGaEZoRdkG3%2BIDphq%2FQDhTDd1o7OBjqkAXz9RsiZfmnLNvg9M04Ke9IM0uyh7%2B%2F6AFvc6el%2B5VN0zgm61pE40emNTiQ63jkBOfxP9s6H3c6H9dprrg2ykaELjT6iBf3LQEdUL2FIUwck%2BD5VV8v2oB6c7OImMorkXNkVsit58I2vlkZzm6ahu%2F7d7dXQJWkin%2FcLfab2I9a8o1Dx0o%2F7o9778Okwq1wvVFC1AFBEcH5J%2FmDQrhKDWHd4zXmE&X-Amz-Signature=864e3e329721f5f837226eb6027655b8f44f1ccfc0ac399f1043ec5264ec6e4b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



