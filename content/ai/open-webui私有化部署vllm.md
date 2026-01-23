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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UNBROUAX%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIQCt%2BU4F%2Bb5HBkygp41NhGmdARnFk%2FpNz5TgNAukH1qRYgIgaZqPRSEJL%2B%2BxAgARe%2FJTmbnoIJDdxcUmHgNgbOTFxhYqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJKb9SrC8WP4Cj0PSSrcA6ZEM7IZtxEmlNSwZCVNA3gVcpijmavLeWfyABPhPS5ivu2zpsrRKtheT1RyLXEw5uf65prz8zITU0ahPh4m0QsUI2hbkO9df1EM0QKy3v2qFgLg%2F3TtRr2Rn03s8pG0QJim27MVNsXbb6W25j1xEnU5AJnlXy2cI5CzDb5K2%2B6erpv1aU1RhaCoOTB6SOg%2F4wHgG90K4EpFPffo4nC0ebDkVA3aw2%2F%2FFLhksB6Uw182sCHAa%2FPSm3a41m4eLa8PvxHh49gbTmDhAxaoy6mORqFGaeVwSg7Ucq3H%2FhzE9mT7qYIAS6tPPg5oQGFLGjsl%2BH0sQVyHUjOn%2BnfkTrkLUGn0iOcVukpozHJSFljgyKNOGABiwBm91Qb4NcYmKQwLmn6i0Hkvy9Z3PiR2nl%2FlCH3kJY%2BHKRBBLOW2RBzn%2BwihJSkBtEZbcPYrBfcTX%2FDFamKVVM%2Flq0E5toeMUBCdQlNNqTmHPD7qZe3L6N7TDrRD7HnXhYwAR60AJonxeOBBwxHMIVFyF06djiFOeFrMmEBQQYGxhy4uhcohvjIdEs85QifJ8ueqly7p7FCZGa1h5vSii2nx6JH3OTUMXASFr0DNE7ejoNC%2Bfa2aEyKyFqA4ryg2tePX8ScEqbfvMOCuy8sGOqUBIpVof4rs%2FzHy4G%2Fu1sSsgs3z87g16PZ5wLMgoS9d6a9hzG61wj1H2g61vyOtQn8SoxkpVwdaVOdYMX%2FaR3osZtgBzFAciMXUOw73MRo7WODLzpJzWIWYKe57rVAdHiYT4ILxL0N%2FnXnLgradtcq8v6aG2WwZatHdX9w%2BUhoC40io%2Fi44IMrMg4gtHbPlXM%2FtEOZEI%2BdBYjv%2FAzLGSOLIT7aVcVfn&X-Amz-Signature=13a7215b1523a4c15973edfccb2e25b9ce2cf9264a216df48b4bdc319543dd21&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



