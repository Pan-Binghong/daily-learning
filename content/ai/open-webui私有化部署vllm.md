---
title: Open WebUI私有化部署|vLLM
date: '2025-03-17T01:36:00.000Z'
lastmod: '2025-03-21T02:48:00.000Z'
draft: false
tags:
- LLMs
categories:
- AI
---

> 💡 在裸金属上对DeepSeek系列模型进行指标测试后，有点无聊。随便部署一个WebUI玩玩。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCI34ARS%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T030004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJIMEYCIQDInhQN8rZUUr3hC9UmFqzSROlqF%2FAzw2%2FffKdR48w1BwIhAOcr56xLXVbYDxpjnBrjOJTpe745NvHWRlA7VbSza0amKogECPH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx6UsLnTeig%2FDf7u4Yq3ANOAHZ0V3njlJEsCwYZu6g5HmdkUxX9FpBi%2BpZvMdXHNMyAKw5Plk9OvuLo763KuqAtOx5RlRl%2Fbcn9C9eCxDbjhJ0YdpqvzXJ%2BKxnHDz4JnK828NsvC5xAkz%2F5v5wJEceCd%2Fej6UszEjXhI2nVk4gFkrAGwVvIfqaixeqG6jRDKXTqLK0xp0hNQozQqJCvUDeVVoLdkiL1eGRYyzANhQRdvOZg%2FGkEJs1HhFI%2BIodD1Denk%2FBT3gyAAgOykz10mRfbwurodWbvZh7W2%2BkDw9c4FhsnDCLydVfy1wB7I2oZ7I0UQXOdu%2Fa7Cenu%2BNEEIUzwhaVM%2Fjbcs8Pg8yML8%2Fegw6M8DBEe14RwBVsvroPHi8Lb8O60pqyA9PKEdvZh%2BPz2V2Mxc23VlY21bYGaJ0AfyTfdbO6suUuo41KRvCfUV9nt6WuvfjMgLGRbq3MKe5hQfMISlO%2F96lr6Z7FJz2cT3uldanxAJsz0aknilQG%2FNmAklO7v2bWo0keAjCmFSn03Qvi%2F3bUlUd%2Fih8nOpHQb8vFxHKmEtI%2FDtvGv%2BSpAbs7l7KwbrmY%2BTtijuayY90X7lV1dpE55jw2A6jIc5XgHBPVqGR24M4xoJacgb8cwY8pXNyNKrHkHLxrckTCqjNzKBjqkAVUzSJpZqVZxmD0JniV7%2F4fF27RodIjObEBQ5Bb8Yi6Tvnd2%2BxQ0H501Ghixj%2B1RmTZkVeQpKDLMxLOUaReaVA0SBR%2FcLe7nUzpRlVtwy5RRALGH9aXUE%2BaFaurnPvZ6t8Q6MuMOaWTpUyWdVyo5fQLJac9Qo7bw%2FPQiveqJMC6Uhld9IPVxzWkfMF3myXyvaJNP6ofE%2BC%2FuBsGLz8ct0EotKuRh&X-Amz-Signature=404a179453b85b0d6682cb8a185a7b4ed04392123b39031cc7ce7fbec851bad4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 安装

该前端框架采用docker镜像部署，模型采用vllm镜像单独发布。

1. 拉取最新版本镜像
1. 启动容器
1. 打开浏览器查看8000端口 
---

## 踩坑

- 模型URL地址要写V1 
- 使用openai api进行链接一直报503的错，进到backend/open_webui/utils/model.py，注释以下代码即可。
---

> References



