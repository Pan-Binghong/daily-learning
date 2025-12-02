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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNKPGVS4%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIH5heOj%2Fulo7Fkp8yX0qk4l5jZNRWCrkA%2BLrXkI4NuXkAiArp4dtouoScTCihJDVqUaUzPuva%2BSU6QThUFfYAFr4Gyr%2FAwgJEAAaDDYzNzQyMzE4MzgwNSIMAUh5xzSBY2Z0QXSXKtwDWaQxLNDKaXtGKRzgCrrK7qZCOUHdwL824dJ0NV9oaW2T%2FgwTHKQWfK59n98TAyWrWMo487fBSyt7JK4MxwYHXM84gRxeOlyX0VGOPeof30FmqdjVd2HlFZB9BJMtU8oOP9zqk3F5yBmm5l9uQyPp%2FMq4cMJP9uQUNMqEU%2FHd1xCBMfZvDoeBA0rfFAxtXSsWK6P8Z0Xqy%2BxORkSEWXFsFHTY3bCGFMfn8rgjg%2FhoCP5Kus9FppkFXg3CgXhaGid78jaQM1ySLxmJsdVI9qKXTeZkoE18dtJfD83Pt%2Fqz0tOqShRJdvFF9lJJFGnIQbbnj2Ob1LbSopQjJEoVFcvoTAZl4zqH%2FWktIuzTR6jvCAGnpIxbl7xajsUgHgpfDhvtb9bVvIv1hKtmeY7pqU9Mie7QkDfsByW1y3vlibPqClHV%2FrkJSF2qqRiO65JYtFadiaFEs6mqzSndGRoGubrHBuUTQ6MwMYfCgtfvvplidvpUWdo6k31sVoP1oDrK8ObabG%2FRXJJqbfn04k0Ms4%2Bd5pSuALc5pIU8%2BCKgRwtEI9DR1Sv6UdG4H2Mrspjui568owhIhk8x2zPytozhU8BPgMxKv0KKjNpX5VGVXf9LyZSDk%2Fx6j197QCaiNPgw1N64yQY6pgFR%2BxE0szOBIdQI8t5dURr8akdg90w5tDW2dxHp91dLBI1A%2B3sj1qM06O%2B7nY3A0d3OhiPbqiAWN4WDstyoXj7Amsz0UHjARHauUEATQI8fUjP2YXSzceNJxvtzWKAdeOrLCIJOzkbOhblU5cMQ0O2AlfE4iplEOpH0yZ1MgAgY3eS%2FN3%2BelhPCs8aqWz3QfIitUsnxYveuZXomM4dbzf7Na1QdJ2xS&X-Amz-Signature=c4fbba4400db40d8f4f9b3b149bb60f68c1b0f4dc9687170ed34541f59cc5a5c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



