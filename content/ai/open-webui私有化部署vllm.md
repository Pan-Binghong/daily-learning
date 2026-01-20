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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3OKUVIT%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFqPEOy3nJ8%2B6m2dqB%2Bi5zG%2F1s2wGpj3TBBdk0SjSh6dAiEAnfse%2FZ8HX0qpP8P4bGFZHcO8kd7XDwDsHPsqAxyUjy4qiAQIoP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKB5Sh%2FGlCfC4aRo4CrcA1YBXS%2BGWtZ0LpfFPbNQfXWa1ETkV3pKdcBAyeyZGG%2Ff9aVWIqKZODGQxmIgMyHszsv8X1WTqgdrqA9whKeb4J7NK8R%2Fu%2BIireYqMXdDj42%2FvCyYC6imP1Vwl6B8wWmJyvF%2FqhMQVe8YluREk9uYQpakeYX2FEQmfAGbbZIMQ231PQpnAjU%2FJ7dhoKNsAAo5ToT7bqn2A0liNSGlxI9niwSd5n1GsbNp9%2FINzs1yQyifWyLG8UAzv4a0r1Jda5eEhieW7nEI3t4SwKvxxoIbF3TFFFiTIP%2B7p7no8OtEMQwGjmGgGEOJSUdCBPiSATQAxUGnJvPv01uqJeW7cT62JkBD9crjP0ScdTxZjb8TUtRpt8QFu8teUJlRDgwxxKq2%2F%2By597pQDDJ%2BFMqxQzvX2dL%2FaFZYaOGnKYdXRDFx9rw1uszxfJw3EYfbjRJZP2gYbmgelV60KxL5FcJBioaPRuqstufbyDfiQohTWeh3%2FxPx1BRd%2F9Km0XBt7fzNp92J4ydR7WFD%2BgUbEjKzeC6jDVnJZgAig849xaqxGO2U4JbJJkdO%2FekeOJpGkpyDlNDZFOqhya2%2Bl1ZItlubCCh5253eQ16w879esvzI4TXJPYjB%2F8tAjHdMTLqjJB68MI71ussGOqUBHScJMKzSy9WTcP%2F9sSJb9Cl%2Fap%2FoxBq7CI4BXqmfAb8ZniHH5dS2CHpQY3mGsG1wo2c1zW8MOiOGyvUP7Kn0ehP4XpTQkHX%2Flc3JZhwNvLYOsmsXESMRPuzcRbC56cdYGN6YsH%2BdSrgFe7ieIVa9V4Jt6FVlKV9P9zt%2FiYWDZkgmhX96VgPKfbmUh5ZxD1vVl%2B1%2BEhQb8A11DGl4O3tBQaHC68wP&X-Amz-Signature=9089df18bd16d6b5b91cf9967d5f740d6c38f96c1709824f3f5e7d3474bc3da9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



