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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UMIF5BK%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T040955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHlYgfoG2M0zthJfHdMNnM6lYcWWQaEJEOCN1OBpp0sDAiBN0VpqzeaNF1Ir0AmRA0jOikm987VlqL5gSQ3L3Is%2B1yqIBAid%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWNy7YP4LgUqRxJ0SKtwDHyUV1uk%2B%2FoQIxbnnjtHni2v5QSrzN0BMAHJXZdb2wnPqD8R8yXvUEjbij8cICxYxATrha0z7wbINuEMkZA%2FF4S4JtzWaTiDSJv%2FkmHROM8ViZ8j4GIkWuKiUktgQsIN5lZoeoRe1KjXoAH%2FsFzvajVwPfpF2f1jIpkK%2Bm1Yj%2BHW9MqBGqzC9kCoIZC%2B8GhhQKmDjrYxlyJJX0LvvzuJq%2Fuurx%2B1o7Cz27C9%2B2vxB5TIOLYFqiKFW5N9Ef01qsAenIDbBUk5M4FAynSC9zz%2B1gFOMSUh8w%2B4SX9SKUQ6oj%2BFuWTTzTDR68JMJRlU7xoQFl5MJd1YEZOz817%2BpZQcVCMLbq%2BUEgkDLOd1SwqSXATtr4SpdwEtb9TcDY%2BQR1rf%2B1MofM638Wh4nJjew%2BhGVtNwzvCNWYhphgOwbqYZbRcmXL8OzawNpQE5pScs8LMp02zTswPd%2BXd2Hhwwsgmg%2F3NxHZ%2Fmm2O37z9Ew%2BwAOICM%2B259K0ZTbdaNtgr8UPVxf0pZ4lKAvU%2FaHo6vcrDWo5Kdf4ZHlAI5lSJIa7E7JqFwtWzzN3U1rpxUE1kEFN6H2U7jfTKsKO4hTsxAUPL2zJnv3vR2UBFXx8rDtxzaQHxik%2FbsIIdIDcPF0%2B6ww1J78zgY6pgHb6Fn0cDTPqdZeOrKd06yDxpwoQKYdt4Ro9GPbwEJs5vkNKwPtosaSCZ7q5R%2BiwEMOBLud8RTNGLEYiJe7g0orKzKmNk7hW6Q7q3EviHYUpu8XW7PanjL1iS%2BF2HgnLQB4fQAYE4bFLP7Vc%2FOWTHvBQuJur864XfD5W8%2BnOUn7CnAlnPat%2Bel8IhXtSgtUJlV7EPLPOAi322vOLVWt6jQBEy50NIyG&X-Amz-Signature=e8d6fe69e6245bf190c67af7f55aab775dddc12e899452c3a512138a59d57dbd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



