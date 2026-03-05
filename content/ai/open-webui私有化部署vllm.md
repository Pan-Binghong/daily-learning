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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666FETPZDH%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033033Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC2efVuacvYe%2B5E%2BtX%2FwFSnrncmXB58t0dLuu4Ts%2FpPxgIgGdSo6%2FfNbhQhRSDBxub8PKFmXx8QlVWZwwlsX9e01LUqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA1FRTgq46T9s94l4ircA%2FL2xL3ohM5Dim0vycnMUGPFVUaus5ICfzTjESzrzoZ9xkKVNYbiJPDKTlS3SZLItloPeGpuKtfDshtdVCglEVPNhYFyDnuN9WVwQ%2BDuH3C7vj3ge7tHfxDWsWIXJ0dwsIZh%2F%2Fc%2FWDchVOYXyE8MuLyFHZTpb3oCwfFl622jz2noFkFk%2BJajG50S076K5A6cMbC2CpW%2F93UYWZNdaoCJUQnGeTlVQ%2FDZHbEtUu9rVntNRpf2jCtTJEHFpCRRX7pfOYzrBJh45w8%2BRhHei9S2E69GLam%2BMMX%2F3FwxyvGPTBqONJppKaoVk7mK2TfvRzm9PuUn2aUAFVhWBZM6%2BAPCHRpCi5gre0RWExTYo%2FZ3JwOVvNvywTXRlNrmrKzQQwCi2Iu1RF8nQMeDMfHojUhCdBy0iXQImsC66F74nE8DJJWZYqjhYCKioCbcIg%2B0NEwit2LlHd0%2FM4zXRZOchvj8wlvRP%2FPKZf30SLzn5QlQZCAKmk30hLGTOFglTFNhorMjwQW0Xccflk04glmwHJa9X64Cv%2Bl8wt80QgULs53V07leWUwpOhvVZEcoA4hGjp5O2Hf3csoghnJfT7MO%2FTAtbAQiZlcbMo27ko%2FJedVmKolxPuH6SHMZkvBGEQotMJPfo80GOqUB%2B99cXNJD6upesBQPykHjeIuczqzYLpLLeNpz57fknVb7ErmtRykH%2FKgoPjhyf5GMGoZyc3T3khErP213hAwvJFBGk92xCylFhLofJ1f76h8xJYAMd%2B1PO5AW9An7n4CIBGatlOcySNKNyf9wVHxk8ZlpmgvhWdkfeAStqUwXXhDtpoWOUh4rq%2BHzjXGg6L6je5rWWcuJIGQW9GFdUCq7XY3Ip06h&X-Amz-Signature=c82997d4089c858c63d7cc66a6a0bc5e3e1c3b182c528ddccc0a0662b1a34c64&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



