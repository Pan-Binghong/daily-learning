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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRFHB6RG%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAvx1KaW0BqF0Q%2BjoOXN9OqU8rxp4EMoz8ePI5FS96EeAiEAlhao8kK4VT0qvpV7mPoNXijrHa72kR6vRMHRxWnEiL8qiAQIgv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB4W3QZuLqDsNzBWxircA7Voh6cRjBec3o8qAeyBJxL8lHeqh8ubVQ4gybDKY2ir3FwC0yj%2FeWrHkTEt2j5Cdj284Cl1gBqElty3kxB8OP%2BZpp9TLUXQ5Rz%2BJr7QVSAuzrsZhLsIMHZPdzVLFPVZ4DQmuv7240qYD3unAr8krirXl3cw4Y6YtPPoqX1NRO0DkyD%2BjC9AJzwwkSeoQLTNkaex8PKs3O6Fhtushz02vJea0JVO6xVGziaPq8CbrQ%2FN0k6ijLkRDNx3HWINIDwCftjA%2Bvqk%2B7sb9f5tLAnV1AwjYZPVO3EatwoGTGE7XB6Vdl%2FAHikFwWr2JhaIxIeUtA%2FjGwXApYNpof2%2Fq7puGspcJX4k7GTkFyI2v63%2FslwQeRnU99YDxtHVg8pPjm9H8wLfGvV6ADM8stBacDIol2H0AeJS34tC12qYgO8tUlY6xjp6YZoCrOw%2B9sbJ5ui0qgXcTOp%2BspzLfp%2BtDA4JHcMYBbpm6rd1WqSGqcHqJC61AWncr1TK5paoygB0DqzOE%2FpTn%2BicDfarVzfPXoKM5QAO47OKXI0PtTCAte4VrK%2Bs9548XdrK%2Fd3kLDEeXUzXu1LoGiycGlBGq%2BT%2F1CoJEc7L6E1Z1YKKH5ZISRqL763DWF517Tf%2FWjzxolJKMIC5zc0GOqUBFxQHrCwo6MtiWoVD%2FfBa%2Bv6MZ1LjJrc5SyLSXMB6RfoGWjEDYeZmTLMYgabxu8URoqa7o8zpt9gEcTgbais3hpaC4HAr45lcecMpDpr2vyz9bz0w%2Bqn%2B2rK%2Fq5Ms41V5hffJDtaSJVM6eHcjHV3F2wO0QkVFTfzqD0bye%2FjTMi5zG1C4%2BTtArBJBtZDr0JnJiPZUWTGxC5Zm59Vbidn7AzxqssZG&X-Amz-Signature=1199b9700144097523d42ba30e6f9a64b48e0af3c1ece502a0fcd6651d12af0d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



