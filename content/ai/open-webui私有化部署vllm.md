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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJGMNF5O%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAifNOXT%2Fs2kKyO17BoGAfpG03CuDGs2EazurbCWRw8AAiAecf%2FsFxfTkt%2B2lalfi9G6XAio9Vef0FnJ87Q%2BnccJ0CqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM8O%2FW7tsyu3UKxU%2FXKtwDLwl%2Bo3OwjfX8YCNntBI3DxydTh1XiyK75lAI2FtIC6SFFClI7PTciHBY6fKqD9Reil05HSnvZ2ERuTjoON2FdfkLSGKOknBC2WuNlfO4Nog2jQRllaPEBC655Aeobv4BTrPf%2F6VlW9oqsu2fFMkkVWShnhza0n4ILlPb%2FLJh9EN7tpjPinSJWvFbcrl7Y5Rpqb4rO%2FVUe5mupuGntKYdn01FcryE%2F22zFJARTyGnonDl7414R%2BGx1sb%2Blq1Y1ROOezyRVyv1373ujiX7nTJaTOsxLEGrk%2B1u0%2Bc5Rvsq29CybL00zuW5bOGz5FZInH4AlAuqybLBNlgtKaTlIoz3n3NZebTjBD29yYS67f8zcsaMMyQ5I4aHj3uyOoKPi86n0j87G47CKGfVgO18MgBfvClltggPyuFqPdVkaZ%2B0BZerQ9Vpf%2FC5LQyGkA%2FsxPLF%2B7KDJNlcSdHQYOFRr1i006dV3y9QKsWQ0wKbz8%2FPINqVrpklZbklJEcYc6KO522R9obpRcPduHTRnYpagH%2FJfsVZ0gCmRW0cLkwKOp7ycYltBCV%2FjMEX2G5k9YUDns7s%2Bfl9EEtGANfnbPoVEEgOs2DI%2Fmy5gJaYA%2BZKFIppElo8keWza%2FBTGFq9x4Mw0PCvyAY6pgHA%2BWI1lWkOpnlmuFWVkSvz1aecxdqCapVZbmmxnlOpB%2FOFl7uYiOxAh63YEKbU3JSTTdzMLIrmLQXFFLkf4aooBs7QLNWOIjNW1YQzHfjk0mFgBsYdlWAn23A067NZ6G6e%2BXB79nKjiA85K6MImfEcTyt%2ByuWFhAnNtYnUOu69Rsr3pUWJa3zCbyS3BS%2FEKrPWsZn7dYBV78cPWgmXaZNcH2sfoXL8&X-Amz-Signature=0bb471cfd0cdbf9cd4a5fb276b18ef4e11b9f99ac45a816f84fab2244ff0b093&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



