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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIPMWUUV%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014255Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC4bIQ71%2FTS5VtaMTv2g7ink8K75auhJOhURwSHhCIGcAiAV%2FNLZsPpoqPlEAjNCr6J3bW%2FrD17qR3bxcUT4nWt52SqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM22eDgrF6uGVC%2Fcs1KtwDHtchxAiAR833JfYQHEmAKAn7Trv5kbO2mbipGR9BvDbEIlIRi9yi9W5pUF1i7Nj4rwfVWU29Y0P61IqJYckIWBIWR00Mcw8sk34ijNKlHRuJ7wrpnsI2LYow7oxSfec5XMauJiEKMTZTRJQS%2FqEHhWbwrJJJGr5XG4y66qDJQnpJ%2B%2BbR%2BZCmPCrzMfgzIp9M1AzdI6l5l7%2BqfyIekVHmwiPpEyYEJxw2vAddm59GC4FQ5eCU8RpDRPdjRKk6q0F0SFP3qT5bYWMZMtljkzKVKoqvbX%2FZxG6fGS25BJ5r2NMtcXYAOCoxMw6FKjmqH7pfd4enCpfkLC9KRan6B0hQ9ZCHxZhKfypr8Me0hOkEa0smF1dpPg2iMHP2mW8U4%2B5xINmeqbo1kHbtSK4FIcSA5sSaFhjwaHlYTH8SVHMl4J4G5OYMy0IL78%2BYvyWynyfZ%2F46GPl1c%2Fyt03zMOnpxTr3JW8SBwBoiuOaYUh24Rfs8DljpiXicS92vS5%2BB8DNc5oG3Lvkxnc%2BVf8A0RKNOgNljJrs%2F6bMIgvPYfLKcvckx6bsmUwohRfd%2BBfpBR6nGErr%2BpZ2hsp2viVXEJSTjPMnasIIqd4GNBwPE7jQYzSVq984r87p6CYmYKkiMwgvKvyAY6pgEdr%2BJkjFep9HL7%2FLeMPVgZ5VfVhitOXfmRZHUjsZrZsU%2F9uNvOtTgn0J2QT2wgrRrfwwhohyujzmiruV1k6rOeIZ5ZCARGbH5qi4zFnO0yKRKsKjpltDwONGWu4bIu4XdLFtzTJcughQjzdoYzEsxmllGWlLN2dTeEVJLYM5Oy3v2GGSLA6Zu2RL3HNNEaJf0W0ulyXu7jbi5NR9z9TyrrZe4U%2Bzy0&X-Amz-Signature=ff0dc1da77f3fa45851d02266febc6285cb6b4821ff0094b96faf62de6959527&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



