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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7EYODHY%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025347Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCwo%2F%2BmVcYcPLUeZySpb0V8TFIh459rrO%2F7qkn8ppJLEAIgTaiK7Ayj%2FJ0XmcYfxTO%2B2IB7gu%2FiirAyR1p8E%2Bn3%2FV0qiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIHwPNl6YmwhKKIOICrcAwRTAZEj21OhyissnXlB0ErB8GE04RChKWogNLFJ9ZiIGeFpR9y8GrRjhfDQsE1E7q44HmI7tdeC%2B0uQYbACNa%2BNv65szUEfuhe7wYvZW6bu9ItROcQqr%2FMK34WNbqTDW4BdMgiB8iR2cwYNw1dpZI%2B52neyps4n0GonCW2CwjIKpc5l5maq8lj2w18tFk5p2jCa3TqKob4SvMfYSFTFwICm8xo2ilXOxCb4GpqbWa4wIfx7KzcHPA%2FUoZhZ4t27BCaC6ExR3uwVbdu3T%2F%2BvEUKn7oKZANMZ7UQ27%2FgbnHscmpDq5IhzW72%2BlPc4Ylvu%2FJdio9qJ3HcY%2B3w9DfoyNoMds4qIGqECQl0P%2BmD7dv6%2Fy3%2F8WEfqwA9MpvVw4j98LOiexI1SjJROKrnmsXnxarW%2FsMPEMWJ2b9ehv8jBH3MWVR6xjZPa4V1UCYoifGHO74qOX7UdGTPpwfkbC9w322Gn%2BAil2ZaCVJnjglq%2FJptrOxWmZnF1v2ww4sAtc0vyT%2Bo1S9jgXRd2iKA0ZfU8CL%2BAey%2FwAkCKogUGDgQmi%2FFUDLQ8Hsw3AvCgmdbWn8ISPIOkSYhlw0iKljiOJC5gsN2Ix0qq7XH1CW6iNN947eEEyVWOB9wj9NTYhhdBMJv5hssGOqUBgl%2FFLwooAskYwbPXUb9oZtVJWXxl7hypuLh6a26bc7C7Cw2kKf%2B%2B2YKvdWiEmlzGFp%2BvGhAfJ92lNrNwVgIyXJlIJ6J%2BrDfOD%2F5E5ovOIaYVdO%2FSwV0HrYABkRj74ixzeAZcN1FxaXbYI3JFDsllh4GZBdcKeTfhsTEw3OCqrp08iQRh21MKsNIW2vd2OKC%2FAg9pPBJwUAaZQPCjn4EjY%2BV58Ud3&X-Amz-Signature=c2a2bdccdd5ccf9a2616a1aa6aa38e3c3ea74d768ccfbc0dc915717a6ea64c28&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



