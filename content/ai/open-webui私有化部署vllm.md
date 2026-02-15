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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDGEI5WK%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJIMEYCIQDbfRzQu20XlHWE0bePk6XTSRhZef00dfzxpx6mcVmEMwIhAN%2FjDpPDSynK8zzQuz309kxELGVMs%2B%2BQGXnWf1Bk5oSYKv8DCBEQABoMNjM3NDIzMTgzODA1IgxaPbs2CrTZWkBBJ0Uq3APWW60XnoAHANPlA%2FkyJdZ8YMfXotuAzRSQILrsztIDvyou23H7xq3lX6At0VfdpGZtAIp8gnc3yErFeyOB%2FWMnmj7nQndrKBpmp0PXv3wz9tEQWYTNDzOn8kH6z%2Fo3j9yKwZJ1bubYSDdox6Y2JmX%2FoWUmRwR25dajxlv6mMPdOacAAjZtxyFHUNaIwpwmvPbifL3gNm4q3E6rT0pE5GRIO1ARrO76vM2e%2BbgziV%2FqMpi0JGfc4CgTk66qIOOfxNqiC85ex97G97%2B49P2XEDM7maCv2tNUTE7Z%2BIiD31btUG%2FF03i6zppCUfpNEelmcUC0%2BaiVwn6o2omzHj24em8JuJYWDIdaOjaU7YE%2BFKnQdUE4DuTw1xZ0lH%2BotGpNrGk6Muio0Fli45%2BwCVVf0Mi2JbnQIdwEjCdjvBS4hcF5L3jFwAJbA5OYIrFqffVcZkWRRXOrHvhKQkRAYQyIz%2F6t1wFzfuQ5HyUDO7x6zlIFw2LOQ6tJjNmYQOwe0rAW4Xlh7C1gFdvjVjXlkfLX8z5aIGeU5KAR5skQAgEbs%2BIa1cmWFVW7eqAmIDF6YCCnpA0PEBmmmmLVkUbodlaHFYlAVW8ohY0LqKgkgkWdrSeE9yUtk9mPGpoKoqQM4TCEnsTMBjqkAWakb4IPAB7mYvIPNNvV1PeWLlfIW0Sts27lFcCmLJgK6BE6U4aFHXW7CjQL3nLxN%2Bgnwp%2BfGKCp2XJgVJn8KSOO54qqELJw%2Fm1NTSKIfyjTTYjZzu4zCaipiuTtrDDFuMFJVH2Vuitg1vyCKxpik%2BtfhidF5GFh2857JeigrZQa3SJJ4gwUKVQwZ91HMn2jEuxtVTWsoq4aXjyD54UUsy70TsKd&X-Amz-Signature=2278693cf084a5122761f16c8bbe92c8ade00dc0edf9a4e62e609ceb40d77523&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



