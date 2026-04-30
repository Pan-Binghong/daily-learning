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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIEIT3VO%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T082134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIALyz3i%2BstX8aXEw1bI2j8HYg2QAa4SBDRpN0lwGC4g9AiA8%2F%2Fo6Fe3ftHZtYjD5QsHAusofNiB3tKQ5buC4OGs0ECr%2FAwgJEAAaDDYzNzQyMzE4MzgwNSIMedHXf1HF1%2Fz%2BVZScKtwD3BIOfd5dR9oTN06Sgq3dz8K%2FSGJiJ0W%2BlDKhq%2BlvEqV%2BhzuJoYMlMqM9bshBcoRAsjXtJHQ9UJeEA%2FDwUjaAyloz%2B%2BHW9LSwK0lx0dndL%2BaZNzkCIQ00q%2BBCxg%2FjToVGuWIF75QzWpKYzsc6um337%2BEkXbtm6GZ7Z828jbwscnExf4KCye9A7%2BLsMVTniFHvfh%2BZjTBC%2BzanGDc8WGtiS0ymapfgRGp3mIkd0A7o1mUsS7xnmXuZgRoKAJ%2BKu5PDr5sB05RVcXKHSqDWTdEDfaYg2T7euG9XH2SQfawgGdRp766IESdCUukvf0QZBtLPl7K1y4IdK63jDpmztKTUn%2B38005T0BZVKrfkXrKgCT7b5kfjLNWemBq0v5RI6OhcEoV%2FArYf5sAVgTLgPkNvMEFpDv2UXtPtCv5eGcBNYhcwdvWf07ynWL4M821FxKrmY3nlEMU7CAgcu0h9DQ9tWmj3byUaQvRjvhU8aQUdfPUjUs863zVlzihX7qxGCxjTtoJNHxLgkuuto%2BdJIk%2B7tJua62bNig%2BgKhMstSh%2FxpKYiyuOrnwC6DzTguhhkK3hrOuX0DkFdSGJxcpXRE1A8JKM%2FxwrWuvMnYIzTy5tMUnYZZBk1MTOmNhxU30w3pvMzwY6pgEGlhbSMMSCQjqAgBViob%2BD9VjQnbMaFKEa1608QyI72digGwaegaEuKGlUcpnfjkxGe3rwQc%2ByNvH%2BUTOuAQyr3AVg2mkeLq8S%2Fs2O9BYk16qnwpVJlR%2BZTqKaNQv9ZIVoQ8aelgbW63jZc%2BBfRnCq7IyMtt74jpNZnPWZxZsDx7e3J04b8vyULqzi8MXYqk7IOr0wiDmw03awCrUo81PJuHx6Qq8Y&X-Amz-Signature=d251d47b43d1dfa62405cb3754a01bae32b2ec340ff4272e175cb98df1bd1986&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



