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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRESR6D2%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIQD8y%2BKIe65FbnsRCzkkZLQ84jbyo5o4JfhAjVrtILEyxgIgGZUjHmsi9hZaAgZxVFw6WuN3zzCZoIx7aEQt68KsDwYqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF4tn7ZHG8Mdi%2FoIMSrcA412n86%2BdBVyM%2BDY%2FWH8vnvyHiBNrVQN13aA28YGZG2P2x9YlexFua0pQLn0wI0w%2BbcAC9bRrlGNca6PtP0GY5PUzqYUPlK4KIhDc9ctDar0cmQcLLTRyTiKmb1pPMSsYK2Q%2FM39WGvtJsZNoWMHxiAUGdKRW5niMdo7bg1jTuW3qQia6qCdtzOle3Pr6gSvKGwDebcx7VprH72%2BQyyhj7STlgXPlaXBwjE0yuOKRrtPnwaBzZZqmN2fQJVGabdVM1AYyMK2HF75rWQPi5LJqS5TAJTbpiGPwE11MwHWY4vA3OJrlMTgW212CmhjHpi8R6bqmBKXIqhPh7vbFjV4yRbnIG%2F2dCIJIeverjWRlhKukFFOHWP%2FMuVIOMCUkiLOTwyOSydeQ%2BqaGStsqYME4VqIskdbmp9CgoVUqv2yPsjAcCu5D2OoxgDs7%2FoedjsLaiiJ4oE7RByT8%2BQnQFBsexSoa5TACOrZ8%2BpqZgpRKb1cwKzEJH%2B3Xe8sznZhsQZOuB798WJPrpBpj4d5mcN%2FmE%2F032f6FcEGEBKb6DO2srGoVonFOc56lsTYgav1%2Fqp%2BxFSzg0sU2GxXrmZ7dqrl0fEA3p6ZHafO8TgHkuFgGplcB4vw3X%2BxGBaPNdpMMNPQusgGOqUBaV3WjNvLGEegFjgozmCK%2FzM06rMXyLy20ApCFQyQZPFYTFrCJJ1Lu%2FRkxqbswsiZIajQzR%2BN8F1sLO22UwiGZmT7Ub0%2FogKIc7OKv8qMwnQ%2BcZ7a37phDMN5WCkYcA79QO3mhZcmZix6%2F9rIgRJZRqg6PayrAhbxTwEabGcZOw8G8c0CNZ727TK6VWJubVwNPLDqKkAok7XV9I8nrg%2FhpyKFbGxj&X-Amz-Signature=6e844061fb0862b92c5e8a3a2bad92a3236d71a3cd0208b1008221dcc93a19ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



