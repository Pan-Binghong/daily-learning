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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OVLKOUY%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCW6FQWf6JO7WYf%2FHrvGq%2F1qhdq34Nf7WrNR1roz9xwwQIgbWBlZTDu3tzV48yMk%2BZZVy4vp7uQmWpKo0bNNV%2BCbcUq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDEQAr709rIeXOxZh4SrcAwGdBD94dr%2FUoofXVNJf96TUvNLbKh0oZjz5NMtQSA7X3ITEYi4UziqhpezWxV4Dixybl%2ByBn3QmnY8JDzQpU3IrdAizo60MnDumhvKP8WFmGhKPTB6zgko5l%2Fsh%2BnQuo%2F%2Bl0t5UtwNXM8QisqdSmCf2gztSflGMaYWb3NqOctxLnoq7%2FeSe5iR%2BO15Y7vVb6C2H%2FT4lXmPy6n2pfXM8aFMvLnDFLpfkotV0R8wHw4Y6A6qQTBoAcwWsJ9NlXhGx2XgoC10bGxKaAOhyXKSLkQ37qw%2FKKdxTNPuqfQm2%2Fnspnt53GH9HNenO3y1vakTJUsUjUYSRtSChS3N%2F0m4PPaWMxNiKCJ8K%2FSecRo0oQHKZhXdSLtsZSpQ37SPk9CaXQdMh%2B5fwtm6uGpInibYkq1eHwZXoJVKiVStQ8atXL0a00W4BtmfSXchVbroVfYaK3fu8axFqGkjRcG2dlZLAIoQBK4o%2BIKvDNKsmt0558yLeRdDDyhUFhXcar9DRZ%2FBlu79QsGk0Kgz0LJNhN76FkCTJWQP28%2BB0Tq%2BvsMyY56U1tnFr7EPJvrVyKEXBoS7ABzE77r%2FrpU0U%2FLMJpoqe5vcQeWS3MOZxLJM6J6B84j3nbC1Xh2GgvCp4ivL4MIfjvM4GOqUB6dEkF3U%2FtNG2f3PrHIuH49RzWI0%2F6Dy%2BB24ZTnci5cz0tWjxcuUKz1HtZPQNywyyxJdHZN0Q1Oa6zSMehTQUrgznk4HuHPWmtLelrp1o7wxqv55tqBlY9xhrp9flHkxx0w%2Fn7hQfonbaV5GlIJ5%2FTzgir5UYnr9GZZ63DjtiewxPBsLXmNKzC3X%2FaACXqBTYLsPysg3eTCo6rBw1cvdEOy22be%2B4&X-Amz-Signature=14f0143155030437fbfa8613a343c48e3079ab59a6df139167fae3c3ebd652f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



