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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667C7ZCHSP%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJIMEYCIQCBr3N4kGbEiP1FhvztS3cA2IFGUbpC1pWtDi1tehgSRQIhAOo9ZS2ojK8ggZX32Xj4YiGuFTmKjNRDxfP3ZiR6OuuOKogECNP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx360VkUol6xWTqTWUq3AOqL%2Fyulcp6tmPYEc%2F2b7ohZGdfHHkQ0bWzTbFnwcZ0f%2Fju1fF7d%2BpWunMs%2FrtZiHOBC6c9LaiPNBzn2D%2F6N174CIgMup4qVP5abuu3siWmOrZ%2Bipfk738jMFH0wWjuTuFOI2JrbZ9DVpeYHqtd4dWa%2B%2BiMplrBJmtDnj20xYmtUa6ElnbVjf9Wmr1KTBZVd%2BgJPpVmZV%2BzQeCoOeBiaBUWTmrHzI1%2BhToyP%2FMvkzEt4pKw4McMr4x1cccqHcMfl1o52pg%2BpkgTVh9WGGh1DIQheG4IGheJxLcSGvfotM5zUYEqETFX0gpk%2BbRIxNLzsJu37aXwGNbTCt1mj70veQhuZhBNOSZeQ8pKugmY45dj86%2FRkLjONIsIgy4Wjb3Tl8rXLi7arf3YwuyxIJ1%2Fa%2BjPyz8sgGN%2F7wCl%2BAdC4ElcKKjj3XMzd36g29FAbXO3yoINmJZk2SSD%2BEuE0aZxi%2BR3c%2F6wBDvwCHzv0eiob5v%2Bd%2BuDbdRPG9q%2FuJXnNzEaSsHu0cg4BWAtTi%2BklyRAy2OM6vSLkmWTqHcB3UjfZpHbsV4lxqcHgjkBgCTtp9Vw9Dny1kbpqmNTkt7m8YELRg62bT2X2vOJZV10ExP1sC5ugJ4TJMtOIvk7QVoY%2FjDIyPTIBjqkAR61O%2F605YtgJLguRESOsduIxs9genD1vX3UZQrgvFgDnsKlI49fLyjM%2BWfnTh1GANpEXhWNAVaH3VPK9oUTwnqa0aZ6cq81f9oaG9apM8X91i7bav4wKQzle1MxJ4MVhFwcq%2FkpjenrrL%2FvInhhQoEYrKIf2kt6f3LyBhwH5j1hNsFupl%2F28aakDhw6GEoU3OX4gntVLVhrDYSmAaXWiaIsxRjL&X-Amz-Signature=225283f275ef5f475368adf93bf360c2a5bfa687142f8428b21a901dde159e30&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



