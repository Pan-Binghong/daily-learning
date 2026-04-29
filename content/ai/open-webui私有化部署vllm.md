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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X2YGTD6Z%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJHMEUCIAY9shQAmz3PvZQ37wTRPrSMo1DmEcsHK6B8vpYaWsIAAiEAsVIm4LcHloWHiL%2FN2Lr7SQfXczHIkVpI5z%2FzCrNeFuUqiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBDxNLvs5w4315g48CrcA3MfgJYAAfK9Y0rTeeaUO0woKa6twH7ydOyaIyw%2B4n8Of0IydswpYV%2BvrTw0yMqW2whS%2Bcs6FwaJ5MZvYtSPA3Mzp7F6KlheKdE5r0YQqxPQuJilmhn6e%2Fud7WL3jBO63f6ZsUBfSGJlzbgqOWTDf90kpFb49Zh9DpWeEOoy96pBpIYgfY3%2FWn0HyDAqI5OWWjvdkzQiS7yCarpoqlE0u4Wd6IdufFhk2jmZ1YtNJk46OFzU8XnfJJDH88msZWbYkqsTnsKK2h8Z4Bsx8kU35h8AvhSZ%2FI7MLCOf%2BqRbZQ09sf9k4pWLRYc7VknX2QvKafYriwe0V4sqVj4gjJqEVpDKCS69dnbdQHOq42%2BMu9526TR5B%2Bur9vSHUUw4y1XdOCoTZQXJLe192dmHQdM5qXe4qq3Bh%2BZ1ytKHRrLrIXGybPjnsn4XUCp7yBe51B8ESyqqzxQr7Vro25WkjipZH7aqgNlBIss9iGA6MuTq7xk4X1WjGN2QZqIOgqtFTrYFC75YIbkjVpP4YGbJhXli42no531E0A422XnS1GoseMG%2Bu2gk%2Bcj%2BUbmP%2F1IXCZYRwNDQzQFmuoGxnZ5s2eMGTMq%2Foj6cEiW3fCO5dQTdJfbRX5q%2BJlzC6jR%2FQgUcMJTsxc8GOqUBJWjloqGHLOYSKWhb5mOaxFhW4b0oqgodhhBZBN2KLlxJPaqAQsJXft0%2FMGRWPxPIs69iJUKr9MtzZ5qtMzRjgDH4%2BwzHIncYZQ7ssN9Aa6Q4vLy2wxxg3IDEVpXhodXPveQwirBLCZUGknQJNh8QmEVjuwp62ICyP8QAzJZFdDdV4TmN32m6WzaL6eGvZT44JlXEVN8wMwecmCrdJeKqxzV3OnAF&X-Amz-Signature=cab04bb2f80ca7da4b6b0c6397c130a793237d5feb22a3552baf553451357b4e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



