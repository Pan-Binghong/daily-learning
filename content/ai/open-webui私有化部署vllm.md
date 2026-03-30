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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSHH5XBD%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T041008Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJGMEQCIDq36%2BORNaDzEP%2BUVkGWuXWD2zmpWIJSf1XXEsnwKS6kAiBTdQEum2WrlAqT4xdVKZS23p38TQ%2FYx82MdY2JpOedJyr%2FAwgcEAAaDDYzNzQyMzE4MzgwNSIMctrKee7PoeqE8LyEKtwDj%2BtA7AKykwMOBVkCUQVK4zjVYDcleuAMKaj1O0l22Rho7UDElVfYklCugnQ3uu0YY30giY8CYIVKM2V23jxTxeU2dLpEwK4ryOYEZei57Z2RL0QWrBmk1SoU9IAFgLCRODoG5ltkWJa7VxZGbBTYLtUWvMYW3MnDofxEE1is5Vswh%2BHgqWYAj4H27cpWTqogxLqYiCLyZrx8khYiiADabllmI01zd%2Bc4ZCf7uO5NZve%2BiOMU2%2BhyRLPX9DovllkBV9ImBEFnyt%2FpyP41pF%2B7zKZt75iFnLZktUYcPHbFmKEUmwpWtDfnPKZNBICaQBjvIGRNJSfbz7n97pN6Ndm1a2d4XW0H9v6CF%2BYmVHat%2FUGFUDW%2FOyfC2oluFwqTjf7PZJREuaZkXCObGkeLhNS%2BQDYw2p78AShSClRkCjF7anv6dkdIBAx99X9Vd3x8LK1en0jiUEb8%2Fgj1U6%2FQ6R9DrCB%2F9FZ7Iwdx1%2BsZ3xTaoG9oRMSZW2sAJSjLYV5RhwilhXYnsdK6ZCzTgK3mEG%2FueyrENRTJMrE51dzY2U4nMiHkHqPzKsN3Nw1f4I7pzINvQg3InctrGqm6cDN8c74HEh6O0fzATu0TKcx4HNTT8qtuoms1x3eFesY%2FQGQw3MmnzgY6pgF8nnbCmzBlh4ULjAFXEtncaGD2cNUySlQqV2UPgjblbw5OqIkxUNih7D%2FM8vaj1fUVki51gl9KvcX%2Bb4lfEfTTRH7YPd9dNNHDZqWvqkmbe%2BaoheIx0D2BlvlA2qm806ZVZX5wkhOlipz3LQSo%2BzpbDD5RcUf0wCJ%2FTKmBLe8PgK5p1kE4qBaurFpd5UV2osa9NNSstcHc6JE8553Fh%2BTdW6w74%2BFU&X-Amz-Signature=9ad2ace57ccd5ba8fc4371492e0c7eaa95cfec68b721e61666a54b90e72b4e99&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



