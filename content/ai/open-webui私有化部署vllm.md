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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3S2TAFB%2F20260320%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260320T033217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIQDFu6CFN%2Bxi4zewh%2BJIwWBRgQoWghDRbaJzzyvpw1QrIgIgdqia6DqqHcD26szAcwWqCaD9hCUrFaDBjHjYC%2Bcwldcq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDNoZ48lLmrEcpYmmPyrcA5UI7GxWB4zAwsROtrAnTt9eHyitCOSuKW4kpSQrUxJ%2Ff2LIXEp8rytjwWvX%2BnQC9EvDY3QL9yzBmb0C8xLXY7H4bfc3vJJli55RvQ4BuVQS%2Bq%2FtfpSYx1WHD%2BXVc1weEpdPa%2FD6EhyLvCvV47J3jZxGFDRgYC9LIUOcqWSGBrf8Sj1IFGuSZx93eXBbsga7mnfpX4YUsHMfabVdB7eRR9Zp8z6EI4pU0858pBNOgR0v6KeCauRFMzD5ceEBiM5g6h8AMgHqw44AQVkOJ6K0g1iqm5ohgxxxiutfKlf%2B5Hiw3WjhJ1vhNjZV5kVnpUsGYIwR46eDpWRAL8IhGyLz1R0Pdx%2FVzifCgbO2aSQRg%2BKn3ULfyDA2MuyqEzsTN%2BrGl9%2B8%2BPnHBhyjFbVn9hGGU1D9ywft7mpjJ7Iv88i3AMpJHWl%2FVvx9EUp0R18NAnh%2Ba%2FLZcyRhgt7yFZrNYbv2NJ%2BGLlqBsexXCm%2BSR49xAZrGOQWVxRroLaysCbbK2295OP8h7e3uwGkj4X4scJB%2Fmjd%2F7Iup%2F%2B0DEAp5iP%2Fwu7sNthQ1J41QRNbVFRCFGIKsQDxEFVmGwpdArvxGAH2lLH5WEcmD7bVW1OhMJDinulopIKeNeN144HNMdN%2BbMKS38s0GOqUBZ9t9FSf46uj6IffDTv6R74tJigmPZCV7Nh29xheKqEmLcdD09MSu0mwK%2FfKD4Hk6h%2BdTgHDmBeAL97snivh9gkCBw5E4cu9uCggMC7cBODr5OtQs6W9cBMqciFVYifErT9g66n11BKfFRrWtqyFgwQRRNt5%2F9fXmQYKqcqrf01JYjPUA%2FpwC8eNz0H5gGirbydei8yyQSCXk7CO23pRad4uSff6P&X-Amz-Signature=d8910ba97e8f2be62508a832f674fb703cf801db2aaf74feb7ae229e498752bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



