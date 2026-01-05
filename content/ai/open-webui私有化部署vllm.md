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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WHMIXG2Z%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLXdlc3QtMiJIMEYCIQDTi9slP3jufg%2BQjv9ZSIz7aAwnUtnMqBs%2FDGQerQUYEgIhAJSxAi5WLveC08Ny3Lx5gyXmTNOpnATxplrQYjsKEtLSKv8DCDoQABoMNjM3NDIzMTgzODA1Igzdvb%2FT0RhXpaI%2Finkq3AOeT%2Byy6Qb0%2BODs1h7SdBWxmrLhgm%2FtTe8gcY9KNP7ojOB1ecQzN%2FPUTGYyhUkaYNCqpqykeT0JmoBqKDaf51vJ9Y1lcakJ%2F28T6fCIvq5rOMD0kiyrjN35WpRC4O0b9vZgRE4eV1IofsbXMlu0TiNYf1LLLFNZjha0va4OZUJlCmH9y8OndLB4izLHzL%2FPFDVJyKjiMYRqtrvVHGp3z7zgJOdgmgIBHVuLbtnAUkzIazC7sUtG7h3ZRzdz7xdUWwQtFm7aCowAMLOBEK9MDZdLKlHTRzKwPrKZu3v0v5GZHz3%2BwoMmDrCN%2Fwjf4AED6sKvCAL7rPsiKT0gG2ddJ0MDRy64fDZqIE%2F4LTSdgp2sGuMozpOO6hrrBdZTv5UWfTHSXv9oI%2FgbfSGIyL0%2FBre%2BRak9s7rRXXnAJiFDjkocxUhBUbH4m3bwP8sUDOsv8GHAs7Q5trGH4dJ7nMQw9GHutMGdvx5KLrsmXG6GejWm0%2BSwwmz%2BzTNMXkKabMLhP6l1%2FNp0jIitpQX3DOjy6rPnelSpX5Fji1XpOHyCbg8InneTMaQxZhPfjexfsqz%2BAyAJ1i4Sz7gF639c2nV4SNdwsVWuI8LXPyceL0bAjpa3%2FM91g%2FoiA6iNosC9WjDHnuzKBjqkAV885qn7FipilCi5ZX7ZtnmqTt%2FrJVOCuIOpTdr4YYf8%2FeCLGgnd1bMzW1EcyIvCzaa0R9hZOq8lozJP2FpiHepADtyfRgb3hwMI%2BdswBmrY9FSyPUX6h8uNitzGk7pxycRGI2RFKDtOJntvdVDOOPxuZ1YfEHEY%2FJLsORy5Fa1vDVUnQfMkq1bispllzSm4SOfk12UzSA2XtA8T6i1U5%2ButcOMn&X-Amz-Signature=67954b52eaf01351164a917542a55395e18500db9fcbbcd00409acdc91535321&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



