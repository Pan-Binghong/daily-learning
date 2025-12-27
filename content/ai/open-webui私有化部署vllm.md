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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634POEMBU%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEjvSCwiGeNbG95c7fO5V92%2FEaLPOUmfrFVO2bF7BN1bAiAd5YVVcfjVkfWnBBrfPQWiBk2%2FBj6hUNWcRjRuS6e43ir%2FAwhiEAAaDDYzNzQyMzE4MzgwNSIMqle7hPRCTVarY6i5KtwDI1bt%2F14u%2BKRI12xtojR2ZT5YUL1ssOkCLeVl5aTQJR95pwUOGCNMI1wYcE0GF%2Bv%2BT%2BxGDAcK6qSpQJ2K1C%2BSiELqpP7N2drlMT67KhJI5RzEL8x17xIG%2FvFN91qtVFXoJpQL7tpyfZq9pgKWTP602OWSw%2BcQ8ThPSj5TRGJDkw5cWX0VGJvBsINHiRGeujt%2FkVwPNZAtmQwG6%2BwRgaHT9Tm%2FqNywdlkFPlsf7rHaNNGYmOfwWWXf94iAuQIy7wxErbjQwbMIBnZyr7eO77xWaTxfmv0c%2BtD6lVgCPqCGHyKs6L7SYVHeK%2F4Hz%2BbqiIRXQVWQRNs3OC1kuArER0F55%2Fm4Rv7FH8%2B6ZLvFDFSlE5DSo4y4HipevMIGpjJBtIbNEANZR0H%2FPjbWehDg6gvSSA6AFK%2B5o%2ByU6yvChhyYmKI2azO6NAGc1IkrTqXebcCqe5pD8mbgnbwSdtYkuDGyxtShVzX2J6dDRVLAbNuAZcR9j8UTI4TCvtEI3dngbXSLS%2B61V0tKWxsW9biI5kBMrdSV%2B7yg3xm%2BXgSegr3oHgo3J9JVn2pBVG8%2FYtoregJX7g4xYC5KXybfjh6Sk%2FjXqwn2YvX5SNZpgAl3gmTk9qR1ncISspwboz%2FKz8Ywm%2Bm8ygY6pgFgJTiJ9ZPe%2B5z7RnoaDgLnmRsmIZHywoUoRdL3rMcRG5a%2Fz3KrW7yKp9irpe5xlBKxdoDc%2FvfZs%2Fdv8rBmvEc4c2fz0ZC1x2taEO8Qv%2B%2FkPeNBIPgEG84i4hDBq%2FkSzwz8KNBja7DUk2SvdLwbc%2FpbQDbkm5mV8m0IDcTqAuT%2BnnxFQ0h%2Fo%2FnCSULK6%2BAzRlFEnMzhqRxCQFFqZpo5Y2ZQuWNpbEUz&X-Amz-Signature=d6b690e1ba4ee7ebadbf5f4f2e1b813782161bb56c1d3a1dcd38709c81583d56&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



