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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ISU2WTP%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJHMEUCIQDW9YewWLeflvMZNj%2FlyFe8xqP9kwedQYNgOzHVEk3WhwIgZwsVIyXqtKuvubjRlyQ5ciJMFuACZyILbVS9Ny3cYioq%2FwMIJBAAGgw2Mzc0MjMxODM4MDUiDAp9Wg%2F5TWiCM4bWryrcA64Pl9wH3xuX6GueUoavyiO4uk4v9UzgdN0KVbH%2BYxwBDdVljofVCg6Cj7%2Ben%2FI1cGFhA4cxUkOOc%2Bl8lZqsG5S%2Ffk3O9Ai0sVcLgIa2mBetVvhwmlKwmJsJpz2mxnkrc2LJAbpZbIvJo3nZYjYO1Wtq43TzjqzSCtx%2BPWu0y4xF3zVcT4IzZZWdz9RIk2yHcsrKGTuHdG6uw6CH98gcr2PejwSVdsezBZTXD2pWpLmotQWIq1iIimaEeq2Le%2Fk9fouSF84zTIPUZh4Y7u%2B2UfshQNFd80o8lLeMb91KUpddjZBPgVINKy4rm5CqsSictvfTh%2B6sOqregBOJoC3MwB90aZT4icPmVhtbPRvt1%2FRnndi8pfUryH2MRW74ZGhISQkTT%2BEA4vrkjQJZFvw1ycFW9sXFPtQLKgtRL2aWKqm2CX%2BIPVbfRdSweQUC6kBrZ6tk97SO4pTceAddn1jo1qnkOW0waCAQObA37X%2FBPpUP3ws%2B4nwLoDKoS%2FfrUQ2K1CYJcB%2BQmh1vrUxBI9WBsJTOQbhaDF0jwQr6H0xd1oYLU%2BMHSjf8jRgFJHxhh3S8KfI0mv1fvcepsF0tUA8oeMW8kRChfaZzXx84o9OKnw28shPrdfXlKHkifz4GMNKTkMwGOqUBjQIzNbUz5M5acyuiBcJeZrdFmaQLr0oOWxbSVimGtknAVYglI6Q49h0jpnOSU6PGPjn5fEzkF%2BTBq7xoL9smQd5n3Z6oVKWK8BhpNsCqIdU3YKcmUgrAXzN5Sx4qGJK5%2BIcsm2TCFvkEMZYk5LFO7AcnQYqy29zjNUlmxHO43uvG4WN9h9j4Ur2GrsDqvZnEvnEDNfHcg2uZ249K1f3B0F1VfIN1&X-Amz-Signature=6810403352acc45cee00a68d248636fb318187b4719c36d51a2bfe661bb885a8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



