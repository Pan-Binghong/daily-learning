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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKXEMW3X%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T035211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCtWc12AiGYr4bGGQRj4WkYXYGGiNEEHSQN1QQgAGIzJwIgAkhKKV4LWsQxUZggrNKJEgZ5N5DFqkNeGjXYl%2BSovuoqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFvXxPWu38e0pOx%2FayrcA3CBfQXk5geWiRTLQOgI%2BmqHacWz7uAiQ8GdpEXdATMR63W2kjfLUFl3BH7k9JY1%2Fe4TAtC4547osu%2B8E2%2BF5ObWrmLdE90g3EgVzk0qlhofvMtb7Xz3eKp7HKEe%2BZhthY%2BDtYKbdRgidd%2FZOA010K5PI3z%2Bo8VTXteXx0ZAWod%2F%2FgD4%2BiycmCRn0W87ARQS%2Boo6m8xmgFGSey6oU3DXCM3dT8lk8QOrmSS8aRLAHFpjAKwe5L%2BlXd9h6LWCFnJaQLSIk%2BSch9uw%2Fh4leH5ZcZXSXB5LyThtW3YvUrvbUZHDhpSwgPzbVRm6KQ3V7%2Bls%2BSyCUq7uTsJX35zaKBQp2w%2BgauCKCDlzW3io16tGb3GLiha6bvzTz6H4EmxHfXw80m2XFPOb67GpIQ43FQbaVzqZ1gzYUwhxcSO5N2Kj89KekvEyJVLdRiemgHYQHDg96CXD7ftJKxvkpIaj2%2BJj%2FdOhupapjQHYSd40jqjugWb1OeEyLivoW8D9mQRswnEXLtad1vCH5S42P79mmE4fFqjjqTYqQh0lIYMibjwKHD8iSmcfMQeIVT4Qaf8VYmxwGKT47QR4k7XYYDPzDCtXVQikhTp3sgca2iLSJ55QpPzOqjUAQRh5u1XVJJ2MMPGP2M0GOqUBlKYVZxq4bjtvyR0b3ja2PEK%2FsTzdDuRKWIYSEaOFEBUSgzjlRlJS%2FqYK3PoV2e%2FNYEgjulHZn1Z9aXHuf4Ex9t9qWF2aoJwIzex1R5ifCdT2m9j%2BniZel8D%2FMQwGZy9T8ubBZ%2Bzdr3mB%2B4U7S0e%2Fi280OO2obQ6Cm9baBDuXP8TJ4zxgT26%2F1QaDZXqueCmt6BJDxJFpeZJEylTNwcyWAMJr6mAr&X-Amz-Signature=532bbf169dad7d67b014bcfc4410f0d3dbac855437e1476f39a48c7a7a932ef2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



