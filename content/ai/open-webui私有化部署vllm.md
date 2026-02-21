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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4MTEART%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGqByXb01UmhKGCEnun86atw90zFDVPe4x%2Fu28tV%2FcXtAiEAt%2FdPTyxmN%2FbnOgu51ZcvC0wxrhPigyL9Xz9jxLDfJI8qiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNH6tkUjJvpwOsjszyrcA82%2FHS3%2BxEzxytwsT5tIno1pziaZAtZqnieDYDu0eNHQZx8K%2Fzby6c0D80PnhCnwlFEo86jne1OabN6lilnVI0rf8qcQoqhzb7X6YGhcfTck4HgY1StvhhHvQ2lS3U8H6XylmjLzPOKZjt%2FYqzcfJi6AaEOwxyqhTY9YbrYqee4%2F%2BxtEAUTnX3X0ytjl3XUSc7ZfYK1CrYN%2Fb3Xr4g%2BFLPZicVEJXkttlF5IS9%2F4mCUeIUllpvsAUFjmtNMNkw380DpwzATzyHlDCI7u7%2FmXbqJNENd7ex4J0nEBZ0Kx5G8YicZ4Lilb9O1XRu1VpZiuXrEOY9sHAhjENcbfDc8RUHXYS812eHmuxpzm63HQ6Fb4qPQ810pZds5nj5evRxl%2FadNTy74J7m6U6LMTW%2B1Q%2FNGBAtwBdY2G0XQ%2B39ER1VU3qUL5W8FT9%2FKMnACnZ7pOIUIK6Avayhw86IIR7E1IgxVpD0r2RscmSCsRHeI1M6yefUqUwdsawuqiX20IuDxwCMYXagvCzsJPxiautdC%2FxuDSpZD7VrWmOhSUCQ8KPIbfJhTrIe3VS5EIThaniFx3yDd0WFBfhMYNfT0elfoCMSDFtHiZYKIrqNa6SHjxvLyG%2B%2FzcwDDsOIN4FqN1MPy85MwGOqUBMrLVfOwxIsmAWWnCDaNpH7QuQyEy80x0d8w5dJWD%2BGGyJwvphLl5zi328XoG%2FXEXuX6dOFNyHgNPoGUmCuQmSZcrDtydPTnggN4CLllcAf6NwtO9WA5cCp%2FqTAWREkxMCGTsoMHcOJD8eyYXhnbpyjwgwdqyU87gnTp4TxDLfgTrfngjMLB3FLNRNHM5jf3QXZAsCzoFw%2FkRLVHascDPanccRX4O&X-Amz-Signature=b2aea7dae8ec6f9b93f25456c4d4defac73f72c64f1e06295fff798a7edf7b65&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



