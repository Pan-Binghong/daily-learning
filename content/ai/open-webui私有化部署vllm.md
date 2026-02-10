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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGC7CMN4%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDpl5u7%2FhUgSbhvX1n%2F0z5ZcVUx097lU8d4f6SwWnZ97gIgMu2zEgls%2BfXb9%2BH5qwvVHI0k5cubudzg5dc%2FHlSpsRoqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIaH6OxmJ3MoQbvlpCrcA7Sym6jPoVfhcFqwfoq4BdTDn6t5ucqCUBCgHpf%2Bsh0BYijkt%2F1oEn0S9IbdMRRBa%2ByqJcLGSk%2FZfYDqUDflihs0YDjfkt4fBvEIgHzVWr37TFjn4Hw1FT6rom0k2Sy6igrQHUsnGfOI4iNv7fjx2hP0r%2ByO4sGmfuztk%2FKKYfHujtpkLQMJbK4bJcM6%2Ff0xfmbJg33WlWNGbgSFt%2FeMY1HOn%2BBL7uFB6uTeSBYSuHuri8xaHZus1X2FilCIBER69JcUQoFj5ITUlZ789fAbEH%2FAbdqVx68IDdZrXUE5R8W%2FyvG0soUbgsp7ypOpglZhdB3u4JS6R4h4QXmq71T4brNacz6xH3T9ZGT7IUYmmBVAcowk7Svt78wngWKuXwa%2B1qdNmbvKjmAaOqndUplDfn6JxSL5bLnULPLVDGA9D%2Fu%2F5MFlNDhvtW%2Bl2ifnAOuQc6da9W2f%2F%2F89T4rtcCvkS8%2BX2k%2B4sbVw7ieW86to09LnT2Yh4H8EQaUYhY1XbsmjeIZrzvpzAT8C%2FZ1pXBM8ahwX1J6do7E4PK1oc1H9XHS%2FwXjurTcReMVf9a%2FbYvpbPkOMxW2labWS0CBIn7xo1caapqbzZMacPYHZTSDKgZhBcgYLMCt9BlsAN7%2FLMK7DqswGOqUBTxIAbl7%2BCVk2V0s0snRirhVJ99Vx6ickECSnrLP83s2HZHzQwI5Rs809yLl65cUDhcSEvODEfY2nzAMK8Pj7nGptFDuJzOvqKdAAzCxaTbfdk6SRfRnuQl%2F36vzpHZplERDUN7vxvhQmILbIyYIUS6eOg1W58Klo%2Bk%2F7rTB2RAMGdxsbnFekyWc8BVAYee9H1RVsFL00GoZIydhZm2WYqOVL%2F6OL&X-Amz-Signature=96731520be99aa5a2b96e5745a31b822bea91606a2a09428b3a8523ce1815ef6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



