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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SX6AAF3G%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCID8xrTsNV5OwCYWOON1GMDRClkOerLeh60JX3On3%2B3kuAiEApMu9kieZBpGEpoeavDgCtgnWgSrk2q0RCXcZwz9ShkEqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDORHn%2FNKs14UfC1c0yrcA437G6piXnGKCSzus8v7vx2TTMX2xp70w190ZtPCp2GCVmoj4MkXzDE2k0saAD0K1mmEVim0VBpUKUy2yHWF8Jvtimu1oqJxqnDMOilzTYeANvJzIyOZrj3gfLphnK1nuysiaIeli%2Bo6M8VVsu9lYEbGayFbuTPvTmOUtiWKFwB28ciJBO3Lff%2BOVD9ttTTNXMS0IpVWYc4PVxvbKercItTHBmfBtnR1mysS2G6vUyDXvRu50EmKiGhsJQGaPTpVJo6FTM0qzKYJgKgSD%2Bk4gGtcw1Cd5KHElqirex8hAHgM%2BgI30KFZT0Q2zyWu1XRn3KlgQ%2BiUe6gR1Y7nUNiInJNNcW4cmuhIJF22BPXmiXKYvYXxBB2dIJqoBELbWygXUMiCMoSmiDfcLnjyHp3BBsM51rExDR7hVzI3AsoPhBimwDS1MRCeLacRBa6I5V5Wzxq8IBvyPds%2FQVUVonlyxoKxGm7gkhRAcMiNQlbi%2F%2Bkq47a3XEA6wSX%2FTh7fqcoV41PlCnHi525oo2NaL0JRouRu8G3vLi1dx3ui7W4dNn0S6Sx%2F1OEEGniSBnEfHAQCL7hLN7ftdp88h0WLSXyBf%2BwUqH8S4uk0dJYf0MjvGWdkl0YabGNmyZc6x%2Fs3MOm06MkGOqUBe3ywDBHuhnGse3JFYMB0pMG4RFT6%2BArdoyROtRTwffsCuwFVSZwmSuAXucK4xfMes%2B%2Fmm063K95C7qwIOgbZMQU40eBI%2F%2B95mkKfqk5%2BpWG6j5UOhq6ZIy%2BzPpHbA7PQlspO9DTSjRuc87G0xJQiA31S45kCGws%2FsVVnr%2FMirIl6AwfLnjisyCMBWHOFYNo8%2FaOC9%2FXPrOEszQpNPz1%2B1vENprCv&X-Amz-Signature=9b0a6e560c6571265598735c9bdf12308a8d5466a8cdcf8b098943de6c1510cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



