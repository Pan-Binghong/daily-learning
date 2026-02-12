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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVWTAZZS%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIBbpG0zj0iWMyMHCkw5RX%2FjTLtEeM3VmsiRjLftJ%2Bph2AiEA1GlP95JX52u5B2%2BChDkaZsQ9Dpi1gCYh3W1qweFaZ9kqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHoSzCDdNZp84eLa1CrcA9RrK1MccFehZK4NtvisxoDfomq8o1ciV%2Fsm%2B32CIgBdzAEsuy0l99VlaU4p4hbLkdkKkj4aw5yctyZRuN%2Fsj9YOeWyhDJUzr9SJi%2BgdlKWBJsScfho7e%2BNE%2BBfP1dGmyzRku9xD5%2F1HDspwURNiBzCcnQK%2F3Qho0RGrrI%2BAGBn%2BDI%2B%2FDjFpigU%2FLjEg%2FDv%2B2eX%2BTA1GFGf6BfXGUKa31hLBG7RXNFZIQJZYPmguh%2BHkYpLilsm5RyDgF3Ph3PT3afALcgXJHkpPWc%2BAWRsOX72abb%2BnokXraqmhgNutET2AxqVhniihadROtzJSftC%2Bm3gRB7LxEM0OeyzniQfmRoJtd0Ykon5V1lhOH1Zc5A2daCfpGlE9%2BlEw5sbWZKoQgLxRtMLd7h64VDf6YhefENgCIiPBW8Yd%2B4Y4ZiUfceoB6IFINWGIjhG8iesv8dEOII%2FkyFa8Y4sC8Wa3Fnr2lA%2B4zTKAGncnbFevnaaV2ZrpORtXKczTWvE45A%2FMCeGrx8ljfY%2B5IoxT9lVq7u0v8FtDIjXvitXml6Cn2jMOC291CFqxyiOOuYBHXSyaB4Mt7Nqz7thOqjGHe4XD%2Bp%2Blgo9uudoa0Vy5qptCiFjysw3I0UW1wQBTWBgwanlcMImStcwGOqUBCpbticjOxJ3WkGwvL%2BOY1yOYqO971uYhz3h%2BragM3WCqlVhi22pIYznkhgqtUwiXjx1CFMqSV%2FPsB%2Bzcw3SBvX6F9edHLcBQMTmTL967O4iLwCiQAnSD5rBGnjzqEdoPkPjsOl0%2BDo0vT6PvQGRDOhfZRjzAXhBgo0VB%2BjhOElBhjmV4xJXAVjhafVbeQEtQC3tm16CmhrNVYFYjI19fW3OZccYG&X-Amz-Signature=02b6ddc9bd879bdc08c3fb53d443a475496337ce84553ff1b6cfffa4f34306ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



