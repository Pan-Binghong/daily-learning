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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRFY2257%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBDsFSf8HZB37Mb6FPEKw62rYlQi18rPWQWGUQgVrmUaAiEA1zezyDeiiqF68a5UQM8dyJEiR9gUTgvTf5mcBpogmDwq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDOqCgwizg3%2BhgTr6vCrcA%2FCua4bxC52XKqnqwRXZKyQBF0oR%2BTJiYu6YmQZLQZIbc7cJdvIbow%2FjdYxmdAqqzHnsi6XfDOQzTRuZ2aRlnJJznXxaTwWVrjIOjY2GXsj0b%2BIYVjn6rcGDW4OmcKZViJKpkRQF6RRPhEh8TqcM0jOGYvCU%2BW%2B7DT6RSrneZLteR2HG%2BT4xYv6HLe1kts7E9vxD83LWLjwHx4%2B3tJImfSEY%2FOwUSYh8EWMtcb%2B%2Bsz%2FiZ8EZgo2z0j8ZEa%2FuWQCaFg00PUGuEh8NxV1%2F2O3kRc7KvX1HNLTBlC6c9Rur0SqFMhfQgdqxO%2FvTBGD3xQOxg4EPxWD0Z%2FwBTkyFlM4z6seyQeF3OBbT%2F9r78TZx1OgnS%2FeUvCL4fZDjBI91yJ1K3q7WKTOz%2B4KNJ39AKZPvM1V0EZ5oi1ZMNEOSoccLMTXmaxpVFMK6gwPvQ%2BzpeCpKUgCa6jeCKg2fX3bb9y3Qmxs9geJlTqPPkuIrimoCYsZAhFRU8yyjx1Y6yT3nBwqboW3MsbcbmTeZ%2Fx1GN6uKeYdKQ7ADgY7jGLWBC3zNifQHZk8HG97XBieRnm1K%2B5gpOyw0cHfjxyneW7x%2Fa%2BOczahzx0rtJB7z6KPk2fiBrcrf1HVy2b20ScsMp9QZMPOuvc4GOqUBbo518idTbABfMfWBvvsLA44pbTvxXkAkv4y9XKKD0OTRvlxAFjlG9SwMFfEEf%2BaytUNx%2BkzYKKP5SP3lRDAesF9hPhkn42ajeFXdBQ0dJ8ZBNH%2BMOs8pZJ%2FkD966qMYnbN%2BWL50JrQlpb5vIThTswf9Shz1oX33bSpt7j01cyN7h7%2FykjMke47mvAuu%2FlLr3hfjyjM9vfFDqXw1trzs6xu8Keavu&X-Amz-Signature=09a1770b72cbc93cbada56c3b96485dac0cd1789d5efebd682bf21ef72bcd4ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



