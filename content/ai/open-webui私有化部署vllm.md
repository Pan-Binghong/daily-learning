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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZMWJPV5%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDa%2ByyzuThNFjKhOR72n%2By8BrNuLtmejX1GAU6KzkWBMAIhAP4SjkElkQPR%2BDnOXYnAbS2BYJTN6qkxri612ltwDyegKogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy8CugNWDdsfPPdnbcq3AMSO4jgUS5fiSa7cqCbFbHXuan7CU30SMoTCaq1WOMJU8ICiyWm1NldyapQ18SJCoGMWx4ggBCchGBKtXQcQW8DYkxwWAPZqAylW5%2B5O3daYrF4aJHK3004J1jzemVZVsH%2FfAQpEF3UZxr5Kt7iRFHyeDi7jtBcMOmXtJItQhme4sqNnd%2BdzGdwwDMG0Qe6UK2kqticCHHlLVry7hCXL5hZ6mZ%2BaUjm4utR4kMzyjMbRZ8WxAdA3SyII%2BHLEcTednjt82qpozsIZ4LC1xq6TxPjagitV3zF2WtFpquFh4nMIUUiMtjiKBUsr6axNq76RM6cuwFGVng%2B9RLZmQc8zYEILNaldt5M7msf%2F3UrZLNXENI0JIgqnpWf%2BJPjBZfbrvREc3dfOD4gnElwUe%2Bkb%2FNs1%2F1E7cpQJtF0ykgTIGzf3i62%2FkIgggQX33boplmRI2jzUZwZB1%2BrVhsLhwNxHzHtzvistFQfrfCti7KMWQV%2BFaiJQwrj9tlXzS4RMnTj1HA7P%2Bh5h2NTTnjhYzsoj91CQi99ZiOTSnhSlXcHgZvLRSrBdWHcu%2B0x2up%2BrVX16D8VSl7xuOMqzaFJdUOMBPaNVP1M%2B46oOQY2%2F%2FOkZeVoJsLaA2owUacM0PHSojDhjrbPBjqkAYusR2UNtAIJdz8TAuNwlgYJX0kgXeh0wQ77GSSdijDVBk8OWht%2FP9O2ihVjUl9Tx8lY8TeQSYmUaQBbvluTT4ZoY%2FOptKjENYGKpLR3PiSs7mGWqhrXYpZGMCa%2BHbXEfyYbak5OlJMqOrefjStxfjYUVHPXXmMfq5n%2FVzmXjVOf4EY2VuGaflBUVSzlDQx6rBdMTAjLPYpPVnxrlr6QOiBV0FmY&X-Amz-Signature=4b4bbebd29e8a54e2bb899800caea7de16ec919d3faeafc1b0d1b65e7a4b497f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



