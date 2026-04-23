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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVMAVFMM%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG1FtuytPaZ1Jkr1NsgDM%2F6Q1DpqoRVUhc%2Fows%2FK%2BCIvAiASOCrtTWee51M8ywhArmdNm2orFWFaK0RD6RHN%2Fah8YCr%2FAwhbEAAaDDYzNzQyMzE4MzgwNSIMKUw9wRLIBBfl%2B98YKtwDiwavq%2B5LSnJF3ss8k08ZwA1wxjN8qqHPLGR0sJNjpE0Z6idcH8Fk7EfzCqCfl1ldX%2FSj2dj9mz2wnonyd7JqWOztvX%2FuIZSqXCUPfLst9%2F3qc4iJnJe%2Fdkivsw477sOvoM04tESPTgnVtFBy98hgz3Fl4JulTeOAVXAHvyoR6Iadl54H5vZmhJ1sJsAZ5NSEAhG9O3BV0I6ecwHzM%2FDRjjYVMIdAMejN3wPFuvNnpb7fAY5IhiejrMs7Ipb2y%2FFC%2Fgz0F1cA87Sw64dLE62Xeh2ILhEO%2Bh05NHpiIeQ%2FaPU7HkXDLXyp1U8qwn%2F8x5ggLIWPboVP57eXXXE%2BQ0v5U8bOkVA%2FeBF038EfRIjfuI9PcGlcGGHKtZTOF8iNukhPwHhvX1G0wBhdmSg8HUf2FagJ4rxGRp8qR1sfA0UOJOolybfudS%2F8B8r2jSyBK8qwjbxIzTLL1VR9j7HwzMAQM8qmXGZlPg0kYSvHLIQJedxC9zzRj595DP3an9VoW4N%2B6cf2cVVjNqF530V%2FnFcyEGLsqae853RjgIsNJahe8ItcQY0vV2DPgCYqcKH1N3m6P1wEIt7v3%2BVyyFb%2BsGngnHS7n9q2JV8CO90c4DKHuahVRGN2pnigDoCmXUww5e%2BlzwY6pgEwOokUoQYpZLNw2BOEtkKIuS88ExQgCaUKkpp%2FTHsymxlvMVQJVg1ScaCACn9FL%2B8TVyayn7QD5BbT3kknR2W%2BOhQQbzyjkzHE%2BnzORdjMngzflSvibm8sm53j4Zuq3I6KNI5wsxpaZCjJa3E3qQbsroWgIuXRyxTKHrg032kTf0cA0USjJtcbzW%2BRXJmtIS5WG%2FUBXayqJrrE%2F6u6HzCjxLz8Y7P%2B&X-Amz-Signature=f62b543436ce8c8ab728334b06c3d9e4504f0f89f881ce8e8c8977b590ac0711&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



