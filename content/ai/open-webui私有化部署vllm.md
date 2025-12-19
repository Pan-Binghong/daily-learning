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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLHIIPYM%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD664igBRprtxT9ce5MLd8cNoeu6BBeVDzXcnDxDOkXogIgbA1JeKtKYIbj3zKKHRmWUjp985gD0UicTOVd4kpcw2IqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJcT4wLwOYlb9vjmNSrcA17uttcau7P6%2BzV7Ar4OzX5I68HpNupUx8yCL39jATESIpuMSV0Ggg%2BbgZuorbyUA0atUBtYGQOk5QQDD%2B7FXWAiuPPvOFBxiRE5dDD%2FpM1HzfB80j8ak0wH7QDfm8Zj4SUIeu5yTh1d9suE46pyMhDRyfITZtpv9ez0JepQsvKMpJipPXelXtZfeHhJJnV7OBhDzn%2BL%2FeOpT4u6i2sVBlqNwoovUdoODtp5knQGKFdxgdVbGuXRbXXBBdM3EPH3Zb54%2B4my02yJD9b5D87I9WsL%2B9AyGEC2Vb6DHuhgiA8HpiJcXI%2FeWCgE%2FzrH%2FQeLFVJh1hVFdde3My4UwkBIpewNg4SQ6SPbUlugMcOhhlnurFe0rsmHX2HaOD5iJwHTNauTYVMmfUNhfzr2Gsjlm1JSTOFulF3vri3LV%2BqPASJwxTV8B1w5wWJUWes%2FqiRP3NnhgSY%2FKtyd74v%2BrdSYsGRAblnmpRWNU%2FzJEHNu%2BTev7HhKx826IOszkKOC%2FLOFdRAyEvoZFQycZXc1FuYyjfaALC7VB2BidRdSVpp8SR3IH3ztjlvEjkU3%2F3cSMlptIjdCZr257gVI2P5gmKMhBJV84Kzecrmgzx6uoUZloC6gzZw6ZbR9NzNxAGEfMNbhksoGOqUB16GWb20oJG%2FvMOOhKhM%2FCHZcH%2BT%2Bgvf32WmPulHxpwKFATDxFXt9bUT529hBUc4bRA%2B5yytAc%2F%2BNVYmMX8bFUnpLr4ZEOspFpqIkJguKeATq72%2BlLyAYNZw0oVDsgL0A0coCWDUBsMtSXTjdrN7NHbYYvIlMd%2F7W3h62xf9Auri0gbpRrlbE4dxJK9ZwYpCBWcmN1BI1vQ2s46OtYIBms%2B1b9XmG&X-Amz-Signature=9ed1a1eebce7e0a5bda7edec2a295e7318519b8e3e9fb50fa943b38469bdc4fe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



