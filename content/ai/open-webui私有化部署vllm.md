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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OXPATUF%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T024539Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIAIkOr6AW4EhpZcNQ57vCG5A4XEO4Ds7WnklpN9UKEKiAiB1hfricdSY%2BDczj5ge2eFIeV4YcgJpk4XvspRTgX0VnyqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAGpnlLsMJpA6y330KtwDOwdaw3miaZ%2B1USL%2Fp6tm5D4fMPKVnX90TK0eXPUl0FFgGVTdUV3kuDjdEWWlHUnwub0ROAaJruSX59lHtSwPcnmDKCP6cE5O%2FM3qeIuUdAWLPk9eYauTZQODWMX%2BvzxcqGRqWrp%2BAR3AkwfMsdxd1JWpqxyGvzuJFNia6B22UJKNxzGiRnUHW4RxeXw%2FE0J0X3RSqMRAHukzO1Afrrv3EMspjRKVzQ5dOt5ASIO8GMiouHTgY51v8o72%2BeBy7koiOWHhRuVXdnSe27tW5gvxr6%2FDRhxXKwgag8n%2BfJor6R8SNY7vKqZqH6hto0CR%2FGcK71hgouw0SEeYTABjPdZ7Frj03cbv1SNEkHgrjiuTALeOdZQdyn45bq0otXR3qhYMeTNBEsh7s3RS%2FjxM27i9jSNtEd9eVj%2FUuEqMgxXo%2BWv%2FVkgecEv0aBODM1Y%2BmTRN39SJQTrWpTbG2NaE%2B5b%2B9fwsS6yCZ0d5M%2FK8uTtDpZr%2BBe4BOo7BSt2rOriV4v21AhgNtC%2FIcH1Vavr46mfmoAaKdpN0aI6c%2FXiLpmooe0wm%2B%2BOu8ZTdoOsSQdpZS0tM%2F0xzQWTNe15%2BEGIcMew2Q%2FNcyKDCvHPv7bV3H734jkQ32QnYcAARbJFr6IownLe%2FyAY6pgHcZH2KW96YWQ7vNTd2HgWBDdsyRBEbCjSeMOeG5ZHnn4ysGxa99HzqJCgZRfYCQReYykouAnHE3RpjN7drPrz%2FMipc9114YDPs7UxzH273e9MX9h71u0vSSEAfuH3tG4xCeCrKRPps4N6nGUFeg4bwmVYjF2aemEQT3mvsc1WxHpLXNpsQq2ejY628Kr5mmqcpExKzQLRyIKavabILrlB3LUC4szaj&X-Amz-Signature=8fc4bc35769d94d85a31777eaeafef9df04fa3fe9e763ad65aec6bb30b8cd667&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



