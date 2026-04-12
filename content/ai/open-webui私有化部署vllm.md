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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDS2FFDW%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE%2FMJVysGILkqf1jA4WAmFfbcpdL7VN9jwEtlcV3fo%2F8AiAV6Akmh7Tpse5W6tzv5cJGx4pmRBfQHSQmCF8f5WRHVCr%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIMdHGuH1t%2F5JsyaEwCKtwDfWWldQPpPQR9YO%2BTVh340cf8AgRlNKnjuPOJCPHP781TKFuJ48XBWT9SUSFVlY4BcIFrbO4RlcFG5s%2F2qTV54T4%2Fpwaue%2FDjnHU2PEQwnyVk2kNg%2FPCYpEXAOYw1oBVvQKgZjMJofFS6tMyPgSJJzp623NabfIb1uV0aYylYRiGAM3vH9U2w4RFYQ0IHGaOFCHrARO6WrLShB%2BCe40lCYtc8lSg6yn8kecfMvRGGjN%2Bta80qt59muLnjovCEzkvHDe6ikiCjmBIUFbsjQMw1151z0ap%2F9cyadTVL73zeRXuHSsH4azlezgZGriGhMxmy09b%2FR1gbs%2FpwgzX9EMH90A%2Bltj5Rvatv7i6%2FipXymlDxsvnfyJk7CoFeyntBVRpu8bXJTL7b2Z9a4ic9KPCekH9sImGvHs7jaW1eE4f2QOh7P1WpVXPUch%2BLFfPtCPk1fniYZiQNeCvdjwmRao4mrN4ysFLG4fXWgRAB7k90na66BDCD0UNl0NNYnskLFjetX%2B2G%2FYI58a7aRB%2FDygxtWes6hAJt%2BcYbBOqVDcVE8u6EN0WimSmTp8Q6dKkjAaabmRhs573u50fAnRt0ps9kDLmuKX4aKw4y2vweMSu3zCrdIVzyh0amoa8%2FKkQw2YjszgY6pgHzknMhxeoV%2F1It%2BNGRoWTlFgjirmZlpgqfppBTBdHBE6iHf1fjQVf9xOMxQqn4wbsIHoHIHt36hw09YZ96RkxIb9qywxGCktuk0UH6D9dLTFo4YXPiDnGtYcsXT4kG7fsvXkJa%2BMW9qFM77f2DKgJCh7Wb3JlyhQm2hebW3K9lZ0ax0w4KkgJjDfJGOEyxg%2F0JdoQAO90hp0UUci0c4MExUrK6lLm7&X-Amz-Signature=96a687eb0e7cd454d4072facb9fc707a18fcd4d5e8715448c6dce97872bf88a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



