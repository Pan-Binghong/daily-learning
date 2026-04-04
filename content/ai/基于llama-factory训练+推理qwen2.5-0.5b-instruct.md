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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ETOZ3AC%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGmnVqPC3J9BHJF3ytgOsDWUwrU3X3vYZbW4Cx7HHRy4AiEA%2F9C6hcjXYF%2BhWbB3YWR0tgDQiDIuIX9YJrUhQk8O51QqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJiRt3fShBz7qZwMlSrcA9ob8LR3UCM6RVSieLliOQik21UrY2WYIEgWk36brvsOuo78G2dHriiHNAP%2FcQ9uyGYXvtwKm0EUyghuXA57O41a2QAKnu4eTsr8J7mkk914E%2BHRVDXUcSO2QJZlc6fVGc8SmKweUguhLK71QCUPx58w9bxAH0Da%2FcOe7MHHophWV7%2F%2FVvJPCt9nO98%2FwaFwmHXEzgS572L1bdfu4MKDdJNeLwYShOQyqA8rrFc9g4r0JJ1wtQbFuRzn6dPOi2f2Cy1JEel3qwPGtCdV2jQ4PypDbXSSLcVWKuNekLId9Mxk5SAJoWg4seFPM4V%2F%2Bdjc9YNQnuIU54tLhhIHNUA84DXKk7WUSqpscZXXiDxFoR4FXcJerXX4mdXV2ze5rkXOm7N6KG2BfL6J4Qvt7XySBmRbngevz%2BafOkTLcAVsP26tZYq6xrdzJhvPe%2BTdweoJNdGemWAc5QOhcjeaV4yas4tRtkdel0mFkso3TJU1phZ2e7P63tDa2UfxX0uJHcW7LhjnzldP6fnHHrbjeYyJTGcBXJTO5tH2VBCWBK6sIXDYkx%2FMON67rUWINFvfaLqTo2uUvQlWO5ifUAoPWlE4S3AT4kp6Z71q%2F%2Bs5EQYC2ozL06J%2B3xTT2nuwPRsRMIPkwc4GOqUBY2l2EwPNtUYrdF%2BRS6bF0yEk036OCxeHyEKNcNt79NZnAbLPIgccRgJWQA03IO7C1FFexi71SLTth88wcIvN%2FbG6uobVL2FJ0Rm7ZZ6nC8dPGNn%2Fqkt9QRdgJGSQ7vF3n67Olb3bmZM%2FlNdeWKO1M3iNiKKtrBsNSVnUgqRMDMwuKV%2FwovNLwfIJ2c4IcnRiSx3Qno%2BEW1L4kj8KpuYz%2FJFBySzL&X-Amz-Signature=0d2d08886dbbb5c18d71e9af56eb1dd4bbbe24febeb695e387b37b1908a0e8d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



