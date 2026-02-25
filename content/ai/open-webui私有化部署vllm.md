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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A3JA7K2%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T033817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJHMEUCIQDrYzbzPp4M6Gq5W8DgsHgIKYBDXwIhZ7yJTsHYFQLhlQIgKcB9nDcqQ3nMWFZvfyAIuwPRpetpEIBHq6gTHc098y8q%2FwMIAhAAGgw2Mzc0MjMxODM4MDUiDKhKXD26b1kUoZyU6SrcA1z3YkyiXvHa6wqzy3sqdgaYyAPctwhIicwKGmhFFrGEOer7bSXHNj4L5TCly3Ln22D3TrFR9uufUBC14k4BKg0jPQxjtm693V8P%2FDqaS9mA7tkFLhY59vrMU6nSr2Yte54asqukFuMFljuxzxRBKswVJIaYIpLhGKWOXToWQy%2FRMnYRI9hsWYeiF3m3waLH0QyJJQI94Euz571KdmPRmbsBormHSWEWZIskLIYeOGfEM8hLqzliDHOKkcebiuuIZnUU75toovgjap3Q1MtfDwfCBa%2BIVYixk4kA0tq2j7Aoee1gvcBfXzxLKA3E8YlmjGxK%2FIzlu44uAHj9WoHcFcMbwqeGOdOahhStHQ81vObkjRB3MVPurscXpB0Ny29Wq4mWbGoq2V9O8q73Ig6l4%2FmDNe2oOoViDBDhtaPmTXC10gkhAG2A8f1CHexsIiUoZMJkf5%2FnpHXWNGkPeHCGqGJ83pm8QfVtkTD6U53i18Kcys%2BKpGdj4QzmMU9w0GNEXcSAGvDlRJwAa3RTdi9J%2F9hfEGc9mOYQiNUBQafVP8kCYHQPhNBZd0tL2kaT4vAiyZd%2FSxw6SMVs4LtdKtiXPKzeZAyeRE875DhwpuZnFxpN2INjGFMJsipFBuOzMMmE%2BcwGOqUBPzc78ZKlqpMYLIwnvbWsSwCVoiZH31AWzagyno%2F4Y1SYdJ%2FomFBMRxwzUkSMlygkB%2FEVhGFFSAG03QypPiTLKmGPBAlzFZ3TmUCap8hfEB4RjcvdlrTIJdG%2BQmCiOQyo3Kw0sdDdZYK3WhCeUG9n%2Fw2%2FwRV%2B6W7x6hC93OlgbyquYZz8yQCwQK1kQHzOV6SehqfswaXqOUPvguLsBC3sEQil7pEW&X-Amz-Signature=fbd1e425cf23a4003a7828766023f7c624ce1390b16934572c56adea6c538cde&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



