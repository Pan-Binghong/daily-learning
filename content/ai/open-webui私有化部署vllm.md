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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GHZ2CSB%2F20260310%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260310T032754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJHMEUCIEAGuaglBp4SEPr6tSp6qGqcr7C2ZJmR00qLYMIKWmbjAiEAsC3Gf7YcUgzh3joI9FPCsT90i54e4MW1ZgEl%2BlTtensq%2FwMIPBAAGgw2Mzc0MjMxODM4MDUiDIcWqB2D23t%2Fp0K4NCrcAz8SlCPbrIeuhiCKybWj1XIepCMmuTSqLTTwXUBxq2yKGnxPMxrOJnNVTY1J3VZQ9BKaycsfUBebDgXcZvOiNDFX%2BhH7tomgsqDxQH8jcYGbpO0u4XM0yq579kSzYjiEQRz5wMQm9wxXETo5lQ8lUXHB7nYrY25etfjSUQXT821nmwRp202CZ8RdPbceXFn4gOJqHk6liS1oumJGrUiuyAAzKOByRI30M80%2FOI9GkPE3RNK0LqOaRrbW91j8lpTNEdGDk22RZjqDP93quL1OGSKgCz0fyiUzSbuYsVXrBM6AvF19Lkn7aAVEoan3t2TieigXN06a3awxBDE%2FiTy1uLKjMqzGPYkTwxhQz339Nj8ZE4sTemokFbXwmWiuCedS%2FxhdMSb2%2B9%2FzSHuHrMmUCKTUKXDTTO5GECOm9BNEN6K4LHl8cfgBIkRqBVSWWC73vLlWN2a8BDarctYeW4V9fErQwvFtWuPL2aoA1U8MASBt%2BByJM9fkIfjVsVbOJoM8KXvkMfctXaM8v49y4zo00S6mzetVnNE2031JVaZe8BQXMjYVVFGC%2BktXbMacGNU6jFIRqMggF4l7dgi%2FdcPq5E6IqI%2BwLTDKb6x2WcrxfHsxjdZDmUvj%2F6ZWp%2FZrMOGPvs0GOqUBSzhbs1qPUA2uY%2FHnthgXf7MAazJHpVxqSXCTuUx95OmAdEs3g94QuN3IGUajrt2Gmjmugqmqpjd2%2FfuREoFqMNGTyREn0qUEbPt1HNgeeOZoiDabOgmeAxNQMliV4G92WX2ksO%2BDXyIW0K9Yvr98ayT9KdHyuwHKajBUwVmnrxI0DqYU7mmJ9r332PPj3Ltdse54rgl6lLgu28mz2V%2F6LFryOVgh&X-Amz-Signature=c87a50cf6b615b61fdeb5945ccd1b04e87dc290c515eff7c43442f34f197f378&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



