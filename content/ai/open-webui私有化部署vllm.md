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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXVVSPIF%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJIMEYCIQCBr8DVBmTNfTI6nDL6KgjqI6X9kAi0enruEUwiOOqYrgIhAIly2NDGckHQ7CIWx%2BFr3PVyQnHHGCdIbhxXe1oBypTiKv8DCCQQABoMNjM3NDIzMTgzODA1IgzB6cOfmhUhyqr9%2FoIq3APfVW0lnYjoW1RusvCk4MpWH5KUTyldJeQ53w8HOIOLJFmfFUtbysoOBLiUjKPGWkvwVFxtw6wDdQhtUCMx7yIizqBe8sHAAr6dYLGJ1%2BwpVUJmkgCMBi9uahK69eRk5hYfxJvCiIZJOOWd4VRNzy3lfb4I3fgisyB9KIVecbu0S3HmTAEfCZCIQFjeEwsFwz3z%2B%2FSvC1G8krIrn4k5S2Cof8WJLvop0QBvUR%2Bkc57RYXhsSGyDp4mR9I2gG2XfPjeudml%2F9c%2FdOztdxCJLJJHNpoad3iMEIt6VAiaZvL3j5vDo4EvSA9EA8xeQJejlF2yC79CJq4AXfASdT8evv9o58%2Fk%2BFO3XMcRki%2Bsilqj3%2FrBLkTjZTU%2BWWQbXONyhDpi06MJNVk0CIqwr29tIf%2FLrWu92qoWbT%2F5OkYCUugrRAgEt69JP2DWB6k95refGx%2BxKcVjAUZhOgP7RHqZRPJJhW6kXcIwuBKNJYEROBwE6vC2pGfdQzYrFP%2BGAtWwX2zqP3ovFKWNQkVhR%2B6%2BzoSn8KUbTqCou2PtQ3iitekRqU0hNAKqa8Y82ynlThgtXWYz5AVbSrm7TJWGnSAX8i4An%2FMwtdtfvSQDb6dfUJXhMw1lpIOmH8qdpwG25iTD7qOfKBjqkAbZgv%2BgeuPisBd7Lz5OE3VEWG5OMGpRNhIg1wPQ5PHhfwTwA7J3LeXp6t0FWEPWh%2FSdv%2FrYCZ2aY6JGKUs3zseRkMtpXHM6zZBitdx5%2FHhcWLHnXFqqOM7UsJdmBWrKHZm7dseyODNsa54Ncu0NQ0f%2FQAfiBC5a%2FwuhveWBFP5hc7FnR1KQjk8mhDebNUYRZcuuAj1XGAhjFrGeF7x0h5h5kxlju&X-Amz-Signature=04e0dd301a5061de71dfbc3603df64ba0612f8b8ead5d2c594c4e450b52201b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



