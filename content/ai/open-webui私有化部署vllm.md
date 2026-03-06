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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SBGG6FD7%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T032834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIDiq3lpqcl3RZTWojC%2B%2BtMVZiW4FiSsPnN2nWadZFvwjAiEAu2Slklq%2Bt7CdJnSY3b7yb7UWVYMjMYuCNxETspe5AKoqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEQ%2BolmjDg%2BI3k8XbircA9kpWwXFqYDjGLtDvTIZhJTt1YMvgaXJ4icfx7VxLmkNkDI5MB%2FUBJW8tJxRKSvtcu0NQKV8trccB6bY5%2Btx4NeVgpvLd9xS4J7JRoBmJUfgltTBYqTedFF8N1tcM5M90jhgkMlVzQE95E9Qh7CDQa3SlE7Igma63wNg76F%2B7jubsRgnf8WFNgdHI5bbTurR4lw1PNmzPw3ONf4%2Fc%2F%2FaqeXizsGkyADfnzWocxrwb471PYflgv8v0frESPl2LHQ7iZ%2FVglkLH5V56%2BNL%2Bpu9lpvwJ%2FTOv7z1sqjHNAyJhYdwElm%2BzYKUVJJ2yIu%2Fbgm42BPJNTDsZX1%2FcRfKK%2FwVnKrPhiGCB%2Fe9H3K5zgKSjWh2Pg8hCa4D1OTsiaV1xGdcBHqLKUlkcaEu3nj7Ez7Pi5U5WNbGOdePDt2zgWA3raH3GX1sDNbYKz2yW6qyIia4fLImZLbaNn%2FToOj%2Bx%2B8Dopg%2B9pF7kKlYyiT%2FAmH5wGW3rcBNNSyOmHJ8tpswH77ElVAppwG7VrogqfwfxitbPGh2r6qBkTjackiKmD2iFT6zglrkKJg9H4A1kkPFbdx0jAy9ukw8kSqV97ibjf4pmuI%2FR88%2Fhiw2BpYpuq3cjAk4o1YEx6QSFP5x%2B0xWMOjQqM0GOqUBl9RWgG57x7fuXotR9xdGBVvAi2zvJYlcUV29aiyoe8ZK13wTtxTvn7p3JzR5Mq0SvrM%2BCLewPRLYWoeb25ICM1TGUp%2Fsc%2Bz6Ng6F9azJaZ8dvdwpKZuNkOvxaQMGf5A0u%2FDcG7zZY8xVF14%2B2k1D2dZ4Je5sBJsxPflU15iiBzOPFFX8jWfftsvGp39UbylPhUEIaMmuHWYBUjc9qrQfnXBbO8Qc&X-Amz-Signature=8c18aa90e7f0e61aeb56fd1023bb5b1d6c1deff827c1d104534544674886cce2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



