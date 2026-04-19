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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNRQ6GCB%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T041622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIHTFRewBtI1ap9Q4R2%2B9EBWnqePZOQd6HHxhc9vaH6tUAiBU2PSbyWDCPbN2Tp2BzREu6OmE8p0aqHlzfltbOukTzSqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIML23jqZyNGCOvGmhoKtwDh9OollKsKehyYSlTKw74pdR4ZSLNpljXkWdc9pz8jRi6LMY5CUX37RBPBkUCJGqDfSrV7ASnS1YOMKbYLMKX0IeN%2BC821ODBgyEvq76VnwGkBUNR3Wt5xOw1qba%2FkQ1lQ47RdPEhgpEBsrGkOGHyq2C1x0iflQzm2JFizbXHC%2B3U3%2BJwIKwsTcBojRMsl8Gf7V0HOjcvs3BpAm2%2FQyjqCYOK6xxP2xiP8y5e126Ya76jUriiSneHEiZB1KjbtMC3T8z02SJHvaACHLT3Q8sB9JWHvPU9ZPCFD0pM5pM7aVUjha7X1Dly9sRUhbhAa1R6Ndchc7nSfSKMJ6Ui6d0yHKryypS5Al21kfwiwTJmLqbcyhrF3lPrPB%2BLvUkMaluod6juT4qPHbyNzw9vATIeyp2X6j%2Bxp27m1fkrkiQUb3CAX5i1L%2BpUSeUpi%2BRE9gdJ%2FFOwuLF3T9KIvzY6EMZOfiXqsBmcCmLaerALWhcHRmwqiwcjRJR27qEt%2BRSYUtvRW9USSyGcDMInEdyYEn%2FPsJgXJQsITm%2FCspwMQQq9eeeDJBiwgapXDuh3JOzJlCDqttLKJiKEF4BCm%2Fh05yDG1Td22ban48ZenBwzPAAtTHLlZF%2Bi9o3fiSsjcZcw89yQzwY6pgFE0wLVCsb7VzUtlslkX9jXLgq0kWKtAQfRQ0yVhu6oi2aKCjIuyfF6GtZ35YpkzHkoe1wyVlQUSATVtFESvmGaz4A2puROg%2FYWTe3wxGBxgNAJSTa%2BhK%2BNFxEBh9e5h1CVa%2FZzOR%2BzYycONnA9ecA9lzfDITRI3GM6ACkdSsMG41K2lix%2BmmRz60FAX%2FrOntB9kjbPcbgbGg%2BboONTHofUhAQyCB0J&X-Amz-Signature=40014a7e3222a2115517c6e17a5db9fb689087773afd84cf801a77e4e3dc515e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



