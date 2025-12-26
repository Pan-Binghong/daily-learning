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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632ZBQ3CG%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDgYbsBcvfiyWRACThiIIToSYJZvm1C2ahfoHPcCAogQQIhAKJf6Qun9klplUsB1AyYtEcEGWGCdd%2Bs9EtfNJHspKABKv8DCEsQABoMNjM3NDIzMTgzODA1Igw9DgA6wc1Nk7J9KAUq3AM51mCNdJmY83LOl3Ao%2FipCcRuhvlrsVrTrbQdXybK%2F16CK0kyLmXmU81s0xIb%2F%2FMNI2m%2FQ5GFyEyd7RlBpRFykKQIm8OT8u1EYu57Lx4qrYShNgJhMth63Bh%2FnnN%2BsQ7VUqb9MIwe5%2B0uF4uDtLFu0EqCqaoLk1vnSxlSTycDo4jSioFRNExIgfCWkXP9E6dW4op%2B7n3xDC24vxLCpFIIEk1OWfDXZqSZ5e9Elitp1rhkrKDdMSPZNld7H05%2FxgBWSltWZMnb7eYpb1GQt9pbMCvWyrC3GwWzjrlf0gkBiMkU8sM3HZHnjB2DJbS5aK685H%2FLku39S8%2FUWaDGANh6d%2BcXCuVnL%2BAlC%2FdOug5IV0OCEY5jrmZ%2Fe1IpEqIP60TLN7MecwnmVbodWIZb7d3yAH%2FnBk%2BGq4Ec3EIolFUDVfSQ0YGmyj0XDZ%2F6jZBYZxLm%2FrxG%2BYmiEfBcoXJWMwJcfcgG0nitCSYx27FLGYmls8MeEu3kFcgQFTnI4t0xXYAGO9bkD01YUXHKxB57xuveu7cz2KqyU4MiSgeoITak70nSiRS3anRHTJd7C6bqmPg9OC8XBF4y%2BKBcHtBGIZdVKHOqtlx0s7FDWlIL4PF8udCGL9VMuFduTMb8DcTCRzrfKBjqkAQM3drRI0EYd24WwB%2Fxv0eOJ%2BS2T1ejT1qWEOrX%2FV0JeYl8kixjB7lH6JrNs8AxePHOe36aso3w7EIGYZus1d49q0oEtAOvROW%2BlfD7vkaZa3Zv%2FXLZeqPz2gDnE2iC1I3CVXFaaOTewV%2BjKBaAJi7zqygML1uyb0YKMthY1Xdo%2BFXpPAZ3lul13cBhEngONAQRkKVBjfJrGRrM7c1A4VRRFfXix&X-Amz-Signature=35907d7cf7a4aed4d417c81ce888f60a44bc65fdea6fbce7d14e3143a7000ab0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



