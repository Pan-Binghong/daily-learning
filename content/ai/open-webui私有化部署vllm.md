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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YU6T3KXT%2F20260420%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260420T042144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJIMEYCIQDn20VC%2FkoPttwLaYAID90NWAr6tnA2fBnRFAypJs7XLAIhAMpt0UDCP1snvhrMuq9o0NYU%2BsYrcqqB55cvxrv86pg6Kv8DCBMQABoMNjM3NDIzMTgzODA1IgyLIVPX0xcqgXIb3aEq3AMjrUSnl5QI3escreBd8dpr1mexJe%2Bqot7o587w02XMJSVnEvXTVqjkBK0TXjOc1995xakLKprCYZqVxeLSpzsJHjffTQoETr9pdabCE917XpP9NfqVF%2BM04WC945%2BzqnbDJtFgS4wepnA08aOUQIWcQeMzhCvR5gQWL3dlCECnCEv4GArAJRw60zP23O6SenMYgXrgy3rKXYGKUcD5yNvXxgcuWMKjZjcnu57BUZrpuSkTXWZlMpRq3eWekRDJFOUSf1X1pb5tyY7h9fn1RfK6pAY%2BbdtT3a7qpxCboobVJ75q15%2B9mmNm5nc3zWmi8stYhLlbCYjZZR84Mszs5ePQ%2F8sF2Gwbgq94rk38UUvDCTbUC7osxoJ%2B6a8IApfX8iQQMJO%2FsMDE1CQVD0exjZhHPFHaxNxvBfXrkjRYzy%2BUF1kbzFPwUK7qbD%2F3ZDuag%2BTXLVpg8Kvf65cQ2IJwIgH64kvzk0ak4%2Bgsqb0RnNAetxS386QeWSrj57hnrvfVElDdskug2%2FdrjLb0FCRisKWU2i46eyvaHN5E3oN5kakdWbqbHaNJyvz5VYaCf2pOpExxCJluPIVBTni0O95iDDdbUMH8q8xfauRMC1ZBjHxYAGm8eDjizhDwxslz4TCrl5bPBjqkARUs59%2FY52yKwsCTk%2BPsYjsgf3LP6i%2F0Y6BVGbQ5x7%2BCWEw4XijlZ9%2FI9Nlqq2UqUDK%2FxsIcK9KfnO5nSeA2Vg4J6kMRB5SLpJ%2BaMFwHKfQl3wC9tO072wjT3V0u3tIP8s%2Fa87SIPQHk6%2B2Ac4s42crEhSd22K8Tk69DpdJGNnK0pDQzwndlgOEq17GhJPMZHPYtyrucrczWwBR0Gc1%2FbvSOVltT&X-Amz-Signature=8789bd35c558141406bf34d041e51ba4efb7aabce66bfd7d278aae072a3494d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



