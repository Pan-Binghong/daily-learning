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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633LNZ5SN%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIClIhpmlsPPH%2Fonsow%2BqIzC3yGlz8Pmrjo9PyEmOgfOfAiBtbjOCGwdA%2BY3gG9avIyVT7U7LNZbunwzf2CISdAZfAyr%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIMau0%2BvO9tvMUv%2F2pMKtwDDDezKjUs7pjwwydZDyXrszy4s1wWw6NyADqSQgMzH84G3mG24APT25hJ%2F6UWggmOanmHKkM7HQTDKhEoxnfgsAj3q8pBSOs34OO65dfQQfXL9FmJf0QscvCM%2BytMiojoMw25m9rVqnxSUr%2Fn%2BBUqsUXrAcVxK%2F%2F3xuv%2Fm8ATxKqULyCAiSjI0BqTHp2TxDSrqWrqpqV7YdrYi7pjHOzuWsI4urkPhEIjDSoIJ35UjyoB%2BPpbr13hbzFcSP3PBqFzNGWzjr%2FUzqK2mXAeeVc85lq9BytnHNLSFXOz2blXeeqAm6fAwe6gWtwfgOlMuf3BJX%2BXIiKQ6CVhoVAN5Vx1eaicsOgwttngNd%2FcAts9QzBs85h%2BY1KhPl8CRTTJYbeNNP%2BfZTPE4pGdwbUhYQK%2FkbxMmh2O%2FbWI0epQrH0od%2BWJJkk9qu2kb1prp7rHQMabfGRs%2F0QbHBFXLz5uhHRkfWH%2BEKJ5xjeQ15uyDZMyhpaSstWlcYah8%2FERSAiFIwA6G8t3q7YLnV%2BcCEdqoQ6nI%2BuntWBfJ8SB0L0or0F1TzyYJi9SsfuSJZqvakjaZKZ%2FOjS%2BgmXYVRgUq6eSGzRLWXz%2B2KkJ7acQdoeNBw%2FpbYdRbObF4Ao2PAni8RYw9MSazAY6pgEV1MepLLFcg%2FIAek6npZKyKgtrHrzU9nnSxWwcJ4ZLH0TP3G5kXbVPucSPLQ242DsVSNnFDrGT%2FmaRwuu6hQBHCSAsBONydyEqLAY0UhMEciENMGe%2FSg3KAxe6hSyb%2BtLYINheH1vG%2BPXG5LreKH5G9%2BAnO8v5X4UBmDl1QpZE0UiINC3T5mvG6Ai%2FrF1PNfF1DYTSrHUWsyu3%2B9qhG%2BfB52bc5jRa&X-Amz-Signature=c148c320085dc9e4d5e5b2004a91e79974c91d5657a8e45c1e3895f6b813c4c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



