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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ALVTTAP%2F20260402%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260402T034529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICS6Lbr%2FXo8HKzFqU00D7rwwU7QzY7CCxVDfhyPEHmTpAiB%2FepXnS%2F7nyCh35RwKBxu7%2F4FzTWMM02RieFV1YLeUtyr%2FAwhkEAAaDDYzNzQyMzE4MzgwNSIMbUM23ASLhE5siV8cKtwDVhDzxngz4hlXuXBw%2Frazt5EvPY8y7nso4mTHX58Rjs6R%2F%2B9Y7DiLNziU66ZTeGUbYshm4hS%2FMOmz5YI84HFECbSvVP7N8X%2Fz6gYCsI7%2B8kXQ9tWaBef6Z1shZ1eg%2FlyaN8G%2F7pDN0aYrhyOSjuxfhb118ekbu%2FmmxLulc7UJMUWyBS22g6ITlUtgMPa9mtfB5E1BhxMO4sjWs4jkK7AT%2FtVy3SbzxCW2aQt2axCXgQl9Ww2ppoe37yb3rNVCh1ELufQR3hD4RbUkeGtu%2BocoCO%2FeXDcnMXsTAWQa3DdkasOt3HuFEm%2F7%2FdOmahPE6r%2BYI1yYMl04HaHSJLMVgvdbHk6tTC24rtpFUeLueDOP3DzWtkO20kJW3SDv2XN1enjnVvUHsVpeZAYPPoDXtELcjMx2r9Ddb8TcLOOHnW9cXs1peFpwH5%2FJpjqStG0U9squjP0fx9X4KzTr32J46aSkpEmB94vJM98so9BucCQJQtTkm0HuOAIa2ibexk75pXy4WImvdj0f2IuVepVBZawkJpy8luOlzoOwQ5uCJ%2Fg35EDTAnTbvDDr967c38dJ3lJaEl6HfR02ACKGoObH0wBPz29XocYUGYNdKJrZ1qe0edyRt0VvIjpkxSxfe8Qwi6%2B3zgY6pgFIg2IKqVZnNu8C7Jhfz1HI0buwb9e3ScmGHEKJq3%2BnZYFsqbmbJbO1zRW%2BVYqNHLJTNeWEJ%2BuSmjSSHwj9B2J%2BuCexZjao89388UDPN8o4JCgJwDesHz03yYP0A%2FurQfJ1HhpAASj79iN4Wi3okfpYO6r819uZIULMFHlppg1rM9CSaI8%2BKMQEW9KWezYuN3vpA1EYGtyxXVMQdu6T9f%2BKfdisjISR&X-Amz-Signature=1baa25cf42d8a2f576b2044d28dc87ce660bd8f75c835e9aabb00adf74c83aa0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



