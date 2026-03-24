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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QD4LVNS3%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033648Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDGvd8Yloex9cdKLNrxUydgKb0l6Vp11%2B69gIuEtwnoIwIgZ1ngKrsRSnQ2MsXj%2FQCNoKy5yny9y44FnEc3EknOmggqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM3Uu2XU8fMY%2BDlQbircAxCBZXwyOUQKG4IRH9RBI85VZsWU0ID1%2F0aeoLRjGBze8CNBs%2FneiCOmiEAhWE7M79xjLx1c5rOjESIQSvjaHNumA2u2CfSH4%2BGE%2FTQIHxTm1%2FZOTOCYIrYfYsSywrDP5CfoZZwbXqGNCjFz%2BGPCdgFmB9eHtVTqFg2upLdH5PswP8P4Z7v1ZzY4IKJWxF3yKxze2saaCAMYw%2FNoB2bCUQkQIT14elm3lATJDVLdrO0EsxMacjl9gicirQ7%2FEfibdJD48TOPOi1zo5P112Qvk1%2B%2F%2FgJZLrQou1ZXCurnJwA%2FqPetQ0opHBM1rafAaBesz%2FcY8NTU4UgVGrTCo85xz3jGHJ2Jc491GNs%2FursSNMLJmiyftxoVGc6Pq9DCUIeIOrrQRgYXMggryzFKH4N9LT%2Bzvg9gRc6N%2B7sTDhhByfwehOxqj4WBwWHhMMRSdyWdNCdUimbohfJyMR%2B7XFLJHWC4y1FWiuwXRvPf%2BxprfHxOlekUmsr4bLdZMLuK8TnFbf9lHvbeUmQ%2BtNI03hUr9Ux8AJgTIm6kI9keYE0Q%2BSM%2Bxs3xx%2F3ToBueknxVPTawojyKktQgYn%2Bcht30PVPKG9ylo5P7AJ%2F%2FpLb%2BlRjDv3RH5lMNXr1bzrzyg5ZaMLryh84GOqUBbqovzGqP%2BvaRZ7hejkqGLFokGMTQhQD5t3BfYqgMMOMv8MsmkchWpjlujkbDuVY%2Fbgn%2FJfDSsovY%2BB1EmQNOZTP2kVQ6oZf4xqs3I5T6gMX9j9lgy2UsM%2Fbf5h%2BEiRLFMAYsRXkfOPbGTeYtGKzpcL%2BngC4LNuT0%2FtuDPyFPvxgS735zuWZKS%2B%2Fftj6I%2Bne9ZSRTjbP9UAK8rc%2FQoAqWT5%2BikSLC&X-Amz-Signature=27b8eb8f2df82b90810f4beca40ca739ac27557a38b254985546f30286283c31&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



