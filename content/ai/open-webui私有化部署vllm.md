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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEKL7QFE%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T032950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIFFSdA2dUV9CztGLiL60oRMBkIARKOgDopJ3EF7QjAtfAiEA1EH6W4pVF1g7y3c2fklQ2hqzb7jBFKPR5BSafNhSLQgqiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLNFWIQHRJwBBVIziyrcAyOZ1hWS%2BNaazVNfoBAhFyOLZtkU9WVMsv7HZIWR1SUWHxLIpwSe3llhT7EQ%2BUR1%2FLa5HdM5pdC6NIEF2If5zQumxJU%2B1UrFt%2BEeFWq2k132aS0q52CdjjLudvjVyrfJkGXjNTjZE3utfORdHj7jCfRgDYHZWjYIsmqEEeECskrkoHCju4EbRTHDF6JQ0eZz6g3QnKEKV8juguFE19WuEyTPi5xfH029qnp0amlFbw%2ByzD8GFocq4IfywEZkUZd8HxxtL67kvV1LP1a0NUfH2YlIKBcILs16emHSorqijkBQaS8MM3A2nXxndOe7Ntd83JgzR4i6FzDkyTl84y11V4ccG6dRC0w6Ev23GimeVta92N0fO3BZ9SNp68hAmJiUdpP8HQ%2FDUa5hrvZpsr8PcjvlEQfmnm02K2z2zr5x0QO9A%2B14RAP1z3HwoiRSoE%2F96woK7Cm7ugQVReBblGBR9wRmQK4CdKLAkRIVGRReAeJTQhVoCIo5DmyKYL5vQwfQW8W5BMJ4BPCYTKtceGdPpSug5sMNl%2FN1Mx%2FcuKOfKxbuyTD3oyPYNPXdrqq4CB1g1TBeqlWB%2FN1qTmTgs6YgijAcGGF%2B78xpDXuPl0M%2B1WBVkwR0bVMudjW5%2BiKMMIXBv8wGOqUBPHD9WyS53L5Obm7qFqmXwwVwWoJ6NSWjFwWIXWqv8UUZGnxVtRm7yo2XPFatd%2F9aYELU41RV4gRc%2FtRzDDv9zq76dy4NHECHvgwoUH6GRcFD5ihID7F%2F9Ojgy%2BXS6uV%2FESII6Mfn%2F%2ByEwmnO5W90sSA9mTk6%2BwGphShauJK1ushtT1CRMhqpvE5S46cVC9L7cbEbNvdj8j1nIVOUcHXpe%2BR603ge&X-Amz-Signature=f4543d2ec00979d7b1a57c08ef74bdf935aea473efddfb63e95b1dd57079723a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



