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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQYYI24R%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035007Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1Jd8T%2BvcOd25la9gj1A0JoCKYiH1LhdApYpFNQ774XQIhAKdhv3RyEmMmYSLd6zntNtG4GXzgjAdG6HgvadtQq8dAKogECMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwUcb4exD3p%2BKufQy0q3APHH5a9veUsoLOIqw8HcQq8VhYOLf8MHiokFu3BRwJ%2F%2FLLq%2B0YmWrAKwLFLFIxmSg1HNvjjFNJaeqQrRhgD22drIHNgi5IoD5TANRgPwotAXUV6ZACpmkm5JvAUUYvuWJ5paQ8W2vNBrYpn8tgkPkr3F3AuIPAqM9YvhYvtritr6HlaOuRx6h0iS%2Fn8yIQm2zIhB7wN%2FLJgBVFapGgqIOVFwlbU%2FTikPXwJfagE93lTzQTCQdMJ36LT5oYORSvyBDXk3xvXs%2Fg7hrqkCmtq5C4ujOIXITs7T5azAPcTOSYnvo5Kf3vp1oELRaLhkNmMF%2FPCQzWbfinbgLFI3LrAI0s2%2BSOtpvGesRpSETfjLk3VK4zXaQhbxEjnofBkr1l9Th4bKIGSbFRVnhtWaecirP2qR1JXkm2f9o2LPl4WdHhtah9UMfYo9PmU9YrOaIDtzO4rcA6wH7vPdrr2E6AxiOzITr5KusBP%2FrFKqEDnYzLjHPK2sTGxhoPDxmyHi4UCjmGhI3YTXf4uoPjWj2E%2Bhrm5zYeZTgv%2BS32%2BVVKlDYHK4O21dAsH9ssPWLDZEBpM0Otmd85oDdtWFHDsvph0D1rhyx4YQLSpfhrXrW8ABjbmGBHAdmx68a1qZxjaIjCejvvLBjqkAQKkMjXDZx5CSK1s9m0%2Bai%2F8fzCUb056XvvVvETltIoTDV35jBU6DBgJCgUjCnXiW%2B%2BR5KA26NGSWvcSVGu4ZJx4uEfyaDzXOKW6Mdh%2FP%2F2XVKg8DcgvxEG0ELdpri3%2BBYG9fv5nJSlYCE6XtIjPTa%2FoKiEMRcLVbh35iNg7qeBvfj%2BKk0Bc%2B2%2BkQfG6LJj9oEriIkKbkhlHLoYlTT%2FuITmEZsyH&X-Amz-Signature=a46374e21116358550295464b954e28bbeba1917b68322e9cf9d673992c5cb87&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



