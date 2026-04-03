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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQQYR54S%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFQSp664dMdJ8veM8BM7EfusmBIw4vmecAs5LhphoH7XAiB6XKC8mOoxOOgURfBv8fy74Clr0KwqAtIze8bHos9jDSr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIM%2FXiTAO8c7A%2BQDlcuKtwDLO8TqRM5tHTcs9E1ZO6uJ52Doa5BKknFtSEbaEgwkjhTTaOHVRzxayackEduIrIo3qzbGcgH8wQWrKNBrsX4vJa5voqs7YkIBE8OwYPdc9VRejksX1mOglhL7hO5wcAvWg2pqAXjgn47xx8hFmrv5MmvQ8nTyXVZ13dbMP5ageWz6izq0HwT0jGBOC%2FIydiQFQZ%2BjPKY2WLwI9RNCpoXGuogm0%2FxX5HHt5f1dU9STSnlbzbKX92T2KL9uwkh1Gj%2FcChU%2F1EokAWur0u4xkEjemPMANL9LEJlg5CRIXKqCa9wQ9uw5LLygXWhMmCYI65grBejWFRkmlkwOOYU4SnHBD3G3yJyWw3FdROLkB60wI6vXY18%2F2J%2BUM3vo1ACyt7hNVJEtHNakBOv0%2FXIWDnjyLruBWB9UuBvgRFYI5k0ojLgYYgixpfSrNihcpsDXXyNPCC0rCt55aNORMNZUeq6ZUy1iaPw2qXp1aPS%2B4YmwCl6uk44TXAxYr%2FE8KlXd%2F8zllfKhm4sGE499IVz8xrwFJsG%2BlwewJkw7PUoRlhu6TqQnqzT4l5hjEiDQh%2Bp8SzAFJLzJklgBfh7lZH2bCxsGgvihPxcqD5ngSLsGfKcpwNo0oUg8ACRk3RsBt8wx629zgY6pgF4Jc5HeXBq38sdoau%2FeCbYe9Au41CzW0zIhOv7cYy3YTxYdVlZTZEDw9ycP5ajTF8mQJyoQSI0%2BeQ4GDOpoFR3eBYLIPmv1w2JLJaTQmPod7qf%2Fd%2FtKH699XvtEKfqY2lZLrF3sX7csf7vqyuPW19UxLi1J%2FOkv1YNzFKraXRildb9X0QNZ0S5IqaVvzQoJU2zRTfq4231t7FRRvBHqiT3b%2FYksuaG&X-Amz-Signature=4596e911fe91454f9cbaf26962ede4b302da711bf0fc6e64848c789a6cb62d01&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



