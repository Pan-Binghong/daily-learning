---
title: 多模态大模型_mPLUG-Owl_部署
date: '2024-11-22T01:44:00.000Z'
lastmod: '2024-11-29T12:33:00.000Z'
draft: false
tags:
- LLMs
- mPLUG-Owl
categories:
- AI
---

> 💡 支持视频以及图片推理的多模态大模型mPLUG-Owl。 记录安装，推理的所有操作过程。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665RRWXHQV%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIDOu%2BBnPj7zzxULQBDxFRedBCQ5TvdCjWkqrxsrJ7XUkAiEAyCB936BX30jV5oV7p2kSsobJAUq8ZmeKb0Ct%2Bkzl4zYqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA7cD7DwNdKOygfEtSrcAznYLMMLbZz%2FmFfZp%2B4%2FyNtnU%2FfgB9vjEUm5K%2BJiA%2FOCyQnK3gaTjGvKq1Si%2BOSzbn47hr9xPU8io9tAl3L6f0PmPgHkEM5xuWnDLhNhDDXucjP3mKZJhEOJzHx1AGXswzsYliHxZsPvDUvcgKCL0IVuWyKYbEFw10iTgdJfyauzrsZeZxswFtxpbK4dy9f1%2F%2F0Z9Zzp%2F%2BCQ4ajKRyPq%2B9EInNZt%2FstuXvdv8xTjJZZyggb5j4ISGYwG0tqdaOgnUjTpdAZMbT%2FvpiRcN09nch1I3C3ccmKMObkZxnPmWaz32G1f1nZZCeR4D45Ebxoaj5BW6RbBye4cXGaVyVPvMVHzBq%2BWpGINf1z0lEw0EYsVnP%2F4KMgabtCSKlhgf26V%2F9orVn1wdjW3qILb0nvv5jvl70hILcFT2jqKpJBaPqd73p1JvUa03AccKanpIku9kMvnoXDHAdrwLRnoU3Tx0gkWtvF%2FWR7Tksc7PdXBgBHZljnGUrXmM4ZdNAEvPKPcXX0e%2BuI4Ko2CX1MmVHyKa7nChoZCK8wg5LmwhCQUqNEHMWgMmHw75URGgOoPOupoCgsaKEb7qSh3CB394CU6lB2Q%2B0oCEJJHwMiqEUEaLtFuyQky7dqNa%2FvlNQ3LMMjI9MgGOqUB3g0x9Ge8zQH%2B2pXO%2Faoqw7%2FC%2BxZzsa6iRs1c6ON%2F755qSyLRC0Z1A9vxptJlD9LfNPBCgDXfQBxKQTzh3i5gMdmJere0XUJevIIDh7%2BImyUyselmr7uTmJaa%2FsADZFf8aXdljieDTZifIi5zos9p6VCUeA9AsIazpQ5KhNueMwxe2YepQDQAxwiltmiXBiGUs626AtIkjGqKiv2J2E67dNfmPgCb&X-Amz-Signature=a9ad1880c903c25e5a6a5a0d8b186022a3097fa99518645a4f10ec42c18ddc5c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 环境配置

- Anaconda安装
- 创建新环境
- 下载代码仓库
- 安装依赖包
- 额外安装
---

## 模型下载

mPLUG-Owl3有2个版本（2B、7B），为了更快的体验，本次实验选用2B参数版本的模型。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665RRWXHQV%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIDOu%2BBnPj7zzxULQBDxFRedBCQ5TvdCjWkqrxsrJ7XUkAiEAyCB936BX30jV5oV7p2kSsobJAUq8ZmeKb0Ct%2Bkzl4zYqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA7cD7DwNdKOygfEtSrcAznYLMMLbZz%2FmFfZp%2B4%2FyNtnU%2FfgB9vjEUm5K%2BJiA%2FOCyQnK3gaTjGvKq1Si%2BOSzbn47hr9xPU8io9tAl3L6f0PmPgHkEM5xuWnDLhNhDDXucjP3mKZJhEOJzHx1AGXswzsYliHxZsPvDUvcgKCL0IVuWyKYbEFw10iTgdJfyauzrsZeZxswFtxpbK4dy9f1%2F%2F0Z9Zzp%2F%2BCQ4ajKRyPq%2B9EInNZt%2FstuXvdv8xTjJZZyggb5j4ISGYwG0tqdaOgnUjTpdAZMbT%2FvpiRcN09nch1I3C3ccmKMObkZxnPmWaz32G1f1nZZCeR4D45Ebxoaj5BW6RbBye4cXGaVyVPvMVHzBq%2BWpGINf1z0lEw0EYsVnP%2F4KMgabtCSKlhgf26V%2F9orVn1wdjW3qILb0nvv5jvl70hILcFT2jqKpJBaPqd73p1JvUa03AccKanpIku9kMvnoXDHAdrwLRnoU3Tx0gkWtvF%2FWR7Tksc7PdXBgBHZljnGUrXmM4ZdNAEvPKPcXX0e%2BuI4Ko2CX1MmVHyKa7nChoZCK8wg5LmwhCQUqNEHMWgMmHw75URGgOoPOupoCgsaKEb7qSh3CB394CU6lB2Q%2B0oCEJJHwMiqEUEaLtFuyQky7dqNa%2FvlNQ3LMMjI9MgGOqUB3g0x9Ge8zQH%2B2pXO%2Faoqw7%2FC%2BxZzsa6iRs1c6ON%2F755qSyLRC0Z1A9vxptJlD9LfNPBCgDXfQBxKQTzh3i5gMdmJere0XUJevIIDh7%2BImyUyselmr7uTmJaa%2FsADZFf8aXdljieDTZifIi5zos9p6VCUeA9AsIazpQ5KhNueMwxe2YepQDQAxwiltmiXBiGUs626AtIkjGqKiv2J2E67dNfmPgCb&X-Amz-Signature=6e47fcb8e3f9156c049d0f22eadb329c18fc08f5e5a0ed88e058d6aa98cebb17&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

