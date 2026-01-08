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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOA3KGEJ%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025903Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGbzGxj1ee6dD6g%2FjRpppIgXtVzboK4%2BQ2DWiEpa0FwWAiB5t%2Bmhl3qiETdyXsuyr7liDvRxJRjn2FsIYKAQMh2YxSqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKWU2exfYvElgxJy5KtwD1czyFKotwfuXXYGcvBY%2FmFDzMoDg5%2BWfhE2pzSUjCoRpMd3mvkpw941DBjwf%2F3QzYpRsWtrUvJVa9y%2F9uBxafSuDysL3dW0EW%2FW4dJQXsvVqnxFVpV0qjyV%2BZzB0NHgHPtfvKQjxFJtXahsw8u8qeQkfHNyohpbI%2FhCKt9TscOMzP0xN6ZaGVAYn0N9c62qj%2BzuLZ1KsEzEQU%2Bi%2BhQbNnXR5JLtrkupybdNbajCmNikUwVkwA6R%2B1PLozzFgYIldhxVLDMcmyAe5dwswRnU2m8KgEBxlJjRPKYSM%2FDQE%2Fgh6TUCFW5C8Tn2Y3q7PRfgOyXrUJvnT5YsOC%2B298%2Bd61TNXXWKAaA3FmfIPm%2BpwvOECi1%2Bis4R7uUuxaRfAGsKx9ATr0jMC3MBDKj6i9UcvC2g0Rip%2Bv2LiBjdiICrsyfiucwzxS%2BTgESXo0VnrGU0oQj0MF%2Fg%2Fkaymk2e738xfGreT54gUsEZTgfikfA%2F6Iw%2Ba9ao7nrXmIYEVpi%2Fu5AMFVzuaqK909SfYllU3Pfr0dhOQc2msiLHlCROxwmhYSTJCVifQ%2Bzvird1HkK97LtjbGQMm7TkKVQkE5khErRHtJHJw34xZD%2Fa81JsM1zpUiNe2OwFFlEk4nBS4ZLUwhqr8ygY6pgEP2ZqbMYEIoX6n2KQTLNvwo%2BnbUz8gN5ka7KTRMz851D1XFfO8QcsjkxwMjOtWL5jgFCnxvEjJ9Nlp4w4iKXvGlrRgUcMxjlWK1CSbEzHTjVtcpNTW3bVbhDu07Aumt%2B11L4BpBy498l0ZEjlxkFTvLLAOWm%2Bm1LybcO2xMDc2Xm%2Beeesy53bbR0pTggQtvJkXU3G%2FSo%2BzVEw%2BKjgPqIyHOEIoXA6Q&X-Amz-Signature=6005aa0302ba395b4521b0535a719f8eb35d50df85f34e6243ab433b29da258f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



