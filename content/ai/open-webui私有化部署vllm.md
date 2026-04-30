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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNEDCDFO%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T043418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIH%2FN6yzm0T4%2FSZUoT%2BHH81cc7cBpmzbsPQJ4FiC0aQhGAiEA4et5mWkXDkz%2FYU6yC86RMyFpinmT9kKQExKymYR6j5Iq%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDGs0%2BdJ7J1w6ZbOZyCrcA2qS%2BX8ewZuX2S6Mah3lUBuBLQsNld1XLDIWal8cZ5jW0x0%2Fd%2BufjhM0NHlTxkbbQXFhg91q%2BHZTPufcth5oIPipOqh7X1EhezgYwHTf7FY6cIYFsVfche2hZZtmB0K%2B3EnBh4arN8lqCriFlE5VnaYrsyjXu3iu%2BcvXHqD1nbX8Kp2ljd8rvDvp3XvNRcJLZJcBVzmqNT6WGyR14CCr1Al%2Fh3G6VQ2jEZmzyI9oCcl3NbvzaZSD8gUcdJIqXBfCVVkw408NLJDtrnkMEiz7t82jev00R330P1Xa%2FqnIes6U6bv8woQ7KvRrYpe3kN5zYlyqR40O50Ju3bYeAK01uhP%2BHH8pSLD8dCFVTD5WhlsXhgtM35C7nh6QZrGTSXIsMRa1ouLJcIfn7EWsB5l4Qy1n07h7hJ2zKqLelDuWFGhDerV15DYPnItvZ4Fwt8pn4Nu8En6AOCEmJajegaSdgZ6%2FKGImA%2F3V9PT%2BXQ8MlUgX0RSpykhCK5fxx19J7mWBLNXrRhN1A23iBo5MrfLL6q45VogbKIXbsSxKJ6Ifsg1JxvYRWPC5shBIak3tQqjaglc6J8Tw2NrbFNqEDfuxAaMxwOMfZjFbZnqqcEDRc8k5ddjx2OTowntayX9DMPmyy88GOqUBd6L7i%2FzIOupvyi41CJZmr6tJxOXQxwSSbeiMt7%2Bp%2Bus1JhCSoGos0sWgSvhw1qxoYfsvjd2WHZm8ZdBYXdnOTOvbYvC1i3YceMRvGTnRRJBMHlQZUWsPr4TBQVdnpqSsNus7brCHmoo6NjXmWB4efrmt9DMfUEuoJxlsQGyJMUuKOTsuP9UgBumGiutZj9HQBUD3I65F8JV3uDFieoWPlwbZ4k%2BC&X-Amz-Signature=ae4a30f0f997e4b9115a285be227e60ac15644ec5d70cf8ecd5672bbc570bc05&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



