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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYBBIEGU%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIGo4h6LkGqVHSRZ0%2FFZ7EI2Vb5uxkmERU%2B7UPvt9Ku%2B8AiEAtgZES8SawqNG88VDwGxln%2FDK4ERJ3fPXSQHKlfM%2Bv9Eq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDO%2FAwk5pdVoGPv6PayrcA4lBzQh3pc8BGiaM%2FKWdCCkHlF3SUldbkpc6KVa0nUiiJdbh9otCZxP%2B5Th20160yo9OX19E49aC%2FtHt4HgZJhTP2zXf2jLKvEZXB29At2U%2B03f0%2Fec8uIi4bHeChKZKUaKnIeS8YYMs8eeGLOWDo85Zz4%2BdVl03iHP26s255QLFmiz43KGiyiPri56jbEccg2Grzm2y0qlKSnDnh2eEfSj3F2kBZw2LK1%2F2bZEWL32LyOCLoznp1YOwRSbr0LbaFoMcuUqYka7viqhwzST6RnFRa0YK5np7u7rRlu9S456F05KbY2gg%2B9%2FwtqcjSI7zeMmQeOLg8VEkw44I72LfYZUV1oJz8BhDHx4V5kRsB%2FmdQ49e%2F0lAUNt3Gn5RpFQ8cG64DC86dejV1JX48Mp%2BvabAOyArGk5%2FOJVzVBl377bR%2FdmFY5JBOrCEVbzzG0c7QM3NyJBr48txeRb639H1KSQz%2FB3JoTqfbmAsEMFOdnKCxIjVeDVqfL7ilYYOtl7Nacpjv8jTi7IVEfAinoF4CqFZVsoYWVrfVM7SDeVooWSD9w%2BpOA9M0cSIL%2FAGTyBkcVHjkusVw0dF%2B2qY%2B75nT%2BPvC5NdFShzpSiKxRlWr%2F%2FJIb7zqfzxobJjwtTTMN7grMoGOqUBbB4gzl2S4WJFNxIjH3slcgRIJYtUvN0TRMvhHpP23n6YGkMbl5rYfPUYouYzWS6AS5AGEdHuDXIcBSLID2FkFgUw5cosa8JxUKR1fIPyX837KbJ9IoAip8OmEOMfOISHvRYUllOIntLxgXuINjYD%2Fm96Ie9MoB0FSmaj099GeqUrPfNY3%2BBqOI%2BTuuxMd0ORJHhuuLiKz7Pqxw8OJ9S8nlBv602T&X-Amz-Signature=dbafa0bbc60957e5d529c1a4c10404cd5681c6e1cd5acaf62a36e81351e0c78a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



