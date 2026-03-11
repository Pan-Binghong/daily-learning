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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNKY7IDN%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFWSiWXIsUuUU3vugviPfR6nBsFjXxRKpAU61mbYqgvmAiEAkF8rzNElRrE32o3cGVoRFmmRjFh1yMCfwAUvbulZPXAq%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDFrti4%2BpBx9jQRhgeyrcAxIE2jRxBD7VF%2BFJ4iTjMV8ZwAwN28yCeVfcbGDoryxksWOs0EkX8K8u0OCQm9LbFB%2B2JWD%2B7hlnOzCTSD9jfFZLl%2BIlF8ulTLuelABLPYgOKEDlDksDrzKRzWQCscfHtWBd2QFMVjlEo76aYLxdjqCukVSE5u93%2Fgj6yexagIEnDMogTq9Ea75w9wfeOYspXH5v2mbvbbFdUWFMsdn0AZUI16hFMxvx%2FYtBqlh5jTOd3lJiD3Cgfer4uA7sGZ5q0rsrpQU3lzPpme3OgWTQVr%2Fhp4n5c%2F0r6R9%2F8u1ACsywBHvuohKdMLwjo3QR2LSxnr9HNdSTb1aOlihYLpZLQFFYUHEsHIdEUUiTslbEdGA%2BbsSvrwFsug7kceqFg%2B2I%2BTOsLGZiTd%2BHX5yEzAmj%2BoqzjAO%2B9daJ2QQFzvSzo8So%2Bjho8r%2Bw025806KkhFYpz%2FGv%2BXn%2BTbunJH9KDuLHL5ZEPHNvbp7fWq8NVhRuu28%2BB%2BVkG%2FYoxILoikVwaHrnO1b5crhSqml1RcdJesVNFPiiOqtIu45k%2BLk6oWy11o0tohCJt%2BeYrpuIFh9HKT42KvtpzFP2jkNvX9W7mVEC5kiRMuThc%2Bx2%2FDmkrzJ0r8W12DTq%2ByEJL4W0QotbMIzBw80GOqUBvV4IEykI3i3b3FmjXJMa%2FxOwnzJoKDGrCyGdXHdEMeAxnRSln838bmrTeKhrfCRTFwcSgVTdTETCfvUCgIfWHy%2BbcaKCa9GHhuYSi%2BQEfOW8uZNvaikTD0WywdTEcQ6IUQcjdmiZHrLXiGtyBrPm4xB5nMgcrtdvKPWzNzqK7pCwovfOjl9u41oRjmvan%2Fn2LQUdK%2B1EzQYdWRbM2n0sdxjoly%2FX&X-Amz-Signature=e7ce304ae811c7db35db80fd32a3bc019b2da67f7e991b7071695a2cff16d27e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



