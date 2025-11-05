---
title: Open WebUI私有化部署|vLLM
date: '2025-03-17T01:36:00.000Z'
lastmod: '2025-03-21T02:48:00.000Z'
draft: false
标签:
- LLMs
categories:
- AI
---

> 💡 在裸金属上对DeepSeek系列模型进行指标测试后，有点无聊。随便部署一个WebUI玩玩。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FAR5MXN%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDxpyljLqXDSxFU1dShY%2B7J31NiZE547mNG1OOPU4GRpAiA4%2FjImqfw%2BuNNl0I3P%2FNzC8kW7GYicDU%2Fldu6s4HlWBCqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5TuiEsT5yM8y%2BvZVKtwDtGntONrf5Wiz1m0tpZ8jLB%2FQIOGgggxniS%2Fh9Mw7nodTN5HmcsuxhCKum2S3CwhCy6hQIzISf0svw%2FV4s6x5hYTXZLKjym8T%2BG5X4ebZakFtMMbBxs0qpPfTfRDM8wCpiWEELy9VfU76aMqQlxIMPEEZ%2FyF37KHqYeR8WTrV7QaDK2ptdPVLle5HGGilKk5B6BagiMEfJ0R5LzCYVzlocRNNE2B1aP%2FA8D1SSqwMfF7xBwlyo5aQuNxNLEQZJ%2BKK3B7ttNByopO2zE5HvobXP5z4TA91q2hqMXDmsjcN58akTRoS5hfJdYaGe2K1eB4pjsJH1jdwQwIhUAImUEewICefnoc%2FuG2spc0DvLtzocvr%2FcdgUP617nlYR5%2F7yhwndkaGKJcMH6R6yAbOapV1btvXtqwDeVn7sXavBexQ9zeJcylAWn9mk8oM5UemwuR01HFnxvz2p9L8xB2GzOnDURHRzxe0IB%2FjEXNL9n3pHo5BafIiORlcbyVxbuV38rvyEVQD6JVQScn7x%2BkOD1HHvtsKJSSI7SggMAvIvyuMQ99SGS6TNxH4Uyc4YTQVOrFszl9eB2xEaqp8do7jwNpHkyXiPSAQlwhSl52PgxHDI18tlgBX4Dg6n4lU5Jgwx6KsyAY6pgENsxdmT2aEs3AryOQiHreAdTNVpaoiowRh54LwNfmQUHbGr%2F3AH5Irml2BZ8x6%2FbVbzQ2v%2Bpm%2BPSkx7DTzX637yxdcfKIyGltV4AFum1CdJRA5ectfdVggDflAeUMXXqf1VDB7oxWhWD3MbRlRG7aWuH7PV6Df05%2FU0U%2BPajcuCuEp7AVQ8Nhk1R6GMAJtDg6xhdlQWEt%2FlFofhqb48QhN6H20o0Db&X-Amz-Signature=1da67e0d91cff0bf3bb74a211db53a80a186962b9f2657987a6e650d74a49e54&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



