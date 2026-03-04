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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KZKW75M%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGLoL1xVlG2IUXCUxW93HTzciwzLm2LEMjLJAnhW6R5AAiAi%2F0i%2B3EYCGCXukXsmcfXknwke%2BPwCoYnxiRgrQRCC8yqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7MvWz%2F9YQyk5y%2FQeKtwDsmu8%2BP1bJMvKCSkrYG2bvn68jeTRS3OmUeKXp7botRh3QcxuHCbFlJTXc9dQTcpBfiw4%2FwHmL8SqaJdJlOdMZfSWtG%2BDl4ao0JAMTU0Mjsp2zWUnmcRTxQS0iIRjQM%2BSgu9Br7BSqyPD816XwwCjvbAJKDEvfPVSYWmkOp1RQojP6TRXpXTs6G1%2BxMwVvBW9N%2FKFrMj%2BIdlpmEhdpf7W4vv1OTfY4QIQrlbJZRbaSZn4xpKLnohzbNf0nmd2q9Npqgp6%2FuHeBpoh08Cg585siUCUGea2GRVTtnIR1JrUqmQdlyXKSnnT%2Bv%2BpsdW%2BLE0Nr1emXro9sv1LnULHhJh4ldusxaokY5p%2B%2Fjs8FCGdcyr3UmMyrmOtzk5%2F6ce74xKdL8TdxtnsaHJhfH%2BKCYbltNNGbNijlz5ATy6lzy1micxQ7ZlQk9biChINCl10ShgqU68Z1LEs5rD%2BRNeFY08XE8mk%2BPs8%2F33H5vW%2BR10d3mTnVLjFDJhyyXVisysgpWPRDW2pZFo0C9ySLAfawb1RDVEr2%2FusKd85zhShhv6%2ByHFoVYImFmmjrkbT%2F3tsviDWl5B%2FkCSLT5bmMkjL9ny0zDAT9ZPOvI5ueqjggp%2FuEP7pXmobTE503Sl4JKQwvZmezQY6pgGfvRzb0X7ZytPN4CrvrjA5BelL1x74ws8qjaEWFAK2Uk6e5B3khMESl3NQ4sx83ovTB7CvzeySpVU2zADQdDMuxyp%2BNxkYTG3s1IHskOq%2F72GHdvH3%2FcGUdH9qIlsBkUkG6TV%2F2dO3k7Ldjlew87dn7PldT3j7x%2FlXucOMFKzK4WbjA1XcEMC5yiARuj2JHE5zaluJeXdPGM32U4Gu8wv8hCnGp8gB&X-Amz-Signature=b713d7fea7a0539030ae535eac7200f5c91847265257b5276469d5ebaaa429cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



