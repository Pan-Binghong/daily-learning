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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LJ3LBN2%2F20260329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260329T035632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIAuwBPZxxqUyZls61rxthtqmdaI%2FwGkGWzqhT63d%2BRs%2FAiEA54piI9mZkDyPpEd4GuuysbogEKyB6vFYoYoD3aKI8l8q%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDHN6eeC%2BFH5dlorQayrcA0qnT%2F8%2BiKH76g4JuHqCQqSiYZbIgN4Z0exwzGjAbnFuqTuwP%2BbAD2qIr3HljOc8nbB5VsTsOlPUNF9mk0QFbtsNTR%2FniRE0MXLNARi63boJqv5GTlnMaO5uW1%2BY9Y11wawFoPsEk9%2BezVap07xn8421Tmhr%2BfhzY6o2hYJOw7Wp95iLrFNFZm0ndsl0t25ulkeTkP17ag%2BqDjoKv5zpuFazZrEbwev7kRTv3RjTlJo7ENTnQapsXCDGi0xoMCk3xTkjOhBgJSeNVQnJSAQO2u1u%2FwUnVwbr1i5jzfbCnbzlOlE7ULmp6P1jGZwtDYiaqpIl%2Fq3KsLDF5yakW8W085TUUr28ayYW%2Fh1We53FvjqfkHVlNDkaK41It%2BD6jnwjZ5VkFyfBob%2B13nQL1WYwB9tBKpqq9sS9HFSoVokYzudJPcSMa0KngsI2H6KwE6KsqlH5c741Vj0CimvxQQdbBpql4VQk%2BwYiYONBbMVNQBE2zI5RFNNXwncGNX6TXdZmDEi2tb8yDcaebJza1r2zGjHs%2FEGtuVaOaHZtKM1M2r0DxkyjabqXKpTj9IUNqPg9AfXceCyCdf591h2qaFiuKXtM7zNTTM3qbgE0xSv25Qq6BrXXgeKoRUruCnkMMKq%2Bos4GOqUB%2BX%2BFxcabr4NNNwhZxi72mE3JhAuVXulmNAYjOLTaKIOZqkVta6WTvxjkEEaziW6jAk%2BqNJs12t9wI%2FlcCKnwIlowkIM1DksTxTDdKGdeUZHjwkf29NxXwccOX9GERdGrjglFupTy7Ik2uWOBquEWI3KeSi7OTisQySCQWg8N8erG56rOx9lo5MN0Wmh%2FiN5YTp8%2Fx5g1FjDrSgJvy67VF7kte7tF&X-Amz-Signature=3be24b374af20fa713667cc4c67da159fb55d57683c89c7e61e05aa4a27f11f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



