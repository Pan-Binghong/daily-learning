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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUSY7JIY%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQCFD8LNHLk8mNDqx2LmlULcProcPn2fjKpz5xVcWD9a8gIgG1JZN6UKl90kUHlNmeYV8Sr8iY3N72fuGQv5BjcLuJ4q%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDL0JazgMNj5fO5%2Fc%2BCrcA8pGv%2FY5bp4MFeRyfGf8Kpw9mg2zsXSkxPMEsNBRlyGPI23XmqCM1I31xb0gwkmK5RWCMIE2kclTkAkYkqfTUgsPnonM5lHD1IcwOy6anryusuoD5xvmNwL5q3BhkC%2Bns%2FzE3%2BEAaLATyDVAZVNDdSx7qtw0KlLlsXGsNake3Qu9fQaQ%2B0j8dkInjCxQE1NNAuPYxTT8u7C0eYKQkI%2Bnn%2Fk1zRfWjQUp2xr9B3a%2Bl6lYNdWujp75zkNIIAs75m8djCHMP2TVTG7WPxEQFMLUTlORDQXyJABwm0cG8faZYn5j%2BcAnqxDoxgGyn0%2Bz5qOva7J2n4Lvc5fABHDOksG9rUNA5lnh5uRFky%2BV4Yb8ViKkgB%2BuISB4SwXOMMW0diyBi8d2PwJtnt0fiLB1YwtEC%2BewhoMLdouJUGCi42owMtk9e0cpiBvnlPELeVvaVtuCWvK8FnSqMmi1lyHNZZcSXZVFrE9YEyv0NRcjmJfvGCO%2FOTjqq%2BL9%2FFfhbC%2FWCq5qNx8jNXrxZQqIEj82hu7H%2FpgIUc%2BfaQjMs7YtpJ8m1UxWdX6Q%2FclOY3%2B0MBMPsm8gi9RKcyeJrugoXQr3%2B4wiYOyzX%2BQ3TJ2FudOp37cSqlrFpHhHoIh7dzlkWRn0MN2dzM8GOqUBNqbjdSAy4wtJZmxS3d5E3Udy9XNg9PbKEpVT6q7j%2Bb%2BzSlD8ACyHEoTLJXsRvNVzIeKnqpp9h9p236RjbMqKDWFD9Jz2ZIMmROXmYrllHoPECZghcCkgFXjAW0aFutBWBM5Ub%2FePdUi7Q7EVrxU424blEzE1IKX%2FjvlUrMYGfF2B%2BIbD7T6KpWxKMYP%2FWmjcKPrC2sxjpS%2BmH9Ivkm3tTrbClwqH&X-Amz-Signature=0e58e0d9c907dfa0d0118007a7358a736cc56ffffc25035ed2ec429ca5bf20f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



