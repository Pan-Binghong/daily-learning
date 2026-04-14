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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663CDKJW3N%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041110Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEj0DIKXrF7voo81tQafgR18ZVhNMhR3tyHrggTQrUeTAiByisr773OFaeasvymi%2Fd5sM6tRhOzgedo1TXMzT2zc0yqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtKcbgeM7Ta%2BcNJNMKtwDSVNC1sMj7CKITlVqV6yw6I0%2B9hZNyyTZz95c2ogBZ%2FKUVZUqyLM0mRiC7YXj0awue%2FGX8h0TGpKjf8EsUgDH5kcUHk7nxSa0Ivyc5NuS9waMoOyxuWv3dNgFbG3h2xyzmy6mpbXoMRSaH2d38LXBsz1Iwe7CYsA6x7gisdmoN2bpitUDVXKk0zLYOjZIHs%2FEfcBJkAcnjC4r0EftXkLCmOxyJataMuCXQve0Ogf%2BKwX0rGbPYUaCimD9%2Fv2%2FJQiFAGpHH0n%2FKai%2Bq8YWTQe0HLkfo%2FWsJlOyvCQiLvqOPvLJfvJLMFo3lLFTohXqF5HTmqXokgPh8yVu6ytfga3w7fiZhSuZ%2BlwbDJ8Jc66EjfhGSKmpr9eDjsO%2FIBN%2F3tnXfsG25YbJSHvwMaOc34OEtsbdC9LgM4TMnMtndk0bsp3LcBAw%2B%2FKaLVxmBihz52ul0WaqqH9x0kBrwEKyu1ORkTHfTdG%2FYjhp2aDMUfczpTZTKMEcYwmcUUo%2B3U19jR6uKoetroKFQzGQoB9n4iRZrihRtc611GVDq5f65eUFGjoMQBA5XHpaO5cnrYIHRhVEN84CO6hEpxNq%2F%2F908THPhPw24EVzZDgYsGhtkUtZKz8FJFmmkaQZmlPwnJMw1t32zgY6pgEeWykf4LNHNJIX%2B2OZw%2BByE4yRLVduGiurzq067Yy8ddv3MdiXajc%2B0oTPBnfFdUmdTCmMrKTeHJomShk8OGNfH%2Bpa7IZjTeiifkRhwqDLo%2F7Ss5bwn86GSzeZeePQz2mslioShnP83m2q5QzIdDDCw8g6INSZMP02zFolJVMO1heS2qc%2Fx1e5txJrAYbvjuyLQsobBt3lvuLSzY0%2FwIZkde72Da71&X-Amz-Signature=5110d6ac0af31fb717da458c46a864d29b76dbcbd90a67070f8ab83bf0ae8e6d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



