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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7M3DVMQ%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T040925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCICZK4wJAmjgB0eJsuU9DmFn1F9pkE%2F%2FevxXKwfXecGinAiEAyWCt%2BeVkUewRb4tlS89zKrRa8W7yrEpBQjkU%2BKV06rAq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDE4En9bHUPWh7XlF8ircA%2Bpu%2FJR87cmcOZmXne8JCLARNlk3wB2sdy%2F2FOxH6eTi7jWJP8lSTlxMqf1t6qXPwnA25pCtHp%2BzgZNIYLqWrK8bFxzxAeBn7QybLkBINxo3ALxCBtw4h3SQt0%2BS5wpG%2FseoYB7MXmMUaRT%2BgQdPsX%2BnIyJqcqe3tRSuWUhXG1GpaZpCSkaKruTWJMnJDjmOKde3IPN%2BcvPzPPeg2ZH%2BMngEllJ4%2BvsfMnCeGmmvbd%2F0vZk%2FTanMDr544T%2FkdpiOtcxc0ugIvMpL3ugFoeYwyl1FbX5hSfPMJRuCh%2B0B8aLX%2BOQ2m8sXBjDJywp6LN6wbGpOSD8QGHgxoPQJIUwZQ%2BTohVxrOKB2d%2Fnwx4fRA984G9It5fs6dVlD%2FixX%2BrVlcC1ck%2BXivVtjKqKlIgHrMBGVymdyyE3e6RxBtDd23PmYc60WJmnQMhSaMm35mBl%2Bl7U5tDTKWGA7VUiKp7ERkFu2SAetQlUAUoDvnmCcZbzDs2732dsJ0mbHZy13ZXyzGJdZhr5ZWePczX2vU%2FUEighAJVP9qlr03fR3xwxKxhf6swkyW%2BSglugPpqv386QmBFQllS4h9KkctjQ%2BiQBKhxSbEWP5uKF4EB7l%2BKSZuNtVauSoW8tO7f8dya7%2BMIbH4c4GOqUBThTGq9wWoaygflcDH88A1LZ3YUsfa%2BrsEqy31IkbCcLholP5gApNOJycThElIG78TQA8kfo0aI1GqDPC0QB6WOCxtPswfWqxstxf5F%2B4wQmaRYEwv%2Fc16GsnQ3RYOHEZrKqdpagjOLwfRPucTy3SqPm1gGWCHxQMcpSzfFu2DzwA8zN%2FEcioA3GkERtVTU1I0XM4NwlmJHeXf3dnXa4IpJ%2BG%2BWw8&X-Amz-Signature=3f656e721868ef6187c752456dd1252157aeea8eb245f4e9ea3819f96e02d369&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



