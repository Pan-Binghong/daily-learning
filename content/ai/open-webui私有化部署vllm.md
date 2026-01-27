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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667P64JJ4N%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030711Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGx9lTtjgxYZr7ixAhlvnrBliejBuxP%2B5XaMigxD6fO7AiB0iv72jbUnQW5YrU3x%2B%2FjRHR4fvSoFkG0Gs%2FNdMaHfqyr%2FAwhMEAAaDDYzNzQyMzE4MzgwNSIMehbVv169RlC%2BdYvIKtwDxoUFBQ5BWmkDYiZlWY4PVFouI9Oc2jvje5BsJiSjmxD%2BUmcepF6AZwzxHgr3MtLLCfs1Pp1YRQf0cIPJJdRDAnUb7sK7nJt92lmJJEdDGseBWC5fXCn7HHlMGb%2FpBua2J6uFqQHxPXsjytI6uPa4drXfZFeSjVW0J7XXOxHQGAAS3z%2BJhE15gybrXY0Fd7%2FpnlxldBznXSOI%2B81XnkBIjihxw%2FRvCIv2cHNhHXyTJ4psgSvYVHAshb1SMofpr5wMDMmBCMF%2B2p92imGeZaWN1vFymob%2F%2BEW5mtbWA8WzTynaIZWBArNxcCY4uPHWBqP35y0Xzz2Q6FF458HeYGca%2B8XPnufneP21tzMDSthVgq%2BNbLM%2BtDkwF76U5pUnZq%2FeP4SB8AtR74ISZAq5P3zYlQlCMVCtpKpYYHsFtESFkKUKmjOCXUgG71tAnK9ifNr%2FZwc%2BdRwg7zossrZrYI6TILk8Mst5ygV5hDZ2NrJs4R8IXz8%2BJw7Liitml61Fjh1jgaHszp275hH3xaTWaLuZxB2kZ1XYjZ%2BJmh63FuhHU%2BhRg5M3AB69szL0UzwpCYK41ywSmSHd%2BTvew9Yr3pD3BigZvnj1fWkI%2BkfSUOtiU9Yr5PqScRNsYNJ88rowlNTgywY6pgH%2BVNPTL4%2FZlEZx6NEMRvJg2SLwsE4N4j0Kd2eCgnmt19H03jYGSFNksXuZNvUrXzCvMHOjEXl%2BvU0zu8lO5iqUTOd8t6RwGcLQnqmfGi%2BAxaTSaLbcFKUj5%2B7Sd%2FiddZQNNU2SOCudTOpuMivw7F7Zld%2FwA5IST0j0DqLNlLUe0kqzC7%2F4SUX0bPOdCuanL8%2Bhk4soQ6di8zKAcLgwvigm5YI7lQaU&X-Amz-Signature=a6cd84fd00cb2bfb8b4070b260d92cfdfb322c7656df29b41d9ec6383b42c04f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



