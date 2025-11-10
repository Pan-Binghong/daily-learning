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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAPDCMQH%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T024952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIBqM%2B6uH6yo34LHtYZgkAF12%2FGV%2BlLsxYacxLyr2vHZ4AiEA7ul0662POIdYfKjl7qlcusazhYXsryz71e9ujcCfFLMqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFhOtQeiSyzH98bO7yrcA6HvSSTSwpfLDCJ7toqjwgLDR7OAHR4a75aDH5S5uTCcVpfSJWdHYVa7LvNGU0rp61aSjWGNdRt4HXD5u2T0UVR%2FMBxC6A8nxcKPH66qayFqDL7VC3Q18dWV8Gl2X63UKINLI5u6VGrW2oS2BU5WZWQUr9BxsGpOMlgBoQ5b4B7Szy3MVmIW%2F5gRrq%2BSFM4gpP6tDKNSIGH39vAHBIboUpfqFLW7hn5hMv%2B1ErBVUcEvV%2FcxCBhP0cFKBe5DuTwLVDu2fo5M6XxQjPrbtApCoaqsK6CJ0Bf2wtNI%2BQ413ZpAqSlDLXNPqLFrIjCmZDJK0DyyMxEfBbSI2CtS0DdRFpUWlhikJV859N7bhOHIm%2F8S7Q4hLOn1oP%2FX0hBqtG56hZwvf97GlTX7DSeGCvgXhBOIT1bUF%2B657TaGb8LATi9mqk0ct1y46KjmgJL45qko8FAFmdD6jCDUr5TpIhMZtc6%2B%2FQTjiaHJ2WQaVEU5K72hp7g3hq1yhPsaTyAiDqnp%2B4Q9XToPCisKDFK6o54X9czvoQPL38cDZG%2BHwISYbOOtix4d4ig1c05ngtRINqgRABUSbIC63VVDhcQ8NUodiE7t0%2BR5H3wBn5HRMfpwzaepxxGGdhFZket7mzXgMMK7xMgGOqUB4Yu8NYMc3%2BO2NIL6tHKBMT7D84q8eXLz%2FdpgU50IP6eI13FOzCCcTdBkWkONRqvCpYDpjv6Jakf5aqBgDpqAHCX5Xu1ayFnX0%2F3KFwD8ZyCQrr%2BfWum4FdJzrcF2csllgcBmJ3%2BuZpi%2FuhkNPg1aErHa3%2FPk%2B7jNoIsMfEF%2FscJ1RonwHPxYVWX%2BpdgvUfnhkNt2gfEfJ6Hg5j9MbmJzUddUxUzi&X-Amz-Signature=1d72420b1acd9d63172b9d2c5f30d93fe01e3b6f77c7fcd378e77d4bd5a3a6be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



