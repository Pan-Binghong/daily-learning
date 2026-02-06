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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLI625DV%2F20260206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260206T033337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQCbSqP%2B2PV4BVi0fghfryiG1WyK6kxsa3mwUNMCvGTS%2BAIhAJqQQL477xIQb0LeAiT2mFKeL%2FTnoxo%2BOLBOsicRgqC8Kv8DCDwQABoMNjM3NDIzMTgzODA1Igyx5gnruGWY3aouT%2Bkq3APJ4G5G9zULGIi2ErvJPLf9xIxP5UpCuL4JLSfT47Ks5BCOgvb4ICHxYQJLxNfA446PVzq2fq8HjE7%2FmgX73vJIqzPaA%2FXQxFpGkTo43I171YqkkCUQfHGsrguuFas4ePuimRyfLyTyb7mOk3xeeoTpyH4iC4D152oSVtegF3CvqUBnhtuintibgf2xpy3kEBm5CWc%2FFaSRUNBiJuMIx%2FmwWC5GaUqmfO1au691hJyiL9Pza0CV4VHy56Z7v3hZrbBiJG7gZn42TMltvYiJoEn2033%2BSJleeyIG0BQmn0AFEi5IwaxULByC3jkknjEInKZKCo8FDNYZLCkIoEYIbmcBAVA5s4WSLsyoytxDp9YdHuYDpQH6R6fSomOGzJRbnW2LkSLOJtGxzDIWELGEY1yV%2BntZEflpeYt%2FKwElBbsQsThqzAo5xyR4A%2Bs%2BpIOIklJEmxhRGZ4y8%2B7Ia2PBTo7bJKRwKLwfEY6WKOekAOY9geKkk9IaJMOpWdnpuachygD7YfgSpTKItl7V1iUnh1w6eWoR3YgSpsJRPiudNbqF7gMZXnLPbXVRZnXO4IxXildPQ50TE%2BtMsDgIB61Z9rMNaLYCC%2B%2FrFrkerxkHuUbeEX07ZOJnNrQPcSAJKjDKu5XMBjqkAZGrPEWfa4Rg0%2B5H%2BRjanyatDq9dKFIguT3sCxjiBwGtumB5eyabr3UFiWtjf0E438QmqO%2BBqoCupPQt%2BVjmji8rCXUjcZv4A7W3h%2Fsu0YTCtN97ceLd82JTWKegHuBkRxhfRWXRsPd2lzlbIUIy3TqMe3FmkW5Jzk%2F6IqIj02XHRTL7PJ3OJWkwYq3b5aUPrlvbbeE6yi2jS5DOrzU966tuefML&X-Amz-Signature=39cb8162a69d82d37e1661ffa849ac3a1e73cdf8284f96c79ea9b81c2988d249&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



