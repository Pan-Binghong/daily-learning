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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTNSOOJC%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDTFKQJstp96QSW49UhgHc0D7Ubmlq6rAADH5fDqKU8nAIhAM7iYBatpvKNJ4MvVeceJOJCXJ%2BcheFDRTLC7Znv%2Fl9WKogECJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxT%2Bw4MuRNjMGwTBsIq3AMCV2AN1lL0m1ry7NU%2FRWyBWnFl8OVrgscFhkOJNIJgOpWBoC%2FcABS7a64wfBZVHPZaZ5DVDKx1cmoyPj7gCkAZ7nQiKCjByJ5G91sULqe2jUtfbJuQ02HeMHC6njsVxQtB2%2BUGgMQolZmVe5%2BQ1AoTpOid0iHVsQ22iDtpMLX7K%2B0Aq0EF0gQQV81f%2BMFFTXvOGveQjoJpogwQvt1NGQ9Z3PDl4MQiryI5jig7ZKwspqdlKbmXtspbb7e7gX%2F8fHGN880BuM6GonWiaK%2BxQUy0tDldwx219NbB%2Bk8r7OUXmWjeUXbdOo%2BPHHXKn%2FsOb0hR0SE5oysKBB4kJcHf5%2BJbg76jJKDGrDOLYpOzKVgPjg5nymlSFj8Sb%2FnYqziY0yRlsZJ5cBe4CZ6T6BdKfacQx%2BnMAuEqS4EE9ID9TO9aeTPblEL8HsIUC0jVRxj%2FR2GIp1%2FB7neQQYnG3mJH24HFZEuxi7QMz5MGjPHGUNK7IYtXQshJP8MtPAT8rxSAuqWep12Ky6y%2FkwLagZhCinYN4a1odM6jw4sbDQZsoQ4Q4pA%2B7HbGg4HGycfjUEagtLjVl9pRyqb8IoThVOQgyO5UwHLit5v24I%2BVt3qwPG4XlKswq8rtiQD92sL3ODCJ5cHOBjqkAYuJcyaKjrYHvx7BSVu07wMfZSeiq3MyhLLLH5WEXSmx8V%2FzAf7U0tBh5uWMGrmlGvHaTCJtNi9RCIBri4hYlltMUrqM7dJfGJneiSRfUMgAMMED0ptaKbqDRnhm8WUqu1ZbqXPtJkmWgbfRacq6h0SDaxZY70VJAiZ2gr1UrdyFcgB0lUv%2FAlG4m5euq8O%2FUyQIJlKYMSHkF1ynimdDjo06H%2B4Z&X-Amz-Signature=f5a76f2ef1cc95b5920330fb7b64385ec48439bb33714a1785545840a8a1ab07&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



