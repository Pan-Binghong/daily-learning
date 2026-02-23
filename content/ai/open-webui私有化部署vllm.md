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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZ7MPFJ3%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDcvrkstZSJaJ353FSSTsl%2Bk7Lv1KuUYuJVPA3KjrtwvAIgNvG2mkQyI42SkKCX9ZXyIr%2FLIQmQkFl7ImUriYAu6CEqiAQI1f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF96FQGpyX61ZBO5oCrcA3AswVUgTt7xGfGNm1Aim7iGFiwknYF8xAddQrMXmlSh7cbr69HGgGysfDKCLSOxr0KFcF2ZLlLvHDKTjMUI4D0bul6koxfSye1watVAa1b2kUBZadCj4J7sxy2FznIr0tmuTmacl96df12vMud4UxEGBz%2BRhe%2BRCe%2F930bL9GkE18FW8tmXY9PzjkBqCeyfzngF1NPsVKJa%2ByLJ6hYEDOQxCR%2B0lXmM38FMlkzhmus3zI7ybPTRvUP3Flls7m4%2B3yE4kilarGAkaDQGhmPuY7hKuiuhViCcEdjMtw9f37Krv1Wuszoi6USgi2enfE3r6GTtMhKGDgM6wi4rbUqhQbO6Q4jNz8lE85gY4Ssqe4PXYTGhnRV83t9%2FDZt3S7x4n9ut9dgyOjty0Wizp5XfVzq3JsjSvGH2ntxORNB3TkSOL87DPBNyk2bLj2AtSm6g5zoOX9PmNS1DFIsLcb0ceQ9ctGZ0A13YIbgMMb1gPom1GXsjnLz73UHAhhNxORh24wf3w29yhQB6asuTUenDzwwXq0Mp5OqKPmpqUPkGzcC97zDaUkVvQvuwHxHLGfsocZACjhbLepLtl5f5keS8rYJogepIvBRKpfmijvOCK5KclGFDBh%2BGtReK6VdeMKOT78wGOqUBIJLU8nAoxFqUErQ8yz9Qs8jh%2B6qpFnql0DIBOI2t6U4Kp80lrurQ6ddnZYrO9DhZQKg%2Fd0M46HTOlOhLESnTygewVDOE6LjqgtZYwWaNC6KePBJu9NNoHWquwjHTl%2Fc%2B74MW9DPGN86zuFQWOaBEzbW7mhiuBLJQc1RRKAQhf3sxiwScHtjiBywy3XKQ0DGhgm%2B6tKDPI4FmHRo7VAjUFu3XiGOS&X-Amz-Signature=70aa8e4c4a2b5346fe5df030e19ff4223db3f50827d1e4e9b77bdbdabbb27b1c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



