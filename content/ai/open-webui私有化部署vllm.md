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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMT2HPAM%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIHTr1IBuSA7A4isGyxzaxqHTTd6ttGxwHGan%2FVqUTVlHAiA0K44e8bOhKqa7FPd8Hk8VL0OcT8csw%2BunHzrjrGSkZyqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsloA3kb816Hmc4BiKtwD%2Fp1j36icngvUi9GbzQYPjQwXIurfriXA8OPYctUkAmuYqTcUT%2BSLFNyg%2BuuzdqagS6qlE%2BNJMzMr4IzTXhPb%2FWxQz0Uqe%2Bn3mKVByUL6PWEItrc88%2FfWaUtCumeN7EIgEbbvUK%2Fzb6NeZ7nZrRdeYyRMlXnyDjOCqgXPDQQm4pcOPP9wslop6sUyRqgW8zru1paJnhttVBJM4WDIjHfTLOWD7tDIYM3xJ2ORgn%2B5Cfrz%2BcZ5r20Eeg%2BLoAuRVNYlEpnWemH6dRvFQaKbHpqE0TTU5%2FyhKoxmrqQ%2FY77EXsikpFmsuJ7U2cF%2Fz%2Bqja%2FP9LJWwchbDYleTiPEtu0OkgjhHI4kMU0Qfeoi6yx3u1TOSs%2BrSblaVjc9xy4KjeKLtCGoIK3dYDpY1U%2B2FRIB%2B4sE%2F3G%2BlVcnqTxYb%2B0rZcrv%2FQ18bMmoeL9qMIyAv%2BhIl0LMswJ6i4V4c3EsLjnjm9AB7etUWP2ZPkHsE9hORaWqGhmO%2FlTZoH4k%2BfXGsOGMzSgsHhJc5xw0525PxqankrK6wGMznnDKJfSoUnHsQ37U2Ign0nCBGid8j0c%2Bu3g8qjOdDORqzTipMIug89D6WzZV50cK3GmOf927lB2B1t89FTaPMDJ0PsaXI0uQwkIeAzAY6pgHhuGxL1qzS12vWpN10Cze%2BTTZud1L5TiehVapYk3baauo2AXXbAjRzgpn%2ByF7fIkTCBKYv3gAH3w%2Fbct6Cr%2F4lAQpIGNW0u6E3ae4Bam210lbR17WZovLGGM5NflXoprwgJVs96CepYccIhNSV0TQVVvU%2BIiumiRk%2FC25XErTMcU%2B54lDK0ganBITeAOQNOMFtDYIUoznzgxWl6vLdQo8r6BqG1WlJ&X-Amz-Signature=db121c6fa653952163cc2197e24a22ee5e216f2216b31e580a2a15ddbc8e4853&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



