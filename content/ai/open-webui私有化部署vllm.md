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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TNO2K5C%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T033925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJHMEUCIQDy4Tb22zRy2adEg4iZZeFbN37v4TDAgAbF6NPxokW%2FKAIgc1U1UUHoGf%2FdlSQcwkPP9jB7nBG8o7hhIHOYn7C4jlEq%2FwMIPBAAGgw2Mzc0MjMxODM4MDUiDOR8LmUl%2BcwB5ZKsvircA5PHnCFRfn6acIZOqdhH7jgkgHhDQovvzX1ytBfK%2BJghycXHZQGtIz%2FVB%2BFM2pGFWoqmVNtST%2BIx54ikBGM2hRrJpIVYFzl9lcyjSx8k4m5IGZQSByvXjbKhRypObg2C56jEbVZVMLPeUVL1EqQe0vaayeVu2hg6xhfp8Ct6e9WqNgYpsCNF%2F4JKc7NRIoX54eEMrnsxzGnlPwSunHV4xehLbTqlngUdvKFB0rtWr%2F8Pc871%2BWfi879FU%2F2HWjaPTzShy1wH8bgij4b7shdf6ZlOW4%2FXAUApbZBIQ3N83fSoFHQM2SahiPN0LODfi9ojNQAkmC6Fk%2Bb8zYBdNlvHJr2RcJm34FMtH06iHMOCy%2FccrWF%2BiTeCaPgj5n2Prc%2BHuCptFPi0pcWXTyG%2FgVidTsc9d401H7RNHZUJ%2FUi%2FjEhoXalI6wE9%2FEzj9W7xr30jexymvcZFHAL2gT3rWXW7blRtPn9%2BwFa0KGlCewXPt60Hnd5vmzyvt3x7flUTJBor1SoCjMKBIBQhUPuHFwyVePq%2BBI5bvbwp5Bbh7kmU0Z8i%2Bl5%2FnIwXKJ76CDdkyyz5vonDM5HTf4QivPz5O8FXaoGFWjhAcd0q9uBAZ8nhPC20Gqp5npd53eFvlj35MIjp5s4GOqUB5TUwe9inXBRUKtUiNN1pHlO0UoZL2c5aQlSZZHaAVdZZ4CBnwsWnoUaytheW8M6EKCNk%2BEROTjDFIIGC64QQFIhrpGumektlapoKyP66mHWpomYmJj7Irxu8pj3cEDnCic9pUeJYnTiHYewVIPLvRatv9MvI%2BlNHeQYlqIuGT%2BBqTigBu%2F7v0KvaT%2BPbC24fPrpDFSUVloyPnjWApFwnrQSqijgF&X-Amz-Signature=e955a3994364b074e3ce34c9ca758954e24d19dad9664c434c63866b0b755ea5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



