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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGX7L3QR%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031115Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCtXm6awYiUblGWO%2FAikVYkH9hEhEqCZGeIoSyyrFnPMQIhAI2RbkHB2Y6aAt8oYGIHp3thMp37sxrlBeSI5WF9zeKCKv8DCEsQABoMNjM3NDIzMTgzODA1IgwyAmKrmBdYsX%2Fy%2FFIq3AP1u6RYNv4BElPSvyDSocEQh8%2FDvpndk2lXWWgmTgWWwV3HO9PpuQv2A3UWsBlNBNeVqUOdoTVRk5yBiJtjhh%2B9aZl6uMzT%2BFFgnytJR2JpvWZz8DKgjNmor333eGItLK3lPty0EYM%2B9wCLH4Cw3sfU69klnKLMQ9ovlPUfNkB1sRYPMsqNa5IKmzF%2FwyaZfoRNbBV0mG%2BXljDyhS8tDjw6OSIiZgdimSzj3yvl3WcVlO7HKKGCFxxYfedmlgb6XcRZMy9yZeuVdlSCVuhDQAMBerwkyf4%2FQ2fPEopbGYxv8JguRxyb7qTHT3yGxHcuzNAuBAwwWl7QFKsQpXBSGS60rxF%2ByDxo3DUYTvEtILc3uHqpbMNB29IHn3QF0oYxPfS7MKlCk0wk3%2FPc3WCX6HtjpJtkPMcmmdJWitGahLNC918n%2F%2BI2dQGy1rY99HgPd2L0bICqlzpHV71h49RWqsdRmSZofhYsQuaHI%2BChVa%2FOIilJcXlgL0hKlvrNvi%2F26d4y%2FATzTliGiVNI4Gi6FW7Lgtjaz3mOh6UUnOxqDvKd0TndAlcTg%2BeYtsbhBZdjxUu7cuaENp9btlpZcQDf%2F5fq7aoA%2BMuQYSDzQbND4jfgq%2BR7j5oLkEfxAhXuYzC7lYnNBjqkAedcAF0bzBLiC%2BY%2FOdfpy9qxVrV%2Fm07J1li67Ans%2BkR9f8d7MpZ5Ypr8dOPEhhtxCS4%2BDqIadGhHw4q%2FqfYBr53InQSCH78BViXcToleMuedh0k%2B0d855sRvUH34oMeenLW1zRYQzms%2B9nunfXeUjQDYvzxVn1kzxi3ZWkdoiLec6CoHb6R9X49rD4MhjpIaLRRA%2B4rLXmwo2JY8I10Wdth%2FseJq&X-Amz-Signature=1a3fe6644035032a5b486ceffdf1140462718fc406f0354525c06126d3705f01&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



