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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R63CCZD5%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJIMEYCIQCXhHKVgnA12tURkSd50FQwYCW%2B9Xl36oTkAH8iOZ4cmAIhAOZ8b0gpB22HueLXvln%2FOTTbYmj1ecrWXIiCXEX%2FKDNNKogECPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz15hsJ0FRiiEbkEbkq3ANSrPLAaooidmkqCNJOPdHlnpaxzizIjIKtHlE%2BXagzcTddaqTWjsy7yFej8ioCIigsUCg%2FIck1ix7a6wYXqfQnbloUfPBGGpTq3HfA1QvCPlqlrBjJ5C9lbO6j0KGk9sIJm9PrZKl0jmR9EL9Sxd%2F5J93J5LY333prJsdJlCvuo5aFBJ8uZos1rnOx84gdRSfhO8ix94QuLkxadPR%2FKivaoziALqGJRdnRV3IJ%2BDvUeFZNGl239zIzuAo7mg8JTSXZjYFFnIXzI1sPqojOzBGY7m%2FzPG1yFvdcBSS%2FN9N6kxAUosioQ6t6Af%2BgYdXXmodZKZzM%2BPEyWhLpzUQ45rlQ207eHB4Y5QrpkZCqNydxFD4npZ2t%2BvMSMXrf%2Bo5AeqLEgL5fHGwcMR1RLs7t4rTw4c1O8P6pg%2FIRxLWmMinYmxFMuP98yU%2BKtYGUq5CbRnHZi%2FcVDp9eY7v2MR80tcXtVlrSMFQYAKoT%2B7tvx0Kq5xHNRBmMh5z%2BEnL2FmI7H54u4PqjPByJp5RhmIZqebuEgIxe1ip%2FSnFYhxfLdGSF6ptdPy6mH%2FV411HNfjgBsPR0WTyZFX9r%2BLTZZk%2Bvfl88U%2Bi%2FSPMQmbBlmM2qoubhy%2B1aw4OnTSX1weun6DDx1O3JBjqkAbLe9%2Ff5gVjh4%2F59Oz3c1rN%2BFdHvrBfseuzUT0Dia1d1ya83mzmRTBU27UzC3lZr9AesVlon%2Fnw7jkz7jGL1jW5xlSXEGpCTO%2BcUEE%2BAKYmzyqdLDf3kCOeLqyyrbAzrv8LbPiAmTjgt7m1%2F4OIZUnksjty7Nqk%2FJFWzkTG93HQtOW5UZ6U3418%2FvYtUd9iqn7QARZj%2F3Hif0yRPT3ItOrbtE1Ar&X-Amz-Signature=9f869a8a481b3045216bc23db38e222e35a8e4b2d0d914dcf87be5162a913294&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



