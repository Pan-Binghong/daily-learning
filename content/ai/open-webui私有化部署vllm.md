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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEGV4BRR%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035255Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQDMpsUenFE9%2BC4qogyoel7SJwVOSqUYjRIdX93gR6zudQIgcFWuT127yARlh8%2BrrLfUk6rWiJcdioJ2NwrzLNnPff0qiAQI9P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOSzCM4GmQRH8kq0RCrcAxZXUg2%2BpTpSNpZAIr5kTlAXE3bIIof1N5RD0o1VVlM89RDqYdLyFLzTBMheV4Ld4IPiZQZP8fTQTmRjAb17zpIvv6EK7JGuhOekMZ%2B8mdH3wsIvbfvZyzCySI4hTqyEzKJwS5lBJc0OYzvwdQPmI%2FTmE6aC6G6IFXmCJoE4rpPv5gnu7dC0iNhUogIQmpSfqCUhsINmu%2Fur3lWrKIhYfHTnKRGZtAlIEFdvbkDH7%2By05B8PP%2FMdPfpUheQATh7fB2b9VbtZd7AMGmWt%2BnNIS9pgPcu1C8Cg8S3QFq2O6QWp%2BCdU1AyhjMWjmELO7su1WwiOjL3x5SLrngT%2F9%2FA%2BRBeuNmPb6obc1MGUxcuYu2378zexOjyUkPHVZLkqXQGFthcKlQBunJeks4njMyGVDAHniXcVXuGJpmhxCKIDFLm3w9yPMANaZB3Pe7uyynV0gjLsNdyBrIDMciMTdxK7a6LWgPb7XBoVPJY0bUdztCHPYoZAtn7zU08EBiCV19SV0b4d0%2B35p3OFiaecB2tPN6iVd6Duf1RUrY1UvorFDwHpPASZUG7pIoxJPyM0YMC%2FaRnYmsxmQOgRh8EfnLqM0IjzU7MepcmKyOkoPSFeJ1eSH7Xv%2Bi0GMN5XJxGLMOmH184GOqUB6CipPX1cRS1zaY8Q6RWzEKZis0RUgJPYN95a2zXkSBXR9SjtTvcjZ27xv%2FNACJtDb%2FoiEVDhzin373pK07Vdy%2FlFsH8c0Lxcx6NzV2O67ZJMmLcCMa%2FYTLLGyaCrlUtC92Gah6aYIscSsWqeCVIpGYluntjzJOTWLzwCa4dPhesFT%2FT%2FpTlhsPjoG8gMG5CGBvXPxJfxL8AzJYVYGhQrz%2F%2Bfkcqy&X-Amz-Signature=46bacd27590b202154675073469b1e69d9a55d6c77cd2d5dd30d1744ce22b303&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



