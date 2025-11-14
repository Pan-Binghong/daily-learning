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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJ5IP36Y%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024422Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC9O9T0CcoMI0v%2FZBlnxiFNtbd0TKZMzwrNrt%2Bsaul6TgIhALW7s6PdlHkR9nDw3kp8lmj35ZPXJfuU0WKfVYZDJnyOKv8DCFsQABoMNjM3NDIzMTgzODA1IgxZTnVK5%2BwqvT3uXMwq3AMfWu%2BPh4AT6%2BAMPn0R09IPxfUNPBJqvTrsR2cVB9J8mrE8lWKcc4XDndvs5%2BEEld%2BRF5EfotivY1cNZbNIxt%2BQUMDfHZOHctAk1BuNBZERnzMzR9glm9jez9pCRn8%2Bm4QzMERxmAyEBaEocyV3rvhintGqYGcIgOK2d%2FnmMS7pfbsxj4CekEjlw7tTMew98ZA%2BrSexeEFFPuXN6%2BG8QKIkK2QzOKlQ4uVdr0mIjJsudW7qGGFY%2BThr8bWTacb9SWqCizQt4HTo59Cux65YvbfNxKQui2oXWC7zkCTk4FJ05bMRwiHFfxMH75MrA4aUUG19%2BfxPBlaOUITpYeRAEETnfiSmlXdFUrUi9D7%2BlZumraYbOimA%2FqlAXr%2FTvhZu2eoXDChn95oa0hu7KAHzOeqc2ZFXpPEmY4KODAU7eWImzLbUq0VmGglbKAnCPAy%2B3k6Esax2edbvpQvb95H7XJ19HqjSpf%2Bj4ZVfIas8ibCGl4Q6KtvC7aRyaitfL5IwUNTcfAHhWkVpS%2Bvs5VSZFd57lF%2FL31bs2eurGbgqwceMmEd%2BSwFU7O5XZlHYH2CIAWQzNYOYXZ11n9q9Avk4FbEZFm0E72Ki7VIYG7NMd4CHDEt8yDhvykJbEFjCETCsitrIBjqkAZt4g%2Bp6MdG7mX0ZNoSmD9yNE4Nej%2FSN6VQSub5hSkFy00JE5n5n5xz%2FRgAJYdVG0EgTz87f4%2F9stCytNb19tUk3xdqAyKgouFOL9%2B8e%2BP2wuUBNU1PVIGUBtZlTvFo0ksvXi3ioTFpPw%2FlgEdQ6mxxvda9Y78FySAFXUJpH%2BlZ0P589tZ%2BKYYN5kn6S0%2F5mzIgTe2crfZnSLy6IV5YQGTxQV7KU&X-Amz-Signature=b9e7cd3a25ccc87fa3f81eba77dd83c25cb0b69a4f99c0cbad67f628ee2bce8e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



