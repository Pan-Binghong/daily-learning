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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QX4ALI2M%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGvZ8WKdyMjpkcayBvjpSX3iId7y45IDTeev%2B9WwraBUAiEAuFMGLR6lsV7P3TGU2TlnO%2BAZVfZDzTkaOAY0HBqrecgqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHLx9YcynK%2BaWfAmVircA25hNK34yAdQxxw%2FJZXXZ2EUMQENZVKMn%2Fjzi2BLPuSm7d7AtrEBTEy70jkiwRWWZRI0K1SXuY8PljEJGbkSjiRex0DEj4rD%2FgC%2FvTf5RcGil6pXvYYLDkPIaPW8jBGgC4nFxf4pSEKRyXvILh2JxSNGKJjj4m6RFvSu43nclBZH6uXpxPqg7dgRMgSNDIgLdxtaxWVijtJ81ia%2BEGYyRVPGc2fqe2RKYignrLHE3oKjzYSzH6V1GihwVRvGx9ntJ8ZDjI0rlRAaJXqLAg5szffryraV65t3W%2F9mqBuNldTvax4y2GjPS3sJlonp0Mx50cM8sxTLcHeX4eBO5A5zjwC3xqgw4GSWH1YlJXS2GWU0gGSgzWd4MJCZxlyOXhCR57l8CRy7Fg%2F6JdOkuXEXomvHi53jIlt7UnuGLAhfiaFo3j65vm0BI2oRwdvwGJupPCR23JX4mPbjCnsX4QGNZqm3f3zCIba0nkpAl5DHI4S2AyMApqzMAM3QcWl1PD9Ttu5YVQiEXtLHKf6orzQbO6STISnK%2BH%2BGACC72XzkTe58uAUQHXUPgGHtf7aGQr5UolEmgRyDegd0NuIrfdX%2BweKAb44Ld4a7S5pUe7KxkUsGoi2aH1Hv4IezgqmIMJHyr8gGOqUBHGw7m72HPlBZlmcC7l09WrXnvMxkXiBhq5D16%2F0%2B0TreX%2B6mKyGCXotWRTkQnOSaWaeA%2BEYpiB4bdlFAH1EpaIGEfmpqY6%2FMHPx4K%2BIgNltuaUV61TazXQOJVCtcThPsjndAIPpkZKB73AsC7FsmFEfxMj9U6E1TUtkgrWQ8Fbi4O37okx1SRXUSGZweBv4pv9vSbTR2O4JTekPkCHVPNwjX1kuh&X-Amz-Signature=ab3257572410c0ce98ccec095ac4c99fad6bb435192082eac4187eef24de48a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



