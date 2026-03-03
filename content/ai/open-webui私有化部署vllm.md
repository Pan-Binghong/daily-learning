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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WF4HZUS%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFxMFbZkXdi7kbB0tflwpSoo4yKytfCfyd%2BvOObxc1ZvAiEAoSPiD5pKw18yc9IhFqcUWdLO%2Fj4%2FqX3R%2F8nF0PQ9X%2FkqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ1fmImsFZc0XNIJxyrcA4jfqD0V9DYm65WyaQEMfJjvCMK6aRUkUIjsEKtYXQ9lWA0gfmJD7mz1PR9B5XC3DXAIIjrAz8vAnqSgQ70E6OtDP9%2BjJqcjNM0cDqHtExhW5ccNfMp7NrZs%2FZgVx17MbQI%2FLlTCVCWTSF4TZ%2FA7mx93vsqyaept%2Bq430V0LRDqlO07tnQ6y2p65Q2CYiEu5VazypKQsHjznT%2FUXxaVsX%2F9Hs2fipKe78l07Zisoh0xzlqMMMyGTRfNQLFvexxxHW3dhaNSD6NpcgKjG%2BrKdc3ROUTuwKp3X6rKqbQT3IFo3ZmdWD%2BfxMikhxdNMqMl1y3SI3rI45PJPCRqH%2F3TPcA7OI9%2BZzVVS2MMUirKRxt5A%2FCrJH6IPcVSYqMhaVWwD6jpn3AYnG4a4H4erXUiQ1J3abZZFBEc62fhOHK1OIt3Ilqzx%2Fv8HGHfzWbFH36H7OJMaJkE4aqa8d7FozVltReWNm4QPqE%2Fp53qpSzaKDVN7JBtLijLB78zJXlNdwfRHkspEPGibCLWSZR8yeSYTU8VyCGgHLfSc5Z3z69qEt1Q664Ng6cJAdV6k%2BPdD2nBizWGeB78NuD8MwbClAqPfC%2BLPr90eXkxZlgsTu2jdds8YpQLVBv8NRuWrzvKuMP60mM0GOqUBrq9lH2njoracqVgFcxS1P7wp9H5f50e%2Bk9q9YyIJgjjiRsBDkP9qPDasYYjpQETzlyxEeovYUkmcbwDuqgF7egc%2BB%2BKPV84ErSuXyb0HDTgUHcTo56WV2zL8rGaGcIdh5hZ%2FWW57aHrgAf0ncLM4DKGD7xpxNrS4K3ZyXYh1tTVwGaauFRIZUQgVW62HI8GR8LPs4OiKItlJ5guqaIo%2FJ6y8KSQA&X-Amz-Signature=f112023186dcb5a0ee1c65fd36b4096e0b1f1f61a0b9be1dcbc771d0e0bc42bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



