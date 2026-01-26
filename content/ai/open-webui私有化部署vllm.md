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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BZ7VYPV%2F20260126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260126T031646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGcaCXVzLXdlc3QtMiJHMEUCIBQmJiHTllZbk%2FXdtl%2BoBgALDs4mzTmwkQcWDdHwQyM9AiEAwGatyGNMnHHQ%2F8gjsPjCXJOSQcYV3zIcu%2F%2F9D6QRh%2Bwq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDDJro68%2BPEz3LPhOnCrcA2Z1xGyHLQ0XOCcu5gvAw7r91ynfzseS01FLRntGW1toT7hIHed6zBUm8FnopDdZOwQ52wrNv78yTPSIq8QNDT4jwbKsCsEdR98u7qAJ5igLnlR1DG3opiucnubtv1fq0l3l6wQ%2BJ4PImT31NqII%2Bu%2BSPfZpToXV%2FcdEC%2FKyvzBCIixGZH7L9yLntp7aff2dl%2F6dt4T5dZbE%2BaDYD%2FBJYmGTb6lzaC%2BegtJZqY3YAYgEbYCwR0V4XVpS5lWkV9Y9iaF3%2BlPWK1lPbV3UA4aqJeyp%2Fm6RsffZsfXPLv%2BNL3NMpNL0zbaMTijws5H6EikorcrVg16ZecuyJGZkrBHKw0FExFceycxfFaIHDOC53p4GLjMMSlMDpFSLtxkt9N4BH5STWd1DC%2Fl6z3%2FQN93ApMQcSApsbWlgGedKEDbU%2FzK8aeHe672VSW94m%2BpLR5MnvL23udkJFFP6YnL4Zckk8yxJNvKd7MDMoHqYXHYD%2BQxVLYBhsCHY1W4uKTvyLL8uBgRzXBoFTTU30YAQNEo7GK6cBUsjv%2FtnRpO4EQiRnPRYYzZSwnJ0dAuBq2ghx33gUBAorhXZxw%2B%2Fx4TmBztzB11d5rWomy7cdLTVnE6u1jJZKJk1kP77EYQt5%2FOCMLqx2ssGOqUBGqNyflKdlwpK%2F5mkFro4wmHT%2BYVeFx76utRTKWjqgiplNz9%2BWUvelMNo5InqUTK7JZin6QLf3uNHtASV%2Far0zU6qOD65FkkYwh6OfhPxeIPtc8TaYeNDM3sHI%2Bza0TR8hxLDBym%2FFE5CAUkctfAM8xlkcpYISWqSxLWMoEIGmM0%2Fw58nXIyVh43OWMxCLvpJhp%2FenLq1YTqQm7TOjhuFoiAS%2F%2BZb&X-Amz-Signature=e01e696af86c768545bb8cd39203d894c30791b88bccec0e47710d9dca6b2439&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



