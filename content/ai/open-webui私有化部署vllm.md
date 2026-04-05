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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X52ENPDY%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTZ5cljoN9Mk%2BDB58l1zfd26Nd0aklv7tcrS9fJgaQPQIgZchnO7hIYORoi9flmNFY6wHef%2BmwXuyWxA2eDse1R4IqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAx4rAh9r0jFG7PfgCrcA2O7pzzFFRmg0VqqKYKKAzFffY6xjLHTufR4Kwa%2Fdtn5NLyGdvh8WWJRKMc1kSvVrq9USk11uetpIbC1daqiyfpStbYeJxghBw2Scf%2F9s2774TE9dHr%2Fq2ruU0Xi1%2Fq%2FmptFn0NBlVaTXi69%2Fvi9xTakliLQdBeYRHWqGVxz7oRwsicX8z6kddp8o9ug4BrM6qwM%2BBnYQ0uBu95WCNEvk50oJinz8p%2Fc9C4U2G6cDRcYNTVHDIwRr1K9GWP5yBWjvJxA1TNHiWH1czQypXBDvNmMksq%2Fqgmwh1Nh2ED%2FDjbOhpczS%2BnYPTM%2BxIjuBJsKf9nrwqjpHC%2BaBNlzRhaPvZ3X73wX4KfTL2RN9pfqJ2LiA60rUuSIXkJfyQFD%2BwTGDtTZFSb6efEy8t7mhYGjWes4e0Frug0TzcKURNkyzVcRYsLt4rIciK3VIMdI1BJTMHIiUb1nWyR7WPX0%2FTFegPILY2TYa4PL8OqKCZvCBMbAK7LDt7NIJ1i4CDleLYgEOam9PPO7nXXCgq6KVJ%2BewR3sSh98h6TlbHAOE08QW5IQd6TYeenwordgIZsOQ6YNtxuIOApgNA82YhlOPk6%2FCO7bqk3viE6%2BrG4BTSlGSbIVW8i4MtrHJg3cKbh%2BMKKex84GOqUB307AFb6e5hOBLO1VDs0KDaZEWQAVWnuR%2FhgKJyqRrx2kaQzl2bS8%2F3bIPPkVYWFwKVdUAcgSYNwnIsJ5VXTroV26KPqN%2FQKQzYpl0jxvJGfA41nRTx3qFTmwI0k7xtkQLIgnDDwxeAFTjeIaKeMSzXD%2BlwRd75fn2iXhGWSYJGQR%2FBubV7zhCmtVlQo8JDnwBl0fqxHa3ygc4SgYSm%2BUOTxCG6Kr&X-Amz-Signature=f3170ee6150b622709b36796b3d891df99b3b4c765cef71b2277296212c10861&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



