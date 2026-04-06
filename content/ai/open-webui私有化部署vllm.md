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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RA33SQMF%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T040910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDeaflFztVIqAv3Ro71g0y29aF4y%2FLxMoGKZKRPWJVG1AiArOYwWaIOsWAuMbnJL6%2FbHoz2iG6LnP6DRNLx%2FVwwaOyqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaVJxCo6BfrqYF%2F3uKtwDpL7ZWbv6VLpi7uIF7lgV9zth6doOlBwSgRAry0dIn0p2%2BE%2FvFLB809CEwCkICrxdiNAO6D9lk5OEvlxSdYIY5JNy55o%2BWWWgprKCzETQkZ%2FOjhLWeekachIe5hAJzyZAde1PnYiBediUKY2M23YEgTSwoz3KwH89KwgmkDcQxf%2FQVoxZeRO3FQ3AA5g3lgnWhifkpQmDlGdsc%2BCpmbqe6FKGrDlPWEpW31B9u37VBu5MFRjQwO3Pqvp5fIWFwmT9ghyqEjHHTg4gZlCfz8Ht6ebhkHUEwkSQEuKz0CpGmTyOiFJwWEyLKgjH1wNvD2IS9iolSA5zVuE0SCDZtjiK%2BxwxceMKi8549K8o8a9TgMyf3RwKRJK1J9aiSJHJvllsxDlQYOWKHfEru%2FtlQhtRzCbGQYiMcs8ud%2FPs2xZXkP1XNntmoyhQVIVJWrfSq0vZSqchNIO44vlF96fUYq2H%2FQtRIkIqKVrJkHAaC%2FwW2bYDbBDJG6zoKEq70UGL06G%2F%2FRgEoSzBSXQZjo6VxFOpAZy2X%2F%2BB0nl%2FHfs7cHyuKPZdULsvYteY083MMlpijpCi4E8uE2Ctk7wmVryelmZMbdvg6%2FZhJTN6PoJbiFIwrnbRcH3XV%2BlXFHJBJCIw6LHMzgY6pgGMBAkq%2BUMq%2BZ2zJZgKZENf4BS6yWE1q3gKrUQav2NvEKqvgRQqy7UU4PuZ%2B36FSAKIVsyXZsofa1lEyub9I8xFzWc3vfAgz%2BqFBSrE5WkZ%2F4UsofRKaWpzr7jWuEVEglHRtpPBxrxzKd9BNGOpBjydIzHaYrcEVHDeZOIOaATjAz%2FFeps5GwlgKxjS%2F7OXm0Iv2558INlxDB0KvWfTlYnmX2KSH6C6&X-Amz-Signature=0959d6796d46482f5006a28dd80ca19cc10c210f23026e1d2ee91d1a8bf22610&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



