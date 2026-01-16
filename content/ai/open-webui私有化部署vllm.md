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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7FWQ2CJ%2F20260116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260116T030119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCIBxfOJR2pIC3HepSBR1EqFNiQKRw5j8B5FD2%2FaCw3BRZAiBbBAQY1zXNgnpisKj9lVg732oIkEx7308kKL79k06oqSr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIM%2BHMgI10Yoj00lP0MKtwDam39XLP%2BKgasSHv6ZZVU3i%2FH8oxWbB6ystCnQTQwUQ5%2Fjpbz6Lr0YP%2FSHkRV5zWuuWmFBzudY1YpAcKsYMVfjYS8ECUy3mLIffiFUxjtuQV3orSkFzxDd7yPQSYk2kkjM2KGOVOixe9d5Fdiacm5sLulpDyGIbHzinbGai7oe1xesBfInfrJLwVgNz1eElZbMvH9wBOSqkpbs1yCYWEHGiYdCMqOXRxR%2B0tEfRyg20B1BeSTEVJTir8uCVtTymT8EaTjjBBGtwm7QKsvLu2RM5D3z2olf3lYRfEFpu3QMgtpqF%2BlTldR3eK8HTQobP7yddsMoyWwK4UyLfq954%2BY73yS5sYHKL4ecut%2F8a%2FHlx6TfzY66zz1rR24o3M24pn1CVIWtUEsSkxLDNOjesexfbKYUyVnD7lR2quCRwtVHyh%2F4GEieQKybFEXlzXWQXUiHeJkyhFYrqQ0pgkIHHhipNJWy4v45cKn72x%2BZJxsYB%2BHHP3dxHVUiR2ZOSoqJiSD%2F17YymHzuPJLj4LDwRic8Xqek%2B98KyQnvBKpRQh6M9%2B080sHk5tpFH5w9K%2FJuKPf99bHwobLCTIvMam%2FUKOxENjojAYhtDdHY54fEe27zAQvES2kk0h%2BGbttDhow2LymywY6pgHf%2FcDZFtwKUpMhY6zVYPFyZamOQm%2Bygt1%2FxiblIWgX%2FwhGO7gGnjjAL6hrNPZelMuuZPF3UhEQd4AwxgfksJe4Vh2zn2iNZlmjbPrSOv32SEe3ZGyQKBCUyZaeV0QuOuMW6gz6nu3i3%2BW75kH9oSs47lEjAfmOl71lXsmL5CSVFecoF%2B4BkF4nEe%2Br%2FsEQGrd4xENnzk1nQWTQhspo1SB7MwNjVoyA&X-Amz-Signature=6f674623f0344127f0576488cb028ebc0a127fede36470bcc15d3b84b1dfbab7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



