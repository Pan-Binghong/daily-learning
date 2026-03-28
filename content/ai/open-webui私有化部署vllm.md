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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DPJQODC%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJGMEQCIEWp2o6x3m0PPnc2DSk9EFou439V4zKmCe5VzfKEZIMfAiB179erp2auCg7rjp8s%2FBDd5UQfLhA7%2FaDU0pcEFRy4JiqIBAjs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2BarQEsJLDSSO7Q5jKtwD6knfXA10uQWAMvXZSFJD5UZnKE%2FCR390av3D24uAjIbl6zszWkj5uKgO0%2Bb66mwucUIJtmo%2BH9XyVdZm4HHAnkRwXLWwgrbDa%2BSqvo90VIDp93ySeX8vXBlH30lkhp%2FOoTkev0M1J4U%2FOpbJnI7ez16PGJcu%2Fi1sxeoVmUDdBhAi5tlD1Y7MM%2BHCppCxd8R8nZOzt5OuvfND%2BeWpP6ineQibo04mObfUvUcKcTwoVrhRfyO3a188wrFLcCXwcknKabOu0%2FdWaoqzGriauiVhLfsUp7G5ZiTAj2uPUn%2FCQkyUDLIEB%2BdE8v%2FaosoIp1fuD0QwwdSX88lQxj6M%2BszDrRzWRvKvg%2B1naTYXu%2BmEekwbw1TnWFmGAV%2FlNk6x9ID3xsHRf8DItFZ3hd4PbTcO%2F43BU5xN1jsY%2B2%2BRQCRtp0EA9IiWJu9ESrdufl%2FYOS3e6NCpKiSEyUtEIQbu2sqkD6IJE65JcLe7Kw97HJJjlBEJ288UmJ0ykbrtGf5jCx0C6gvZ9tEEZZaejqzdyzEcwYRx1iwM0Knt5d8j51VbDctUfIbzUyJJEFnqAHtV2vzk9RTr65IY1JvoPgQ2mM8myYKT3MHS3ruYdpjw%2B9TPSuYLuNM4AuhuGQ5v85MwvZGdzgY6pgH6qJkN6wkMKzhof5%2FamkxcA%2Fd4Hp%2Bol33OZgkjSBsaxMJy32mY%2BMOgWl6YzCRkyCv1fKUoWGg%2BW8Fe6mmUgXV%2FkbS8de2QxYzGbsC%2B%2FOhZlIcqds%2BxcSu4YWX6eJ%2BaO9IDNYqZ6eqt6vjp8wupPK3NjTCF%2FfYUaiuUNY98sStwfWO4nedAc8Q%2BdhTH%2BKLpoOPlCQ7X%2BwrZ1h80bY5jO07O%2Bf2valp%2F&X-Amz-Signature=a4c3826ff3ce4df9da0e879b47928de235c92d1f0b050d2fd7ad27b94b7be098&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



