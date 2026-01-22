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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PE4ZKN6%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJGMEQCIAJSpEJFw5iU9mf0f3%2B9GBL7Slm9GqZbqwE8C3aTtaaAAiBrRfdQwbiDdDikmY0q0uqqiIcKRtQf%2Bub2xRrXC4AYuyqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoYuyOOVD%2FKTI0fruKtwDmYIWZuh3b%2FG0c%2B3k79Hpj7Ng9gZIjX0LU1%2Ffn5e4kAN43IhAmVbLNcIMSTlXb07fQLs3lxeNtI9GqR2iYmmQkf2Fnz4aeIVHBIvtxdHBx%2Fu1Q8pfQ86Mg%2FOXsNfaT143o6SdUDf3KzgElM%2FPOVOIF5l6B3w2iwzATTQKHeE3pDXRFFUiSUJDI26KWa8AT%2F78v5IW1VvyoO%2FrElUkDNRzlIekV2a7Rbr9vRCexjwSkxS62X1MeUru3mnbyynrXATwNQ7p0WNjRpsml%2Fteg2jrmGifVdwCmpyzLBGAy%2BWIYd01kfVdY%2FFlzUdU5csR3q0EjVeDWOugk1C97BqxrIwqMeHtVAUe1Z00x6EOirt4oFTF6dpo%2Bs8WDLwXYZw9Hdo%2BOnTlnRTCUMOaUH9eI5I8pcDPqC0drIfG6aOMf6ZFzH8V%2FxCLUc0zDIigTP2I6QhkS3g2bf755fMw%2FLIPBBimBGBNd4NLzSEY%2FqMiBL7PS%2B6hjf8egJ2a1zGC8d%2FMlJYxaU1n%2B1j3EE4fygQvSf3yRlZqY1DetZDfMj4GeZgvAuSvjnMMeXrtWJrdpeVTlCdpoR8f%2F4jpBbwTc2qeMGTjmDrUOounQOebtFAnGeSC1fy%2BqnkZ7TTo6t5bRQcwhtfFywY6pgF0vQqHq8nu5x4%2F7TKYdTa%2FeFwF%2FNdQNwK9OGQq24DJU66KVlkiN55WJdl1smy5mt%2BFcr%2Bsw6PXwYXGEg7aW2Ygb3Fac%2F8w9ZD%2B0215yxhSBTt4h2c1lm9sCWxRrAX0Fa5y3Xgk5f7j%2FK7xbgwLHLxykMHTBe3mMfI0arh12H8HaAZosDimiTdoRohw7qiNLSLhbuv7cB4V3J6Q0UBBaBPK2RgAD0Jf&X-Amz-Signature=63815b342cc421de515512e79e1f08b0518431111d0bde37edd01caa8993c3db&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



