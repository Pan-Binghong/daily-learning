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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XUPNHW4%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030807Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCEjlqhQxmzGWcOzBRK6U6dNFIxBiXVAgr1HgcwYg07zAIhAJGeyVbT3v%2BiANZuhxwxfRXVfBgNpN4Qd6DUGURLQPuRKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxwlCuQ%2F%2Brx3Clna7Eq3AMdkeCNjVfMvd%2FUwvonfCPsq2JA%2B5L3rf%2FS3E4eIeMu%2FAlbJ6ARbpazVOBYQ5mRXjngcB35ZSJGaJQeUdspF%2F4hQ7IIZa4OJAaHt3%2FTOuHy9xI0LeUdAKeSxyTTjA3zMrPvK7FhEKtpOhrK5KOiVZ3wWVRzwPwlVbCWcunaVxRJg6fEdsA6kgcjqlCcgNExw7oAtcE4ZLMNerol47J2DHsYyrjpyljGOyYEhsSrqENJzfE7xHrMYVZDR8Fz6rpykN9Iu22RmxHHk5dVLzk9gylCAPXHDamdi9kt3ALPH4mOZBKNMTXI%2Bm%2BOoX9A%2Bf%2Feus6kxl4GtV8%2F1%2BYpHFrv8Ddd%2FyubyEUm55cuh1ojVlOBVv%2B0eIF2ULcO4fXntTA%2BvdkzFDOMrnh478SVjHAtwFp%2FNfxoPfERxzmCB2jgOFa0yVF2Cu8Rp%2BfZPV9qXzL7LCpG00KEQiwz9wuYdiW4NKb8VAFP3%2B4gdQQqw9k%2FoXv65OV%2FQWTTaxuyPY11wA8Vzpprrk7rrEZtnxZD19RLJQun3%2FZEAoTLA1yP54sppmZDRB0%2B9ZXt29sFdz%2F%2Ben4JEqf4ihOIN6VqMUDrNbaIYLiqp8uh0vQZB4%2FeybzQyNi0u%2BOrOk7XLBTYJnWrjTCL3bXLBjqkAeXPkmy1I36YU6v47fCN%2BlqxY9lwOfyYa5M0leXCxCXFJWGr0bjMGTVhEHdL%2FsH6MY%2BR1MRnloOYoMobiMLA7Fy3XteLJOnPOuku3eWXK59DYBaUxDfzcBqUwkmQ%2Bmq8WXouWRhT9XFS2ORWdBWWWwMZvTCo9Eu%2FYrF1G2%2BpGVCy9JinwNb5k5A%2FtcPekgPhr4TJiowGZIcYCsnH97DbtQMG1gAA&X-Amz-Signature=c17901805af174ecca3292c2107b1aabdbac908b26cb3ae01356b72e6f3e8eba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



