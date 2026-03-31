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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YWLSTGH%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIEV0oPmzKuKVfWLIC%2BKt%2BKvlT5bgAKf5AA%2Fjhn0NYiT5AiEAzzjQJV5d%2Fp3fdOuxoufebk5EWWCBDZDMCI65tob%2Bc6sq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDI%2FTGagzKT0kOwVXAircA8vgBC5Q%2FlDVSs1eG%2F%2BjVbb8%2BOh%2Bzv3%2FMc27Wm32Zd1dXXAoa85K3nlBJlm3RbooL75y62L8VEj44Tprzy4NeaMNs0%2FxrqhFWnqu340cYDrYlS9TSDECvIsfVU63%2FVov2eVHWmdayCOWzC0UbAws8YjLHU5JLCxuRPSjBhfa4ufH1doUUQReGrGc%2F3c4nYF%2FwDSfbamKloIHewC7BBvV68PBKKcokPgiB%2Bvnzg%2B6fX5MQ2cTMNmCYXczox%2BuViFUPIE7pEBbMGxTsPu98Kw%2BUXSlI1YqkA%2BOQBy%2FqqSxFczAY1GUR43RDOyaY%2FMHAG6dkMwJEkmzOIENkRFhFXs5be9Ix%2FYKuKPLxpUwRtlyJMgpH0KT7bjWP41ICQqoTxgv95C8ok4OWg4IF8QlJWkaPbTy6gHvtzM1Hs2pfMrRUXdOqS5kjQjDuW1Bf9CI4EU7kNrceMq7eHk6R1cRZFVhHQEVUsg0qpEaaEW9V64iHsGyXZQwDy3hM19Pig50xJ55szyNj9ph4mPGAkoSC5MZ%2FD%2F239O7Oj6Pwq290ShnBnmmy48cHETQAqzVJrHDuZZXW1u5d%2FM2T7fDPXi3ncBccvpKiN%2FcqMYGF%2B0sWIOKhkloK4hRdgpm2HaqnfadMN3urM4GOqUBWaHPyLLTGbx9Mz%2Fi6bUCKF8T4m6qHCMffKtpoWhXuUbyIH18maLhqp2Y3BTh5f%2BLm9Vzzm3On49YccM2egWOss0aKccPi0aB6iYtW719St2JI%2FZ7ufGNoA6xtwvFKEelzlZwaUoh6TUXvrP8UHH%2FpoY7ACgd%2FgoSL7VRYsLL7%2FUuB%2Bg881XpKSMFDSnVgmOQJL0Bmsn%2Fresc114qHW4jnHi%2Bwx2l&X-Amz-Signature=652d94e6869cc30df8932ead24d3715ef63ee22df746d0f50d3e422ae2693861&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



