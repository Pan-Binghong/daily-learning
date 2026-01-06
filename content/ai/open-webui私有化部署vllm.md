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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663KS53VCQ%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T025905Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFiGKlHYLsq32%2F5vyL2YjNNkqNe6n3aLVg91W8hj7fNdAiBZbit69bWlx9iE%2FGpr4Mu%2BEYF9OiYhsE8kvnZrHzI8vir%2FAwhTEAAaDDYzNzQyMzE4MzgwNSIM1lJZIaHQdGvyogQzKtwD5nyftyebrpwBgTMW59CbTEtwhQWnOa2%2BFDGKyacQKPRKU1FUjMa3KbFBvhl%2BmAuILUplzMBidSBB%2FVyhrAy%2F7uWBguje4EuMajm10K8vWAwiSrw94lhjv2ACF55ADiR7TetDilAmOCK1nSrrXzl%2BsJIhQVgVAY%2BPSbezlOA181fMDatPzzESnlhYUdhTxkbwJ9WZMiYpkLVlR0xgKKSc6wif2P1RLlaG6w%2FAatakvi5UsCuWZCsxw7XVcTR6Kbcb7TpcXEHaTjRARtfPk7uK8YraXBfgiDMilHxRLBEHBtbBAHh%2Bu%2F3X98O7F9kxE3ZATffhdlzj8PJcujMVTzr9%2FXmZ1FQpt8zOpYQnz74lYvJfkVKtGsvBLHLXMyQlFXEhVPdQptX0fWBu%2Fpea7n5y89VyiK9EZCIM56VZh59ZTppLGxUbD7IYd%2FCpgAOlhDlO7s1h5XM0jY9pTpSKE1h1uj3xjuakTQhm5mq5FlsX%2Bt3bLnnk9bqsnfyDSA1RGk8LM%2FMZ3Pr%2FoPoo3dhwKY2bAcciJT56ty1Ccmbs%2B2wuRF%2FnrCytQbLIIf7k5o2tuWQoNMs1rFbqshSmSSckRDOAh%2BzRnaxLJTrCsmqvbwi%2F%2BZxtIVHFawS7zduznqUw5%2BXxygY6pgGZ4HRJmo2hH3sD%2BkmG%2FRVo7diN2ErW4K2dXf%2FR6tW2zpsMWEWEmma7U%2FqqUMczy0baQdeebwwtgf51XHW2Zg%2BS5MWziIm5ZlDRaxCs10i76eUinhf2I60MwWsWoXaXcPqh4IPPi1SjG3SsF1xlDKNYeONZBmW5PSHoRbkk079YqmwsD8UXEXbhGzk0ohAky617YD6tsiAGyl44QkneaGTtdzBfNRBh&X-Amz-Signature=0801cf6bb18c568f5f7adaf476c32c9eeeae4591fcb3f7d2d1e7ce60bd0f2aa9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



