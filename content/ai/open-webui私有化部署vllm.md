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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FHZUTBI%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020101Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGaSQsYJM538BcIt4JfAgCbmfo%2Farw6c%2Fy55J4wg%2Bsa%2BAiEA9Oym83XZpz%2F5aVx6kd%2BePZ8I4adctgJCz0THeCSd70YqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO8Cph3aNEBb87Cq7CrcAygnLr3VP%2BDpFoIw50VMpcI2x%2BCseennb9dgjAz1UF9it8KCyoDdFgN6uk%2Fz6AnRVhfZczX9TFdqKLOFs4qaZe%2Bo%2Bp7jRTyLq%2FhKNVmmaGvSPbXhV%2BNV6wYMvi4X7mtU%2BCtQNj5hY%2B0NdFBsxEIkt1VBwh4i0ceuxrMHXwnlsN7CFE%2FGlmr%2F7WwL3N3lhM5E6WEk6%2FW7PZX8%2Bf1wBIn0ax%2FhQEwekLw4Spze1sjdIzLQ7bhr2uaIqbUJoCiX%2B8erWdmRNb4Nsg7brKubGAdsqpilywSYt6530SVkZJC2DTZiLtskUsDeqONT1eA0FX32CUDdH%2FsEGb7sMB4mW6i%2B5nakbR1koySOiMdobN9wZfe40ymc8C7wY1EfvEtW7ELKnJwNgjgmY5VRp5mVJ%2Fofpwvfg2GpblXDFYFOOhlYLgZ5sg2p2fYI2N9g1bbjgq6GlaC1UzfT%2FoWAIo%2BPXbMbgij%2FC4a9xfKZnJomj9NVGtHKfZvL%2BWhq8jarbYVG7FvbSMDbTaCgeJgO8LmiR0yoPtHuRl%2BXLbWrpRE2OKt4adX9efiMuV3o4NbHFCDnz7G9iQ3c%2BWUqe4%2BZbR9L3mNrHHqQeeJFtJ3PLq8wd9pPv%2B7DvPubX0ueujWLvsmUMKbyr8gGOqUBVFDVnURMharR4Lml%2BgZxfwZFC1bAoINCjMf1biWLo%2F039QNrER3dKTL1C1a2jcXWinNWskwG%2FRJun2c%2BZwkaOt76IymQcsgySmyNx9w1IbOUT7%2BnA93YbEpUrL5eNJqHNyNEU6Oa%2BpQO3wPgS5UnMB0kTsBCdfO%2BgWJ6PmFj8KT1n5XtegF484I990uKaXF5%2BNMIoZYI746S7TfgYOJ9pGDdl%2FKb&X-Amz-Signature=a919bfb889b760f7dc6d81df9f3faa7c80078d0f49f80cc3164ff8cdb162584a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



