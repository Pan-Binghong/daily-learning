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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642OY2KTV%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T043536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCICcF0ZulCZuX6pB6qmMykpIbH6%2FeXeSqYla1%2B7NnR32TAiEAvZKjiUioJhbUkPswKhKwq5y1cwILeJQhnxYU0liLolUqiAQI1v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP0GAndVyJYw4JF8ASrcA2cgFQ3DWBmZEcADbqBOdDU1zlqmxTdpVSs1r1b7cv9MmCt2bdWMQeatmeXs2ggr2I%2BiWwsd0zDS%2BIZypvk9aAd4XofTyQpZ09IMFd5L2qpf3yaZcCfsBxqd%2FY6G%2FAM37mJgBORmxZPPExDmgv7k4fy%2BoEqLhp0GGa4Up96etZrCSUyxiTGoiwvwXha68M6X2IuduE5GS1pw6lUbu%2B96vyKPiabgKhnwM0220P2x1cz9mEcOrBDPJl6DZjCN68aMUWk0CWA5k7s7R%2Bln7DYJ3mtK%2BD7e0GtyW4r77lnhDm2wH0zaj6ydhd5A150yG57vAjNaUGuaVx2h%2Ba9B6iFQSCGFGfSRtKoHTN87J9wg0ksoc0rz7rOqhDmRn2r6hbEcjEMpuhnEbbD8WuG%2FoJSKA%2FnyEu6BQdFSCOjn17JNa8CDQlaHREG0ZqhLuiefLgcZy1JWrh1you2hXpZztB6M0HMhXTr7dEWpzslMw%2F01%2B3iu6b6IQ9%2FGjLRGRJZtpIcr3cXJ7zlR0Ed6lqAaRbGL7V1mMepfLaXd2vMaxAL8IVN%2F0XmdPOWfUSEBcvmNwiFs2bEmt2JT%2FQILFzbC%2FGBhgHakva4r5e%2BPdsQtkU%2BP9bIuRwEJElkC1l5i7%2BLPMJ7uwM8GOqUB8NFljX4j9rd7CoCpouK3SiUzDF2bfmU0KSn48ZmU811g7ypUNnzNQ44iZ1itjYIwfHjlD4oGOlcZbNFBfKQAnyqm8JOF2fYAiaC008vzymnj8xCpRXA%2BQIzrru%2Fhv3OzWiGIW0pr5oKcjSlEYQg2zbUgvWjCa3ZY6LvkhL3m0lMkgFXWT7126lwQLljPTk5km96iBIch5dy5wckEcgCIjidJ6gIX&X-Amz-Signature=9a503bec9e38ae18f759fc1fe3346a7e606d2c33a75706b6aad64b8b282b325a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



