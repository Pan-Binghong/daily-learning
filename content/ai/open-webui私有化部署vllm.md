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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SJNR7HH6%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICSdj%2BHIf9njxg2pLc0CmBgkXNIuMr8AF6GGqlCDoS%2B0AiEAv5neGO0Tt3Pm%2FjRNx4KL1nUoBEqg%2FwCfkpAVNecue%2FQqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMkfc45bf3BacMXYuyrcA4s7HCfSYyEzzjvR5iifJNhSqZ2AlSF%2FzBhWNU9sjt5FWsas%2FhWbTm4zyRBKbr78giNbOiOe72E60QSHGxFC%2FXJEAnyi3cqAvrhFWBzCxaeblmCVPV7PqF9S%2FoQ%2BqLgljywlLAXpcOmr6Ps0W%2BwRYiOIZosbT33z%2FaNo%2FEXIPo8ax29OfBvJM%2FkcnGZeDT3lku479d0Tne%2B7ZRvig6Zvf3BU380oNLGbrrKJXNYtpzNLaT2ns%2Fks7%2BR%2Ftjb7PQuEkzHAW3zPUPnhSc0T9rO1wgivNjxTHY6VoiAUvqIwUwe69Hxv380K3QtfOJMJ3fb7av0xSONQFCu3bE%2F8jSoQgl%2BVjsSkCeZWtiWKNkm6YllGXx0pyCziAVsdg7cw%2B8aWsFp0KygS09oGeSH9iA71GxVhAr1uB2X6myTPTVTQvzT5e1uvZRXoY0SAgmjiS8M3ij1TQ%2Bs%2BWGPDrJblURhAkrzjMCt%2FvKvzWfu6ZfL%2BqmvuGr92vLh3q3WgFYhQ3W9Tg3luzSeQ5VjlUglWSrKxW%2BUokbNM%2B0XevYMBki8N3gnrUyxD%2BlSGo0HhiV1utKg%2Ff9SVPdZFK7GEnI21LDFIxCP%2BgAYvOnkXpECbbzaEewm5QG5WXkD7eZlG54s4ML6R38wGOqUB7%2FGc4NZlio%2FGhHQxNW2rBnDgPwPgUQ7z5oeRRUboRj2oMNWjF52lxaJjPNGpSHBqE6pVZ057acD4U3fQnM0HscL6ZIWehP08vKoEt1QwnO2jHBiBhGOEKx%2FepxXEC1o%2BGKig%2FtBfiyQsxs1Cud7H3ThYIBJMroLgZpy0VFaUgTASOeuHApt0RuqYaB3ljSU6W10YsFJ210T2lr8%2BW2Pprq%2B1HLAu&X-Amz-Signature=c273f3753fc567bf53876ead31cba064a02aced8661b8efb9a71d8ec7f2cb9ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



