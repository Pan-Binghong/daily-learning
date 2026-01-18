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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QNQXMDI%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030745Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFJxS22kTT0rd4uWxcWFLUFdDR5OLi9NQ%2Fd9J5YP08NvAiBUEZuuSqQbwhidNsEoSUVpjod4g6iAasPHkEphsbSV6Sr%2FAwhzEAAaDDYzNzQyMzE4MzgwNSIM2dGAK7EuPNQ7KnM2KtwD%2FfOl9zzpratopBfFHHNWTK0xE9nOFdklSVBUdP%2FnClLsJ099WeVpOMZ5UrQpWd%2FGvwBbx070kFiimLr59mlKl%2BDTPacJhISy3oWeXbu%2FZN6FGj%2FaAdG7Yte8E2qTr0eqYM0CorIc1NtrHy2sIb34H%2Bst5GPX7FIPsutDvSaQDzSohzF41adTeAkXwH8ZwBhN9%2F01SK9maQ0mgBcEB90muLmdYU88e%2FPLbHN9GxLGNGsAHwjk3Ix%2B%2FeIKzW91flTEFAklD7HR0tW%2FU5LShGc8lHO66YXXdh863K7vH7I97mLmGlUHoKx6sFt3kULP0Su4TpMnPa05cciYBNozPyYpFUm5YJ3E8kDjPmqX5B857XstcBNJtQ9qQauoUdpG1XCgDS33VDCX%2Bo5uxDGIe2dOBytP%2BZWjGDfobzqDf9x03JKx%2BwsnbTxsdCnHjgMtjNNI%2FvIUf975b3ed%2FzkXbpgbkyNYSAm8wN%2BBs6rVfZ8awXON%2BjTlTvIgwZkIrCIghLm5e3zSHf7v5UjxvWgO2E%2BP5YPfPIKh%2FN24ZFtfHU5E%2F%2BhbjLUQVI5WTBAqA5erf5oo4zY4w9XpT9UaQBqKK63ysv3f8DtkK1L8cnX04QNOxbldAJ2iow%2B3nmVQwK8wm4KxywY6pgH8q7Glh0qxgJkfNOUUCuQ8yC0I4sxYZ0n3U4e1A5wqRl57b7fV2JnNGWIFx2DbUTF0u32ERkRwdk5v%2F0DOop8SbvRwq3PlbGPSfLIF0wePsFaesWWahj87a7tuFX5hY%2BDk87vD0aGgIzO5tyCx3cFnNmSVWdTX25u0bERXU1ow6zP%2BdAnCNpyidQiKLWkV%2BYxpMjX5uXB5aHkQBa2rF8H4riVfP6hH&X-Amz-Signature=4f0a2fc9a6f3f35b349ffe1c2547d20b3f6a9af16774e2c358717c6a5c0c6f7f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



