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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676JRHKPM%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025115Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC8%2BkRJwC%2FrFPqpsrH5%2FizsXfyoH%2FurUWoYJRKOZ3EU%2BQIhAOklgyMVt6S8EH4s%2FilmrDlo42qBS7g4LjIV5FFQM40FKogECIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxKB2NlmMxx3ys1RzEq3AOu1E09llutkaAYetZy6zy%2BTkPcOS2fDWCRdyD67bpezchZYZDNp20JJT3aFPWAAhK4200e5qKeD5KkjTSu8xZk8RZVTqqPwogcqjANmIwwtGdUxUx9qLyeoGYl7bw8LItXhqABXcC%2FkzhwlOCN20vg%2FHh%2BArmnxBUkr0TVBelqlH3lWa0DozDsq48gsHsZqs2uXTEp7hFmTVHMNXA6GaDf%2Fqrj7tBdYn9x5nXgwxl0T6thor0P0933MWi8ZJN2k39i90A4wAd2AA1r9vMH0uOZTSWfg%2FEdDOrsJjcbn%2Fu%2B8LFgHjmxeqVX1EGisAq2%2B6nqDGeONUDAH42B59gnrSQab%2BIhuSmekG%2FW89dCAFeRVypJ8DZMoxENb9P9i9zxpEVl6ZHedbpfzam28HIA9FvLYdb4cJtcw%2BjKz7IC%2FWaJX%2Fl2q7aWA%2F%2F3QRLd41zKziMYHiB3wBffapFHvVpgwMgewMeNmSYqpAGhcOd%2BBBWAE5LdBAVHbyGn50J%2FeV2CULVsdxXAnUJGefxh4yEWZhVpQRFF2l5h4Bw1HhvcnxYB5zZDa43YZ9d%2BpObUxNWjMGv7pJ%2Fj06ovb6F8N71k3M3%2FcfdijmtEbm7SsoAVTjGcQMMhwnrcq%2F5AiPFY%2BzDyyY3KBjqkAU1bXf5Oey9w7c0ccmd4tAy3sgLgJXBhor86nxmChGlzhSNZVrh%2B2nobU064uaWwtifcCEceM7OJnsXY%2F%2BsSGNfIQeMf0cCI3G7AHu7lJMYKNkRUlVxrHQoQdmpaDw6rFVpXaWZD%2BsEtJkwzLaElHX1RPTW%2BnwFi8dn8VaK3Eam3Zrkf3iWeHsy9cYLIxUtwnVjmSTLxnUHSJQOag%2BQk2Q%2Bt5Zz%2B&X-Amz-Signature=1253dc8450878e58c53ae72a5dc86272a7677ffe6decc73b76906b278a3e7120&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



