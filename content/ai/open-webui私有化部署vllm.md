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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HNPGDSR%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T030741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHQe3s%2FrD0ml4NH0DSv1bQx1L5WaXX9euJFfoDIiaP%2FIAiB3XhQk6xVNMknBGFItb%2BtEPlvWjgaKydfLwSMkZrae%2FCqIBAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMc1JdoE2z5Elfh9izKtwD0MNz1JTn4fPC7c3yW9rbhKF1GCvlCSadpHTSF1R4FoSb0yvcKmM1%2BuIQ020c6ZXzjddFVV19OULTtpDWbdpdXOTpCqlIcCaGV9qMnDySiLOJgcoXzIyp8GVp08DCiUI%2FGYiFGElD2Q5tAEvcNf9sAHveCmMW%2Brgedt8%2Be58RTkbGBo6AzhWix68ieU9ks8s8voMNpzSwxCFK9BYJVqpzHfe9Dwbt9k9oUO6PUwZLAOhyfr8eG7FB%2BTWoL%2B%2B537nToC6pMpej5lGJmCudz0kQ0TDA7%2By5VV66lD8AWNnTl97VjUZuDdNjzqXm3GmrhQ2HdvaSMdaYV9dsgSpgyWz%2BbdHCMg96Sr8P3OX6%2F7Pf4cVmhdfqfhqt5f9d2d8lYRVTVp4rWeH736Vb84hxPtJWddQTW2itRagp8nnq2efhGO8kYOvTqPjleOpL4LCPMlNXoIUgSREdEln5Arrr%2BHaEqpXcUt9Oyi79R%2B9EwBaDCyHKat9Aj32N6DV9HtGhhGBW8akck9sEFi7hgXm79BpA2anHm%2FypYxHnaBujUSxPLdXPVpmJbjnzUOtE524swHlJ6jQg28jJkDGJuNmY0Fz6RUdlhkVfnKcU5W1QHzsLwSNwNkQdIQfn5ok47L4wsaDHygY6pgH9WnstYIjK3E5%2Fx%2F16Qmg%2BDHaMZddHM6gcTd0URhgvzZ108Yyx3UAaBN8Nwi2jAIFBDbKIY05a9fQYOrL1ICZdnbrypsH%2FgLJWFXhC2YQYiZIycxsdb92nbbYkzNeE31JEXmeY5DUkBOAaFHDn8Yl7ASGOOBTtehzEiKSRMv2Meq2BmIn6bnJPu4iijQOTdUS9hXAK0u8rax55TMBjKEqlaBQ863Cn&X-Amz-Signature=517fdd3ee6a387e7cc66153f3f45cfe91b9c27bde0105aab8f445bf5daa5b69b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



