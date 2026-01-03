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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WMDSWPYP%2F20260103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260103T025120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJHMEUCIQDvj6nJ3utkLaNZ8jhYkxQ2pWjDT1ha5kyVu1g4xdVs2wIgFtKwhJ90MAwHrLJK6ozzcE63deOZ6deVQNX4hWIRYgwq%2FwMICxAAGgw2Mzc0MjMxODM4MDUiDKJtWELUmAHkZvZsqyrcA%2Fw9gGVJlbJUHisDw%2FjPlFL4T4KC6cXYw%2FAiRVL6OcMKeZgRNZp%2FqJh2ot84K9PXOaT8%2FDQc20tS%2Fp%2BGKD6uJCaw%2BDVi5ixLxry2cEE3CT73xjxw4JWgu%2FXxMLK5u3e6G5Fio8Ge%2B%2BpAoBDKib75iDsWrrwJWtbf9%2Bq2DeKCNGuOGoVQKl5ju0ELqhJlPSxQfNTqcgIjIFzwiI74o2urr73KTizoTdyCa6GaJLFeMtn%2FfDNA%2FUmi3YxPj4tRZQS%2FiJ4aJk8D6FvVW2fxrYk2rzuxEwpZqqx%2B%2BTE1UR5%2FX558VLM2b1fkx%2BFMX4UUXt0lcd6IcBT79XZPnVAjS96Mn1QkDUWZR5GjcZOVfYHawTpTZpetymwAAQuNGF0IASeg0GiicQNO85PPd1E0EF0Vi1k9Sq8mfRh5VES1unRTlDoOCN7dhAd0YDM16zN7Eul37jnEfEn%2FWQDtnILsXAABItkBPGfy4pajlypIbyAMswAcY%2Bdj4%2FAFsHqCiCZqsRFSKvRQS%2BNS4HuCz5AL9JubCeA02nItpRqxM7ke6fFBiEg0mLWf2KT8TFJR9VlfWOVKLty%2B8c0BY1uBArB%2BOjxgT%2BYEdi8Rzkdwmtyyde5z5%2FX1%2FcExda1LNCKz1SiVMND14coGOqUBUBi2kPtB9vcf2Fxthdp4Oa5kExxx8TSFiim2kKEb%2ByWpeosV6tIsl%2BdEA5lJlQPHJCCwx64jOKFa7o3MGQnSy%2FvyENa61GXQD59jRpWyq%2FdBlNs9z0uqOPXm3fuGnu6uxeEZ1zFDQ4ZeeVaVswWIh2xMUx9X0csC%2FwlAjs7Ey0CMZp6ku6NWSTfL1Egn61jnJC0XHj%2FogaClIJEzdPF3GtudxcJR&X-Amz-Signature=e75313c9634b8a94c90c4399b1b06fc13afcd5a7e974837a9176e212dd56df79&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



