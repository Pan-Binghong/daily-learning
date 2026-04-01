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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTKKZ76P%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCOyd0jf492wpJ%2BLddQtet%2FDwedq2dwly8beLxW%2BvbE3AIhAP3fByoL2PDIgt7NNH9cbGJsIYuZrWitb8HiBLl%2F%2BHIEKv8DCEwQABoMNjM3NDIzMTgzODA1IgwcDTWW6Qb5ueLj%2BdIq3AMplcLL%2Fghn3rlmfcQaSkGZooq3aRBehnKsCz13aACwx8dTeHLPueaVR6spljL7IRCTsx7uQIm9bKnm%2FTO7O1vUq1YLpDcVDEkaxmRkCvSOyr8GGfUTgqj6%2FwturK%2BPUUM93eMZexVbfKkIq6LJv0E3sfd%2BcCV%2FoYzauFeRcSVbnwPLCa00YX%2BwPDeG04btD%2Bk9tUT0KUcYVBEie7aaaawMxISzDT7jmBu2Dy46QZ4MgJ9RKAznR0cvoeHXLGVzhVW5QuleBm6spFkbhw%2Fg%2BiIAeFH2NljYoowW2Hx8vAwH4PVEaYt1MV3ZItuCUyu0SyJPIsPKWxa3g2lnprZnAmcLF9J2ky2AvvGAr1XZ5SKjasgiwIZjta0DdCkV%2F51OhafEYhed1iIuzoEGXOv0zc4OY7yHUWK2bfVAmvQ5ze7o3LxI9UtWXq3e1ByaLIH9H3q2KwttV3LXEJ2XtY5nvuAhJaa%2Bd6Hmh2HvZxnWjqFLDUXDulKASCcRaiKik0%2FEGej7GeUgrQifMTVM8oeKyXnHCW%2BtX4JY%2FOWYuAfUa47Eg2%2BT6MhRZfZOSdphhxfIMyGyNNa7VegYwXKb26WSebkE8crbCorNriRswuNuO41wtcyTWkbGVeQOD9NYrDDNoLLOBjqkAXKbCK7YUmvTK0SdRaIGVy4IDnkQfA5PbN%2FZv5%2FF7zUJvrorVpoq0ObpeP7rNE6cvb1M0toLambuKwngRRf1dSMrgUa7YyylE%2BDl4MMp0XIdUMMRdYJzxNzZ%2B6BFHajE4noCsvuoadIHloZCNiHBmp5Y2dB6GzHK1Lwk38k%2FDIi2Dk1dOWAC0wHT26uRNqoWj%2FOUpZybK0uFOOweZ1M1z7bpuW1R&X-Amz-Signature=3722e57c238447fff5ebc7de769b9b598919911930b78d783bf9c2d6089f60d3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



