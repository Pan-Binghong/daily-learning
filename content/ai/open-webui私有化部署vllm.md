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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643H5ERNE%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T025930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCaqdkNe76d8GPLko%2FdltAgMbKlFS00hlFZzAuYgQCEkwIgBccoMIlG7A7hdTgi%2FIEOj4W481eZ32DPMK6kMBd%2Frgkq%2FwMIbBAAGgw2Mzc0MjMxODM4MDUiDDKsu%2FAfKE%2BtzlfhQCrcAxThHyNRwjNNHmHk%2FV65j69TM2q7OSqYDj2WuBjB1Hr5qnzgKDDPwypWbRbCdTG0jIEJHbKaapqdLJ2oj4zf6jvSBLJ592KFknkcgp74bwSfkjLBbZkC9BELvF3GJdDzJJkk750AEEJK9sKaMWHTMVmCfzYSnYsD7x8VJVrXxq%2F6rNdGMr%2FttU5fD3f2TV6ZuoAYDugEX3Jxwaj6CVDpeTDd0pWVJ2dvZCQ58zcmgjnOK8%2FR68APbKjYsMlT9JG6IOi%2B7gixQECWZmins4H%2Ff5EdTdaHb7zywIsobnWdLfb7T8y9iJUJdOgDPRMO%2BdN4tLBBM1BMctmZq6v%2FdgVnS%2BdJOyAgHow%2BtuN3nuNVkeWhydDeTF6poTTAouERlhVO2DG%2Fz2v5Ut7ELXFqY%2B4yX5neUx127V7JfTU%2BBShWA3y7mSHlg0AAs342kj9whvp0X3RMuheSaukNslem1UQI%2BuVTQUlxWOx2HqceEsXT3lIu52enhyiRVUuhxakoLx0FozyVrJCWDWLbEo7kB0vJR90iul%2F4xfiuqxMHImr81LdAsZPPwGHGC1m83coB7VNYOCo7i1b%2BxQRvy0%2Bh8xdRXndcLQJF3wl%2BvWSp1TuIZJZ54P02A5%2FL8gh9fNWfMJKP98oGOqUBuqCN2Hyj%2BRAfJFljLTre8HtgiEr0DQg1MjY95VLFlh5sEp9Nix5DjEC%2BAJsBRopOV4PnBqfOFWjNNAt87o6A0Akb3GabJ1xKTGFptgEFAMr1qHAsX8WWrBrHuv4yQ8lOVRLZPNJTjs1jnVSpMK%2BJEaPIC9nWRuJdBv6kq680s1cZTQOwX3pxPvfOaJBL1eCAdzI3ox6lti3FFin82%2Fx43I6wc31W&X-Amz-Signature=879cc75411c3ad2b32b7d9f1416ffec9a87a69f1563d74167ae3501d364a7df0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



