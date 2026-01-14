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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662PHSLCOJ%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030613Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJIMEYCIQDVGlKoDeNxBzepECtKXHiJxO%2BfAcvZP48AzxkUMj%2F0HAIhAIZPwRrDk6t4bwnrhJMA5VZYpMKiWaKv9SZ6aS0T2JXBKv8DCBMQABoMNjM3NDIzMTgzODA1IgzXQcjioVzgSVzpmOAq3APHdcimLkIkqszcztXoFpJhm1Dao%2BFphyBx4T40wEP6etCmJIYTPNIe8QffvvLKVFJ8kIhHfm5BsLiIQN198BciBQ8eIXFrMyIONUc9YzNwYBr6cgyasE2GeoRhk8%2Fw92fp8BwIRLK5cXZaS0HRTmg1xcZE9djYH3ZPZTGQ0x0OAc0HFohTHdY6ZxJvSDKzb7027oXfTH8pzTvLudVdV9B6H0Ssyl7kEMeTYrB5RzMjPijZX2uJqmAkQrzuPkFfJ2pEQX3fY%2BtcfqHqvY0CbihsAaTSMjYvtXybGg10ddHHrtukeEUmK0UUZGs4zt%2F879izDT6AoBDgcG4issY%2FvPxRRQ9lLhE2CC%2FVmqExRYFGWMkoqsJeUlljkyob%2Fa0cBCm6dDHcr2x4MAZL4UrFqtjXvSLqAx%2Fo0QNnlRCWHGkCE8OKSXK7oRB8cowF8Rc1NoitDfnf3L%2FhWzKpxXCsd0SlvmIey1RNKU3UZt%2BV2luEHKZO9UWxlzG1C8Fcbbjs26SoexAKsyE5eks%2BEBEtkw7cYYSVfwivIC865Hok1ObG2DBOU2xVs%2BuHIgY0xqfdeY4MxkI%2BOPxCXb8ml3hMngekDWlyLbuE8vWna2Aej%2FaHPpM0Sp0rgWhyY8%2B3rDC58JvLBjqkAQV4VC8nem47QQY%2FyMI%2FlqcPy8gcAkJm2lPfgb2TmLe0hnrWu2aY7c6FQr4Nx%2FpESw71oSQFJOzPwAFOv9cKMt28dywFLXQvOYHmWZvd9rk8E0SGIgVMuyKaPM37A8fXAMTEOnIgpL2cIqWVnZeuew9qKwdABnu25pwbp7DvjblmJAivpBvWm7JSD83n6ZiN25mqKG0vizHQgn9X2CJIK4wr2Ese&X-Amz-Signature=b95290e9e0e21a03d2c804ce52700a008c98367a9359c9608f06114c6ad78012&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



