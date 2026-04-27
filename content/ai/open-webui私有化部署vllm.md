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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SA6IKCNC%2F20260427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260427T043239Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDaRixiE80qZmcmq0bn0cj%2BSHTaOx1mMUeL9Dsx3Gr2mQIgHKHGf4FXbufQSqKGSslQgGyPNR0OdXAH3CaeO%2BTQGQsqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEWdRq6Q1lo9c6t1tircAxBCCJDa1TXKlOt4FIUgtyteZTVp1xTFUNj8TdsAanYtRtSsWMjcFln2Gd0CORei3SwnhaVj2pLheKyJC%2FrA3r39mXrbtd6Qj0X%2FbyZnwCQwDFszLVqR5MyZVDuHWuDD50OS3Hc5WB1RSXCShGYKycq4w%2FyyuD87AVKQpNml8%2BG0gAPbP2vExC4b%2FRiRGyBJAh3ZWY29W%2BJq5NacvMAAqT6kNPo1JFxEiMnujRSenXFtElDcjbjrzmLTTzfUq2ecJUW3FynSnFADnQOirJgAySrS9QoXqfyfNo0SYxuKTf43m%2FuiFg9kM565p6rqQRKw3%2F5uaamfdmrtSnJ6mce5ekJaEUNF8VBmWEmHrpYZHieL7EFAspUc2DEuk%2FoyjvaNjFsGz%2FM9itl2lnCEZ9VTmI4plXglsfAUbEWGlIOEgBPvLv1unwBD4z%2FMDxtCekVrJC8zcdSGSkEKd8axKPbYEGIRuy4Kh5iAVyQbuetsLoUqtSlBB4pFKh6f6emi2rWYF5mi2vyUVN0bv7MxePGPIYqvd9pfvV%2FHnhSsAG9QCkzi4dpjNkIpDg1SvutTaaHbbZxHPB6f881W%2BJnAauHM5Oi%2B31Blk1Qm2nTtcILXi1yiBVcsh8bGCBCtGy2mMP21u88GOqUBd%2BCGeyv8d8I23Ny%2Fd4k%2FGM0tiBS7rVcc8jq1tbnW5xl0XEjmwFrx1oZDK5Spz0ddA8xtM5fuJMVL8XVIH3tP9%2BdBuJFCfRawyAqHfkRHYsalrDIDR%2BzNPPpXxWNWCzAV1Yad918USsGmIRBy3mpK3PfISpgwdTodMf8I8%2FU%2FgGhWBGrrYNMrJetgyQLAw5TRx1lbPeuavUwPtGVZOo%2FfAmSePX%2Fj&X-Amz-Signature=b6d66275bdac5af8df29d76a8c6eb0c1873cf69e6820588e6fb3c77adcdd7cdc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



