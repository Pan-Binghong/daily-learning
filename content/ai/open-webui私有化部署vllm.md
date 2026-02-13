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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W74AWFB4%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQDeUH%2Bwi4TR3ZcqeLkkES%2FWTIBkmKru2K78SHCYt4zm%2FwIhALgpNtEizB5dYs2vz5TMg9%2BAJT4PfQuXy5hzpZe20MalKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxdFskT7lhuAAzKyhgq3AM2JQzCeoB1vWB7cPr9PFSZNSqZhMLr%2FZuAroc51MRsFMn9pS6tCHvV2WSZYRSGYvjn6F15VEQbKD847FFRrvsPLd19E6G6L9J9cTCA71ECqxvEvW88psCULHBrUxi1QicUkQDDxtNGtdw4TX7YmHR6hj2KpcANi4%2BOE2S69%2BLELyQMH6vvwpv5DbV12woQFJYyGCnnE9r0GwEh2Fp1hMkjKk6Btfzym9i%2F6F9G1vsRejtAVeSeTgBqCXeWPOBCAsAtrIzw56GN%2F9gVy%2FdNwkI9Vo5nfsv%2F%2Fv0GUbfEvsduQzP179LqgrSEG7x0dZJf3vBpe1LVdjjZH1Zo917Q6pi8kFpFkHmGTitLHKfCCdo0EGXZsiiEi%2BDah%2B59nmnCEOMj%2Fh5uW66cmwPsdA5yo368ALlbQJus1bziUJ1aGP219f3wUQ1Ix6Kd%2Be0EGMH%2BkPcLny7Y6c%2FBOSpD3tm7kkZVXLUheQUoHWrRCzrtLplIIBNNFiiezxkQ0zbPYD1KA35UGnumt0MOw1JN3x1ec1yLGfIT5dDlItxxGLBdKXtPp6yZ6omwQLJoKEgZ9d41rbslAPqePy3zG6%2FNPfdCppXeFKK2TGfCYOo0Tyv5UweWMNMLSFvL3mzsXN5PGzDUubrMBjqkAaSTny1qBXwvzAG9KtLopFsXDw03APCTOfYzwDAJ4V0dRg94%2Bv7UQY6QKWcxNjqXRaSiPV2%2BaUla4fBWNd5TWpsShwohc4OJEotk6XzZQ4vT4dN7eCHbRXBCEcBrgE7UzxksKJRzna%2BDEj%2BidJcMeN5%2BLU%2F24hK9if1rhfOXh97OMJhEZVBn3NNOL06V4QQICnpXbCzjrya8ny1xx2yWZyUf9%2B5g&X-Amz-Signature=a6484303f30092d11754cee293e354e7352ce7c3109686decd42877eeb624715&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



