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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VC5LDK4%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICpuKlw%2F9xmPzad6ybFYlvvWZ5wvdAA0zLDZa9GweW9WAiBHaXrNzaNZunTfl8tTvtaLa4j4gJhE5mZYj60BqnhBriqIBAjD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMASltmSFNbPovTiVgKtwD8pyuG2k9xCnmEBuUbRGGZ3e9pYvhF2Ncmbk4BbLGasUF3i%2FJubwXDJk9HdtWQnm9TUQWSTBmOgLWASbqyeLB6IyJG71uNXEVPfCIqb5LEQnBeo0hI5rIB%2B1kV3RsMfvJMKf7LkjH4pmgOxU3rye3d%2BTAxu32P%2Bs96qEPqKDG9vK%2FgajGJMVCoOhK%2FVHEsyWgJSgi1VCS3lkbcdm9T6D8qUzSJIHcWsyiu25GJKapuCf51qDfznqRTyErPU2UYBqnnul0hR%2BrjiYXRfdShXsYqLIUUqlgpQyl4h%2BjK7Fpj%2BGRZ%2F88eYuwcZsPxJmTgztdEwuujy%2FRLoSu08JmgsYnZ4%2BHWi6Q2lm1Adl4iDQMH%2BmgFL5fok0ZYIS%2FbVr%2BKgjK2a5myO17ChLQ1qz69LVBQ%2FcUwFRuCiTjxS8sjZHRu86jFHXuLd7URHaIMd36LB3741KJUxTxIs0in3gH%2Fxk95lLlXCxYw2bHzCGm3XbDIF3k6aphE6skBjPQi%2Bb8Uko6bCessQ9cd77YGwu7dJoIR6bm4eZj6xDxXPwMPhP8AsNVBb8C%2F1rPCQnlep1X9iwpqGj1JogzIq8gZ%2FQBsKe8xQbf7ZE8nA7Nznsv0zHG1Y33z%2F8xP67i2YDO8Acw%2BZupyQY6pgEo9zpXyNq8HUg0DPBYXaoT7nfcNGXA8DBu36vQl8029dokch%2F%2Fsv3hzkuIPje2lSBO%2BNToMmuZIGlah0axKWRuGggkid4EcTJKS1tEAt0wDBa9YDIGEq6BKUEqCgFVZd%2BuzMw9mZO8lZY8GXDrDF0pZpTHnCBhltMnVRuNVNd58aXIbMLu87MuT4kosBfOWAe3lvXeepm1NTBrHr8C3epjcNKOF9mx&X-Amz-Signature=ac22eb4520c05b81d5e17bd25db99912fd8acde3acc3fbe9ffc78c62b74e5a4f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



