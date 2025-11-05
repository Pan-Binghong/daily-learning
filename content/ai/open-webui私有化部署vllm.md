---
title: Open WebUI私有化部署|vLLM
date: '2025-03-17T01:36:00.000Z'
lastmod: '2025-03-21T02:48:00.000Z'
draft: false
标签:
- LLMs
categories:
- AI
---

> 💡 在裸金属上对DeepSeek系列模型进行指标测试后，有点无聊。随便部署一个WebUI玩玩。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VP2YN3JV%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095851Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsZkid%2Be77MZYKXo6Qpu3WOuZ1U5EsYJDZMxHlhhuWLwIhALgPAdT%2BjVqz%2F4jbw%2BO7P9nKMAgZKQWDMkegj3tsqDNYKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxe0UC9p1w1cppfkk0q3AMNNmEM9vbMmQMdwDnLwWi%2Ffv%2FX7UW9HchItdTp4oAMLLrO%2FS9vgV7dimkkb5DVGH7kRuYQZkvz2uNCnsBH9fwRaA82epLskEkPsKc41v8Ulef9TxHqx4AO0ciHTOAe3XMtRgybEl94D3COr4nFJ8EmgCHgSbf50fYAINxXWpPItUQk43W2RkIqUw0xzzNwersPfoy4gf6DWgws3ljk1FpBsyjwunsfXD%2Fd%2FG6dZ00SEjbd%2B25Fig90zQu3mXg8H3GO2%2BOy%2B5BA1D5u2ZE6J0YTBGZmlZBkSQ5yU%2F5K4Mpeby5wSKd86Fo%2BOvr1uIsb5f9yT4uVy87MT9Ppeuq7gkXgrk95BUFmz4MFUmp%2FHhiEJ%2Br7rmd6DJy%2BpaqEQsyZ6eeCVdl2oOV1JyuCRDgoWIfCMbqRzDCJ1msAF94HkSx1mtfJPr5pHtfaXvIKqMbTgoyhsJoQa2gnEhS%2F4VZWfOMMbE3m2ATVa%2BSxde1kmypldTzdkswt70uPmyzJp5MZcw%2BO5ZBDVjf%2FPdIUw6D9SVfivQPsUCX6Or2KtdOSLZ5VQN%2BZU15%2BAGV5RQ5JAorZza%2BOnZIE7xQNCwaL2WVykCKv1DjoIzjuCaPLZYVM8VAFyCsHv%2B1JjgcxrWIRKjC8o6zIBjqkATiNoCrEyZId4wDRFZsZIuN0dnvgXgAEfjS4DgKQPWh%2F8fblL56FCO%2BX8ednzFSEdnAhz7B1qsa%2BWEVPO0fN7J6BUePLVQNdYP2OomQgt6whW01NrhUbR3f23wknNe2IA%2BVEQDg8QUuj2A5ow4%2FTfC0pvBeSlB9dadHor%2FSIyMuKOzlmT3yXXa1yShKTYGa5E8quYUYAvRFcR0A0hRxwYhr%2Fv2Ow&X-Amz-Signature=6933a676840f7e9ea186943ebc00b23589c9fa6184d27e784ce96dd14359c6b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



