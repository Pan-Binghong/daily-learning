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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDF6N26X%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T024837Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJIMEYCIQCNcO9MinBB165ISOsrabMSOwwtDsRZZivyzDbhMUt3RAIhAKB9pXrlXkMEbaD4k59MoJh%2BwKRub9EjdbxaroZQqA91Kv8DCCIQABoMNjM3NDIzMTgzODA1Igz2y6uQ%2BJEJbmyEtHEq3APv15JHr%2F2aNRabgUjlgy9MCiSyAuBOOHPk5AF2NdSTr8FAkY%2BAluMYHSKwgDJZzgXhFKDU%2FCzu%2F7i%2B1VXzwk1%2BXT2VGi9b9bXkMcyGB2B6lmSjp7gWjXM0WJPhscE%2Bpa1IZMJkH9k0yVtsuysTqatOOBsxTksfMOWncClj8ylRkI043Qp2FW%2Bx9LXuLz6UliMysnWpVW%2FBYu%2FWqOXFlFg6Tk3lylxhNFjdf6qCx0FaMJ25hm9j6Q9lylKGJC1sUDbBYgGREVd9BkepkBLMaORw9iT77rr0BIPO6xiyqhNrx75JFB%2B3s1JXvql5mMbjY%2BIzfvFWdQU8IoNytNc9wnJOymcj05K8gRST6iY54wSnZhdTp54xb4s7Jp2ltUh78%2FiUFV8Bs1EnbWz6NAWHvteix55fuHW31pMzb5%2FfXPJMNHk%2Bs47TyCtPrnXEAzCVYa7jdsDZ%2FDovIZc8Hrp8VMLeayncMbtk9r4D9UXpFX3qxGImB5RtgluMGYvZU6PftHPN049vCtbVx2i9WF%2BZvbBnmHcUTPyDEm3ZE62vHb0TGNVvNjPodnIQszQtyU53EWWRxHMGsmciaJ0D456HzqMnI68mJ96JY3dR1xfaW9gqvb98GDDCglBRx1B7lTD2lb7JBjqkAU0I49T95JgbEF5RUG96Mz5Clv5AQQbnHFTl6RKsv%2BH%2BTNbnM2%2BWjbDWUuVOoUGgib7yHvsE%2B9F1Dxp4KGT5jUZXeLEVOfmn97824QGnSZUVXuosLtLvvcQYr07IXn3QfqqYUdo7OemVAV%2Bx%2Bx7NUbNc45EeusW6HpeYbJ8tavuPS50KfvnCfeSE%2F1qz%2FWkxncigD7K3EabpkT3wQE5PBWjnaV%2F9&X-Amz-Signature=f73a407caa3b0e362a83122e09d7f6b54f1c3103ff6c7c8907627b976f18ebc9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



