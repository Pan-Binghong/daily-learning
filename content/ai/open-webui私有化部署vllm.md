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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UQC5KAQ%2F20260409%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260409T034906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIDLYdBCpvKtfEj0YwwhR1fibfjWeOqQY%2Bsk10H2woAS8AiEA%2FNh7an2%2BdVuBS510IjhIVDR%2F%2FYL6FgydXwD1OYbX5ukq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDCV799Ro%2BaQ9uOjPASrcA2rbI12ToWuNwXAYIDefGhOrV%2BhqMvEV68mV2qQ%2BVtExuHPyiM%2BQEcjVKQii%2FN9tcVxmG9a54mrFMukVnexvgBI1DfAFaJSDOsnKvY7XAo59y51k434pnIYHNAOEgoUaRjUBCgR8ezitw8SrF7juGKsdd%2Bj%2Fbnx4LzzHLOsXo8WyDS0weUVCb6XWSYiHntSPTFvcgMpKBUlj%2FwJVNsW1U6am9rbOnXQLdI51sxL94%2B5GZ%2B%2Bu6X2vo5QdNGJZqy%2BLlbYmD%2FA%2Bc0IxhKpDTm%2FepZTG0qWlttBz2Trt7zND5WqyST%2F2EFG3IkLKCSR8luVYlFwAqa8knqLZ37bqR5YbGYi0vkNho3toYeRVs9ZoXhOMkH5I%2BL8JvOvUp7HrsJgwOSUqKE1uj2fOe8lnGxN7X9vKU2%2FlQMrWsr0VaWPBKOlqLv7YHqyZApiI75iMzE7ZBAoxymRZIlvy4yDr5%2FDvfNfURg5MD2VM2319pD3MEk6ZSCx8St%2BdxHrsoLFiWeB%2F31D7clP3GJHMbBijqxuSHfQh8uNrLMHBcTxnWCLJjQzNHzyl0s86hCQ%2Bve46jYgw770A8cSO5E7len8NzLswryOVCrNA2ZvsxBCqJjUJ2Tn4oXVdAWxxr8MTkzDOML6z3M4GOqUBVBFXubjrmDPPS2bh1d1PZVBrAnVbyOh%2BbRgNnSldoNcR%2BOFUt4ktWqC%2BPKmYM7IatWXtR7Bm%2FKHrL%2FAwg1%2BAB0AwAYOVNzTiW5kGYDFJFx%2BgrZwyc5%2FNKwNUiBxfLXRUyDRBXP%2Bk8bDw6zlsA1wHYt%2BR6kZEfYg64pn72tl%2B4QswUerdwoYYQjNpOAzLrLzYwXkvT4oDo2yoE1gJ6HZMh%2Fqk8%2Fso&X-Amz-Signature=cb8bb972724b44ffb62c6b4be6baf6a7995c78dc6c03623ec9ac59c2feab4710&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



