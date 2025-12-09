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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFQULO2J%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T024951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICScRBDUllSRhziKKh8S5zbIv%2FRkustJrZ7aadCkLDC%2FAiAE71obeXHQA2J1kDTNkj%2BJ55hSfxWL4ePsYQAv1%2B7E1iqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMliOeAg3XY0h70QmXKtwDdDL37UqIIOd1hQhk7R%2FSCY52zmWxZVx7nDNHSf6GFyBhbsVfJEOQ%2FkhUjigK5fCOYeVHaG%2BruiczMuaEFjb2SnC7tDf%2F1CtykHQ4hhr0%2BcA6XdsCvhkWMaMVzYaXtden%2BsZMGCT5KxjWuLTXgWdileMxa9Bu9bhHywsY0UhEx%2F59wTEGr8QVm10uwpXx4e%2B5d0C2SXMBnhOnQkEN5O20updQwGCStQ5G3utnkafn9QtKRG%2FRQ5INsuhN2HUQIgVCkm3%2Bl9NGBH1l4ApQMY1f7PGpm9DBxtrM%2F%2FRUmD9zGOZSoTzD2BwbQVSlCxlZpXO5ipo2%2BpTGioMIkFqAR8mtWr4DaaAvDnwDSHX9kT8Dc0tNxLrN99cPvXas8NpdrET8W55vERjo5eq4%2B3XJEZI%2BLbMFkebZjRytSMCi8%2BxDsSKf94qTmB6H%2FCmUh37WnN3JRexjWXEc8XB8Lz8chEqirUzcMEG89yxLlIaNV98ez%2Bp248irp096mf6WovsorvFcoixEUg0FQehVlKR3BvPj3HbKkLaQqjmOpWAa4Fbe4YqSUVFEI4Ik8Mk3%2Blr%2Fp0pfMKyHnWMzviqusehj55xsBjoQayRnx5%2BFwEQONeu9w8O0qRIMSXJ0X6KMwPkwi43eyQY6pgFJey03g5O0ND5uVOQtbhn4ml3tZZQAjf1gwZalVQpWwq75npcmJ1olIn55s2dO6QNVgXN%2FqzbETZBMpgUKzt1w%2F58uuUV%2FSy5BZJkM0eqnF31WXB0c3a5D9UvHQj00dm356SKZb2caVc%2BlXMYXgUU9Yu6e9Bxg1SmItLK8VdiN0YNVImduVhXV4T4qOjUN4Q9Hv3Cr95WsLT0Rd53XteDWeVKPvj8G&X-Amz-Signature=13eddb905c02c2b3f83ff7618a810de0f13c2cc549ae4c2574d7711e092ce841&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



