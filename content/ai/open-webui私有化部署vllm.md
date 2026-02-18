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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHDA3JDS%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCM4D%2FVp%2FXK7A9s%2FYCch31gOodPJ4%2FIoc65aXvu12ZuiwIhAMX5k553qfqzPCfKB0TkuepMDkWXBMK%2FN9iWP3tRS17qKv8DCFoQABoMNjM3NDIzMTgzODA1IgxEv77DoQShKSg3DFsq3AMvu7km%2BQUnK1msiajexEcBHRG7WSh8tYPzui2JUSRW2vKtkZ45t5FnnBmAX3MgCeKT%2FBwopKcyg%2B6Cw%2FaxR41mlKTaXIDGGUg9ugCcU%2BpzQ1JfW718nWUso7ef3RJP6gbhCc2%2B%2BUNL4HMoiD1rTVfq%2BVdJ%2BnQ%2B48HJ5ccIb3GSsLugrBeCifzmCM7UdHLoqyCK7Y4BIkUcSyOBxqkCg71MFibeZDpQP0Ly2SLIIofTzQ%2BQHaJ%2BP1AjgBM%2BFd4lP239%2BHlaJBOfiwiUyaamOTHxAyahZHYGJfqu2CcIlRnXhRg7IpNzCkVXO2TxpJSePHL7vztUqK7SN1QAbiKIfSwWHGaml02cNYpPyFT3trSsljd%2FfMW9I3y3zYkx7Ok9Rp0cxYWCT6%2FP%2BED75E1lVkbHnHu%2FkKkFBk4MbejtANiQ18sYJGskVHuVHaQU3g6PwBm3RcnNAmtqiJTTVrr6jSvJsbqngYPlx5wlSGQu8g1cmgHd%2BcgWU1ZqYByfeZX7wpF%2FhiHq%2B%2F5vkAcK9z1l59ftsoy0mylMk9J2iZqaDIuEzmDvmTx7Ri221WZeGxGnnh084fE%2BVrbuZFsLBLr2JW8PKVyyoewW7zadFg76UNu9BHgrqmgpKgTpshw2YDCrn9TMBjqkAfZuwGsJC0M0LwHR3MM5bya96YKXtuj5MvQ2tIF1qV22pRQ8zaphqcAoW1xRvI2QgGY5grcxndv4t3cfogWLL%2FjeCTqj%2BmFDwewaLilClyuTWfA8JCy4j7zQWsm7RhRIoEhBU7ikNHwuvfP2aYWGhkrjKTPOcT6vv5GxpO1g9KLhgERjLxrRtAI73MC2EL%2Bnft9A%2FkczcFm0YWlIUQ1Ic%2BNSolkR&X-Amz-Signature=38658ef7b3c81c82ae5f9b61dd95c7710e6790e5292af36b3985c6157003206b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



