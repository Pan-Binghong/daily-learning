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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEF6TJDU%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T025831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJHMEUCIQDn3tBLv1DDqylDI9xs5EJMFbMdKc0SyZRW2U6bVNQt3AIgefu5%2FXGlpq4QiBjNtmI4qqvDRCMRMFnbi3eBzSMO%2F%2Boq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDH61%2BzxwFCDFdVsYSyrcA4zxmY0DTekGtECH1yUxa73N2LHsHZg98rGTCX%2B4ajbG33rhpOU3EePGND4HgO7LFHxQTYNxBhNmEmWw5tMXxtm05PD2QmCFQOsy5Lm7y%2FAjs9y6b9mYJEVlJei9iA8HKV28JZnxQDKoZLUm5d9tMtmaV87jeJxlbjStCwYjFvw1bxRHF%2BRmsXsKnUG7t%2F%2FKGAzlCmtxoLJuoRWzuSFNMtyz2Fc6mzVabPBlkb%2BOwbpN2oaZOos%2BE7jWDS8aDq%2BM0JwiX1YS28uY8XqjFM3EWAORR9JnscMH6GSXTUiGT%2FHPJhZG3kXr6rc8R%2Fq1QjXl4cH1s70X520we5kU1L29FAM0HFDvAH8RJV5d4mSg8w6nqdcui28CDYZ%2FZlh7JlbB18kkEfZqCRkhB%2BMpRIHPKTEpZrK4x9r%2FulrKZnxMbQsGxBbZMMGHncmCJ7YcIs5Gdc3quJoYW7g2g3kqygezhTdYIKOuEdVYO9I2qd1puIpLtfU8PNQVrWoE%2B4VO%2FzXEBj5qpLKW7L2BlNPY3JHbAezwJiV3PmCefrnyM5xJmVn8zF66zAM2q5lhiV6%2B%2FywFvP05GAUocqgNwzej873azHuXHJ6AqPk2Ym4%2BywyINzTnUcysQ9KJqsc327GOMKCwickGOqUBiuKvi4voRShuFR1Q%2Fe7nIOTc5eL%2FH%2FsK28r0PQF9fumo8UAqMzDLYmPzN67w7N%2FuZ01NuKWHo59rVryEqFYPwQrNzU8tiGd1UO605x4RBxVLPlk3J8eOCI44WOiDZOjnOlMeMSGw4raz9UC6edFwGMF6UeNmhEVQ6JVBfI6D1TWUWSnu4GOAwXklvehGH6Sv3Yz7t6XzQXHG48RzaHofq0KSvExG&X-Amz-Signature=cf0a8278d402965a196ca3b6c483934992d029bf4f2a1ea5ac057b01f3066933&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



