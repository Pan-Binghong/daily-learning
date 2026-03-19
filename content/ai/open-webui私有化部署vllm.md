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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQPDK4JG%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T034159Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIQDBo1eesRmXniVmzBTuwUxJ1HZakUV8zY2wUYa0uqzg5AIgTkIKddFWl%2BkeK1QKHzTfSoAhzoI8wUI1nORWx3pQbj0q%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDH8csGRZWh945lHGkyrcAyOnnAzW89yD4Zg7Ll6KOJyG%2Bby%2BS13rS3FNUrXzg1iWsOSrQAG5fUoml3Ch54J%2BlauZxInbsMg5cZXQnIRI56os6%2Bdp0oXfVzQ45Rz%2F7xV8l8p35b8O%2BchspeW00D0G3ge6pUh5bF%2F3lU80FjyPrwvWyQsvM5tGK3EQYnyLpLXJNJjgi%2B6vsA77grWn0LAls6DHqz6kS97%2F4GDVtIZ02eRiu1p9b2vafBWOMpabFrZ8vb%2B8VdOme%2Fzpc8V3noe7XnjoaS7xB7HUeSQQElq8%2FQtV3UoMwzjigq6r91gIIs%2Fmavw5CD6hvG9hxJnG3I6fpRpVgsY8Znrm4bNJ675jfy%2FlGCIZPkzwCpAAagh1fmZn0VAEgZZPs6fAstFUUUhlPhFABnDtYmQn2Pbwm2GWYHntpwRNTb8GmR59gjYUkrKCbAouqyEvcWkrdtt2%2FIIPGEwI1PEn%2FOhDQGGmn6Gl4%2BRE7t9qmtsyMnFTB8Zh3ijWV7i4OHmNNq24LcJriftq%2FG1RWjio9hPbT3d3T4kGe1Hy6LMdoeP%2FDjsgPwgZUKiTcHp7UquRhAVIgoAdZhgPMC%2FVdbwPagrw6RQaPpIEhc6w5tR4VzHe1Q5pwm%2BCSjse%2FZMps8X7HeQtENRrMKnH7c0GOqUBE%2BUS4P26ThR1%2B7UXSXvtxAZQHhcw5o67arTM7fjywDJucHxsLih%2BMlBzxkYz6Ofev906iLzesDZuo3rFywbRYJFjrIg7n%2Bpp3AUUcsVlGEqYev3zUddh2a12BAm5GpyWZtji0LJ583I3rjOeBC2qv8Jvn5m2ivjSBbodGkjfPE9QBmL%2FDgc46T6ZN5tR2gVevCX5lddPuMEbYoUTem8qzpSoIS%2FS&X-Amz-Signature=eb308fbade8fa164d0ce8ced50634e42d21190c9ee8d507984c645f39ce8d404&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



