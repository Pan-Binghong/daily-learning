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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVQZPCLO%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034545Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDRM9YFPbH%2BNF1G4742yxayz1BNLaZYi2jWLB7Aze3yPQIgJyJfB%2Fhjw%2FsFzfXR5oOmfoLWUuKQgsHMmbw4%2FMRbNeAq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDIvADDxgzsCYZI%2B7lyrcA0xxijMuqIDufq7nFDDbF%2FWfkj1wDyXbBAtDeluaC0CCD%2FjRqxc%2BUVYWDl%2FjxdJWyIl1Jf9IkEGWUTZy830WgJi4OfCrVkttYoJoJxf0TsmDR0XvEiJ7rcV2FBJJLzAMqhH%2FNGSOJsihyT5Dk4rWN5u7Gus9%2F%2FNutKgdnGMmiCRnRrmZ2RCfrY8suwlTdeKWhDnxVdO0TSsuSL4S0SxEUygVKIZQMJr3RlXPkLZS6dTZhEWfAvdGGwExr1Wswu5or6yeRWq6dh0UGssmKtBrj3r9j2anup1Ii%2Fhc3KW56%2B0XojM%2FAcF6gRIVHSulGsCNYoQU37hcGlZUgcCMlcXVaJI3q%2Bfm2udrYNz7EXCveXefmQeIdlqbHS2pBgm2fx%2BcvCeSbiO%2FtveTZ6%2B3NpWLwQ8g53dFGfwP%2FgeGJTpw%2Fv2uBeDZmPOlqVZz0MZDlI8UHzz2jXwmC%2FALhUXFjZAmeIv0zDxHt6eGnKqYiMMQzwxbLhphTBvWzwqQPV0cagXYi48IXc3Cmqm3ZEhkfkAgTT021WQazmN%2BJHBYnXqg%2FlWDteYonIHyAFhVhWVp4atwEwOxFnrSYeOFSDQcmP8VmasS%2BswLXdPmEfFAaYa%2BqQYy%2BRyFZPCQWc2h2oQiMI3kgs4GOqUBpOgYOU08FIfHyR1YS2th%2BBVylMLZwOZOcFHe36rR6RZa7SpuVlCVp9ohPxbugZZlAL7UY4GDWT8x73gsP6d4oc2YcC6NL8iuzdbpU0apy8CVc%2BILAaB7Qj83vKgp6Ax8CeR%2Fdnt57qf6oMduvRIvDbz4Gll2r0T%2B0d0QumPCH4bAEZF%2FClzBZD7%2Bzx2QVOxiVPPqgagSd%2BT2zQYz8VywD6KtXpIV&X-Amz-Signature=d223a8970b6a633e6ff3c71dc143530eb715ebee49e76a4fbfdeebba5efe7d2d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



